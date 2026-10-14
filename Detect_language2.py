# file: detect_languages_realistic.py

import os
from azure.core.credentials import AzureKeyCredential
from azure.ai.textanalytics import TextAnalyticsClient, DetectLanguageInput

# ---------- 1) Credentials (env vars) ----------
endpoint = os.getenv("LANGUAGE_ENDPOINT", "https://nlpservicepro.cognitiveservices.azure.com/")
key = os.getenv("LANGUAGE_KEY","Put your API key here") # <-- yahan naya key paste karo

if not endpoint or not key:
    raise RuntimeError(
        "AZURE_LANGUAGE_ENDPOINT and AZURE_LANGUAGE_KEY must be set as environment variables."
    )

# ---------- 2) Create authenticated client ----------
credential = AzureKeyCredential(key)                   # key ko secure object me wrap karna
client = TextAnalyticsClient(endpoint=endpoint, credential=credential)

# ---------- 3) Realistic documents (mix of languages, ambiguous and emojis) ----------
documents = [
    DetectLanguageInput(id="1",
                        text="Hi, my order #1234 hasn't arrived yet. Can you check the tracking?",
                        country_hint="US"),
    DetectLanguageInput(id="2",
                        text="¿Cómo puedo cancelar mi suscripción? Necesito ayuda urgente.",
                        country_hint="ES"),
    DetectLanguageInput(id="3",
                        text="मेरा ऑर्डर अभी तक नहीं पहुंचा — कृपया मदद करें।",
                        country_hint="IN"),
    DetectLanguageInput(id="4",
                        text="Hello! ¿Hablas español? Je parle français aussi.",
                        country_hint="US"),  # mixed text — predominant language expected
    DetectLanguageInput(id="5",
                        text="こんにちは、配送状況を教えてください。",
                        country_hint="JP"),
    DetectLanguageInput(id="6",
                        text="??????",                # garbled or unsupported characters (simulate error)
                        country_hint="US")
]

# ---------- 4) Call the detect_language API ----------
# detect_language returns a list of DetectLanguageResult / DocumentError objects
results = client.detect_language(documents)

# ---------- 5) Process and print results ----------
for res in results:
    # res is either a DetectLanguageResult (successful) or DocumentError (if error)
    if not res.is_error:
        # primary_language is a DetectedLanguage object with name, iso6391_name, confidence_score
        lang = res.primary_language
        print(
            f"Document id={res.id} -> language='{lang.name}', "
            f"iso='{lang.iso6391_name}', confidence={lang.confidence_score:.3f}"
        )
    else:
        # res.error has error.message and code
        print(f"Document id={res.id} -> ERROR: {res.error.code} : {res.error.message}")
