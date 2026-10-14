import os
from azure.core.credentials import AzureKeyCredential
from azure.ai.textanalytics import TextAnalyticsClient
from azure.ai.textanalytics import (
    DetectLanguageAction,
    ExtractKeyPhrasesAction,
    AnalyzeSentimentAction,
    RecognizeCategorizedEntitiesAction
)

# ----------------- config -----------------
endpoint = os.getenv("LANGUAGE_ENDPOINT", "https://nlpservicepro.cognitiveservices.azure.com/")
key = os.getenv("LANGUAGE_KEY", "Put your API key here") # <-- yahan naya key paste karo

if not endpoint or not key:
    raise ValueError("Please set LANGUAGE_ENDPOINT and LANGUAGE_KEY environment variables.")

client = TextAnalyticsClient(endpoint=endpoint, credential=AzureKeyCredential(key))

# ----------------- input -----------------
documents = [
    "Satya Nadella announced a new Microsoft AI product. Exciting times ahead!"
]

# ----------------- actions -----------------
actions = [
    DetectLanguageAction(),
    ExtractKeyPhrasesAction(),
    AnalyzeSentimentAction(),
    RecognizeCategorizedEntitiesAction()
]

# ----------------- run -----------------
poller = client.begin_analyze_actions(documents, actions=actions)
# poller.result() yields pages of action results
pages = poller.result()

# ----------------- parse & print -----------------
for page_idx, page in enumerate(pages, start=1):
    print(f"\n--- Page {page_idx} ---")
    for action_result in page:
        kind = action_result.kind
        print(f"\nAction: {kind}")
        # action_result.results is a list of per-document results for this action
        for doc_idx, doc_result in enumerate(action_result.results, start=1):
            # doc_result is a DocumentResult-like object (has .is_error if error)
            if doc_result.is_error:
                print(f" Document {doc_idx} (id={getattr(doc_result, 'id', None)}) → ERROR: {doc_result.error}")
                continue

            # Handle each action's per-document result shape
            if kind == "DetectLanguage":
                # doc_result.primary_language
                lang = doc_result.primary_language
                print(f" Document {doc_idx} → Detected language: {lang.name} (iso6391={lang.iso6391_name}, score={lang.confidence_score:.2f})")

            elif kind == "ExtractKeyPhrases":
                print(f" Document {doc_idx} → Key Phrases: {doc_result.key_phrases}")

            elif kind == "AnalyzeSentiment":
                sentiment = doc_result.sentiment
                scores = doc_result.confidence_scores
                print(f" Document {doc_idx} → Sentiment: {sentiment} (pos={scores.positive:.2f}, neu={scores.neutral:.2f}, neg={scores.negative:.2f})")
                # sentence-level
                for si, sentence in enumerate(doc_result.sentences, start=1):
                    sc = sentence.confidence_scores
                    print(f"   Sentence {si}: '{sentence.text.strip()}' → {sentence.sentiment} (pos={sc.positive:.2f}, neu={sc.neutral:.2f}, neg={sc.negative:.2f})")

            elif kind == "RecognizeCategorizedEntities":
                entities = doc_result.entities
                if not entities:
                    print(f" Document {doc_idx} → No entities found.")
                else:
                    print(f" Document {doc_idx} → Entities:")
                    for e in entities:
                        subcat = getattr(e, "subcategory", None)
                        print(f"   - '{e.text}' | category={e.category}" + (f", subcategory={subcat}" if subcat else "") + f", score={e.confidence_score:.2f}, offset={e.offset}, length={e.length}")
            else:
                # Unexpected/other action kinds
                print(f" Document {doc_idx} → (Unhandled action kind: {kind})")

