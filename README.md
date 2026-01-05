# 🩺 Physician-Notetaker

## 📌 Overview
The Physician Notetaker Console is a command-line–based medical documentation assistant designed to process physician–patient conversations and convert them into structured, clinically meaningful outputs. The project helps automate clinical documentation tasks such as medical entity extraction, summarization, sentiment analysis, and SOAP note generation.

This project is useful for understanding how Natural Language Processing (NLP) techniques can be applied in healthcare workflows while maintaining clarity and structure in medical records.

---


## 🎯 Key Features

* 🩺 Medical Named Entity Recognition (NER)Extracts important clinical entities such as symptoms, injuries, dates, and treatments from conversations.

* 📝 Conversation SummarizationGenerates concise summaries from long physician–patient dialogues.

* 😊 Sentiment AnalysisAnalyzes the patient’s emotional tone to identify distress, improvement, or neutrality.

* 📋 SOAP Note GenerationAutomatically converts conversations into structured SOAP (Subjective, Objective, Assessment, Plan) clinical notes.

* 💻 CLI-Based InterfaceSimple and safe multiline input system for entering real-world medical conversations.

---

## 🗂️ Project Structure

```
physician-notetaker-console/
│
├── main.py              # Entry point of the application
├── ner.py               # Medical entity extraction logic
├── summarizer.py        # Text summarization module
├── sentiment.py         # Sentiment analysis module
├── soap_generator.py    # SOAP note generation module
├── utils.py             # Helper utilities (input handling, text processing)
├── requirements.txt     # Project dependencies
└── README.md            # Project documentation

```

---

## ⚙️ Installation & Setup

# 1️⃣ Clone the Repository
```
git clone https://github.com/your-username/physician-notetaker-console.git
cd physician-notetaker-console
```

# 2️⃣ Create a Virtual Environment (Optional but Recommended)

```
python -m venv venv

# On Windows:
venv\Scripts\activate

# On Linux:
source venv/bin/activate
```

# 3️⃣ Install Dependencies

```
pip install -r requirements.txt
```

---

# ▶️ How to Run

```
python main.py
```

* Paste or type the physician–patient conversation when prompted.

* End input as instructed in the CLI.

* The system will output:

    * Extracted medical entities

    * Conversation summary

    * Sentiment analysis

    * Generated SOAP note
 
---

## 🧪 Sample Use Case

* Automating clinical documentation

* NLP practice for healthcare datasets

* Medical text processing experiments

* Resume or academic project demonstration

---

## 🚀 Technologies Used

* Python 3

* spaCy / NLP libraries (for NER)

* Rule-based & ML-based text processing

* Command Line Interface (CLI)

---

## 📈 Future Improvements

* Integration with transformer-based models (BERT, ClinicalBERT)

* Web-based UI

* Support for audio-to-text input

* Medical coding (ICD-10) integration

* Enhanced clinical safety checks

---

## 👨‍💻 Author

* Rishi Jha
* B.Tech CSE, VIT Bhopal University
* Interests: NLP, Healthcare AI, Data Science
