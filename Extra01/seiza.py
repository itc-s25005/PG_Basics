seiza = ["", "山羊座", "水瓶座", "魚座", "牡羊座", "牡牛座", "双子座", "蟹座", "獅子座", "乙女座", "天秤座", "蠍座", "射手座"]
kugiri = [0, 20, 19, 21, 20, 21, 21, 23, 23, 23, 23, 22, 22]

month = int(input("月を数字で入力してください:"))
day = int(input("日を数字で入力してください:"))

if day >= kugiri[month]:
    month += 1
    if month == 13:
        month = 1

print("あなたの星座は" + seiza[month] + "です")
