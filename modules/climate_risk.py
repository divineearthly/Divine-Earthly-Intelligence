
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'core')))
from hybrid_engine import HybridEngine

class ClimateRiskModule:
    def __init__(self):
        self.engine = HybridEngine()

    def analyze_trends(self, carbon_levels, sea_level_rise, avg_temp):
        data = {'carbon_ppm': carbon_levels, 'sea_level_mm': sea_level_rise, 'temperature': avg_temp}
        return self.engine.predict(data)
