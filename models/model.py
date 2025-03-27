from dataclasses import dataclass
from typing import Optional, List
from .message import Message

@dataclass
class Model:
    provider: str
    model: Optional[str] = None
    emotionRecognitionEnabled: Optional[bool] = None
    knowledgeBaseId: Optional[str] = None
    maxTokens: Optional[float] = None
    temperature: Optional[float] = None
    toolIds: Optional[List[str]] = None
    numFastTurns: Optional[float] = None
    messages: Optional[Message] = None # This includes the role and content of the system prompt

    