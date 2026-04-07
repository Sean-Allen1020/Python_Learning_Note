from 第一章.面向对象练习.Student import Student


class EduManagement:
    system_version = 1.0
    system_name = "教务管理系统"

    def __init__(self):
        self.student_list = []

    # 添加学生
    def add_student(self, student=None):
        if student is None:
            name = input("请输入学生姓名")
            for s in self.student_list:
                if s.name == name:
                    print("学生已存在")
                    return

            chinese = int(input("请输入语文成绩"))
            math = int(input("请输入数学成绩"))
            english = int(input("请输入英语成绩"))
            if 0 <= chinese <= 100 and 0 <= math <= 100 and 0 <= english <= 100:
                stu = Student(name, chinese, math, english)
                self.student_list.append(stu)
        else:
            self.student_list.append(student)

    # 修改学生
    def update_student(self):
        name = input("请输入学生姓名")
        for s in self.student_list:
            if s.name == name:
                s.name = input("请输入新学生姓名")
                chinese = int(input("请输入新语文分数"))
                math = int(input("请输入新数学分数"))
                english = int(input("请输入新英语分数"))
                s.update_score(chinese, math, english)
                return
        print("学生不存在")

    # 删除学生
    def delete_student(self):
        name = input("请输入需要删除的学生姓名")
        for s in self.student_list:
            if s.name == name:
                self.student_list.remove(s)
                return
        print("学生不存在")

    # 查询学生
    def select_student(self):
        name = input("请输入要查询的学生姓名")
        for s in self.student_list:
            if s.name == name:
                print(s)
                return
        print("学生不存在")

    # 展示全部学生
    def get_all(self):
        for s in self.student_list:
            print(s)


if __name__ == '__main__':
    s1 = Student("Tom", 82, 93, 76)
    s2 = Student("Marry", 77, 96, 68)
    s3 = Student("Jack", 99, 97, 91)

    em = EduManagement()

    em.add_student(s1)
    em.add_student(s2)
    em.add_student(s3)
    print(em)
    em.update_student()
    print(em)