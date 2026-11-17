from pathlib import Path

def test():
    prompt_path = "data/prompt/IDENTIFY_PDF_TEXT.txt"
    text_path = "data/text/FICTIVE_LAMP_RECEIT_PDF_TEXT_V1.txt"

    prompt_text = ""
    with open(prompt_path, "r", encoding="utf-8") as f:
        prompt_text = f.read()

    #print (prompt_text)

    text = ""
    with open(text_path, "r", encoding="utf-8") as f:
        text = f.read()

    #print (text)

    prompt = prompt_text.format(text=text)
    print(prompt)

if __name__ == "__main__":
    test()
