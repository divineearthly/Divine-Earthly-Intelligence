
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'core')))
from hybrid_engine import HybridEngine

class DisasterPredictionModule:
    def __init__(self):
        self.engine = HybridEngine()

    def identify_threats(self, sensor_type, value, temperature, humidity):
        data = {'sensor': sensor_type, 'val': value, 'temperature': temperature, 'humidity': humidity}
        return self.engine.predict(data)
