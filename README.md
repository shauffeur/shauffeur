
# Shauffeur

**Shauffeur** — an open-source research project: small/edge LLMs (Mistral / Mixtral) applied to ADAS explainability, reasoning, and edge optimization.

This scaffold includes:
- ROS2 node skeleton to integrate with Autoware/ROS2.
- Simple inference backend (Hugging Face + bitsandbytes) example for local dev.
- Data preprocessing stub for ADAS event logs.
- A first experiment: `experiments/01_explain_event.py` — simulates ADAS events and runs a local LLM inference pipeline (mocked by default).
- Quickstart and instructions to run locally.

> NOTE: This scaffold does **not** include model weights. Follow Quickstart to download models (Hugging Face) or use `llama.cpp` for CPU quantized runs.
