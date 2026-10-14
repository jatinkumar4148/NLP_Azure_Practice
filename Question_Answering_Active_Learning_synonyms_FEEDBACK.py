# Feedback System hai isme quit
import os
import time
import json
import requests
from azure.core.credentials import AzureKeyCredential
from azure.ai.language.questionanswering import QuestionAnsweringClient
from azure.ai.language.questionanswering import models as qna

# === Configuration (Azure Resource details) ===
# Endpoint: Azure Language resource ka endpoint URL
ENDPOINT = "https://nlpservicepro.cognitiveservices.azure.com/"   

# Key: Azure Question Answering ki API key (query key)
KEY = "Put your API key here" # <-- yahan naya key paste karo

# Project name: Language Studio me jo aapne QnA project banaya tha wahi naam
PROJECT = "MYNLPPROJECT"

# Deployment name: test/production (Language Studio me deploy kiya hota hai)
DEPLOYMENT = "production" 

# ===== Runtime client =====
client = QuestionAnsweringClient(ENDPOINT, AzureKeyCredential(KEY))

# ===== Authoring (active learning) =====
API_VERSION = "2023-04-01"

def _auth_headers():
    return {
        "Ocp-Apim-Subscription-Key": KEY,
        "Content-Type": "application/json"
    }

def _authoring_list_qnas():
    url = f"{ENDPOINT.rstrip('/')}/language/authoring/query-knowledgebases/projects/{PROJECT}/qnas"
    params = {"api-version": API_VERSION, "top": 1000}
    r = requests.get(url, headers=_auth_headers(), params=params)
    return r.json()

def _authoring_patch_qnas(patch_body):
    url = f"{ENDPOINT.rstrip('/')}/language/authoring/query-knowledgebases/projects/{PROJECT}/qnas"
    params = {"api-version": API_VERSION}
    r = requests.patch(url, headers=_auth_headers(), params=params, data=json.dumps(patch_body))
    return r.headers.get("Operation-Location", "")

def _poll_job(op_location, seconds=2):
    while True:
        r = requests.get(op_location)
        data = r.json()
        status = data.get("status", "")
        print("🛠️  Update job status:", status)
        if status in ("succeeded", "failed", "cancelled"):
            return status
        time.sleep(seconds)

def add_alternate_question(qna_id: int, new_question: str):
    data = _authoring_list_qnas()
    items = data.get("value", [])
    target = None
    for it in items:
        if it.get("id") == qna_id:
            target = it
            break
    if not target:
        print("⚠️  QnA id not found in authoring list.")
        return
    existing = target.get("questions", []) or []
    if new_question in existing:
        print("ℹ️  Question already present; skipping.")
        return
    updated_questions = existing + [new_question]

    patch_body = [
        {"op": "replace", "value": {"id": qna_id, "questions": updated_questions}}
    ]
    print("➕ Adding alternate question:", new_question)
    op_loc = _authoring_patch_qnas(patch_body)
    if op_loc:
        _poll_job(op_loc)

# ===== Runtime (multi-turn + prompts) =====
def ask_kb(question, *, previous_qna_id=None, previous_question=None, force_qna_id=None):
    options = qna.AnswersOptions(
        question=question if force_qna_id is None else None,
        qna_id=force_qna_id,
        top=3,
        confidence_threshold=0.2,
        answer_context=(
            qna.KnowledgeBaseAnswerContext(
                previous_qna_id=previous_qna_id,
                previous_question=previous_question
            ) if previous_qna_id is not None else None
        ),
        include_unstructured_sources=True
    )
    result = client.get_answers(options, project_name=PROJECT, deployment_name=DEPLOYMENT)
    return result.answers or []

# ===== Helper: quit detection =====
def is_quit(s: str) -> bool:
    s = (s or "").strip().lower()
    return s in ("q", "quit", "exit")

def run_chat():
    print("💬 Python FAQ (multi-turn + active learning). Type 'quit' / 'exit' / 'q' to leave.")
    prev_id = None
    prev_q  = None

    while True:
        user_q = input("\nYou: ").strip()
        if is_quit(user_q) or not user_q:
            print("👋 Bye!")
            break

        answers = ask_kb(user_q, previous_qna_id=prev_id, previous_question=prev_q)

        if not answers:
            print("Bot: Maaf kijiye, mujhe kuchh nahi mila.")
            prev_id = None
            prev_q  = None
            continue

        best = max(answers, key=lambda a: a.confidence)
        print(f"Bot ({best.confidence:.2f}): {best.answer}")

        # feedback -> active learning
        fb = input("👍 Helpful? (y/n or 'quit'): ").strip().lower()
        if is_quit(fb):
            print("👋 Bye!")
            break
        if fb == "y":
            add_alternate_question(best.qna_id, user_q)

        # follow-up prompts
        prompts = []
        if getattr(best, "dialog", None) and getattr(best.dialog, "prompts", None):
            prompts = best.dialog.prompts

        if prompts:
            print("\n  (Follow-up options):")
            for i, p in enumerate(prompts, start=1):
                print(f"   {i}. {p.display_text}")

            choice = input("  -> Option number (Enter to skip, or 'quit'): ").strip()
            if is_quit(choice):
                print("👋 Bye!")
                break
            if choice.isdigit():
                idx = int(choice)
                if 1 <= idx <= len(prompts):
                    picked = prompts[idx - 1]
                    fanswers = ask_kb(
                        "",  # ignored because qna_id is provided
                        previous_qna_id=best.qna_id,
                        previous_question=user_q,
                        force_qna_id=picked.qna_id
                    )
                    if fanswers:
                        fbest = max(fanswers, key=lambda a: a.confidence)
                        print(f"\nBot ({fbest.confidence:.2f}): {fbest.answer}")

                        fb2 = input("👍 Helpful? (y/n or 'quit'): ").strip().lower()
                        if is_quit(fb2):
                            print("👋 Bye!")
                            break
                        if fb2 == "y":
                            add_alternate_question(fbest.qna_id, picked.display_text)

                        prev_id = fbest.qna_id
                        prev_q  = picked.display_text
                        continue

            # skipped or invalid → carry context
            prev_id = best.qna_id
            prev_q  = user_q
        else:
            # no prompts → reset context
            prev_id = None
            prev_q  = None

if __name__ == "__main__":
    run_chat()
