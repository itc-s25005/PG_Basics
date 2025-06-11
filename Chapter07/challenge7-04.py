answer = (3, 6, 9)

while True:
    user_input = input("1から10のどれかの数字を入力してください(qで終了):")

    if user_input == "q":
        break

    elif user_input.isdigit():
        if int(user_input) in answer:
            print("正解")
        else:
            answer:print("不正解")
    else:
        print("数字を入力するか、qで終了します")



