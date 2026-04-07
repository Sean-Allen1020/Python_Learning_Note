try:
    print("=====================================")
    print(my_name)
    print("=====================================")
except NameError as e:
    print(f"捕获到异常: {e}")
finally:
    print("释放资源")