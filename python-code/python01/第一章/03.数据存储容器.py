# list
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
# 字符串 -- 验证邮箱格式
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