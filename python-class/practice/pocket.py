mon = int(input("주머니에 얼마가 있나요?: "))
if mon >= 17000:
    print(mon, "원으로 구매 가능한 메뉴는 치킨이다.")
elif mon >= 14000:
    print(mon, "원으로 구매 가능한 메뉴는 떡볶이이다.")
elif mon >= 7000:
    print(mon, "원으로 구매 가능한 메뉴는 국밥이다.")
elif mon >= 5000:
    print(mon, "원으로 구매 가능한 메뉴는 한정식이다.")
else:
    print(mon, "원으로 구매할 수 있는 메뉴는 짜장면이다.")