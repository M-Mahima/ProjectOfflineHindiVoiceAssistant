# ==========================================
# MASTER TASK ENGINE
# Offline | Privacy Preserving
# ==========================================

from datetime import datetime
from runtime.task.scheduler import Scheduler


class TaskEngine:

    def __init__(self):

        print("\n[Task] Engine ready.")

        self.scheduler = Scheduler()

        self.water_active = False
        self.breath_active = False
        self.med_active = False

        self.notes = []
        self.list_items = []

    # --------------------------------------

    def extract_content(self, text, trigger_words):

        for word in trigger_words:
            if word in text:
                return text.split(word, 1)[1].strip()

        return ""

    # --------------------------------------

    def execute(self, intent, text):

        print(f"[Task] Intent → {intent}")

        # ==============================
        # SYSTEM CONTROL
        # ==============================

        if intent == "SYSTEM_RESTART":
            return "__RESTART__"

        if intent == "SYSTEM_SHUTDOWN":
            return "__SHUTDOWN__"

        # ==============================
        # TIME
        # ==============================

        if intent == "GET_TIME":
            now = datetime.now()
            return f"अभी {now.hour} बजकर {now.minute} मिनट हुए हैं"

        # ==============================
        # DATE
        # ==============================

        if intent == "GET_DATE":
            today = datetime.now().date()
            return f"आज की तारीख {today}"

        # ==============================
        # WEATHER (Placeholder)
        # ==============================

        if intent == "GET_WEATHER":
            return "मौसम की जानकारी अभी उपलब्ध नहीं है"

        # ==============================
        # WATER REMINDER
        # ==============================

        if intent == "SET_WATER_REMINDER":
            self.water_active = True
            return "पानी रिमाइंडर चालू कर दिया है"

        if intent == "REMOVE_WATER_REMINDER":
            self.water_active = False
            return "पानी रिमाइंडर बंद कर दिया है"

        # ==============================
        # BREATH REMINDER
        # ==============================

        if intent == "SET_BREATH_REMINDER":
            self.breath_active = True
            return "साँस रिमाइंडर चालू कर दिया है"

        if intent == "REMOVE_BREATH_REMINDER":
            self.breath_active = False
            return "साँस रिमाइंडर बंद कर दिया है"

        # ==============================
        # NOTES
        # ==============================

        if intent == "TAKE_NOTE":

            content = self.extract_content(text, ["नोट लिखो"])

            if not content:
                return "क्या नोट करना है बताइए"

            self.notes.append(content)
            return "नोट सेव कर लिया है"

        if intent == "READ_NOTES":

            if not self.notes:
                return "कोई नोट नहीं है"

            return "आपके नोट: " + ", ".join(self.notes)

        # ==============================
        # LIST
        # ==============================

        if intent == "ADD_LIST_ITEM":

            content = self.extract_content(text, ["लिस्ट में जोड़ो"])

            if not content:
                return "क्या जोड़ना है बताइए"

            self.list_items.append(content)
            return "लिस्ट में जोड़ दिया है"

        if intent == "READ_LIST":

            if not self.list_items:
                return "लिस्ट खाली है"

            return "आपकी लिस्ट: " + ", ".join(self.list_items)

        # ==============================
        # CALCULATOR
        # ==============================

        if intent == "CALCULATE":

            try:
                expression = text.replace("जोड़", "+") \
                                 .replace("घटाओ", "-") \
                                 .replace("गुणा", "*") \
                                 .replace("भाग", "/") \
                                 .replace("plus", "+") \
                                 .replace("minus", "-")

                result = eval(expression)
                return f"उत्तर है {result}"

            except:
                return "गणना समझ नहीं आई"

        # ==============================
        # CUSTOM REMINDER (JSON Based)
        # ==============================

        if intent == "SET_CUSTOM_REMINDER":

            content = self.extract_content(text, ["रिमाइंडर लगाओ"])

            if not content:
                return "क्या याद दिलाना है बताइए"

            return self.scheduler.add_reminder(content)

        if intent == "READ_CUSTOM_REMINDER":
            return self.scheduler.read_reminders()

        if intent == "REMOVE_CUSTOM_REMINDER":
            return self.scheduler.clear_reminders()

        # ==============================
        # MEDICATION
        # ==============================

        if intent == "SET_MED_TRACK":
            self.med_active = True
            return "दवाई ट्रैकिंग शुरू कर दी है"

        if intent == "STOP_MED_TRACK":
            self.med_active = False
            return "दवाई ट्रैकिंग बंद कर दी है"

        if intent == "TRIGGER_MED_REMINDER":

            if self.med_active:
                return "दवाई लेने का समय हो गया है"

            return "कोई दवाई ट्रैकिंग सक्रिय नहीं है"

        # ==============================
        # UNKNOWN
        # ==============================

        return "यह काम उपलब्ध नहीं है"