
import sys
import os

# Add project root to sys.path for internal imports
sys.path.append(os.getcwd())

from core.hybrid_engine import HybridEngine
from agents.multi_agent import MultiAgentSystem
from modules.orchestrator import DomainOrchestrator
from ai_connectors.factory import ConnectorFactory
import self_improvement

def run_comprehensive_demo():
    print('=== Divine-Earthly-Intelligence End-to-End Demo ===\n')

    # a. Test Hybrid Intelligence Engine
    print('[1/5] Testing Hybrid Intelligence Engine...')
    engine = HybridEngine()
    res_sym = engine.predict({'temperature': 40, 'humidity': 10}) # Symbolic Trigger
    res_stat = engine.predict({'temperature': 25, 'humidity': 50}) # Statistical fallback
    print(f'   - Symbolic Result: {res_sym}')
    print(f'   - Statistical Result: {res_stat}\n')

    # b. Test Multi-Agent System
    print('[2/5] Running Multi-Agent Workflow...')
    mas = MultiAgentSystem()
    mas_result = mas.run_workflow('Develop a drought mitigation plan for East Africa')
    print(f'   - MAS Final Output: {mas_result}\n')

    # c. Test Domain Orchestrator
    print('[3/5] Running Domain-Specific Analysis...')
    orch = DomainOrchestrator()
    agri_res = orch.route_request('agriculture', soil_moisture=10, temperature=38, humidity=15)
    climate_res = orch.route_request('climate', carbon_levels=415, sea_level_rise=3.4, avg_temp=1.5)
    print(f'   - Agriculture Risk: {agri_res}')
    print(f'   - Climate Risk: {climate_res}\n')

    # d. Test Self-Improvement Loop
    print('[4/5] Running Self-Improvement Benchmark...')
    improvement_suggestion = self_improvement.run_improvement_loop()
    print(f'   - Improvement Suggestion: {improvement_suggestion}\n')

    # e. Test AI Connector Factory
    print('[5/5] Testing AI Connectors...')
    openai_sim = ConnectorFactory.get_connector('openai')
    local_sim = ConnectorFactory.get_connector('local')
    print(f'   - {openai_sim.generate_text("Hello AI")}')
    print(f'   - {local_sim.generate_text("Status check")}')

    print('\n=== Demo Completed Successfully ===')

if __name__ == "__main__":
    run_comprehensive_demo()
