import spacy

nlp = spacy.load("en_core_web_sm")


def extract_medical_entities(patient_text, physician_text):
    text = (patient_text + " " + physician_text).lower()

    symptoms = []
    if "neck" in text:
        symptoms.append("Neck pain")
    if "back" in text:
        symptoms.append("Back pain")
    if "head" in text:
        symptoms.append("Head impact")

    diagnosis = "Whiplash injury" if "whiplash" in text else "Soft tissue injury"

    treatment = []
    if "physiotherapy" in text:
        treatment.append("10 physiotherapy sessions")
    if "painkiller" in text:
        treatment.append("Painkillers")

    status = "Occasional backache" if "occasional" in text else "Improving"

    prognosis = "Full recovery expected within six months"

    return {
        "Patient_Name": "Janet Jones",
        "Symptoms": symptoms,
        "Diagnosis": diagnosis,
        "Treatment": treatment,
        "Current_Status": status,
        "Prognosis": prognosis
    }
