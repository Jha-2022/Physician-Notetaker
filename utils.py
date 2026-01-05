
def split_conversation(text):
    patient_lines = []
    physician_lines = []

    for line in text.split("\n"):
        line = line.strip()

        if line.lower().startswith("patient:"):
            patient_lines.append(line.replace("Patient:", "").strip())

        elif line.lower().startswith("physician:"):
            physician_lines.append(line.replace("Physician:", "").strip())

    return {
        "patient_text": " ".join(patient_lines),
        "physician_text": " ".join(physician_lines)
    }
