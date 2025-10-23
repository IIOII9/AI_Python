import os
import sys

import charset_normalizer as cd
import pandas


def getEncoding(fileName: str):
    with open(fileName, "rb") as f:
        data = f.read(200000)
        enc = cd.from_bytes(data).best().encoding or "utf-8"
        return enc


def outPutCsvCols(fileName: str):
    enc = getEncoding(fileName)
    df = pandas.read_csv(fileName, encoding=enc)
    print(df.columns.to_list())
    for col in df.columns:
        print(col)


def testReadCSVParam(fileName: str):
    with open(fileName, "rb") as f:
        data = f.read(200000)
        enc = cd.from_bytes(data).best().encoding or "utf-8"
    df = pandas.read_csv(
        fileName,
        encoding=enc,
        usecols=[0, 1],  # 只读出前两列
        names=["A", "B"],  # 为前两列取别名
        header=None,  # 当没有别名时跳过标题行
        skiprows=1,  # 跳过指定行
    )
    print(df.columns)  # 这样只读出两列


def testReadByColName(fileName: str):
    with open(fileName, "rb") as f:
        data = f.read(200000)
        enc = cd.from_bytes(data).best().encoding or "utf-8"
    df = pandas.read_csv(fileName, encoding=enc, names=["A", "B"])  # usecols=[0, 1],
    print("✅ 读取的列:", df.columns.tolist())
    for row in df.itertuples(index=False):
        print(f"A={row.A}, B = {row.B}")


def readFile(fileName: str, chunk_rows=100000):
    with open(fileName, "rb") as f:
        data = f.read(200000)
        enc = cd.from_bytes(data).best().encoding | "utf-8"
        print(enc)
        return pandas.read_csv(
            fileName, encoding=enc, chunksize=chunk_rows, engine="python"
        )


def main():
    fileName4Read = ""
    if len(sys.argv) < 2:
        print("用法： python CharDetectParactice.py csv文件路径")
        # 获取当前脚本所在目录
        scriptDir = os.path.dirname(os.path.abspath(__file__))
        fileName4Read = os.path.join(scriptDir, "DeductionRules.csv")
        # return 1
    else:
        fileName4Read = sys.argv[1]
    if not os.path.exists(fileName4Read):
        print(f"{fileName4Read} 文件不存在")
        return

    ##outPutCsvCols(fileName4Read)
    testReadByColName(fileName4Read)


if __name__ == "__main__":
    main()
