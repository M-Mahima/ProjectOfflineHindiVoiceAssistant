# ==========================================
# MAIN ENTRY — FINAL VERSION
# Dual-Mode Wakeword Integrated
# Restart + Shutdown Supported
# ==========================================

from runtime.vad.vad_listener import VADListener
from runtime.processor.audio_processor import AudioProcessor
from runtime.asr.asr_onnx_infer import ASRInference

from runtime.nlu.hybrid_intent import HybridIntentEngine
from runtime.task.task_engine import TaskEngine
from runtime.tts.piper_tts import PiperTTS

from runtime.core.wake_controller import WakeController


def main():

    print("\n=== Hindi Voice Assistant ===\n")

    vad = VADListener()
    processor = AudioProcessor()
    asr = ASRInference()

    nlu = HybridIntentEngine()
    task_engine = TaskEngine()
    tts = PiperTTS()

    wake = WakeController(
        wakeword="सुनो साथी",
        timeout=8
    )

    while True:

        audio = vad.listen()

        if audio is None:
            continue

        processed = processor.process(audio)
        text = asr.transcribe(processed)

        print("\n[ASR OUTPUT]")
        print(text)

        mode, cleaned_text = wake.process(text)

        # Wakeword only
        if mode == "activate":
            print("[Wakeword] Activated")
            tts.speak("जी बताइए")
            continue

        # Wakeword + command
        if mode == "execute":

            print(f"[Wakeword] Command → {cleaned_text}")

            tts.speak("जी")

            intent = nlu.infer(cleaned_text)
            response = task_engine.execute(intent, cleaned_text)

            if response == "__SHUTDOWN__":
                tts.speak("डिवाइस बंद किया जा रहा है")
                break

            if response == "__RESTART__":
                tts.speak("सिस्टम रीस्टार्ट किया जा रहा है")
                continue

            print(f"\n[RESPONSE] {response}")
            tts.speak(response)
            continue

        print("[Wakeword] Not detected. Ignored.")


if __name__ == "__main__":
    main()