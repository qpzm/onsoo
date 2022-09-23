num = int(input("정수를 입력: "))
if num > 0:
    if num % 5 == 0:
        if num % 2 == 0:
            print("5의 배수인 짝수")
        else:
            print("5의 배수인 홀수")
    else:
        if num % 2 == 0:
            print("짝수입니다")
        else:
            print("홀수입니다")
else:
    print("양수가 아닙니다.")