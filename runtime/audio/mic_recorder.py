import sounddevice as sd
import numpy as np


class MicRecorder:
    """
    Silero-compatible microphone recorder
    Optimised for ARM + PC deployment
    """

    def __init__(self, samplerate=16000):
        self.samplerate = samplerate
        self.frame_samples = 512   # REQUIRED for Silero VAD

    def record_frame(self):
        """
        Records one 512-sample frame
        (~32 ms audio)
        """

        audio = sd.rec(
            self.frame_samples,
            samplerate=self.samplerate,
            channels=1,
            dtype="float32"
        )

        sd.wait()

        return audio.flatten()
