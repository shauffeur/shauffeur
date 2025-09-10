
"""First experiment: simulate ADAS events and get LLM explanations.

Usage:
    python experiments/01_explain_event.py --mock
    python experiments/01_explain_event.py
"""
import argparse, yaml, json
from shauffeur.data.preprocess import convert_event_to_prompt
from shauffeur.inference.run import explain_event
from shauffeur.eval.benchmark import simple_latency_test

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--mock', action='store_true', help='Run without loading HF models (fast).')
    args = parser.parse_args()
    cfg = yaml.safe_load(open('shauffeur/config/mistral.yaml'))
    sample_event = {"event":"pedestrian_detected","distance_m":7,"speed_kmh":45}
    prompt = convert_event_to_prompt(sample_event)
    print('--- Prompt ---')
    print(prompt)
    print('--- Running inference ---')
    explanation = explain_event(sample_event, cfg, mock=args.mock)
    print('\nExplanation:\n', explanation)
    print('\n--- Latency benchmark (mock) ---')
    stats = simple_latency_test(sample_event, cfg, runs=5, mock=args.mock)
    print(stats)

if __name__ == '__main__':
    main()
