import random

randNumlst=[]
a=0
b=0
c=0

def dice():
    dice_lst=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
    for i in range(3):
        randNumlst.append(random.choice(dice_lst))
    global a
    global b
    global c
    a=randNumlst[0]
    b=randNumlst[1]
    c=randNumlst[2]
    val=(a+b)*c
    print('랜덤 숫자 생성 ',"a=",a,",c=",c,"(a+b)*c=",val)


dice()

for i in range(3):
    input_b=int(input("b의 값을 입력하시오 : "))
    if b!=input_b:
        print("틀린 값입니다.")  
    else:
        print("올바른 값입니다.")
        break
