from utils import split_conversation
from ner import extract_medical_entities
from sentiment import analyze_sentiment
from soap_generator import generate_soap
import json


def collect_multiline_input():
    print("\nPaste the conversation below.")
    print("Type END on a new line when finished:\n")

    lines = []
    while True:
        line = input()
        if line.strip() == "END":
            break
        lines.append(line)

    return "\n".join(lines)


def main():
    print("\n🩺 PHYSICIAN NOTETAKER – CONSOLE VERSION")
    print("-" * 60)

    text = collect_multiline_input()
    convo = split_conversation(text)

    patient_text = convo["patient_text"]
    physician_text = convo["physician_text"]

    print("\n⏳ Processing...\n")

    medical_info = extract_medical_entities(patient_text, physician_text)
    sentiment = analyze_sentiment(patient_text)
    soap = generate_soap(patient_text, physician_text, medical_info)

    print(json.dumps(medical_info, indent=2))
    print("\n" + json.dumps(sentiment, indent=2))
    print("\n" + json.dumps(soap, indent=2))

    print("\n✅ Analysis Complete")


if __name__ == "__main__":
    main()
