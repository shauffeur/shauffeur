
"""Simple inference runner that accepts structured events and returns natural-language explanations."""
from ..data.preprocess import convert_event_to_prompt
from ..models.load import load_model

def explain_event(event: dict, model_cfg: dict, mock=False):
    model, tokenizer = load_model(model_cfg.get('model_id'), device=model_cfg.get('device','cpu'),
                                 load_in_4bit=model_cfg.get('load_in_4bit',False), mock=mock)
    prompt = convert_event_to_prompt(event)
    if mock or tokenizer is None:
        return model.generate(prompt)
    inputs = tokenizer(prompt, return_tensors='pt').to('cuda' if model_cfg.get('device','cpu')=='cuda' else 'cpu')
    outputs = model.generate(**inputs, max_new_tokens=128)
    return tokenizer.decode(outputs[0], skip_special_tokens=True)
