"""
Template experiment for Shauffeur
- Config-driven
- Reproducible (seeded, logged)
- Minimal dependency: standard library + PyYAML

Usage:
    python experiments/00_template_experiment.py --config experiments/configs/template.yaml

This template demonstrates how to structure an experiment that explains an ADAS event using a small LLM.
It intentionally avoids heavy model calls; instead it sketches the hooks where inference and quantized models would be used.
"""
import argparse
import logging
import random
import yaml
import time
from pathlib import Path

LOG = logging.getLogger("shauffeur.template")


def set_seed(seed: int):
    random.seed(seed)


def load_config(path: Path):
    with open(path, "r") as f:
        return yaml.safe_load(f)


def run_experiment(cfg: dict):
    """Run a minimal experiment flow:
    - load event (simulated)
    - run model INFERENCE hook (placeholder)
    - produce explanation (placeholder)
    - log timings and seed
    """
    seed = cfg.get("seed", 42)
    set_seed(seed)
    LOG.info("Experiment seed=%s", seed)

    start = time.time()
    # Simulate an ADAS event: object detected at 12m, relative velocity -3 m/s
    event = {"type": "object_detected", "distance_m": 12.0, "rel_vel_m_s": -3.0}
    LOG.info("Loaded event: %s", event)

    # Inference hook (replace with real model call)
    # model = load_model(cfg['model'])
    # explanation = model.explain_event(event)
    explanation = f"Detected object at {event['distance_m']} m approaching at {abs(event['rel_vel_m_s'])} m/s."

    elapsed = time.time() - start
    LOG.info("Explanation: %s", explanation)
    LOG.info("Elapsed time: %.3fs", elapsed)

    # Output artifact path
    out_dir = Path(cfg.get("output_dir", "experiments/out"))
    out_dir.mkdir(parents=True, exist_ok=True)
    with open(out_dir / "explanation.txt", "w") as f:
        f.write(explanation + "\n")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", type=Path, required=False, default=Path("experiments/configs/template.yaml"))
    args = parser.parse_args()

    logging.basicConfig(level=logging.INFO)
    cfg = load_config(args.config)
    run_experiment(cfg)


if __name__ == "__main__":
    main()
