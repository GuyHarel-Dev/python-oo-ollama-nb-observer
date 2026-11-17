from typing import Any
from pathlib import Path

import json
from os import PathLike

def write_to_file(file_data_path: str, file_data: Any, json_dump: bool = False):
    path = Path(file_data_path)
    with open(path, "a", encoding="utf-8") as f:
        if json_dump:
            f.write(json.dumps(file_data))
        else:
            f.write(file_data + "\n")


def read_from_file(file_data_path: str | PathLike[str]) -> str:
    with Path(file_data_path).open("r", encoding="utf-8") as f:
        return f.read()