# 字典容器练习题：
# 开发一个购物车管理系统，实现商品信息的添加、修改、删除、查询功能。系统使用字典结构存储商品数据，通过控制台菜单与用户交互。
# 具体功能如下：
#
# 1. 添加购物车：用户根据提示录入商品名称，以及该商品的价格、数量，
#    保存该商品信息到购物车。
#
# 2. 修改购物车：要求用户输入要修改的购物车商品名称，然后再提示输入
#    该商品的价格、数量，输入完成后修改该商品信息。
#
# 3. 删除购物车：要求用户输入要删除的购物车名称，根据名称删除购物车中的商品。
#
# 4. 查询购物车：将购物车中的商品信息展示出来，格式为：
#    "商品名称：xxx，商品价格：xxx，商品数量：xxx"。
#
# 5. 退出购物车

print("\t欢迎来到购物车", end="")
print("""
    1.添加
    2.修改
    3.删除
    4.查询
    5.退出""")

shopping_cart = {}
while True:
    selection = input("请输入选项")
    match selection:
        case "1":
            while True:
                name = input("请输入商品名称")
                if name not in shopping_cart:
                    price = int(input("请输入商品价格"))
                    amount = int(input("请输入购买数量"))
                    shopping_cart[name] = {"price": price, "amount": amount}
                    print(f"商品添加成功：{shopping_cart[name]}")
                    break
                else:
                    print("商品已存在，请重新输入")
        case "2":
            while True:
                name = input("请输入需要修改的商品名称")
                if name in shopping_cart:
                    price = int(input("请输入商品价格"))
                    amount = int(input("请输入购买数量"))
                    shopping_cart[name] = {"price": price, "amount": amount}
                    break
                else:
                    print("无该商品，请重新输入")
        case "3":
            while True:
                name = input("请输入要删除的商品名称")
                if name in shopping_cart:
                    pop = shopping_cart.pop(name)
                    print(f"商品删除成功: {pop}")
                    break
                else:
                    print("无该商品，请重新输入")
        case "4":
            for item in shopping_cart.items():
                print(f"商品名称: {item[0]}, 价格: {item[1]['price']}, 数量: {item[1]['amount']}")
        case "5":
            print("退出购物车")
            break
        case _:
            print("错误选项，请重新输入")
