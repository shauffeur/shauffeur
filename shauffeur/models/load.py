
"""Model loading helper. Uses Hugging Face transformers when available.
   This loader supports a 'mock' mode for fast local dev without models.
"""
import os
try:
    from transformers import AutoModelForCausalLM, AutoTokenizer
    HF_AVAILABLE = True
except Exception:
    HF_AVAILABLE = False

class MockModel:
    def generate(self, prompt, max_new_tokens=64):
        # deterministic mock response for testing
        return "Mock Explanation: The vehicle detected a pedestrian at 7 meters; slowing recommended."

def load_model(model_id=None, device='cpu', load_in_4bit=False, mock=False):
    if mock or not HF_AVAILABLE:
        print('[load_model] Running in MOCK mode (no HF model loaded).')
        return MockModel(), None
    tokenizer = AutoTokenizer.from_pretrained(model_id)
    model = AutoModelForCausalLM.from_pretrained(model_id, device_map='auto', load_in_4bit=load_in_4bit)
    return model, tokenizer
