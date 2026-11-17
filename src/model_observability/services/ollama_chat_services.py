from typing import Any, Mapping

from model_observability.services.chat_service import (
    ChatService,
    ChatMessage,
    ChatResponse,
    ChatGenerationOptions,
)


from ollama import (
    Client,
    Message as OllamaMessage,
    ChatResponse as OllamaChatResponse,
)


class OllamaChatServiceResponse(ChatResponse):

    def __init__(self, chat_response: OllamaChatResponse):
        super().__init__(
            model=chat_response.model,
            role=chat_response.message.role,
            content=chat_response.message.content,
            prompt_tokens=chat_response.prompt_eval_count,
            inference_tokens=chat_response.eval_count,
            duration=chat_response.total_duration,
            prompt_tokens_eval_time=chat_response.prompt_eval_duration,
            inference_tokens_eval_time=chat_response.eval_duration,
        )


class OllamaChatService(ChatService):
    "Send prompt to Ollama and receive response"

    def __init__(self, model_name: str):
        super().__init__(model_name)
    
    def send_chat(
        self, chat_message: ChatMessage, chat_options: ChatGenerationOptions
    ) -> OllamaChatServiceResponse:

        client = Client()

        # map chat service classes to Ollama classes
        ollama_message: list[OllamaMessage] = [
            OllamaMessage(role=chat_message.role, content=chat_message.content)
        ]
        ollama_options: Mapping[str, Any] = chat_options.model_dump()

        ollama_response: OllamaChatResponse = (
            client.chat(  # pyright: ignore[reportUnknownMemberType]
                self.model_name, ollama_message, options=ollama_options
            )
        )

        # map response returned
        service_response: OllamaChatServiceResponse = OllamaChatServiceResponse(
            chat_response=ollama_response
        )

        return service_response


"""


"""
