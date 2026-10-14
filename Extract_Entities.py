import os
from azure.core.credentials import AzureKeyCredential
from azure.ai.textanalytics import TextAnalyticsClient

# 1. Environment vars (replace fallback values with your real ones or set env vars)

endpoint = os.getenv("LANGUAGE_ENDPOINT", "https://nlpservicepro.cognitiveservices.azure.com/")
key = os.getenv("LANGUAGE_KEY", "Put your API key here") # <-- yahan naya key paste karo

if not endpoint or not key or "<your-azure-key-here>" in key:
    # It's OK to use a friendly error here so you don't accidentally run with a dummy key
    raise ValueError("Please set LANGUAGE_ENDPOINT and LANGUAGE_KEY environment variables with your Azure resource values.")

# 2. Authenticate and create client
credential = AzureKeyCredential(key)
client = TextAnalyticsClient(endpoint=endpoint, credential=credential)

# 3. Documents to analyze (same format you've been using)
documents = [
    {"id": "301", "language": "en", "text": "Microsoft was founded by Bill Gates and Paul Allen in Albuquerque."},
    {"id": "302", "language": "en", "text": "I flew from Bangalore to London on Air India last week."},
    {"id": "303", "language": "en", "text": "The price of Bitcoin reached $60,000 in 2021."}
]

# 4. Call the Entity Recognition API
#    Note: method recognizes named entities (persons, organizations, locations, quantities, URLs, emails, etc.)
response = client.recognize_entities(documents=documents)

# 5. Print results in a clear, structured way
for doc in response:
    if doc.is_error:
        print(f"❌ Document ID={doc.id} → Error: {doc.error}")
        continue

    print(f"\n🆔 Document ID = {doc.id}")
    print(f"Text: {next(d['text'] for d in documents if d['id'] == doc.id)}")
    if not doc.entities:
        print("→ No entities found.")
        continue

    print("→ Entities found:")
    for idx, entity in enumerate(doc.entities, start=1):
        # category and subcategory (subcategory may be None)
        category = entity.category
        subcategory = getattr(entity, "subcategory", None) or ""
        # confidence score
        score = getattr(entity, "confidence_score", None)
        # offset and length (character positions)
        offset = getattr(entity, "offset", None)
        length = getattr(entity, "length", None)

        print(f"  {idx}. '{entity.text}'")
        print(f"     - Category: {category}" + (f", Subcategory: {subcategory}" if subcategory else ""))
        if score is not None:
            print(f"     - Confidence Score: {score:.3f}")
        if offset is not None and length is not None:
            print(f"     - Offset: {offset}, Length: {length}")
        # If the service returned a link to the entity in an external KB (knowledge base), print it
        if getattr(entity, "data_sources", None):
            # data_sources is a list of DataSource objects (name, id, url)
            for ds in entity.data_sources:
                print(f"     - KB Match: {ds.name} (id={ds.id}) -> {ds.url if getattr(ds, 'url', None) else 'no url'}")

# Optional: if you want to also return the results programmatically, you can collect them into a dict/list here.
