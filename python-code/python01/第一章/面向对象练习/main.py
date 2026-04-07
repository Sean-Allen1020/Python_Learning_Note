from 第一章.面向对象练习.EduManagement import EduManagement
from 第一章.面向对象练习.Student import Student

em = EduManagement()

s1 = Student("Tom", 82, 93, 76)
s2 = Student("Marry", 77, 96, 68)
s3 = Student("Jack", 99, 97, 91)
em.add_student(s1)
em.add_student(s2)
em.add_student(s3)

while True:
    print(f"""
    欢迎使用{em.system_name} V{em.system_version}：
    1. 添加
    2. 修改
    3. 删除
    4. 查询
    5. 展示全部
    6. 退出""")

    selection = input("请输入选项")
    if selection == "1":
        em.add_student()
    elif selection == "2":
        em.update_student()
    elif selection == "3":
        em.delete_student()
    elif selection == "4":
        em.select_student()
    elif selection == "5":
        em.get_all()
    elif selection == "6":
        print("教务系统已退出")
        break
    else:
        print("错误选项，请重新输入")