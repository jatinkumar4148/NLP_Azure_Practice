"""Multi-turn means:Bot previous conversation ki context yaad rakhta hai,
             aur uske basis par agla answer generate/choose karta hai."""

import os
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

# === 2) Client banao ===
client = QuestionAnsweringClient(ENDPOINT, AzureKeyCredential(KEY))

def ask_kb(question, *, previous_qna_id=None, previous_question=None, force_qna_id=None):
    """
    Knowledge base se answer laata hai.
    - previous_* pass karne se multi-turn context maintain hota hai.
    - force_qna_id dene se kisi specific follow-up ko directly fetch kar sakte ho.
    """
    # AnswersOptions: yahin par thresholds, context, filters, short-answer, etc. set hote hain
    options = qna.AnswersOptions(
        question=question if force_qna_id is None else None,
        qna_id=force_qna_id,                     # agar follow-up prompt ka exact qna_id pata ho
        top=3,                                   # top N answers
        confidence_threshold=0.2,                # kam score waale hata do
        answer_context=(
            qna.KnowledgeBaseAnswerContext(
                previous_qna_id=previous_qna_id,
                previous_question=previous_question
            ) if previous_qna_id is not None else None
        ),
        include_unstructured_sources=True        # (optional) Agar aapne unstructured sources enable kiye hon
    )

    # SDK call: get_answers(project + deployment pe)
    result = client.get_answers(
        options,
        project_name=PROJECT,
        deployment_name=DEPLOYMENT
    )
    return result.answers  # list[KnowledgeBaseAnswer]

def run_chat():
    print("💬 Azure QnA demo (multi-turn). 'quit' likh ke bahar niklein.")
    previous_qna_id = None
    previous_question = None

    while True:
        user_q = input("\nYou: ").strip()
        if not user_q or user_q.lower() == "quit":
            break

        answers = ask_kb(
            user_q,
            previous_qna_id=previous_qna_id,
            previous_question=previous_question
        )

        if not answers:
            print("Bot: Maaf kijiye, mujhe kuchh nahi mila.")
            # reset context
            previous_qna_id = None
            previous_question = None
            continue

        # sabse best (highest confidence) pick
        best = max(answers, key=lambda a: a.confidence)
        print(f"Bot ({best.confidence:.2f}): {best.answer}")

        # --- Multi-turn: agar follow-up prompts milein to dikhhao ---
        prompts = []
        if getattr(best, "dialog", None) and getattr(best.dialog, "prompts", None):
            prompts = best.dialog.prompts

        if prompts:
            print("\n  (Follow-up options):")
            for i, p in enumerate(prompts, start=1):
                # display_text = user ko dikhane layak sawal
                print(f"   {i}. {p.display_text}")

            choice = input("  -> Koi option number enter karein (ya Enter skip): ").strip()
            if choice.isdigit():
                idx = int(choice)
                if 1 <= idx <= len(prompts):
                    picked = prompts[idx - 1]
                    # Follow-up ko laane ke do tareeke:
                    # (A) qna_id se exact answer mango:
                    followup_answers = ask_kb(
                        question="",  # ignore, kyunki qna_id de rahe hain
                        previous_qna_id=best.qna_id,
                        previous_question=user_q,
                        force_qna_id=picked.qna_id
                    )
                    if followup_answers:
                        fbest = max(followup_answers, key=lambda a: a.confidence)
                        print(f"\nBot ({fbest.confidence:.2f}): {fbest.answer}")
                        # next turn ke liye context update
                        previous_qna_id = fbest.qna_id
                        previous_question = picked.display_text
                        continue

            # agar user ne follow-up nahi liya to context ko best answer se set kar do
            previous_qna_id = best.qna_id
            previous_question = user_q
        else:
            # no prompts -> context close karo (fresh query next time)
            previous_qna_id = None
            previous_question = None

if __name__ == "__main__":
    run_chat()