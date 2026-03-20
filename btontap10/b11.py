while True:
    print("\n===== MENU =====")
    print("1. Bài 1")
    print("2. Bài 2")
    print("0. Thoát")

    chon = input("Chọn: ")

    if chon == "1":
        print("Chạy bài 1...")
    elif chon == "2":
        print("Chạy bài 2...")
    elif chon == "0":
        print("Thoát!")
        break
    else:
        print("Chọn sai!")