# 入力されたテキストから特定の文字を取り除く
import re

def extract_char(text: str, chars: list) -> str:
    """
    引き数：text（入力するテキスト）, chars（取り除く文字と正規表現のリスト）
    返り値：text（特定の文字を取り除いたテキスト）
    """
    for char in chars:
        # text = text.replace(char, "")  # 文字列だけのやつ
        text = re.sub(char, "", text)  # 正規表現はこっちじゃないと入らない

    return text

def read_file(file_path: str) -> str:
    """
    引き数：file_path（読み込むファイルのパス）
    返り値：text（読み込んだテキスト）
    """
    with open(file_path, "r", encoding="utf-8") as f:
        text = f.read()

    return text

# print(text)
# 普通に指定するだけのとき
text = read_file("README.md")  # 読み込むファイルのパスを指定
lst = ["### ", "## ", "# ", "- ", " "]  # 「#」は多い順で指定して、空白まで含めた方が良いっぽい
print(extract_char(text, lst))

# 正規表現を使って[]や()を取り除くとき
# text = read_file("README.md")  # 省略
# lst = ["### ", "## ", "# ", "- ", " ", r"\[.*?\]", r"\(.*?\)",]  # 「[]」や「()」を単なる文字として認識するための「\」、出来るだけ小さい範囲で探すために「?」を付けた方が良いらしい
lst = ["### ", "## ", "# ", "- ", " ", r"\[", r"\]", r"\(.*?\)",]  # 消しすぎたとこ（[]()の並びだと文字が残らなくて項目が分からなくなる）を修正したやつ
print(extract_char(text, lst))