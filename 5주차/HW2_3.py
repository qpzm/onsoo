'''
작성자: 박성온
프로그램의 목적: 두 개의 양의 정수를 입력받고 if문을 사용하여 크기를 비교하고자 한다. for문이 돌아가면서 +와 -를 바꿔주고 입력된 수들을 계산하고자 한다.
'''
num1 = int(input("첫번째 양의 정수 입력: "))
num2 = int(input("두번째 양의 정수 입력: "))
op = "+"
res = 0
if num1 < num2:
    for i in range(num1, num2 + 1):
        if i == num1:
            print(i, end=" ")
        else:
            print(op, i, end=" ")
        if op == "-":
            res = res - i
            op = "+"
        else:
            res = res + i
            op = "-"
    print("=", res, end=" ")
elif num1 > num2:
    for i in range(num1, num2 - 1,-1):
        if i ==num1:
            print(i, end=" ")
        else:
            print(op, i, end=" ")
        if op =="-":
            res = res - i
            op = "+"
        else:
            res =res + i
            op = "-"
    print("=", res, end=" ")
else:
    print("다시 입력하시오.")
        
