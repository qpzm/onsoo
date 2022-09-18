#Kimhaeun
#22100224
#두번째로 큰 수

n1=int(input("Number1:"))
n2=int(input("Number2:"))
n3=int(input("Number3:"))
n4=int(input("Number4:"))
n5=int(input("Number5:"))
n6=int(input("Number6:"))
n7=int(input("Number7:"))

b1=n1
b2=n1

if n1==n2==n3==n4==n5==n6==n7:
    print("동일한 수")
else:   
    if n2<b1:
        b2=n2
    if n3<b1:
        b2=n3
    if n4<b1:
        b2=n4
    if n5<b1:
        b2=n5
    if n6<b1:
        b2=n6
    if n7<b1:
        b2=n7

    if n2>b1:
        b1=n2
    if n3>b1:
        b1=n3
    if n4>b1:
        b1=n4
    if n5>b1:
        b1=n5
    if n6>b1:
        b1=n6
    if n7>b1:
        b1=n7

    if n1>b2 and n1<b1:
        b2=n1
    if n2>b2 and n2<b1:
        b2=n2
    if n3>b2 and n3<b1:
        b2=n3
    if n4>b2 and n4<b1:
        b2=n4
    if n5>b2 and n5<b1:
        b2=n5
    if n6>b2 and n6<b1:
        b2=n6
    if n7>b2 and n7<b1:
        b2=n7
        
    print("두번째로 큰 수는",b2,"입니다.")

