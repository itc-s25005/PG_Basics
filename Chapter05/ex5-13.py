colors = ["blue", "green", "yellow"]
guess = input("何色でしょうか？(入力してください):")

if guess in colors:
    print("当たり！")
else:
    print("ハズレ！また挑戦してね。")
