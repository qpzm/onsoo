# num = int(input("양의 정수를 입력하세요: "))
# for i in range(num,0,-1):
#     print(i, end=' ')

# 5!일 경우 5! 계산하고 /5 하면 4!, /4 하면 3!, /3 하면 2!이다. 그 접근 방식으로 한번 풀어보자!

num1 = int(input("첫번째 양의 정수 입력: "))
num2 = int(input("두번째 양의 정수 입력: "))
op = "-"
x = 0
if num1 < num2:
    for i in range(num1, num2 + 1):
        if num2 == i:
            op = "="
        print(i, op, end=" ")
        if op == "-":
            op = "+"
        elif op == "+":
            op = "-"

    for i in range(num1, num2 + 1):
        if (i - num1) % 2 == 0:
            x = x + i
        else:
            x = x - i
        # print(f'i: {i}, x: {x}, y: {y}')
    print(x, end=' ')
elif num1>num2:
    for i in range(num2, num1 - 1):
        if num1 == i:
            op = "="
        print(i, op, end=" ")
        if op == "-":
            op = "+"
        elif op == "+":
            op = "-"

    for i in range(num2, num1 - 1):
        if (i - num2) % 2 == 0:
            x = x + i
        else:
            x = x - i
else:
    print("입력 에러입니다")