def show_records():
    with open("log.txt", "r",encoding="utf-8") as f:
        records = f.read()

        print("===学习记录===")
        print(records)