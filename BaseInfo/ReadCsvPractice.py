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


def testReadByIterrows(fileName: str):
    with open(fileName, "rb") as f:
        data = f.read(2000)
        enc = cd.from_bytes(data).best().encoding or "utf-8"
    df = pandas.read_csv(fileName, encoding=enc)
    for idx, row in df.iterrows():
        print(idx)
        print(f"ID:{row['ID']}, EntType: {row['EntType']}")
        print(row.index)  # row.index为属性，该行的列名集合
        nIndex = row.index.get_loc("EntType")
        print(row.values[nIndex])
        rowDict = row.to_dict()
        print(rowDict)
        rowItems = row.items()
        for col, value in rowItems:
            print(col, value)  # col:列名， value:值


def testReadByItertuples(fileName: str):
    with open(fileName, "rb") as f:
        data = f.read(2000)
        enc = cd.from_bytes(data).best().encoding or "utf-8"
    df = pandas.read_csv(fileName, encoding=enc)
    for row in df.itertuples(index=True, name="Row"):
        print(row.Index, row.ID, row.EntType)
        print(row[0], row[2])


def testReadByIterItems(fileName: str):
    with open(fileName, "rb") as f:
        data = f.read(2000)
        enc = cd.from_bytes(data).best().encoding or "utf-8"
    df = pandas.read_csv(fileName, encoding=enc)
    for colName, colSeries in df.items():
        print(f"Col Name: {colName}")
        for idx, val in colSeries.items():
            print(idx, val)


def testReadByloc(fileName: str):
    with open(fileName, "rb") as f:
        data = f.read(200000)
        enc = cd.from_bytes(data).best().encoding or "utf-8"
    df = pandas.read_csv(fileName, encoding=enc)
    # 按位置访问(更快、更显示)
    nLen = len(df)
    for i in range(nLen):
        row = df.iloc[i]  # 返回Series(与iterrows类似，但更直接)
        print(row)
        print(i, row["ID"])

    # 按标签访问
    for lable in df.index:
        row = df.loc[lable]  # 返回Series(根据行标签)
        print(lable, row.to_dict())


def testReadbynumpy(fileName: str):
    with open(fileName, "rb") as f:
        data = f.read(200000)
        enc = cd.from_bytes(data).best().encoding or "utf-8"
    df = pandas.read_csv(fileName, encoding=enc)
    arr = df.to_numpy()
    print(arr.shape)  # shape:行数，列数
    for i in range(arr.shape[0]):
        row = arr[i]
        # row 是一个numpy 1d array,按列顺序
        print(i, row[0], row[1])  # 需要知道列顺序


def testWritecsv():
    df = pandas.DataFrame(
        {
            "ID": [101, 102, 103],
            "Name": ["Tom", "Jerry", "Spike"],
            "Score": [88.5, 91.0, 77.3],
        }
    )
    # 创建目录并导出 CSV
    os.makedirs("export", exist_ok=True)
    df.to_csv(
        "export/students.csv", index=False, encoding="utf-8-sig"
    )  # index=False不输出默认行号
    print("✅ CSV 文件已成功创建：export/students.csv")


def readFile(fileName: str, chunk_rows=100000):
    with open(fileName, "rb") as f:
        data = f.read(200000)
        enc = cd.from_bytes(data).best().encoding or "utf-8"
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
    # testReadByColName(fileName4Read)
    # testReadByIterrows(fileName4Read)
    # testReadByItertuples(fileName4Read)
    # testReadByIterItems(fileName4Read)
    # testReadByloc(fileName4Read)
    # testReadbynumpy(fileName4Read)
    testWritecsv()


if __name__ == "__main__":
    main()
