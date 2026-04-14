import csv
from pathlib import Path

# 获取当前文件路径
base_path = Path(__file__).resolve().parent
# 如果不存在 文件夹 csv_data 则创建，有就跳过
csv_path = base_path / "csv_data"
csv_path.mkdir(parents=True, exist_ok=True)

# 通过传统文件读写来创建csv --- 省略

# 通过 csv库 来写入csv                                        此处需要定义newline=""来让默认换行符变为空串，否则会多重换行
with open(csv_path / "name_list.csv", "w", encoding="utf-8", newline="") as f:
    # 创建csv写入对象
    writer = csv.DictWriter(f, fieldnames=["姓名", "年龄", "性别", "爱好"])
    # 写入表头
    writer.writeheader()
    # 写入数据
    name_list = [{"姓名": "张三", "年龄": 18, "性别": "男", "爱好": "Java"},
            {"姓名": "李四", "年龄": 19, "性别": "女", "爱好": "Python"},
            {"姓名": "王五", "年龄": 20, "性别": "男", "爱好": "C, C++"}]
    writer.writerows(name_list)

# 通过 csv库 来读取csv
with open(csv_path / "name_list.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row)