'''
작성자: 박성온
프로그램의 목적: 양의 정수를 입력하여 그 정수의 팩토리얼 값을 출력한다.
첫 번째로 각 팩토리얼을 계산하는 for문, 두 번째로 그 값을 차례대로 출력하는 for문을 사용한다.
'''
num = int(input("양의 정수를 입력하세요: "))
if num>0:
    for i in range(num,0,-1):
        x=1
        for j in range(i,0,-1):
            x = x * j
        print(x, end=', ')

else:
    print("계산할 수 없는 값입니다.")
