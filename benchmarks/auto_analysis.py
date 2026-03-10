import time
import os
import psutil

def get_memory_usage():
    process = psutil.Process(os.getpid())
    return process.memory_info().rss / (1024 * 1024)

class PerformanceAnalyzer:
    def __init__(self, latency_threshold=10.0, memory_threshold=500.0):
        self.latency_threshold = latency_threshold
        self.memory_threshold = memory_threshold

    def profile_component(self, component_name, func, *args, **kwargs):
        start_mem = get_memory_usage()
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        end_mem = get_memory_usage()
        latency = (end_time - start_time) * 1000
        
        report = {
            'name': component_name,
            'latency_ms': latency,
            'memory_mb': end_mem,
            'is_bottleneck': latency > self.latency_threshold,
            'issue': []
        }
        if latency > self.latency_threshold:
            report['issue'].append(f"High Latency: {latency:.2f}ms")
        return report

    def generate_bottleneck_report(self, reports):
        bottlenecks = [r for r in reports if r['is_bottleneck']]
        if not bottlenecks: return None
        slowest = max(bottlenecks, key=lambda x: x['latency_ms'])
        return {
            'slowest_component': slowest['name'],
            'summary': f"Optimization required for {slowest['name']}. {slowest['issue'][0]}"
        }