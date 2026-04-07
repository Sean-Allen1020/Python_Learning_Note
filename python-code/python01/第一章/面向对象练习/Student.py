class Student:
    def __init__(self, name, chinese, math, english):
        self.name = name
        self.chinese = chinese
        self.math = math
        self.english = english

    def __str__(self):
        total = self.chinese + self.math + self.english
        return f"姓名：{self.name} | 语文：{self.chinese} | 数学：{self.math} | 英语：{self.english} | 总分：{total}"

    # 学生成绩修改
    def update_score(self, chinese=None, math=None, english=None):
        if chinese is not None:
            self.chinese = chinese
        if math is not None:
            self.math = math
        if english is not None:
            self.english = english

# 测试
if __name__ == '__main__':
    s1 = Student("张三", 90, 80, 70)
    print(s1)

    s1.update_score(english=100)
    print(s1)