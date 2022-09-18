
#Kimhaeun
#22100224
#Problem2
fac=1
n=int(input("양의 정수를 입력하세요:"))

if n<=0:
    print("계산할 수 없는 값입니다.")
else:
    print(n,"가 입력되면,",end=' ')
    for i in range(n,0,-1):
        fac=1
        for j in range(1,i+1):
            fac=fac*j
        print(fac, end=' ')
