
import sys
import os
from datetime import datetime

# Ensure local imports work
sys.path.append(os.path.dirname(__file__))

from planner import Planner
from research import Research
from critic import Critic
from optimizer import Optimizer

class Message:
    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

class MessageBus:
    def __init__(self):
        self.agents = {}
    def register_agent(self, name, instance):
        self.agents[name] = instance
    def send(self, message):
        if message.receiver in self.agents:
            return self.agents[message.receiver].process(message.content)
        return 'Error: Receiver not found'

class MultiAgentSystem:
    def __init__(self):
        self.bus = MessageBus()
        self.bus.register_agent('Planner', Planner())
        self.bus.register_agent('Research', Research())
        self.bus.register_agent('Critic', Critic())
        self.bus.register_agent('Optimizer', Optimizer())

    def run_workflow(self, query):
        print(f'Starting workflow for: {query}')
        plan = self.bus.send(Message('User', 'Planner', query))
        data = self.bus.send(Message('Planner', 'Research', plan[0]))
        feedback = self.bus.send(Message('Research', 'Critic', data))
        final = self.bus.send(Message('Critic', 'Optimizer', feedback))
        return final
