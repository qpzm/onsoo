'''
작성자 : 박현민(21900326)
프로그램의 목적 :if문을 이용하여 기준표에 부합하게 성적을 채점하는 프로그램이다.
'''

score=float(input("Input your score : "))
grade=input("Input Letter(L) or PF(PF) : ")

#grade가 L일때와
if grade=="L":
    if score<60:
        print("Your grade is F")
    elif score>=60 and score<70:
        print("Your grade is D")
    elif score>=70 and score<80:
        print("Your grade is C")
    elif score>=80 and score<90:
        print ("Your grade is B")
    else:
        print("Your grade is A")

#grade가 PF일때를 나누어 처리한다.
elif grade=="PF":
    if score<60:
        print("Fail")
    elif score>=60 and score<70:
        print("Pass")
    elif score>=70 and score<80:
        print("Pass")
    elif score>=80 and score<90:
        print ("Pass")
    else:
        print("Pass with Distinction")

#grade에 L과 PF외의 다른것을 input 받았을 때 다음과 같이 처리한다.
else:
    print("Not correct type!")
