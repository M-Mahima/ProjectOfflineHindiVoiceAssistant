# ==========================================
# SILERO VAD LISTENER — DYNAMIC SAFE
# Mic → Speech Segment
# Offline | ARM + PC
# ==========================================

import torch
import sounddevice as sd
import numpy as np


class VADListener:

    def __init__(self):

        print("[VAD] Loading Silero…")

        self.model, _ = torch.hub.load(
            repo_or_dir="snakers4/silero-vad",
            model="silero_vad",
            force_reload=False
        )

        self.sample_rate = 16000
        self.frame_size = 512

        print("[VAD] Ready.")

    def listen(self):

        print("[VAD] Listening…")

        audio_buffer = []
        speech_detected = False

        silence_frames = 0
        silence_threshold = 8   # ~250ms

        stream = sd.InputStream(
            samplerate=self.sample_rate,
            channels=1,
            dtype="float32",
            blocksize=self.frame_size
        )

        with stream:

            while True:

                frame, _ = stream.read(self.frame_size)
                frame = np.squeeze(frame)

                audio_tensor = torch.from_numpy(frame)

                speech_prob = self.model(
                    audio_tensor,
                    self.sample_rate
                ).item()

                if speech_prob > 0.6:
                    speech_detected = True
                    silence_frames = 0
                    audio_buffer.append(frame)

                elif speech_detected:
                    silence_frames += 1
                    audio_buffer.append(frame)

                    if silence_frames >= silence_threshold:
                        print("[VAD] Speech captured.")
                        break

        if not audio_buffer:
            return None

        return np.concatenate(audio_buffer)