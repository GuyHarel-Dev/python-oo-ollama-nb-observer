import json
from typing import Any
from pathlib import Path

import model_observability.core.file_utils as file_utils

from model_observability.core.chat_logger import ChatResult


def load_log_files_results(folder_path: Path) -> dict[str, list[ChatResult]]:

    log_files_results : dict[str, list[ChatResult]] = {}

    for file_path in folder_path.iterdir():

        if file_path.is_file() and file_path.suffix == ".jsonl":
            print(file_path)

            log_files_results[file_path.name] = load_log_file_results(file_path)
            pass

    print(log_files_results)
    return log_files_results


def load_log_file_results(file_path: Path) -> list[ChatResult]:

    results : list[ChatResult] = []

    jsonl_file_lines = file_utils.read_from_file(file_path).splitlines()

    for line in jsonl_file_lines:
        results.append(ChatResult(**json.loads(line)))

    return results