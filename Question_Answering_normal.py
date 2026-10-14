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

# === Client initialization ===
# Ye client Azure QnA Runtime ko call karega
client = QuestionAnsweringClient(ENDPOINT, AzureKeyCredential(KEY))


def ask_kb_simple(question):
    """
    Ye function aapka question QnA KB (knowledgebase) ko bhejta hai
    aur best (highest confidence) answer print karta hai.
    """

    # Ye options QnA system ko batate hain:
    # - question (user input)
    # - top=3 (3 best answers laane ki koshish kare)
    # - confidence_threshold=0.2 (20% confidence se nichle answers ignore)
    # - include_unstructured_sources=True (agar aapne URLs/Docs add kiye hain to unse bhi answer mile)
    options = qna.AnswersOptions(
        question=question,
        top=3,
        confidence_threshold=0.2,
        include_unstructured_sources=True
    )

    # Azure QnA ko request bhejna
    result = client.get_answers(
        options,
        project_name=PROJECT,
        deployment_name=DEPLOYMENT
    )

    # Jo answers aaye unhe list me lo
    answers = result.answers or []

    # Agar answer nahi mila
    if not answers:
        print("Bot: Maaf kijiye, mujhe kuchh nahi mila.")
        return

    # Highest confidence wala best answer choose karna
    best = max(answers, key=lambda a: a.confidence)

    # Bot ka answer print karna
    print(f"Bot ({best.confidence:.2f}): {best.answer}")


def run_chat():
    """
    Ye function conversational loop handle karta hai.
    User se input leta hai jab tak wo 'quit' na likhe.
    """

    print("💬 Azure QnA (simple). 'quit' likh ke bahar niklein.")

    while True:
        user_q = input("\nYou: ").strip()

        # Agar user kuch nahi likhe ya 'quit' likhe to loop stop
        if not user_q or user_q.lower() == "quit":
            break

        # Har question ka answer laye
        ask_kb_simple(user_q)


# Program ka entry point (yahi se start hota hai)
if __name__ == "__main__":
    run_chat()

