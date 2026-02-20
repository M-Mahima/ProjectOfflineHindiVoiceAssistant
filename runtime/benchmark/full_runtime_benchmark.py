# ==========================================
# FULL RUNTIME BENCHMARK
# Engineering + System View
# Non-invasive
# ==========================================

import time
import psutil
import os

from runtime.vad.vad_listener import VADListener
from runtime.processor.audio_processor import AudioProcessor
from runtime.asr.asr_onnx_infer import ASRInference
from runtime.nlu.hybrid_intent import HybridIntentEngine
from runtime.task.task_engine import TaskEngine
from runtime.tts.piper_tts import PiperTTS


def bytes_to_mb(x):
    return x / (1024 * 1024)


def main():

    process = psutil.Process(os.getpid())

    print("\n===== FULL RUNTIME BENCHMARK =====\n")

    cold_start_begin = time.time()

    vad = VADListener()
    processor = AudioProcessor()
    asr = ASRInference()
    nlu_engine = HybridIntentEngine()
    task_engine = TaskEngine()
    tts = PiperTTS()

    cold_start_time = (time.time() - cold_start_begin) * 1000
    print(f"[Cold Start Time] → {cold_start_time:.2f} ms\n")

    print("Speak a command clearly...\n")

    idle_cpu = psutil.cpu_percent(interval=1)

    total_start = time.time()

    # ---------------- VAD ----------------
    vad_start = time.time()
    audio = vad.listen()
    vad_time = (time.time() - vad_start) * 1000

    if audio is None:
        print("No speech detected.")
        return

    # ---------------- Processor + ASR ----------------
    processed = processor.process(audio)

    asr_start = time.time()
    text = asr.transcribe(processed)
    asr_time = (time.time() - asr_start) * 1000

    # ---------------- NLU ----------------
    intent_start = time.time()
    intent = nlu_engine.infer(text)
    intent_time = (time.time() - intent_start) * 1000

    # ---------------- Task ----------------
    task_start = time.time()
    response_text = task_engine.execute(intent, text)   # ✅ FIXED
    task_time = (time.time() - task_start) * 1000

    # ---------------- TTS ----------------
    tts_start = time.time()
    tts.speak(response_text)
    tts_time = (time.time() - tts_start) * 1000

    total_latency = (time.time() - total_start) * 1000

    active_cpu = psutil.cpu_percent(interval=1)
    peak_ram = bytes_to_mb(process.memory_info().rss)

    # ---------------- REPORT ----------------
    print("\n=========== PERFORMANCE REPORT ===========\n")

    print("FULL RUNTIME METRICS")
    print("------------------------------------------")
    print(f"Cold Start Time     → {cold_start_time:.2f} ms")
    print(f"End-to-End Latency  → {total_latency:.2f} ms")
    print(f"Idle CPU Usage      → {idle_cpu:.2f} %")
    print(f"Active CPU Usage    → {active_cpu:.2f} %")
    print(f"Peak RAM Usage      → {peak_ram:.2f} MB")

    print("\nPHASE BREAKDOWN")
    print("------------------------------------------")
    print(f"VAD Time            → {vad_time:.2f} ms")
    print(f"ASR Time            → {asr_time:.2f} ms")
    print(f"NLU Time            → {intent_time:.2f} ms")
    print(f"Task Time           → {task_time:.2f} ms")
    print(f"TTS Time            → {tts_time:.2f} ms")

    print("\nRecognized Text     →", text)
    print("Detected Intent     →", intent)
    print("Response Text       →", response_text)

    print("\n==========================================\n")


if __name__ == "__main__":
    main()