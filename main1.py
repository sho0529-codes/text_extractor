import os
import re
import tkinter as tk

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

def main():
    # 初期設定
    root = tk.Tk()
    root.title("text_extractor/main1.py")
    input_text = None
    output_text = None

    # 完了ボタン
    def push_button():
        nonlocal input_text, output_text
        input_text = left_text.get("1.0", tk.END)
        print(input_text)
        output_text = replace_char(input_text)
        # text.config(text=output_text)  # そもそもtextにいじれるもんがない
        right_text.delete("1.0", tk.END)  # 普通は消してからinsertするらしい
        right_text.insert("1.0", output_text)

    # 文字表示1
    label1 = tk.Label(root, text="下に文章")
    label1.pack()

    # 完了ボタン
    button = tk.Button(root, text="完了", command=push_button)
    button.pack()

    # 入力欄
    left_text = tk.Text(root, width=100)
    left_text.pack(side=tk.LEFT)

    # 出力
    right_text = tk.Text(root, width=100)
    right_text.pack(side=tk.LEFT)

    # メインループ
    root.mainloop()

main()