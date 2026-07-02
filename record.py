def save_record(text):
    with open("data.txt", "a", encoding="utf-8") as f:
        f.write(text + "\n")

    print("✔ 记录已保存")
from datetime import datetime

def save_record(text):
    time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log = time + " | " + text

    with open("log.txt", "a", encoding="utf-8") as f:
        f.write(log + "\n")

        print("✔ 已记录：", log)