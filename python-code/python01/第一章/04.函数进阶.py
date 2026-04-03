# 位置传参 -- 传参位置必须与函数一致
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