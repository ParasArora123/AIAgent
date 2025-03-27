from dataclasses import dataclass, asdict
from typing import Optional, List, Dict, Any

@dataclass
class Transcriber:
    provider: str
    model: Optional[str] = None # Required if provider is "openai"
    language: Optional[str] = None