from model_observability.core.chat_log_analyzer import ChatLogAnalyzer
from model_observability.core.chat_log_loader import ChatLogLoader

import model_observability.core.json_utils as json_utils

import json

def tests():

    folder_path = "C:/GH-ORDI/DATA/Data-Model-Observability"

    chat_log_analyzer = ChatLogAnalyzer()

    chat_log_analyzer.analyze_log_files(folder_path)

    pass

def content_tests():
    loader = ChatLogLoader("C:/GH-ORDI/DATA/Data-Model-Observability")
    results = loader.load_log_file_folder()

    global_key_values: dict[str, str] = {}

    for _, chat_results in results.items():
        for result in chat_results:
            result_key_values  = json_utils.extract_key_values(result.chat_response.content)

            for key, value in result_key_values:
                if key not in global_key_values:
                    global_key_values[key] = value

    print(json.dumps(list(global_key_values.keys())))

        

if __name__ == "__main__":
    #test_load_log_file()
    content_tests()
