# 字面量
print(100)
print(3.14)
print(True)     # 首字母需要大写
print(False)
print("Hello World")
# -------------------------------- #
print(None)     # 空值. 输出 None
print(True + 9)     # boolean类型的值本质是整型, 所以可以做加减法

# 变量
print("-----------------------")
# Python为动态类型语言, 变量可以根据接收的值, 自动转换类型
a = 10
print(a)
a = "Hello World"
print(a)
# 查看变量类型
print(type(a))
print(isinstance(a, str))   # 是str, 就会输出 True

# -------------------------------- #
# 字符串 ""
s1 = "Hello"
s1 = "I'm Allen"    # 双引号方便包含单引号的内容
# 字符串 ''
s2 = 'Python'
s2 = 'He said "hello"'  # 单引号方便包含双引号的内容
# 字符串 """
s3 = """
    Hello World
    Hello Java
    """     # 三引号方便对文本进行排版
print(s3)

# 字符串拼接的三种方式
name = "Jack"
age = 18
print("My name is " + name + ", I'm " + str(age) + " years old.")
print("My name is %s, I'm %s years old." % (name, age))
print(f"My name is {name}, I'm {age} years old.")   # 常用