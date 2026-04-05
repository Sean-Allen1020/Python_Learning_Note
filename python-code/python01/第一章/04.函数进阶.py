# 位置传参 -- 传参位置必须与函数一致
from typing import Any, Callable


def func_1(name, age, height):
    return {"姓名": name, "年龄": age, "身高": height}


person = func_1("张三", 23, 172)


# 关键字传参 -- 传参位置随意，但参数名必须与函数一致
def func_2(goods, price, amount):
    return {"商品": goods, "价格": price, "数量": amount}


goods_info = func_2(amount=10, goods="可乐", price=3)


# 默认参数 -- 函数形参定义默认值，调用时可以不传入该参数
def func_3(start="上海", destination="北京"):
    return {"起点": start, "终点": destination}


travel = func_3()


# ------------------------------------------------------------#
# 不定长参数 -- 最好用 .get()来获取值，直接用 字典[key]的话，key为None时会直接报错
def calc_data(*args, **kwargs):
    min_data = min(args)
    max_data = max(args)
    avg_data = sum(args) / len(args)

    float = kwargs.get("round")
    if float is None:
        float = 1

    if kwargs.get('print'):
        print(f"最小值：{min_data}，最大值：{max_data}，平均值：{round(avg_data, float)}")
        return None
    else:
        return min_data, max_data, round(avg_data, float)


calc_data(12, 27, 34, print=True, round=2)
data = calc_data(12, 27, 34, round=3)
print(data)
data = calc_data(12, 27, 34)
print(data)

# ------------------------------------------------------------#
# 匿名函数
output_line = lambda: print("--------------------")
add = lambda x, y: x + y

output_line()
print(add(20, 30))

# 匿名函数实际运用
words = ["apple", "sky", "elephant", "go", "book", "a", "dictionary", "blue"]
words.sort(key= lambda word: len(word))     # 也可以用py函数可以传入函数的特性，直接成 key= len
print(words)

# ------------------------------------------------------------#
# 类型注解
# 基本类型
a: int = 695
score: float = 98.5
hobby: str = "Python"
flag: bool = True
pic: None = None

# 数据容器类型
names: list[str | int] = ["A", "C", "E", 100]
phones: set[str] = {"13309091111", "15209109121"}
options: dict[str, int] = {"count": 0, "total": 0}
goods: tuple[str, int, int] = ("手机", 5999, 1)

# 特殊类型
data: Any = None  # 表示可以接收任意类型的参数
key: Callable[[int], Any]  # 表示只能接收函数类型的参数，[]中表示函数接形参类型和返回值类型