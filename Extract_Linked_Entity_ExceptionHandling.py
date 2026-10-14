import os
import json
import sys
from azure.core.credentials import AzureKeyCredential
from azure.ai.textanalytics import TextAnalyticsClient

def link_entities(text: str):
    # --- Read environment variables (support both common names) ---

    endpoint = os.getenv("LANGUAGE_ENDPOINT", "https://nlpservicepro.cognitiveservices.azure.com/")
    key = os.getenv("LANGUAGE_KEY", "Put your API key here") # <-- yahan naya key paste karo
    if not endpoint or not key:
        print("ERROR: Missing Azure credentials.")
        print("Please set AZURE_LANGUAGE_ENDPOINT (or LANGUAGE_ENDPOINT) and AZURE_LANGUAGE_KEY (or LANGUAGE_KEY).")
        return None

    # Normalize endpoint
    endpoint = endpoint.rstrip("/")

    # --- Create client ---
    try:
        client = TextAnalyticsClient(endpoint=endpoint, credential=AzureKeyCredential(key))
    except Exception as e:
        print("ERROR creating TextAnalyticsClient:", str(e))
        return None

    # Use the document format with id and language to be explicit
    documents = [{"id": "1", "language": "en", "text": text}]

    # --- Call the API ---
    try:
        response = client.recognize_linked_entities(documents)
    except Exception as e:
        print("API call failed:", str(e))
        return None

    # --- Parse results and build JSON-like output ---
    output = {"documents": [], "errors": []}
    for doc in response:
        # If the SDK returns a per-document error
        if doc.is_error:
            err = {"id": getattr(doc, "id", None), "error": str(doc.error)}
            print("Document error:", err)
            output["errors"].append(err)
            continue

        doc_out = {"id": doc.id, "entities": [], "warnings": []}
        # If no entities, note it
        if not doc.entities:
            print(f"No linked entities found in document id={doc.id}")
        for ent in doc.entities:
            ent_obj = {
                "name": ent.name,
                "id": getattr(ent, "id", None),
                "url": getattr(ent, "url", None),
                "dataSource": getattr(ent, "data_source", None),
                "matches": []
            }
            for m in ent.matches:
                ent_obj["matches"].append({
                    "text": m.text,
                    "offset": m.offset,
                    "length": m.length,
                    "confidenceScore": getattr(m, "confidence_score", None)
                })
            doc_out["entities"].append(ent_obj)

        output["documents"].append(doc_out)

    # Pretty print and return
    print("\n--- Entity Linking Result (pretty) ---")
    print(json.dumps(output, indent=2))
    return output

if __name__ == "__main__":
    # quick test text
    sample = "I saw Venus shining in the sky"
    result = link_entities(sample)

    # Exit code for CLI use
    # if result is None:
    #     sys.exit(1)
    # else:
    #     sys.exit(0)