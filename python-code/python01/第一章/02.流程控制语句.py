# if --> python中的 if 是根据缩进来判断代码块的
import calendar

year = 2026
if calendar.isleap(year):
    print(f"{year}是闰年")
else:
    print(f"{year}是平年")

# match...case
day = int(input("请输入星期几"))

match day:
    case 1:
        print("周一：周例会日")
    case 2:
        print("周二：学习培训日")
    case 3:
        print("周三：项目开发日")
    case 4:
        print("周四：代码审查日")
    case 5:
        print("周五：总结规划日")
    case 6 | 7:             # | 为 or
        print("休息日")
    case _:                 # _ 类似 java的 default
        print("输入错误")

# while
sum = 0
i = 1
while i <= 100:
    if i % 2 == 0:
        sum += i
    i += 1

print(sum)

# for
msg = "Hello"
for ch in msg:
    print(ch)
else:           # else为循环结束语句，可写可不写
    print("遍历结束")

sum = 0
for n in range(1, 101, 2): # 1 ~ 100 的奇数数组
    sum += n
else:
    print(sum)