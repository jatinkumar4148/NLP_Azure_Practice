[README_NLP_Azure_Practice_Interactive (1).md](https://github.com/user-attachments/files/33422274/README_NLP_Azure_Practice_Interactive.1.md)
# NLP_Azure_Practice::: {align="center"}
# ☁️ NLP Azure Practice

### Explore Natural Language Processing with Microsoft Azure AI Language and Python

A hands-on collection of Python examples for language detection,
sentiment analysis, key phrase extraction, entity recognition, entity
linking, custom text classification, and conversational question
answering.

[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Microsoft
Azure](https://img.shields.io/badge/Microsoft%20Azure-AI%20Language-0078D4?logo=microsoftazure&logoColor=white)](https://azure.microsoft.com/)
[![Made with
Python](https://img.shields.io/badge/Made%20with-Python-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Learning
Project](https://img.shields.io/badge/Type-Learning%20Project-10B981)](#-learning-roadmap)

**[Explore the
repository](https://github.com/jatinkumar4148/NLP_Azure_Practice) ·
[Setup guide](#-quick-start) · [Script directory](#-project-file-guide)
· [Troubleshooting](#-troubleshooting)**
:::

------------------------------------------------------------------------

## 🧭 Navigate this README

-   [About the project](#-about-the-project)
-   [What you can explore](#-what-you-can-explore)
-   [How the examples work](#-how-the-examples-work)
-   [Quick start](#-quick-start)
-   [Project file guide](#-project-file-guide)
-   [Azure configuration](#-azure-configuration)
-   [Troubleshooting](#-troubleshooting)
-   [Learning roadmap](#-learning-roadmap)
-   [Security](#-security)
-   [Contributing and next steps](#-contributing-and-next-steps)

## 🌟 About the project

**NLP Azure Practice** is a learning repository containing focused
Python scripts that demonstrate how to use Microsoft Azure AI Language
capabilities.

Each script concentrates on a particular task, so you can explore a
feature independently, run a sample, inspect the response, and then
adapt it for your own text data.

> **Project scope:** This repository is a collection of practice
> scripts, not one integrated web application. Some examples require an
> Azure Language resource, and custom classification or
> question-answering examples also require a configured project and
> deployment.

## 🧠 What you can explore

```{=html}
<table>
```
```{=html}
<tr>
```
```{=html}
<td width="50%">
```
```{=html}
<h3>
```
🌍 Language Detection
```{=html}
</h3>
```
Identify the predominant language of a text and inspect the language
code and confidence score.
```{=html}
</td>
```
```{=html}
<td width="50%">
```
```{=html}
<h3>
```
💬 Sentiment Analysis
```{=html}
</h3>
```
Analyze positive, neutral, and negative sentiment, including
sentence-level results.
```{=html}
</td>
```
```{=html}
</tr>
```
```{=html}
<tr>
```
```{=html}
<td width="50%">
```
```{=html}
<h3>
```
🔑 Key Phrase Extraction
```{=html}
</h3>
```
Extract important phrases from customer messages and sample documents.
```{=html}
</td>
```
```{=html}
<td width="50%">
```
```{=html}
<h3>
```
🏷️ Named Entity Recognition
```{=html}
</h3>
```
Identify entities such as people, organizations, locations, and
quantities.
```{=html}
</td>
```
```{=html}
</tr>
```
```{=html}
<tr>
```
```{=html}
<td width="50%">
```
```{=html}
<h3>
```
🔗 Entity Linking
```{=html}
</h3>
```
Explore entity matches, knowledge-base URLs, data sources, and text
offsets.
```{=html}
</td>
```
```{=html}
<td width="50%">
```
```{=html}
<h3>
```
🎯 Custom Text Classification
```{=html}
</h3>
```
Submit text to an Azure Language custom classification deployment and
inspect its labels and confidence scores.
```{=html}
</td>
```
```{=html}
</tr>
```
```{=html}
<tr>
```
```{=html}
<td width="50%">
```
```{=html}
<h3>
```
❓ Question Answering
```{=html}
</h3>
```
Query a configured Azure Language knowledge base and select the best
answer by confidence.
```{=html}
</td>
```
```{=html}
<td width="50%">
```
```{=html}
<h3>
```
🔄 Multi-turn Q&A & Feedback
```{=html}
</h3>
```
Experiment with conversational context, follow-up prompts, and
alternate-question authoring workflows.
```{=html}
</td>
```
```{=html}
</tr>
```
```{=html}
</table>
```
## 🔁 How the examples work

``` mermaid
flowchart TD
    A["📝 Sample text or user input"] --> B["🐍 Python script"]
    B --> C["🔐 Load Azure credentials"]
    C --> D["☁️ Azure AI Language"]
    D --> E["📦 API / SDK response"]
    E --> F["🔎 Parse results and handle errors"]
    F --> G["📊 Print labels, scores, phrases, or answers"]
```

Typical flow: provide text → authenticate with Azure → call a language
feature → inspect the response. Question-answering and
custom-classification scripts may require additional project/deployment
configuration.

## 🚀 Quick start

### 1. Clone the repository

``` bash
git clone https://github.com/jatinkumar4148/NLP_Azure_Practice.git
cd NLP_Azure_Practice
```

### 2. Create a virtual environment

**Windows PowerShell**

``` powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

If PowerShell blocks activation, allow scripts for this terminal session
only:

``` powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned
.\venv\Scripts\Activate.ps1
```

**macOS / Linux**

``` bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

``` bash
python -m pip install --upgrade pip
python -m pip install azure-ai-textanalytics azure-ai-language-questionanswering azure-core requests python-dotenv
```

These are the main packages used across the examples. You do not need
every package for every script; if an import fails, install the package
that provides that module in your active environment.

### 4. Configure your Azure resource

Create a local `.env` file in the project root. Use your own resource
details:

``` dotenv
LANGUAGE_ENDPOINT=https://YOUR-RESOURCE.cognitiveservices.azure.com/
LANGUAGE_KEY=YOUR_AZURE_LANGUAGE_KEY
```

Make sure `.env` is listed in `.gitignore`. **Never commit a real Azure
key.**

### 5. Run an example

Try these from the repository root:

``` powershell
python "Detect language.py"
python Extract_key_phrases.py
python Sentimental_Analysis.py
python Extract_Entities.py
python Entity_Linking.py
python Question_Answering_normal.py
```

Scripts that ask questions in the terminal will prompt you for input.
Where supported, type `quit` or `exit` to stop the conversation.

```{=html}
<details>
```
```{=html}
<summary>
```
`<strong>`{=html}🧪 What should I run first?`</strong>`{=html}
```{=html}
</summary>
```
If you are new to Azure AI Language, try these in order:

1.  `Detect language.py` --- start with language identification.
2.  `Extract_key_phrases.py` --- inspect extracted phrases.
3.  `Sentimental_Analysis.py` --- compare sentiment labels and
    confidence scores.
4.  `Extract_Entities.py` --- inspect entity categories and metadata.
5.  `Question_Answering_normal.py` --- try question answering after
    configuring a project and deployment.

```{=html}
</details>
```
## 🗂️ Project file guide

```{=html}
<details open>
```
```{=html}
<summary>
```
`<strong>`{=html}🌍 Language detection and combined
analysis`</strong>`{=html}
```{=html}
</summary>
```
  -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  File                                                                                                                                                                                                                          What it demonstrates
  ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -----------------------------------
  [`Detect language.py`](https://github.com/jatinkumar4148/NLP_Azure_Practice/blob/main/Detect%20language.py)                                                                                                                   Basic language detection using
                                                                                                                                                                                                                                sample text in multiple languages.

  [`Detect_language2.py`](https://github.com/jatinkumar4148/NLP_Azure_Practice/blob/main/Detect_language2.py)                                                                                                                   Language detection with realistic
                                                                                                                                                                                                                                inputs and per-document error
                                                                                                                                                                                                                                handling.

  [`Detect_Lang+Extract_KeyPhrase+Extract_Entities+Senti,mental_Analysis.py`](https://github.com/jatinkumar4148/NLP_Azure_Practice/blob/main/Detect_Lang%2BExtract_KeyPhrase%2BExtract_Entities%2BSenti%2Cmental_Analysis.py)   Combines language detection, key
                                                                                                                                                                                                                                phrase extraction, sentiment
                                                                                                                                                                                                                                analysis, and categorized entity
                                                                                                                                                                                                                                recognition through analysis
                                                                                                                                                                                                                                actions.
  -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

```{=html}
</details>
```
```{=html}
<details>
```
```{=html}
<summary>
```
`<strong>`{=html}🔑 Key phrases, sentiment, and
entities`</strong>`{=html}
```{=html}
</summary>
```
  ---------------------------------------------------------------------------------------------------------------------------------------------------------
  File                                                                                                                  What it demonstrates
  --------------------------------------------------------------------------------------------------------------------- -----------------------------------
  [`Extract_key_phrases.py`](https://github.com/jatinkumar4148/NLP_Azure_Practice/blob/main/Extract_key_phrases.py)     Extracts key phrases from sample
                                                                                                                        customer messages.

  [`Sentimental_Analysis.py`](https://github.com/jatinkumar4148/NLP_Azure_Practice/blob/main/Sentimental_Analysis.py)   Shows document-level and
                                                                                                                        sentence-level sentiment scores.

  [`Extract_Entities.py`](https://github.com/jatinkumar4148/NLP_Azure_Practice/blob/main/Extract_Entities.py)           Recognizes named entities and
                                                                                                                        prints categories and metadata.
  ---------------------------------------------------------------------------------------------------------------------------------------------------------

```{=html}
</details>
```
```{=html}
<details>
```
```{=html}
<summary>
```
`<strong>`{=html}🔗 Entity linking`</strong>`{=html}
```{=html}
</summary>
```
  -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  File                                                                                                                                                        What it demonstrates
  ----------------------------------------------------------------------------------------------------------------------------------------------------------- -----------------------------------
  [`Entity_Linking.py`](https://github.com/jatinkumar4148/NLP_Azure_Practice/blob/main/Entity_Linking.py)                                                     Linked-entity recognition through a
                                                                                                                                                              helper function.

  [`Extract_Linked_Entity.py`](https://github.com/jatinkumar4148/NLP_Azure_Practice/blob/main/Extract_Linked_Entity.py)                                       A compact linked-entity recognition
                                                                                                                                                              example.

  [`Extract_Linked_Entity_ExceptionHandling.py`](https://github.com/jatinkumar4148/NLP_Azure_Practice/blob/main/Extract_Linked_Entity_ExceptionHandling.py)   Linked-entity processing with
                                                                                                                                                              exception handling and structured
                                                                                                                                                              output.
  -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

```{=html}
</details>
```
```{=html}
<details>
```
```{=html}
<summary>
```
`<strong>`{=html}🎯 Custom text classification`</strong>`{=html}
```{=html}
</summary>
```
  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------
  File                                                                                                                              What it demonstrates
  --------------------------------------------------------------------------------------------------------------------------------- -----------------------------------
  [`Custom_Text_Classification.py`](https://github.com/jatinkumar4148/NLP_Azure_Practice/blob/main/Custom_Text_Classification.py)   Submits a custom multi-label
                                                                                                                                    classification job, polls its
                                                                                                                                    status, and prints returned labels
                                                                                                                                    and confidence scores.

  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------

**Before running:** Set the correct prediction URL, Azure key, project
name, and deployment name. The script uses a REST API job workflow, so
check that the endpoint and API version match your Azure Language setup.

```{=html}
</details>
```
```{=html}
<details>
```
```{=html}
<summary>
```
`<strong>`{=html}❓ Question answering, multi-turn context, and active
learning`</strong>`{=html}
```{=html}
</summary>
```
  -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  File                                                                                                                                                                                  What it demonstrates
  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -----------------------------------
  [`Question_Answering_normal.py`](https://github.com/jatinkumar4148/NLP_Azure_Practice/blob/main/Question_Answering_normal.py)                                                         A basic interactive
                                                                                                                                                                                        question-answering loop.

  [`Question_Answering_By_Multiturn.py`](https://github.com/jatinkumar4148/NLP_Azure_Practice/blob/main/Question_Answering_By_Multiturn.py)                                             Carries previous-question context
                                                                                                                                                                                        and presents follow-up prompts.

  [`Question_Answering_Active_Learning_synonyms.py`](https://github.com/jatinkumar4148/NLP_Azure_Practice/blob/main/Question_Answering_Active_Learning_synonyms.py)                     Adds alternate questions through an
                                                                                                                                                                                        authoring API workflow and supports
                                                                                                                                                                                        follow-up prompts.

  [`Question_Answering_Active_Learning_synonyms_FEEDBACK.py`](https://github.com/jatinkumar4148/NLP_Azure_Practice/blob/main/Question_Answering_Active_Learning_synonyms_FEEDBACK.py)   Adds user feedback to the
                                                                                                                                                                                        question-answering and
                                                                                                                                                                                        active-learning flow.
  -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

**Before running:** Configure the Azure Language question-answering
project name, deployment name, endpoint, and key. Authoring examples may
modify the configured knowledge base, so use a test project while
learning.

```{=html}
</details>
```
## 🔐 Azure configuration

The scripts use more than one credential-variable style. For a
consistent setup, prefer environment variables and avoid hardcoded
secrets.

Example pattern for Text Analytics scripts:

``` python
import os
from dotenv import load_dotenv
from azure.core.credentials import AzureKeyCredential
from azure.ai.textanalytics import TextAnalyticsClient

load_dotenv()

endpoint = os.getenv("LANGUAGE_ENDPOINT")
key = os.getenv("LANGUAGE_KEY")

if not endpoint or not key:
    raise RuntimeError(
        "Set LANGUAGE_ENDPOINT and LANGUAGE_KEY in your local .env file."
    )

client = TextAnalyticsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(key)
)
```

For scripts that currently use names such as `ENDPOINT`, `KEY`, or
`API_KEY`, update the configuration to read the appropriate environment
variables. The exact API call still depends on the script and the Azure
feature being used.

## 🧯 Troubleshooting

```{=html}
<details>
```
```{=html}
<summary>
```
`<strong>`{=html}401 / 403 --- authentication or access
error`</strong>`{=html}
```{=html}
</summary>
```
-   Confirm the key belongs to the endpoint you configured.
-   Check that the key is current and has not been revoked.
-   Confirm the `.env` file is in the directory from which the script
    loads configuration.
-   Never paste the key into a public issue or commit.

```{=html}
</details>
```
```{=html}
<details>
```
```{=html}
<summary>
```
`<strong>`{=html}404 --- endpoint, project, or deployment not
found`</strong>`{=html}
```{=html}
</summary>
```
-   Check the endpoint URL.
-   Confirm the project and deployment names match Azure.
-   Verify the required project has been deployed.
-   For custom classification, check the prediction URL and API version.

```{=html}
</details>
```
```{=html}
<details>
```
```{=html}
<summary>
```
`<strong>`{=html}ImportError / ModuleNotFoundError`</strong>`{=html}
```{=html}
</summary>
```
Activate the intended virtual environment, then install the required
dependency:

``` bash
python -m pip install azure-ai-textanalytics azure-ai-language-questionanswering azure-core requests python-dotenv
```

```{=html}
</details>
```
```{=html}
<details>
```
```{=html}
<summary>
```
`<strong>`{=html}Some documents return errors`</strong>`{=html}
```{=html}
</summary>
```
Several examples process lists of documents. Inspect each result's
`is_error` property and error details instead of assuming every document
succeeded.

```{=html}
</details>
```
```{=html}
<details>
```
```{=html}
<summary>
```
`<strong>`{=html}Question answering returns no useful
answer`</strong>`{=html}
```{=html}
</summary>
```
-   Confirm that the knowledge base contains relevant questions and
    answers or connected sources.
-   Verify the deployment name.
-   Review the confidence threshold and the follow-up context.
-   Try a test question that closely matches the configured knowledge
    base.

```{=html}
</details>
```
## 🛣️ Learning roadmap

-   [ ] Run language detection and understand language codes.
-   [ ] Explore key phrase extraction.
-   [ ] Compare document-level and sentence-level sentiment.
-   [ ] Inspect entity categories, offsets, and linked-entity matches.
-   [ ] Configure and test a custom classification deployment.
-   [ ] Run a basic question-answering example.
-   [ ] Explore multi-turn prompts and feedback-based alternate
    questions.
-   [ ] Refactor repeated configuration into shared helper code.
-   [ ] Add tests and document sample outputs.

## 🔒 Security checklist

-   [ ] Keep `.env` out of Git.
-   [ ] Keep `venv/` and other generated files out of Git.
-   [ ] Read credentials from environment variables.
-   [ ] Rotate any credential that has been exposed, even if it is
    believed to have expired.
-   [ ] Remove secrets from Git history before pushing; deleting a key
    from the latest file alone does not remove it from older commits.
-   [ ] Never bypass GitHub secret scanning to publish credentials.

## 🚧 Contributing and next steps

This is a learning project, and improvements are welcome. Useful next
steps include:

-   Add a tested `requirements.txt` with pinned package versions.
-   Standardize credential loading across all scripts.
-   Add unit tests and sample expected outputs.
-   Group scripts into folders such as `text_analytics/`,
    `custom_classification/`, and `question_answering/`.
-   Add screenshots or terminal examples using synthetic, non-sensitive
    data.

## 📄 License

No license is currently specified. Add a `LICENSE` file if you want to
define how others may reuse the code.

------------------------------------------------------------------------

::: {align="center"}
**Built for learning, experimenting, and understanding Azure AI Language
with Python.**

[⬆ Back to top](#-nlp-azure-practice)
:::
