from record import save_record
from view import show_records


print("=== 学习记录系统 v3 ===")

while True:
    print()
    print("1. 添加学习记录")
    print("2. 查看历史记录")
    print("3. 退出系统")

    choice = input("请选择功能：")

    if choice == "1":
        text = input("请输入学习内容：")
        save_record(text)

    elif choice == "2":
        show_records()

    elif choice == "3":
        print("已退出系统")
        break

    else:
        print("输入错误，请输入 1、2 或 3")