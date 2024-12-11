from enum import Enum
from pydantic import BaseModel,EmailStr

class AIProvider(str, Enum):
    open_ai = "open_ai"
    gemini_ai = "gemini_ai"

class PromptRequest(BaseModel):
    prompt: str
    ai: AIProvider