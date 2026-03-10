
from base_agent import BaseAgent

class Optimizer(BaseAgent):
    def __init__(self):
        super().__init__('Optimizer', 'Refine outputs based on feedback')

    def process(self, feedback):
        return f'Output refined based on: {feedback}'
