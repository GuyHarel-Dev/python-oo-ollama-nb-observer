from pydantic import BaseModel
from typing import Any
from pydantic import BaseModel

from abc import ABC, abstractmethod # abc = abstract base class


class ChatMessage(BaseModel):
    role: str
    content: str


class ChatResponse(BaseModel):
    model: str | None = None
    role: str | None = None
    content: str | None = None

    prompt_tokens: int | None = None
    inference_tokens: int | None = None

    duration: int  | None = None
    prompt_tokens_eval_time: int | None = None
    inference_tokens_eval_time: int | None = None

    generated_token_log_probabilities: Any | None = None


class ChatGenerationOptions(BaseModel):
    num_chats: int = 0
    temperature: float = 0.8
    top_k: int = 40
    top_p: float = 0.9
    seed: int | None = None

    def __str__(self) -> str:
        return f"n: {self.num_chats}, :{self.temperature}, k:{self.top_k}, p:{self.top_p}, s:{self.seed}"


class ChatService(ABC):
    "Base class for a chat service"

    def __init__(self, model_name: str):
        self.model_name = model_name

    @abstractmethod
    def send_chat(self, chat_message: ChatMessage, chat_options: ChatGenerationOptions) -> ChatResponse:
        ... 


"""
    @property
    @abstractmethod
    def model_name(self) -> str:
"""