from model_observability.services.chat_service import ChatMessage, ChatGenerationOptions
from model_observability.services.ollama_chat_services import OllamaChatService

from model_observability.core.chat_logger import ChatLogger

from data import PROMPTS
from data import CONTENTS


def test_send_chats_with_temps():

    model = "gemma3:1b"
    data_path = "C:/GH-ORDI/DATA/Data-Model-Observability"

    number_samples=50

    ollama_chat_service = OllamaChatService(model)

    chat_logger = ChatLogger(data_path, ollama_chat_service)

    content = PROMPTS.IDENTIFY_PDF_TEXT.format(text=CONTENTS.FICTIVE_LAMP_RECEIT_PDF_TEXT_V1)

    chat_message = ChatMessage(role="user", content=content)
    chat_options_list = [
        ChatGenerationOptions(temperature=0.0),
        ChatGenerationOptions(temperature=0.1),
        ChatGenerationOptions(temperature=0.5),
        ChatGenerationOptions(temperature=0.8),
        ChatGenerationOptions(temperature=1.0)]

    for chat_options in chat_options_list:
        chat_logger.log_chats(chat_message=chat_message, chat_options=chat_options, number_samples=number_samples)

    pass

def test_send_chats():

    model = "gemma3:1b"
    data_path = "C:/GH-ORDI/DATA/Data-Model-Observability"

    number_samples=10

    ollama_chat_service = OllamaChatService(model)

    chat_logger = ChatLogger(data_path, ollama_chat_service)

    content = PROMPTS.IDENTIFY_PDF_TEXT.format(text=CONTENTS.FICTIVE_LAMP_RECEIT_PDF_TEXT_V1)

    chat_message = ChatMessage(role="user", content=content)
    chat_options = ChatGenerationOptions()

    chat_logger.log_chats(chat_message=chat_message, chat_options=chat_options, number_samples=number_samples)

    pass


if __name__ == "__main__":
    test_send_chats_with_temps()

