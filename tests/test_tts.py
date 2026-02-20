# ==========================================
# TTS PHASE TEST
# ==========================================

from runtime.tts.piper_tts import PiperTTS

print("\n[TEST] TTS Phase\n")

tts = PiperTTS()
tts.speak("यह एक परीक्षण वाक्य है")