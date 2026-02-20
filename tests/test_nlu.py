# ==========================================
# NLU PHASE TEST
# ==========================================

from runtime.nlu.hybrid_intent import HybridIntentEngine

print("\n[TEST] NLU Phase\n")

nlu = HybridIntentEngine()

samples = [
    "समय क्या है",
    "पानी याद दिलाओ",
    "नोट लिखो यह टेस्ट है",
    "रिमाइंडर लगाओ दवा लेना"
]

for text in samples:
    intent = nlu.infer(text)
    print(f"Text: {text} → Intent: {intent}")