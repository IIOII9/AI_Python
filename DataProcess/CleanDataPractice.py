import os
import re
import sys

import charset_normalizer as cd


def clean_text(text: str):
    # 去掉首尾空格
    text = text.strip()

    # 将所有非字母、数字字符替换为空格
    text = re.sub(r"[^a-zA-Z0-9\s]", " ", text)

    # 将多个空格替换为一个空格
    text = re.sub(r"\s+", " ", text)

    text = text.lower()
    return text.strip()


def clean_data(input_file: str, out_file: str):
    with open(input_file, "rb") as f:
        data = f.read(20000)
        enc = cd.from_bytes(data).best().encoding or "utf-8"

    # clean_lines = set()  # 使用set去重
    clean_lines = dict()  # 保留顺序去重
    with open(input_file, "r", encoding=enc) as f:
        for line in f:
            cleaned_line = clean_text(line)
            if cleaned_line:
                clean_lines[cleaned_line] = None

    with open(out_file, "w", encoding="utf-8-sig") as f:
        for line in clean_lines:
            f.writelines(line + "\n")


def main():
    scriptDir = os.path.dirname(os.path.abspath(__file__))

    input_file = (
        sys.argv[1] if len(sys.argv) > 1 else os.path.join(scriptDir, "dirty_data.txt")
    )
    output_file = (
        sys.argv[2]
        if len(sys.argv) > 2
        else os.path.join(scriptDir, "cleaned_data.txt")
    )

    clean_data(input_file, output_file)


if __name__ == "__main__":
    main()
