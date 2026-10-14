import os
from azure.core.credentials import AzureKeyCredential
from azure.ai.textanalytics import TextAnalyticsClient

# 1. Environment variables से credentials लीजिये
endpoint = os.getenv("LANGUAGE_ENDPOINT", "https://nlpservicepro.cognitiveservices.azure.com/")
key = os.getenv("LANGUAGE_KEY","Put your API key here") # <-- yahan naya key paste karo
# 2. Authenticated client create कीजिये
credential = AzureKeyCredential(key)
client = TextAnalyticsClient(endpoint=endpoint, credential=credential)

# 3. Documents list बनाइये जिनकी भाषा पता करनी है
documents = [
    "This document is written in English.",
    "这是一个用中文写的文件",  # This is written in Chinese
    "Bonjour tout le monde", # This is French
    "Te amo", # This is Spanish
]

# 4. detect_language API call कीजिये
result = client.detect_language(documents)

# 5. Result को loop करके दिखाइये
for idx, doc in enumerate(result):
    if not doc.is_error:
        print(f"Review #{idx} is in '{doc.primary_language.name}', ISO639-1: '{doc.primary_language.iso6391_name}'")
    else:
        print(f"Error in document {idx}: {doc.error}")

