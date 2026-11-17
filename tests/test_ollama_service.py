from unittest.mock import Mock

from model_observability.services.chat_service import ChatGenerationOptions
from model_observability.services.chat_service import ChatMessage

from model_observability.services.ollama_chat_services import (
    OllamaChatService,
)

from ollama import (
    Message as OllamaMessage,
    ChatResponse as OllamaChatResponse,
)


def test_send_chat():
    model_name = "gemma3:1b"
    message_role = "tester"
    message_content = "this is the content"
    prompt_eval_count = 1111
    eval_count = 2222
    total_duration = 3333
    prompt_eval_duration = 4444
    eval_duration = 5555

    ollama_message = OllamaMessage(role=message_role, content=message_content)

    ollama_response  = OllamaChatResponse(
        model=model_name,
        message=ollama_message,
        prompt_eval_count=prompt_eval_count,
        eval_count=eval_count,
        total_duration=total_duration,
        prompt_eval_duration=prompt_eval_duration,
        eval_duration=eval_duration,
    )

    service = OllamaChatService(model_name)
    service.client.chat = Mock(return_value=ollama_response )

    chat_message = ChatMessage(role="user", content="are you there ?")
    chat_options = ChatGenerationOptions(temperature=0.7, top_k=40, top_p=0.9, seed=123)

    response = service.send_chat(chat_message, chat_options)

    service.client.chat.assert_called_once()

    assert response.model == model_name
    assert response.role == message_role
    assert response.content == message_content
    assert response.prompt_tokens == prompt_eval_count
    assert response.inference_tokens == eval_count
    assert response.duration == total_duration
    assert response.prompt_tokens_eval_time == prompt_eval_duration
    assert response.inference_tokens_eval_time == eval_duration
