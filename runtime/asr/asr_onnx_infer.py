# ==========================================
# ASR ONNX INFERENCE ENGINE (DYNAMIC)
# IndicWav2Vec2 Hindi
# Offline | Stable | ARM + PC
# ==========================================

import onnxruntime as ort
import numpy as np
import json
import time


class ASRInference:

    def __init__(self):

        print("[ASR] Loading ONNX model…")

        sess_options = ort.SessionOptions()
        sess_options.intra_op_num_threads = 1
        sess_options.inter_op_num_threads = 1

        self.session = ort.InferenceSession(
            "onnx_models/asr/indicwav2vec2_hindi.onnx",
            sess_options=sess_options,
            providers=["CPUExecutionProvider"]
        )

        self.input_name = self.session.get_inputs()[0].name
        self.output_name = self.session.get_outputs()[0].name

        with open(
            "models/asr/indicwav2vec2_hindi/vocab.json",
            "r",
            encoding="utf-8"
        ) as f:
            vocab = json.load(f)

        self.id2token = {v: k for k, v in vocab.items()}

        print("[ASR] Ready.")

    def _ctc_decode(self, logits):

        pred_ids = np.argmax(logits, axis=-1)[0]

        decoded = []
        prev = None

        for idx in pred_ids:
            if idx != prev:
                token = self.id2token.get(idx, "")
                if token not in ["[PAD]", "<pad>"]:
                    decoded.append(token)
            prev = idx

        text = "".join(decoded)
        text = text.replace("|", " ").strip()

        return text

    def transcribe(self, audio_tensor):

        start = time.time()

        outputs = self.session.run(
            [self.output_name],
            {self.input_name: audio_tensor}
        )

        logits = outputs[0]
        text = self._ctc_decode(logits)

        latency = (time.time() - start) * 1000

        print(f"[ASR] {latency:.2f} ms")
        print(f"[ASR] TEXT → {text}")

        return text