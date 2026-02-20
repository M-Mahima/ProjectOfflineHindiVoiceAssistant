# ==========================================
# AUDIO PROCESSOR — DYNAMIC LENGTH
# No trimming
# ARM + PC safe
# ==========================================

import numpy as np
import time


class AudioProcessor:

    def process(self, audio):

        start = time.time()

        if np.max(np.abs(audio)) > 0:
            audio = audio / np.max(np.abs(audio))

        audio = audio.astype(np.float32)
        audio = np.expand_dims(audio, axis=0)

        latency = (time.time() - start) * 1000

        print(f"[Processor] Done → {latency:.2f} ms")
        print(f"[Processor] Shape → {audio.shape}")

        return audio