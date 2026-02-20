# ==========================================
# INDICBERT FALLBACK ENGINE (Placeholder)
# ==========================================

class IndicBERTIntentEngine:

    def __init__(self):
        print("\n[NLU] IndicBERT fallback ready.")

    def infer(self, text):

        print("[IndicBERT] No rule matched.")
        return "UNKNOWN_INTENT"