#kimhaeun
#22100224
#problem3
import random

randNum=[]
a=0
b=0
c=0

def dice():
    dice_n=[1,2,3,4,5,6]
    for i in range(3):
        randNum.append(random.choice(dice_n))
    global a
    global b
    global c
    a=randNum[0]
    b=randNum[1]
    c=randNum[2]
    hint=(a+b)*c
    print("랜덤 숫자를 생성하였습니다.")
    print("a=",a,",c=",c,"(a+b)*c=",hint)


dice()

for i in range(3):
    guess_b=int(input("b의 값은?"))
    if b!=guess_b:
        print("틀렸습니다.")
    else:
        print("정답입니다.")
        YN=int(input("계속 진행하시겠습니까? (Yes:1. No:2)"))
        if YN==1:
            dice()
        else:
            break
