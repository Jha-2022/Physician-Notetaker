def analyze_sentiment(patient_text):
    text = patient_text.lower()

    if "pain" in text or "rough" in text or "discomfort" in text:
        return {
            "Sentiment": "Anxious",
            "Intent": "Seeking reassurance"
        }

    return {
        "Sentiment": "Neutral",
        "Intent": "Providing information"
    }
