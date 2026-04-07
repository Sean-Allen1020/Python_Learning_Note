# 列表 list
s = [1, 2, 3, 4, "Hello", True, 2, 16, "World", 26]

print(s[-1])  # 反向索引，从末尾开始
del s[3]  # 删除指定元素

s_ = s[1:10:2]  # 切片 --> startIdx:endIdx:step --> 包头不包尾，step为间隔数
print(s_)

# list方法
s.append(100)                   # 尾部追加元素
s.insert(1, 100)    # 指定索引之前，插入元素
s.remove(2)                     # 移除列表中，第一个匹配到的值
print(s)
e = s.pop(5)                        # 移除列表的指定索引的元素，并返回该元素（不写，则默认最后一个）
print(e)
s.reverse()                     # 反转
print(s)

s1 = [8, 7, 9, 10, 1, 4, 6, 2, 7, 0]
s1.sort()                       # 排序，元素类型必须一致
print(s1)

avg = sum(s1) / len(s1)         # 求平均值
print(avg)

# 序列推导式
num_list = [19, 23, 54, 64, 87, 20, 109, 232, 123, 43, 26, 55, 72]
new_list = [i*i for i in num_list if i % 2 == 0]
print(new_list)

#------------------------------------------------------#
# 字符串 str -- 验证邮箱格式
mail = "zhuzhuzhu11330@126.com"
if mail.count("@") == 1 and "." in mail:
    print(mail)
    print("right email")
else:
    print("wrong email")

# 回文字符串
str = "上海自来水来自海上"
str_reverse = str[::]
print(str_reverse)
print(str_reverse == str)

#------------------------------------------------------#
# 元组 tuple
# 利用解包组包的元素交换
a, b, c = 100, 200, 300
c, a, b = a, b, c

print(f"{a}, {b}, {c}")



# 学生成绩元组
students = (
    ("S001", "张三", 85, 92, 78),
    ("S002", "李四", 92, 88, 95),
    ("S003", "王五", 78, 85, 82),
    ("S004", "宋六", 88, 79, 91)
)

# 1. 计算 学生 平均分
for id, name, *score in students:   # 解包可以直接用在 for循环行内
    avg = sum(score)/len(score)
    print(f"{name}: {avg:.1f}分")

# 2. 分别获取 语文 数学 英语 成绩
chinese = [s[2] for s in students]  # 通过列表推导式来获取
math    = [s[3] for s in students]
english = [s[4] for s in students]
print(f"语文：{chinese}")
print(f"数学：{math}")
print(f"英语：{english}")

#------------------------------------------------------#
# 集合 set
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
# 交集
print(set1 & set2)
# 并集
print(set1 | set2)
# 差集
print(set1 - set2)
# 对称差集 -- 两集合差集的汇总
print(set1 ^ set2)
# 判断两集合是否没有交集，没有则返回 True
print(set1.isdisjoint(set2))