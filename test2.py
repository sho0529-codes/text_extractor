# 入力されたテキストから特定の文字を取り除く

import re

def replace_char(text: str, mode = 0) -> str:
    """
    引き数：text（入力するテキスト）, mode（たぶんあとでいじるとこ）
    返り値：text（特定の文字を取り除いたテキスト）
    """
    replace_lst = [["- ", "・"], ["###", "<3>"], ["##", "<2>"], ["#", "<1>"]]  # 置き換えるもの
    extract_lst = [r"\[", r"\]", r"\(.*?\)",]  # 取り除くもの

    for old, new in replace_lst:
        text = text.replace(old, new)

    for char in extract_lst:
        text = re.sub(char, "", text)  # 正規表現はこっちじゃないと入らない

    return text

def read_file(file_path: str) -> str:
    """
    引き数：file_path（読み込むファイルのパス）
    返り値：text（読み込んだテキスト）
    """
    with open(file_path, "r", encoding="utf-8") as f:
        text = f.read()
    print(f"{file_path} is read")

    return text

def save_file(file_path: str, text: str) -> str:
    """
    引き数：file_path（保存するファイルのパス）, text（保存するテキスト）
    返り値：text（保存したテキスト）
    """
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(text)
    print(f"{file_path} is saved")

    return text

text = read_file("README.md")  # 読み込むファイルのパスを指定

out = replace_char(text)
save_file("test2_output1.txt", out)