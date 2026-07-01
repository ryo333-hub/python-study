def save_record(text):
    with open("data.txt", "a", encoding="utf-8") as f:
        f.write(text + "\n")

    print("✔ 记录已保存")