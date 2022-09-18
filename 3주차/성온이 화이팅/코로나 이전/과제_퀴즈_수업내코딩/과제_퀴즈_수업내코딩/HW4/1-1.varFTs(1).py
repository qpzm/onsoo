#Kimhaeun
#22100224
#def1

def middle(string):
    if len(string)%2==0:
        a=len(string)//2
        return string[a-1:a+1]
    else:
        a=len(string)//2
        return string[a]

for i in range(2):
    wo=input("문자열을 입력하세요:")
    print(middle(wo))
