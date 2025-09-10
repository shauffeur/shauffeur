"""
Experiment 02 — CARLA Simulation Bridge
---------------------------------------

This script connects to a running CARLA simulator, listens for perception
events (pedestrians, vehicles, traffic lights), converts them into ADAS-like
events, and runs them through Shauffeur's inference pipeline.

Usage:
    # Start CARLA first:
    ./CarlaUE4.sh -quality-level=Low -world-port=2000

    # Run this experiment (mock mode for fast testing):
    python experiments/02_carla_bridge.py --mock

    # Run with real Mistral (GPU recommended):
    python experiments/02_carla_bridge.py
"""

import argparse
import random
import time
import yaml

try:
    import carla
    CARLA_AVAILABLE = True
except ImportError:
    CARLA_AVAILABLE = False

from shauffeur.data.preprocess import convert_event_to_prompt
from shauffeur.inference.run import explain_event


def connect_to_carla(host="127.0.0.1", port=2000, timeout=10):
    if not CARLA_AVAILABLE:
        raise RuntimeError("CARLA not installed. Install carla Python API first.")
    client = carla.Client(host, port)
    client.set_timeout(timeout)
    world = client.get_world()
    return world


def simulate_event_from_actor(actor):
    """
    Convert a CARLA actor into an ADAS-like event.
    """
    if actor.type_id.startswith("walker.pedestrian"):
        return {
            "event": "pedestrian_detected",
            "distance_m": round(actor.get_location().x, 1),  # simplification
            "speed_kmh": random.randint(30, 60),
        }
    elif actor.type_id.startswith("vehicle."):
        return {
            "event": "vehicle_detected",
            "distance_m": round(actor.get_location().x, 1),
            "speed_kmh": random.randint(40, 100),
        }
    elif "traffic_light" in actor.type_id:
        state = actor.state if hasattr(actor, "state") else "unknown"
        return {"event": "traffic_light", "state": str(state)}
    else:
        return {"event": "unknown"}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--mock", action="store_true", help="Run without HF models (fast).")
    parser.add_argument("--host", type=str, default="127.0.0.1")
    parser.add_argument("--port", type=int, default=2000)
    parser.add_argument("--ticks", type=int, default=5, help="Number of simulation ticks to run")
    args = parser.parse_args()

    cfg = yaml.safe_load(open("shauffeur/config/mistral.yaml"))

    if CARLA_AVAILABLE:
        world = connect_to_carla(host=args.host, port=args.port)
        actors = world.get_actors()
    else:
        print("[WARN] CARLA not available, using synthetic events.")
        actors = None

    for i in range(args.ticks):
        print(f"\n=== Tick {i+1} ===")
        if actors:
            actor = random.choice(actors)
            event = simulate_event_from_actor(actor)
        else:
            # Synthetic event for mock testing
            event = {"event": "pedestrian_detected", "distance_m": 6 + i, "speed_kmh": 40 + i}

        prompt = convert_event_to_prompt(event)
        print("--- Prompt ---")
        print(prompt)

        explanation = explain_event(event, cfg, mock=args.mock)
        print("\nExplanation:\n", explanation)

        time.sleep(1.0)


if __name__ == "__main__":
    main()
