wea = input("계절을 입력하시오 : ")
temp = float(input("온도를 입력하시오 : "))
if wea == "winter":
    print("겨울철 실내 적정 온도는 20~22도입니다.")
    if temp >= 20 and temp <= 22 :
        print("적정 온도입니다.")
    else : 
        print("적정 온도가 아닙니다.")
elif wea == "summer":
    print("여름철 실내 적정 온도는 24~26도입니다.")
    if temp >= 24 and temp <= 26:
        print("적정 온도입니다.")
    else :
        print("적정 온도가 아닙니다.")
else :
    print("겨울도 아니고 여름도 아닙니다.")