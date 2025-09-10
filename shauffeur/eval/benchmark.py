
"""Benchmark utilities (scaffold). Measures simple time to run explanations."""
import time
from ..inference.run import explain_event

def simple_latency_test(event, cfg, runs=5, mock=True):
    times = []
    for _ in range(runs):
        t0 = time.time()
        _ = explain_event(event, cfg, mock=mock)
        times.append(time.time()-t0)
    return {'runs': runs, 'times': times, 'mean_s': sum(times)/len(times)}
