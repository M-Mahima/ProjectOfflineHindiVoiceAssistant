# ==========================================
# SIMPLE HINDI RULE INTENT ENGINE
# Offline | Privacy Preserving
# ==========================================

class RuleIntentEngine:

    def __init__(self):

        print("\n[NLU] Rule engine ready.")

        self.rules = {

            # TIME
            "समय": "GET_TIME",
            "कितना बजा": "GET_TIME",
            "टाइम": "GET_TIME",

            # DATE
            "तारीख": "GET_DATE",
            "आज कौन सा दिन": "GET_DATE",

            # WEATHER
            "मौसम": "GET_WEATHER",
            "तापमान": "GET_WEATHER",

            # WATER REMINDER
            "पानी याद": "SET_WATER_REMINDER",
            "पानी हटाओ": "REMOVE_WATER_REMINDER",
            "पानी बंद": "REMOVE_WATER_REMINDER",

            # BREATH REMINDER
            "साँस याद": "SET_BREATH_REMINDER",
            "साँस हटाओ": "REMOVE_BREATH_REMINDER",
            "साँस बंद": "REMOVE_BREATH_REMINDER",

            # NOTES
            "नोट लिखो": "TAKE_NOTE",
            "नोट पढ़ो": "READ_NOTES",

            # LIST
            "लिस्ट में जोड़ो": "ADD_LIST_ITEM",
            "लिस्ट दिखाओ": "READ_LIST",

            # CALCULATOR
            "जोड़": "CALCULATE",
            "घटाओ": "CALCULATE",
            "गुणा": "CALCULATE",
            "भाग": "CALCULATE",
            "plus": "CALCULATE",
            "minus": "CALCULATE",

            # CUSTOM REMINDER
            "रिमाइंडर लगाओ": "SET_CUSTOM_REMINDER",
            "रिमाइंडर हटाओ": "REMOVE_CUSTOM_REMINDER",
            "मेरे रिमाइंडर": "READ_CUSTOM_REMINDER",

            # MEDICATION
            "दवाई शुरू": "SET_MED_TRACK",
            "दवाई याद": "TRIGGER_MED_REMINDER",
            "दवाई बंद": "STOP_MED_TRACK",

            # SYSTEM CONTROL
            "रीस्टार्ट": "SYSTEM_RESTART",
            "डिवाइस बंद": "SYSTEM_SHUTDOWN",
            "बंद हो जाओ": "SYSTEM_SHUTDOWN",
        }

    def infer(self, text):

        for phrase, intent in self.rules.items():

            if phrase in text:
                print(f"[Rule] Matched → {intent}")
                return intent

        return None