import os
from azure.core.credentials import AzureKeyCredential
from azure.ai.textanalytics import TextAnalyticsClient

# 1️⃣ Environment variables or fallback values
# (replace the fallback key and endpoint with your own secure values)
endpoint = os.getenv("LANGUAGE_ENDPOINT", "https://nlpservicepro.cognitiveservices.azure.com/")
key = os.getenv("LANGUAGE_KEY", "Put your API key here") # <-- yahan naya key paste karo

# 2️⃣ Authenticate client
credential = AzureKeyCredential(key)
client = TextAnalyticsClient(endpoint=endpoint, credential=credential)

# 3️⃣ Sample customer reviews/messages
documents = [
    {"id": "201", "language": "en", "text": "I loved the product quality. But the delivery was too slow."},
    {"id": "202", "language": "en", "text": "This new update is terrible, it keeps crashing all the time."},
    {"id": "203", "language": "en", "text": "Customer support was helpful and polite. Great experience!"},
    {"id": "204", "language": "en", "text": "I have passed my interview"}

]

# 4️⃣ Call the Azure Sentiment Analysis API
response = client.analyze_sentiment(documents=documents)

# 5️⃣ Display results
for doc in response:
    if not doc.is_error:
        print(f"\n🆔 ID = {doc.id}")
        print(f"➡️  Overall Sentiment: {doc.sentiment.upper()}")
        print(f"   Confidence Scores: Positive={doc.confidence_scores.positive:.2f}, "
              f"Neutral={doc.confidence_scores.neutral:.2f}, Negative={doc.confidence_scores.negative:.2f}")

        # Sentence-level breakdown
        print("   Sentence-level sentiments:")
        for idx, sentence in enumerate(doc.sentences, start=1):
            print(f"     {idx}. '{sentence.text.strip()}' → {sentence.sentiment} "
                  f"(Pos={sentence.confidence_scores.positive:.2f}, "
                  f"Neu={sentence.confidence_scores.neutral:.2f}, "
                  f"Neg={sentence.confidence_scores.negative:.2f})")
    else:
        print(f"❌ ID={doc.id} → Error: {doc.error}")
