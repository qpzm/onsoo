'''
서로 다른 양의 정수 2개를 입력 받는다.
2와 8이 입력되었다면 "2-3+4-5+6-7+8=5" 를 출력하고, 5와 2가 입력 되면 "5-4+3-2=2"라고 출력한다.
입력 받은 수가 양의 정수가 아니거나 2개의 숫자가 같은 값인 경우에는 "입력 에러입니다"를 출력한다.
print(i, "+", end=' ') 사용하면 여러 개 출력문이 한 줄에 출력된다.
출력 시 마지막 숫자 후에는 연산자가 출력되지 않고 “=”이 출력 되도록 조건문을 사용한다.
<< 예시 >>
입력 정수가 8과 5인 경우,  8 - 7 + 6 - 5 = 2
입력 정수가 2와 5인 경우,  2 - 3 + 4 - 5 = -2
입력 정수가 3과 3인 경우, “입력 에러입니다”
'''

# num1=int(input("첫번째 양의 정수 입력: "))
# num2=int(input("두번째 양의 정수 입력: "))
# op = "-"
# if num1<num2:
#     for i in range(num1, num2+1):
#         if num2 == i:
#             op = "="
#         print(i, op, end=" ")
#         if op == "-":
#             op = "+"
#         elif op == "+":
#             op="-"
    

num1 = int(input("첫번째 양의 정수 입력: "))
num2 = int(input("두번째 양의 정수 입력: "))
op = "-"
x = 0
y = 1
if num1 < num2:
    for i in range(num1, num2 + 1):
        if i == num2:
            print(i, end = ' ')
        else:
            print(i, op, end=" ") # (3 -) (4 +) (5 -) (6 +)
        if op == "-":
            op = "+"
            x = x + i # op == "-" 이면 더하기를 하라
        elif op == "+":
            op = "-"
            x = x - i

    for i in range(num1, num2 + 1):
        if y % 2 == 1:
            x = x + i
        elif y % 2 == 0:
            x = x - i
        y = y + 1
        #print(f'i: {i}, x: {x}, y: {y}')

    print("=", x, end=' ')
# elif num1>num2:
#     for i in range
# else:
#     print("입력 에러입니다")
