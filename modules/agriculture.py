
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'core')))
from hybrid_engine import HybridEngine

class AgricultureModule:
    def __init__(self):
        self.engine = HybridEngine()

    def assess_crop_health(self, soil_moisture, temperature, humidity):
        data = {'soil_moisture': soil_moisture, 'temperature': temperature, 'humidity': humidity}
        return self.engine.predict(data)
