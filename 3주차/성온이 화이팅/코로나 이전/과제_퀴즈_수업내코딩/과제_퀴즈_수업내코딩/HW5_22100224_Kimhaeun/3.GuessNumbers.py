#Kimhaeun
#22100224
#GuessNumbers

import random


def check_list(listname, input_num):
    while input_num in listname:
        print("Duplicate number")
        input_num=int(input("Input a number:"))
    return input_num

c_numList=random.sample(range(0,10),4)


trial=0
u_numList=[]
while c_numList!=u_numList:
    u_numList=[]
    for i in range(4):
        n=int(input("Input a number:"))
        while n not in range(10):
            print("Please input a number from 0 to 9")
            n=int(input("Input a number:"))
        n=check_list(u_numList,n)
        u_numList.append(n)
        
    strike=0
    ball=0

    for i in range(4):
        for j in range(4):
            if c_numList[i]==u_numList[j]:
                if i==j:
                    strike+=1
                else:
                    ball+=1
    print(strike,"strike,",ball,"ball")
    trial+=1

print("You win! on",trial,"try...")


