from dataclasses import dataclass
from typing import Optional

@dataclass
class Message:
    role: str
    content: Optional[str]
    