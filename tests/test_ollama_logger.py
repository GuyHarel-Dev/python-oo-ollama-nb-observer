from unittest.mock import Mock

from model_observability.observability.ollama_logger import OllamaLogger
from model_observability.models.text_generation_options import TextGenerationOptions


def test_log_chats():
    log_file_path = "./tests"
    model_name = "gemma3:1b"
    prompt_text =  "hello are you there?"
    number_samples = 1
    text_gen_options = TextGenerationOptions(temperature=0.7, top_k=40, top_p=0.9, seed=123)

    
