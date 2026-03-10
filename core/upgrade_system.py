import os
from datetime import datetime

class CodeModifier:
    def __init__(self, upgrades_path="proposed_upgrades"):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        self.upgrades_path = os.path.join(os.path.dirname(current_dir), upgrades_path)
        os.makedirs(self.upgrades_path, exist_ok=True)

    def generate_patch(self, component_name, suggestion):
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        content = f"# Optimized {component_name}\n# Suggestion: {suggestion}\ndef optimized_routine():\n    pass\n"
        filename = f"upgrade_{component_name}_{timestamp}.py"
        filepath = os.path.join(self.upgrades_path, filename)
        with open(filepath, "w") as f:
            f.write(content)
        return filepath