# ==========================================
# ASR PHASE TEST
# ==========================================

import numpy as np
from runtime.asr.asr_onnx_infer import ASRInference

print("\n[TEST] ASR Phase\n")

asr = ASRInference()

# Dummy silent audio (1 sec)
dummy_audio = np.zeros((1, 16000), dtype=np.float32)

text = asr.transcribe(dummy_audio)

print("ASR Output:", text)