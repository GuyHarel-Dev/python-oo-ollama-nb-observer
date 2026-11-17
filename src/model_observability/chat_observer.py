from pydantic import BaseModel

from model_observability.services.chat_service import ChatMessage, ChatGenerationOptions
from model_observability.services.ollama_chat_services import OllamaChatService

from model_observability.core.chat_logger import ChatLogger

import argparse
import json


class Observation(BaseModel):
    model_name: str
    prompt_path: str
    prompt_data_path: str
    log_folder: str
    options: list[ChatGenerationOptions]


def run_observation(
    observation_config_path: str,
    model_name: str,
    log_folder_path: str,
    prompt_file_path: str,
    prompt_data_file_path: str,
):

    # get observation json
    with open(observation_config_path, "r", encoding="utf-8") as f:
        observation = Observation(**json.load(f))

    observation.model_name = model_name
    observation.log_folder = log_folder_path
    observation.prompt_path = prompt_file_path
    observation.prompt_data_path = prompt_data_file_path

    # resolve the prompt to send
    prompt = ""
    with open(observation.prompt_path, "r", encoding="utf-8") as f:
        prompt = f.read()

    # resolve the prompt data do send (if any)
    prompt_content = ""

    if observation.prompt_data_path:
        with open(observation.prompt_data_path, "r", encoding="utf-8") as f:
            prompt_content = f.read()

    prompt = prompt.format(data=prompt_content)

    # run
    ollama_chat_service = OllamaChatService(observation.model_name)
    chat_logger = ChatLogger(observation.log_folder, ollama_chat_service)
    chat_message = ChatMessage(role="user", content=prompt)

    for option in observation.options:
        chat_logger.log_chats(chat_message=chat_message, chat_options=option)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--observation_config",
        required=True,
        help="Path observation json config file.",
    )

    parser.add_argument(
        "--model_name",
        required=True,
        help="Name of the model to use.",
    )

    parser.add_argument(
        "--log_folder",
        required=True,
        help="Path to the folder to create the logs.",
    )

    parser.add_argument(
        "--prompt_file",
        required=True,
        help="Path to the file containing the prompt.",
    )

    parser.add_argument(
        "--prompt_data",
        required=True,
        help="Path to the file containing optionnal data for the prompt.",
    )

    args = parser.parse_args()

    run_observation(
        args.observation_config,
        args.model_name,
        args.log_folder,
        args.prompt_file,
        args.prompt_data,
    )


"""
python -m model_observability.chat_observer --help

python -m model_observability.chat_observer \
    --observation_config="C:/GH-ORDI/PROJ/AI/Model-Observability/observations/param-temp-(0.0)-7x30.json" \
    --model_name="gemma3:1b" \
    --log_folder="C:/GH-ORDI/DATA/Data-Model-Observability" \
    --prompt_file="C:/GH-ORDI/PROJ/AI/Model-Observability/data/prompt/IDENTIFY_PDF_TEXT.txt" \
    --prompt_data="C:/GH-ORDI/PROJ/AI/Model-Observability/data/prompt_data/FICTIVE_LAMP_RECEIT_PDF_TEXT_V2.txt"


python -m model_observability.chat_observer \
    --observation_config="C:/GH-ORDI/PROJ/AI/Model-Observability/observations/classify_statement-temp-(0.0-0.8)-7x30.json" \
    --model_name="gemma3:1b" \
    --log_folder="C:/GH-ORDI/DATA/Data-Model-Observability" \
    --prompt_file="C:/GH-ORDI/PROJ/AI/Model-Observability/data/prompt/CLASSIFY_STATEMENT_V2.txt" \
    --prompt_data=""

python -m model_observability.chat_observer \
    --observation_config="C:/GH-ORDI/PROJ/AI/LLM-Model-Observability/observations/complete-sentence-temp-var-5x30.json" \
    --model_name="gemma3:1b" \
    --log_folder="C:/GH-ORDI/DATA/Data-Model-Observability" \
    --prompt_file="C:/GH-ORDI/PROJ/AI/LLM-Model-Observability/data/prompt/COMPLETE_SENTENCE.txt" \
    --prompt_data=""

"""
