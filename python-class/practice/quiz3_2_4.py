num = int(input("정수를 입력하시오 : "))
if num > 0:
    x = num / 5
    if x == 0:
        print("5의 배수인 짝수")
    else:
        print("5의 배수인 홀수")
elif num / 5 != 0:
        if num / 2 == 0:
            print("짝수")
        else:
            print("홀수")
else:
    print("양수가 아닙니다.")
