
class BaseAgent:
    def __init__(self, role, goal):
        self.role = role
        self.goal = goal

    def process(self, task):
        raise NotImplementedError('Subclasses must implement process()')
