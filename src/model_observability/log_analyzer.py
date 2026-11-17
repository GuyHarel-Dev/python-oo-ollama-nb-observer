import argparse

from model_observability.core.chat_log_analyzer import ChatLogAnalyzer


def analyse_log_files(folder_path: str):
    chat_log_analyzer = ChatLogAnalyzer()
    chat_log_analyzer.analyze_log_files(folder_path)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Analyze model observability JSONL log files.",
        epilog="""
Example:
  python -m model_observability.log_analyzer "C:/GH-ORDI/DATA/Data-Model-Observability"
        """,
    )

    parser.add_argument(
        "--log_folder",
        required=True,
        help="Path to the folder containing observation JSONL log files.",
    )

    args = parser.parse_args()

    analyse_log_files(args.log_folder)


"""
python -m model_observability.log_analyzer --log_folder="C:/GH-ORDI/DATA/Data-Model-Observability"

"""
