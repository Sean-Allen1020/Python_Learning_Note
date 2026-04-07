# 定义类
class Car:
    # 类属性，所有实例共享的静态变量
    wheels = 4
    tax_rate = 0.1

    # __init__方法会在实例被创建时自动调用
    def __init__(self, c_brand, c_name, c_price):   # 类似java构造体。形参实际上不需要 c_ 也可以，示例暂时这么用
        self.brand = c_brand
        self.name = c_name
        self.price = c_price

    # 魔法方法
    def __str__(self):
        return f"{self.brand} {self.name} {self.price}"
    def __eq__(self, other):
        return self.brand == other.brand and self.name == other.name and self.price == other.price
    def __lt__(self, other):
        return self.price < other.price

    # 自定义方法
    def running(self):
        print(f"{self.brand}{self.name}正在行驶")


# 创建实例
c1 = Car("BMW", "X5", 500000)
print(c1.__dict__)
c1.running()