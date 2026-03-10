
from base_agent import BaseAgent

class Critic(BaseAgent):
    def __init__(self):
        super().__init__('Critic', 'Evaluate outputs for quality and accuracy')

    def process(self, output):
        return f'Score: 8/10. Improvement needed on detail for: {output}'
