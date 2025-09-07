# 入力されたテキストから特定の文字を取り除く

import re
import os

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

def select_file(folder_path: str = "input") -> str:
    files_lst = os.listdir(folder_path)  # フォルダ内のファイル名をリストで取得
    for i in range(len(files_lst)):  # 選択肢の表示
        print(f"{i}：{files_lst[i]}")

    while True:
        select_index = int(input("select num: "))  # 選択肢の入力
        if 0 <= select_index < len(files_lst):
            break
        else:
            print("retry")

    return folder_path + "/" + files_lst[select_index]

folder_path = "test3_input"  # フォルダのパスを指定
input_file = select_file(folder_path)  # フォルダ内のファイルを選択
# print(input_file)

text = read_file(input_file)  # 読み込むファイルのパスを指定
out = replace_char(text)
save_file("test3_output/test3_output1.txt", out)