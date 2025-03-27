from dataclasses import dataclass
from typing import Optional

@dataclass
class Voice:
    provider: str
    voiceId: Optional[str] = None
    speed: Optional[float] = None

