
"""CAN bus demo adapter (scaffold): convert CAN logs to ADAS events."""
def parse_can_line(line: str):
    # Very small placeholder parser.
    # Real parser would parse IDs and payloads to detect events.
    if "PED" in line:
        return {"event":"pedestrian_detected","distance_m":8,"speed_kmh":40}
    return {"event":"unknown"}
