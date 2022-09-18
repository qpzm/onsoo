#Kimhaeun
#22100224
#Quiz1
#Problem2

n1=int(input("첫번째 정수를 입력하시오:"))
n2=int(input("두번째 정수를 입력하시오:"))
n3=int(input("세번째 정수를 입력하시오:"))

if n1>n2>n3:
    print("순서정렬")
elif n1<n2<n3:
    print("순서정렬")
elif n1==n2<n3:
    print("순서정렬")
elif n1==n2>n3:
    print("순서정렬")
elif n1<n2==n3:
    print("순서정렬")
elif n1>n2==n3:
    print("순서정렬")
else:
    print("순서미정렬")
    
