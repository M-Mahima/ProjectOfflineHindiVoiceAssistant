# ==========================================
# MEDICAL TASK ENGINE
# ==========================================

import json
import os


PATIENT_PATH = "runtime/task/data/medical/patients.json"


class MedicalEngine:

    def __init__(self):

        print("[Medical] Engine ready.")

        os.makedirs(os.path.dirname(PATIENT_PATH), exist_ok=True)

        if not os.path.exists(PATIENT_PATH):
            with open(PATIENT_PATH, "w", encoding="utf-8") as f:
                json.dump([], f)

    def add_patient(self, name):

        with open(PATIENT_PATH, "r", encoding="utf-8") as f:
            data = json.load(f)

        data.append({"name": name})

        with open(PATIENT_PATH, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

        return "पेशेंट जोड़ दिया गया है"

    def view_patients(self):

        with open(PATIENT_PATH, "r", encoding="utf-8") as f:
            data = json.load(f)

        if not data:
            return "कोई पेशेंट दर्ज नहीं है"

        names = [p["name"] for p in data]

        return "पेशेंट सूची: " + ", ".join(names)