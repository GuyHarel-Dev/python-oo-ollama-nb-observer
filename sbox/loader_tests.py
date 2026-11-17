from model_observability.core.chat_log_loader import ChatLogLoader

def test_load_log_file():

    log_file_folder = "C:/GH-ORDI/DATA/Data-Model-Observability"

    loader = ChatLogLoader(log_file_folder=log_file_folder)

    log_entry = loader.load_log_file("gemma3_1b-2026-08-31_09-06-57-x10.jsonl")

    print("log_entry len=", len(log_entry))
    print("log_entry=", log_entry)
    pass

def test_load_log_folder():

    log_file_folder = "C:/GH-ORDI/DATA/Data-Model-Observability/2026-08-31"

    loader = ChatLogLoader(log_file_folder=log_file_folder)

    log_files = loader.load_log_file_folder()

    print("chat results files:", [k for k in log_files.keys()])
    print("chat results in files:", [len(v) for v in log_files.values()])

if __name__ == "__main__":
    test_load_log_folder()

"""

"""