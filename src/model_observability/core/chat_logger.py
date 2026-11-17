from pathlib import Path
import re
from datetime import datetime
import json

from pydantic import BaseModel

from model_observability.services.chat_service import (
    ChatService,
    ChatGenerationOptions,
    ChatMessage,
    ChatResponse,
)


class ChatResult(BaseModel):
    chat_options: ChatGenerationOptions
    chat_response: ChatResponse


class ChatLogger:
    "Allow to send prompts and store responses in a file"

    def __init__(self, file_path_str: str, chat_service: ChatService):
        self.file_path = Path(file_path_str)
        self.chat_service = chat_service

    def log_chats(
        self,
        chat_message: ChatMessage,
        chat_options: ChatGenerationOptions
    ):

        model_name = self._remove_invalid_file_char(self.chat_service.model_name)
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

        log_file_name = f"{model_name}-{timestamp}-x{chat_options.num_chats}"

        file_data_path = f"{self.file_path}/{log_file_name}.jsonl"

        # send chats and save response in jsonl file
        for index in range(chat_options.num_chats):
            print("log_chats=", index)
            chat_resp = self.chat_service.send_chat(
                chat_message=chat_message, chat_options=chat_options
            )

            chat_result = ChatResult(
                chat_options=chat_options, chat_response=chat_resp
            )
            with open(file_data_path, "a", encoding="utf-8") as f:
                f.write(json.dumps(chat_result.model_dump()))
                f.write("\n")


    def _remove_invalid_file_char(self, file_name: str):
        return re.sub(r'[<>:"/\\|?*]', "_", file_name)
