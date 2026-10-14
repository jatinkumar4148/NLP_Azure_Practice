# Simple Code
import os
from azure.core.credentials import AzureKeyCredential
from azure.ai.textanalytics import TextAnalyticsClient

# 1. Environment vars for secure credentials
endpoint = os.getenv("LANGUAGE_ENDPOINT", "https://nlpservicepro.cognitiveservices.azure.com/")
key = os.getenv("LANGUAGE_KEY","Put your API key here") # <-- yahan naya key paste karo

# 2. Authenticated client creation
credential = AzureKeyCredential(key)
client = TextAnalyticsClient(endpoint=endpoint, credential=credential)

documents = [{"id": "1", "language": "en", "text": "I saw Venus shining in the sky"}]

response = client.recognize_linked_entities(documents)

for doc in response:
    for ent in doc.entities:
        print("Entity name:", ent.name)
        print("  ID:", getattr(ent, "id", None))
        print("  URL:", getattr(ent, "url", None))
        print("  Data source:", getattr(ent, "data_source", None))
        for match in ent.matches:
            print(f"    Match: '{match.text}' (offset={match.offset}, length={match.length})")
    # print a separator for clarity
    print()