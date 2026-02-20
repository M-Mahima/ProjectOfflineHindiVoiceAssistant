# ==========================================
# HYBRID INTENT ENGINE
# ==========================================

from runtime.nlu.rule_intent import RuleIntentEngine
from runtime.nlu.indicbert_infer import IndicBERTIntentEngine


class HybridIntentEngine:

    def __init__(self):

        print("\n[NLU] Initializing…")

        self.rule_engine = RuleIntentEngine()
        self.bert_engine = IndicBERTIntentEngine()

    def infer(self, text):

        print(f"\n[NLU] Text → {text}")

        intent = self.rule_engine.infer(text)

        if intent:
            return intent

        return self.bert_engine.infer(text)