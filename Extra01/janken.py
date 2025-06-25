import random

while True:
    # pleyerはinput
    print("グーなら1,チョキなら2,パーなら3,を入力してください。")
    pleyer = input("あなた:")

    #computerはrandom
    jankens = ["1", "2", "3"]
    com = random.choice(jankens)
    print(f"コンピュータ:{com}")

    if  pleyer == "1":
        if com == "1":
            print("あいこ")
        elif com == "2":
            print("あなたの勝ち")
        else:
            print("あなたの負け")

    elif pleyer == "2":
        if com == "1":
            print("あなたの負け")
        elif com == "2":
            print("あいこ")
        else:
            print("あなたの勝ち")

    elif pleyer == "3":
        if com == "1":
            print("あなたの勝ち")
        elif com == "2":
            print("あなたの負け")
        else:
            print("あいこ")

    else:
        print("間違えてますよ。1 or 2 or 3 でお願いします")

    retry = input("もう一度やりますか? (y or n): ")
    print( )
    if retry != "y":
        break

