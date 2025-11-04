import csv
import json
import os

import charset_normalizer as cd
import pandas


def get_enc(file_name: str):
    with open(file_name, "rb") as f:
        data = f.read(200000)
        return cd.from_bytes(data).best().encoding or "utf-8"


def json_to_csv(json_file: str, csv_file: str):
    enc = get_enc(json_file)
    with open(json_file, "r", encoding=enc) as f:
        data = json.load(f)
    # 确保数据是列表格式
    if isinstance(data, dict):
        data = [data]
    elif not isinstance(data, list):
        raise ValueError(f"文件格式错误：{json_file}")
    # 提取所有键名(表头)
    keys = set()
    for item in data:
        if isinstance(item, dict):
            keys.update(item.keys())

    keys = sorted(keys)

    # 写入CSV
    # with open(csv_file, 'w', newline='', encoding='utf-8-sig') as f:
    #     writer = csv.DictWriter(f, fieldnames=keys)
    #     writer.writeheader()
    #     for item in data:
    #         writer.writerow(item)
    df = pandas.DataFrame(data)
    df.to_csv(csv_file, index=False, encoding="utf-8-sig")


def batch_convert_json_to_csv(input_dir, out_dir):
    if not os.path.exists(out_dir):
        os.makedirs(out_dir)

    for filename in os.listdir(input_dir):
        if filename.endswith(".json"):
            json_path = os.path.join(input_dir, filename)
            csv_path = os.path.join(out_dir, filename.replace(".json", ".csv"))

            try:
                json_to_csv(json_path, csv_path)
            except Exception as e:
                print(f"转换失败{filename}:{e}")

    print("\n done")


if __name__ == "__main__":
    scriptDir = os.path.dirname(os.path.abspath(__file__))
    input_folder = os.path.join(scriptDir, "data")
    output_folder = os.path.join(scriptDir, "output_csv")

    batch_convert_json_to_csv(input_folder, output_folder)
