
---

# 🧪 Experiment 03: Benchmark Latency

`experiments/03_benchmark_latency.py`

```python
"""
Experiment 03: Benchmark Latency
--------------------------------
Compare FP16 vs quantized (int8/int4) inference latency for Mistral-7B.
"""

import time
import argparse
from shauffeur.models.load import load_model


def benchmark(model_name: str, quantization: str, prompt: str):
    model, tokenizer = load_model(model_name, quantization=quantization)

    inputs = tokenizer(prompt, return_tensors="pt").to(model.device)
    start = time.time()
    _ = model.generate(**inputs, max_new_tokens=32)
    latency = time.time() - start

    return latency


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--model", type=str, default="mistralai/Mistral-7B-Instruct-v0.2")
    parser.add_argument("--prompt", type=str, default="A pedestrian is detected crossing the street ahead.")
    args = parser.parse_args()

    for q in ["none", "int8", "int4"]:
        try:
            latency = benchmark(args.model, q, args.prompt)
            print(f"Quantization: {q:<5} | Latency: {latency:.3f} sec")
        except Exception as e:
            print(f"[!] Failed for quantization={q}: {e}")
