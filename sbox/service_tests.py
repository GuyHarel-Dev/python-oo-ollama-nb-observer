from model_observability.services.chat_service import ChatMessage, ChatGenerationOptions

from model_observability.services.ollama_chat_services import OllamaChatService


def test_send_chat():
    model_name = "gemma3:1b"

    service = OllamaChatService(model_name)

    message = ChatMessage(role="user", content="are you there ?")
    options = ChatGenerationOptions(temperature=0.7, top_k=40, top_p=0.9, seed=123)

    response = service.send_chat(message, options)

    print(response)


if __name__ == "__main__":
    test_send_chat()
