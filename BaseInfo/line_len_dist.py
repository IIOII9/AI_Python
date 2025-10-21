import random
import string
from collections import Counter
from pathlib import Path


def generate_big_file(path: str, rows: int = 100_000, max_cols: int = 2000):
    """生成随机文本文件， 每行长度0~max_cols之间随机变化， 行数为row"""
    with open(path, "w", encoding="utf-8") as f:
        for _ in range(rows):
            line_len = random.randint(0, max_cols)
            line = "".join(
                random.choices(string.ascii_letters + string.digits, k=line_len)
            )
            f.write(line + "\n")
    print(f"已生成{rows} 行测试文件 -> {path}")


def line_length_distribution(src: str, dst_csv: str | None = None):
    cnt = Counter()
    with open(src, "r", encoding="utf-8") as f:
        for line in f:
            length = len(line.rstrip("\n\r"))
            cnt[length] += 1

    print("行长度分布情况:")
    for length in sorted(cnt):
        print(f"长度 {length}: {cnt[length]} 行")

    # 可选： 保存为CSV文件
    if dst_csv:
        with open(dst_csv, "w", encoding="utf-8") as f:
            f.write("length,count\n")
            for l in sorted(cnt):
                f.write(f"{l},{cnt[l]}\n")

    return cnt


if __name__ == "__main__":
    # 生成测试文件
    FILE = "test.txt"
    CSV = "line_len_dist.csv"

    if not Path(FILE).exists():
        generate_big_file(FILE)

    # 计算行长度分布
    counter = line_length_distribution(FILE, dst_csv=CSV)
