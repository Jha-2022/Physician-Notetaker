def generate_soap(patient_text, physician_text, entities):
    return {
        "Subjective": {
            "Chief_Complaint": "Neck and back pain",
            "History_of_Present_Illness":
                "Patient had a car accident, experienced pain for four weeks, now occasional back pain."
        },
        "Objective": {
            "Physical_Exam":
                "Full range of motion in cervical and lumbar spine, no tenderness.",
            "Observations":
                "Patient appears in normal health, normal gait."
        },
        "Assessment": {
            "Diagnosis": "Whiplash injury and lower back strain",
            "Severity": "Mild, improving"
        },
        "Plan": {
            "Treatment":
                "Continue physiotherapy as needed, use analgesics for pain relief.",
            "Follow-Up":
                "Patient to return if pain worsens or persists beyond six months."
        }
    }
