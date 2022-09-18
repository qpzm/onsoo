mon = int(input("월을 입력하시오: "))
if mon in [1, 3, 5, 7, 8, 10, 12] :
    print (mon, "월은 31일까지입니다.")
elif mon in [2] :
    print(mon, "월은 28일 또는 29일까지입니다.")
elif mon in [4, 6, 9, 11] :
    print(mon, "월은 30일까지입니다.")
else :
    print("입력오류")
