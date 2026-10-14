import os
from azure.core.credentials import AzureKeyCredential
from azure.ai.textanalytics import TextAnalyticsClient

def link_entities(text: str):
    endpoint = os.getenv("LANGUAGE_ENDPOINT", "https://nlpservicepro.cognitiveservices.azure.com/")
    key = os.getenv("LANGUAGE_KEY", "Put your API key here") # <-- yahan naya key paste karo
    client = TextAnalyticsClient(endpoint=endpoint, credential=AzureKeyCredential(key))
    documents = [text]

    response = client.recognize_linked_entities(documents)

    for doc in response:
        if doc.is_error:
            print("Error:", doc.error)
            continue
        print(f"\nDocument ID: {doc.id}")
        for entity in doc.entities:
            print(f"- Entity Name: {entity.name}")
            print(f"  Wikipedia URL: {entity.url}")
            print(f"  Data Source: {entity.data_source}")
            print(f"  Occurred {len(entity.matches)} time(s)")
            for match in entity.matches:
                print(f"    Match Text: \"{match.text}\" (Offset: {match.offset}, Length: {match.length})")
