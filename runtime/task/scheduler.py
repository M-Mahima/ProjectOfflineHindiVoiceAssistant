# ==========================================
# LOCAL SCHEDULER
# Fully Offline | Privacy Safe
# ==========================================

import json
import os
from datetime import datetime


DATA_DIR = "runtime/task/data"
DATA_PATH = os.path.join(DATA_DIR, "reminders.json")


class Scheduler:

    def __init__(self):

        os.makedirs(DATA_DIR, exist_ok=True)

        if not os.path.exists(DATA_PATH):
            with open(DATA_PATH, "w", encoding="utf-8") as f:
                json.dump([], f)

    # --------------------------------------

    def add_reminder(self, text):

        with open(DATA_PATH, "r", encoding="utf-8") as f:
            data = json.load(f)

        data.append({
            "text": text,
            "created_at": str(datetime.now())
        })

        with open(DATA_PATH, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

        return "रिमाइंडर सेव कर लिया है"

    # --------------------------------------

    def read_reminders(self):

        with open(DATA_PATH, "r", encoding="utf-8") as f:
            data = json.load(f)

        if not data:
            return "कोई रिमाइंडर नहीं है"

        texts = [r["text"] for r in data]

        return "आपके रिमाइंडर: " + ", ".join(texts)

    # --------------------------------------

    def clear_reminders(self):

        with open(DATA_PATH, "w", encoding="utf-8") as f:
            json.dump([], f)

        return "सभी रिमाइंडर हटा दिए गए"