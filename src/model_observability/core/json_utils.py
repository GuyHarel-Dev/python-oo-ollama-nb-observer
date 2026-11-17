import re

def get_json_from_json_markdown_str(content_str: str | None) -> list[tuple[str, str]]:

    if content_str is None:
        return []

    content_json_str = remove_json_markdown(content_str)

    key_values: list[tuple[str, str]] = []

    pairs = re.findall(r'"([^"]+)"\s*:\s*"([^"]*)"', content_json_str)

    for key, value in pairs:
        key_values.append((key, value))

    return key_values


def remove_json_markdown(content_str: str) -> str:
    return content_str.replace("\n", "").removeprefix("```json").removesuffix("```")
