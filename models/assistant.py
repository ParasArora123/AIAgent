from dataclasses import MISSING, dataclass, fields
from typing import Optional, List

# Need to use relative imports to avoid circular imports
from .voice import Voice
from .transcriber import Transcriber
from .model import Model

@dataclass
class Assistant:
    name: Optional[str] = None
    transcriber: Optional[Transcriber] = None
    model: Optional[Model] = None
    voice: Optional[Voice] = None
    firstMessage: Optional[str] = None
    clientMessages: Optional[List[str]] = None
    serverMessages: Optional[List[str]] = None
    silenceTimeoutSeconds: Optional[float] = None
    maxDurationSeconds: Optional[float] = None
    backgroundSound: Optional[str] = None
    backgroundDenoisingEnabled: Optional[bool] = False
    modelOutputInMessagesEnabled: Optional[bool] = False
    voicemailMessage: Optional[str] = None
    endCallMessage: Optional[str] = None
    endCallPhrases: Optional[List[str]] = None
    compliancePlan: Optional[List[bool]] = None
    firstMessageInterruptionsEnabled: Optional[bool] = False
    firstMessageMode: Optional[str] = "assistant-speaks-first"