
"""Preprocessing utilities to convert ADAS logs into training / inference prompts."""
import json

def convert_event_to_prompt(event: dict) -> str:
    """Simple mapper that turns a structured ADAS event into an LLM prompt."""
    # event example: {"event":"pedestrian_detected","distance_m":7,"speed_kmh":45}
    lines = []
    lines.append(f"ADAS event: {event.get('event')}")
    for k,v in event.items():
        if k == "event": continue
        lines.append(f"{k}: {v}")
    lines.append("")
    lines.append("Task: Provide a concise natural-language explanation and recommended action.")
    return "\n".join(lines)

if __name__ == '__main__':
    sample = {"event":"pedestrian_detected","distance_m":7,"speed_kmh":45}
    print(convert_event_to_prompt(sample))
