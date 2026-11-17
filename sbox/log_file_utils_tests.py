from pathlib import Path

import model_observability.core.log_file_utils as log_file_utils


def test():
    folder_1 = r"C:\GH-ORDI\DATA\Data-Model-Observability\param-default-7x30"
    folder_2 = Path(r"C:\GH-ORDI\DATA\Data-Model-Observability")

    data = log_file_utils.load_log_files_results(folder_2)

    pass


if __name__ == "__main__":
    test()

"""
python -m sbox.log_file_utils_tests

"""