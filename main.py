print("Hello GitHub!")
print("Hello AI")
from record import save_record

print("=== 学习记录系统 ===")

text = input("请输入你今天学的内容：今天学了GitHub和Python基础")

save_record(text)

from record import save_record

print("=== 学习记录系统 v2 ===")

while True:
    text = input("请输入学习内容（输入exit退出）")

    if text == "exit":
        print("已退出系统")
        break

    save_record(text)