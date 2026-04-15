import re

s1 = ("18809090000是我的手机号，188开头的，以00结尾的；"
      "我的另一个手机号是15500008888，两个QQ号分别是1259989092和13809091293821，"
      "邮箱为python666@163.com。请给我发邮件。")

# 正则表达式
print(re.findall(r"188.*", s1))     # * 匹配任意字符
print(re.findall(r"188.?", s1))     # ? 匹配任意字符，但至少匹配一个
print(re.findall(r"188.+", s1))     # + 匹配任意字符，至少匹配一个

print(re.findall(r"188\d{8}", s1))        # {8} 匹配8个
print(re.findall(r"155\d{6,10}", s1))     # {6,10} 匹配6-10个
print(re.findall(r"155\d{6,}", s1))       # {6,} 匹配6个以上

print(re.findall(r"1[38]\d{8}", s1))      # 匹配13或18开头的
print(re.findall(r"1[^38]\d{8}", s1))     # 匹配非13或18开头的
print(re.findall(r"1[3-9]\d{8}", s1))     # 匹配13-19开头的

print(re.findall(r"\w+@\w+\.\w+", s1))    # 结果：[邮箱为python666@163.com]
print(re.findall(r"\w+@\w+\.\w+", s1, re.ASCII))    # 不匹配非ASCII字符(中文汉字等)：[python666@163.com]

s2 = "电话号码：18809090000"
print(re.findall(r"^1[3-9]\d{9}", s2))    # ^ 从字符串的起点开始匹配 -- 开头非1，结果为[]
print(re.findall(r"1[3-9]\d{9}$", s2))    # $ 匹配字符串的结尾 -- 结尾为18xxx，结果为[18809090000]
print(re.findall(r"^1[3-9]\d{9}$", s2))   # 匹配字符串的从头到尾，开头非1，结果为[]

s3 = "现在的时间是2026-02-06 10:05:25，今天的天气还可以，气温是28度 "
print(re.findall(r"\d{4}-\d{2}-\d{2}", s3))           # 匹配日期['2026-02-06']
print(re.findall(r"(\d{4})-(\d{2})-(\d{2})", s3))     # 只匹配分组内容，结果为[('2026', '02', '06')]
