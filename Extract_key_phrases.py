import os
from azure.core.credentials import AzureKeyCredential
from azure.ai.textanalytics import TextAnalyticsClient

# 1. Environment vars for secure credentials
endpoint = os.getenv("LANGUAGE_ENDPOINT", "https://nlpservicepro.cognitiveservices.azure.com/")
key = os.getenv("LANGUAGE_KEY","Put your API key here") # <-- yahan naya key paste karo

# 2. Authenticated client creation
credential = AzureKeyCredential(key)
client = TextAnalyticsClient(endpoint=endpoint, credential=credential)

# 3. Realistic customer messages
docs = [
    {"id": "101", "language": "en", "text": "My package hasn't arrived and I'm worried about delivery delay."},
    {"id": "102", "language": "en", "text": "I want to cancel my subscription immediately."},
    {"id": "103", "language": "en", "text": "The product quality is excellent but charging port is broken."}
]

# 4. Call key phrase extraction
response = client.extract_key_phrases(documents=docs)

# 5. Handle and print results
for res in response:
    if not res.is_error:
        print(f"ID={res.id} → Key Phrases:", res.key_phrases)
    else:
        print(f"ID={res.id} → Error:", res.error)

