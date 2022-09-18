#Kimhaeun
#22100224
#학점 계산

score=float(input("Input your score:"))
type=input("Input Letter(L) or PF(PF):")

if type=="L" or type=="Letter":
    if score>=90:
        print("A")
    elif score>=80:
        print("B")
    elif score>=70:
        print("C")
    elif score>=60:
        print("D")
    else:
        print("F")
elif type=="PF":
    if score>=90:
        print("PD(Pass with Distinction)")
    elif score>=60:
        print("Pass")
    else:
        print("Fail")
        
