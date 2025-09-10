
def test_mock_inference():
    from shauffeur.inference.run import explain_event
    sample = {"event":"pedestrian_detected","distance_m":7,"speed_kmh":45}
    cfg = {"model_id":"mock","device":"cpu","load_in_4bit":False}
    out = explain_event(sample, cfg, mock=True)
    assert "Mock Explanation" in out
