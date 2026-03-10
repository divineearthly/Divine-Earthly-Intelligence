from core.upgrade_system import CodeModifier
from agents.optimizer import OptimizerAgent
from agents.message_hub import MessageHub

class EvolutionOrchestrator:
    def __init__(self):
        self.modifier = CodeModifier()
        self.optimizer = OptimizerAgent()

    def run_cycle(self, benchmark_data):
        suggestion = self.optimizer.process_task(benchmark_data.get('summary'))
        proposal_path = self.modifier.generate_patch(benchmark_data.get('slowest_component'), suggestion)
        print(f"Proposed Upgrade saved: {proposal_path}")
        return proposal_path