
from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, Optional

@dataclass
class Message:
    sender: str
    receiver: str
    content: Any
    message_type: str
    timestamp: datetime = field(default_factory=datetime.now)
    context: Optional[dict] = field(default_factory=dict)
