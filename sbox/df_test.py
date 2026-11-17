import pandas as pd

def test():
    df = pd.read_json("data/log/gemma3_1b-2026-08-06_10-41-37-x3.jsonl.jsonl", lines=True)
    print(df.head(10))
    pass


if __name__ == "__main__":
    test()
    
    