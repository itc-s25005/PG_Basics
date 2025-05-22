def number():

    """
    この関数は、入力された整数の二乗を求めます。
    また、メッセージと求めた結果を出力します。
    全ての処理はこの関数内で完結するため、
    プログラムの引数なしでこの関数を呼ぶだけで機能します。

    引数：なし
    戻り値：なし
    """

    num = input("Enter a number: \n")
    result = int(num) ** 2
    print("num =", result)

number()
