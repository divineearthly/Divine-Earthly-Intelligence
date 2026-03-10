
from base_agent import BaseAgent

class Planner(BaseAgent):
    def __init__(self):
        super().__init__('Planner', 'Decompose complex tasks into actionable steps')

    def process(self, task):
        return [f'Step 1: Analyze {task}', f'Step 2: Collect data for {task}', f'Step 3: Finalize {task}']
