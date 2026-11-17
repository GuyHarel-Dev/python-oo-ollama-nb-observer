from pathlib import Path

from model_observability.core.chat_logger import ChatResult


class ChatLogLoader:

    def __init__(self, log_file_folder: str):
        self.log_file_folder = Path(log_file_folder)

    def load_log_file(self, log_file_path: str) -> list[ChatResult]:

        file_path = Path(self.log_file_folder) / log_file_path

        if not file_path.exists():
            raise FileNotFoundError(
                f"ChatLogLoader: '{log_file_path}' does not exist."
            )
        
        with open(file_path, "r", encoding="utf-8") as f:
            chat_results = [ChatResult.model_validate_json(line) for line in f]

        return chat_results
    
    def load_log_file_folder(self) -> dict[str, list[ChatResult]]:

        log_files: dict[str, list[ChatResult]] = {}

        folder = Path(self.log_file_folder)

        for file in folder.iterdir():
            if file.is_file() and file.suffix == '.jsonl':
                log_files[file.name] = self.load_log_file(file.name)

        return log_files
