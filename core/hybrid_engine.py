
import logging

# Setup basic logging
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')
logger = logging.getLogger('HybridEngine')

class SymbolicReasoning:
    """Handles rule-based logic for agricultural risks."""
    def evaluate_rules(self, data):
        temp = data.get('temperature', 0)
        humidity = data.get('humidity', 100)
        
        # Rule: if temperature > 35 and humidity < 20, set risk to 'High'
        if temp > 35 and humidity < 20:
            return 'High'
        return None

class StatisticalInference:
    """Simulates an AI model call returning a mock prediction score."""
    def predict(self, data):
        # Mock statistical logic: higher temperature slightly increases predicted risk score
        base_score = 0.3
        temp_factor = (data.get('temperature', 25) - 20) * 0.02
        score = min(1.0, max(0.0, base_score + temp_factor))
        return 'High' if score > 0.7 else 'Moderate' if score > 0.4 else 'Low'

class HybridEngine:
    """Orchestrates Symbolic and Statistical models."""
    def __init__(self):
        self.symbolic = SymbolicReasoning()
        self.statistical = StatisticalInference()

    def predict(self, data):
        logger.info(f'Processing input data: {data}')
        
        # 1. Run Symbolic Check
        symbolic_result = self.symbolic.evaluate_rules(data)
        if symbolic_result:
            logger.info('Decision made via Symbolic Rules (High Risk Triggered).')
            return {"prediction": symbolic_result, "method": "symbolic"}
        
        # 2. Run Statistical Inference
        statistical_result = self.statistical.predict(data)
        logger.info('Decision made via Statistical Inference.')
        return {"prediction": statistical_result, "method": "statistical"}

# Test the engine if run as a script
if __name__ == '__main__':
    engine = HybridEngine()
    
    # Test Case 1: Triggering Symbolic Rule
    input_1 = {'temperature': 40, 'humidity': 15}
    print(f'Test 1: {engine.predict(input_1)}')

    # Test Case 2: Falling back to Statistical Inference
    input_2 = {'temperature': 28, 'humidity': 45}
    print(f'Test 2: {engine.predict(input_2)}')
