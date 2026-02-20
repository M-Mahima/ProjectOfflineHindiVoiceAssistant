# ==========================================
# UNIVERSAL PIPER TTS ENGINE (FIXED DLL LOAD)
# Windows + Linux ARM
# Voice: hi_IN-pratham-medium
# ==========================================

import subprocess
import tempfile
import os
import platform
import sounddevice as sd
import soundfile as sf


class PiperTTS:

    def __init__(self):

        print("[TTS] Initializing Piper...")

        system = platform.system().lower()

        if system == "windows":
            self.bin_dir = os.path.abspath("bin/piper/windows")
            self.piper_exe = os.path.join(
                self.bin_dir, "piper.exe"
            )
        else:
            self.bin_dir = os.path.abspath("bin/piper/arm")
            self.piper_exe = os.path.join(
                self.bin_dir, "piper"
            )

            if os.path.exists(self.piper_exe):
                os.chmod(self.piper_exe, 0o755)

        self.model_path = os.path.abspath(
            "models/tts/piper/hi_IN-pratham-medium.onnx"
        )

        if not os.path.exists(self.piper_exe):
            raise FileNotFoundError(
                f"Piper executable not found:\n{self.piper_exe}"
            )

        if not os.path.exists(self.model_path):
            raise FileNotFoundError(
                f"Voice model not found:\n{self.model_path}"
            )

        print("[TTS] Piper ready.")

    # ----------------------------------------------------

    def speak(self, text):

        if not text or text.strip() == "":
            return

        print(f"[TTS] Speaking → {text}")

        with tempfile.NamedTemporaryFile(
            suffix=".wav",
            delete=False
        ) as tmp_wav:

            wav_path = tmp_wav.name

        try:

            # Ensure Windows can find DLLs
            env = os.environ.copy()
            env["PATH"] = self.bin_dir + ";" + env["PATH"]

            subprocess.run(
                [
                    self.piper_exe,
                    "--model", self.model_path,
                    "--output_file", wav_path
                ],
                input=text.encode("utf-8"),
                cwd=self.bin_dir,
                env=env,
                check=True
            )

            data, samplerate = sf.read(wav_path)
            sd.play(data, samplerate)
            sd.wait()

        finally:
            if os.path.exists(wav_path):
                os.remove(wav_path)