import os
from azure.core.credentials import AzureKeyCredential
import requests
import time

# ====== CONFIG (sirf yahan change karna hai) ======

# Get prediction URL popup se EXACT URL
PREDICTION_URL = "https://nlpservicepro.cognitiveservices.azure.com/language/analyze-text/jobs?api-version=2024-11-15-preview"
# Language resource key (Keys and Endpoint me se Key1 / Key2)
API_KEY = "Put your API key here" # <-- yahan naya key paste karo

# Language Studio project ka exact naam (breadcrumb me jo dikh raha hai)
PROJECT_NAME = "customtextclassification"   # agar naam different ho to EXACT change karo

# Deployment tab me jo naam hai
DEPLOYMENT_NAME = "production"



text = input("Enter text to classify: ")

headers = {
    "Ocp-Apim-Subscription-Key": API_KEY,
    "Content-Type": "application/json"
}

body = {
    "displayName": "colab-multilabel-test",
    "analysisInput": {
        "documents": [
            {
                "id": "1",
                "language": "en",
                "text": text
            }
        ]
    },
    "tasks": [
        {
            "kind": "CustomMultiLabelClassification",
            "parameters": {
                "projectName": PROJECT_NAME,
                "deploymentName": DEPLOYMENT_NAME
            }
        }
    ]
}

print("Submitting job...")
submit_resp = requests.post(PREDICTION_URL, headers=headers, json=body)
print("Submit status code:", submit_resp.status_code)

if submit_resp.status_code != 202:
    print("Submit ERROR:")
    print(submit_resp.text)
else:
    operation_location = submit_resp.headers["operation-location"]
    print("Operation URL:", operation_location)

    # ==== Poll job status ====
    while True:
        poll_resp = requests.get(operation_location, headers=headers)
        result = poll_resp.json()
        status = result.get("status")
        print("Job status:", status)

        if status == "succeeded":
            break
        if status in ("failed", "cancelled"):
            print("Job failed/cancelled:")
            print(result)
            raise SystemExit

        time.sleep(2)

    # ==== Read results ====
    task = result["tasks"]["items"][0]
    docs = task["results"]["documents"]

    print("\n--- RESULTS RAW DOC ---")
    print(docs[0])  # just so you can see what Azure returned

    print("\n--- CLEAN RESULTS ---")
    for doc in docs:
        # multi-label project -> 'classes'
        if "classes" in doc:
            labels = doc["classes"]
        # (backup: single-label project -> 'class')
        elif "class" in doc:
            labels = doc["class"]
        else:
            print("Unknown result format:", doc)
            continue

        for c in labels:
            print(f"Label: {c['category']} | Score: {c['confidenceScore']:.3f}")
