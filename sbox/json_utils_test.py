import json

import model_observability.core.json_utils as json_utils
import model_observability.core.file_utils as file_utils

def test():
    #folder = r"C:\GH-ORDI\DATA\Data-Model-Observability\param-default-7x30"
    folder = r"C:\GH-ORDI\DATA\Data-Model-Observability"
    data = json_utils.get_json_from_json_markdown_str(folder)

    output_file =  r"C:\GH-ORDI\DATA\Data-Model-Observability/output.txt"
    file_utils.write_to_file(output_file, data)

    pass


if __name__ == "__main__":
    test()
    pass
