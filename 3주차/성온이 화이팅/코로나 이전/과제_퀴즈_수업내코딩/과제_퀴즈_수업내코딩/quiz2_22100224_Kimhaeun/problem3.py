#Kimhaeun
#22100224
#Problem3

sum=0
a=0
n1=int(input("첫번째 양의 정수를 입력해주세요:"))
n2=int(input("두번째 양의 정수를 입력해주세요:"))

if n1<=0 or n2<=0:
    print("양의 정수가 아니라서 입력 에러입니다.")
elif n1<n2:
    if(n2-n1)%2==0:
        for i in range(n1,n2,2):
            sum=sum+i-(i+1)
            a=i+1
            print(i,'-',a,'+',end=' ')
        sum=sum+n2
        print(n2,'=',sum)
    else:
        for i in range(n1,n2+1,2):
            sum=sum+i-(i+1)
            a=i+1
            if a==(n2):
                print(i,'-',a,end=' ')
            else:
                print(i,'-',a,'+',end=' ')
            
        print('=',sum)
 
elif n1>n2:
    if(n1-n2)%2==0:
        for i in range(n1,n2,-2):
            sum=sum+i-(i-1)
            a=i-1
            print(i,'-',a,'+',end=' ')
        sum=sum+n2
        print(n2,'=',sum)
    else:
        for i in range(n1,n2-1,-2):
            sum=sum+i-(i-1)
            a=i-1
            if a==(n2):
                print(i,'-',a,end=' ')
            else:
                print(i,'-',a,'+',end=' ')
            
        print('=',sum)

#TA님 풀이

num1=int(input("첫번째 양의 정수를 입력해주세요:"))
num2=int(input("두번째 양의 정수를 입력해주세요:"))

if num1<0 or num2<0:
    print("에러")

else:
    if num1<num2:
        res=0
        control=0
        for i in range(num1,num2+1):
            if control==0:
                res=res+i
                print(i, end=' ')
                if i==num2:
                    print('=',end=' ')
                else:
                    print('-',end=' ')
                control=1
            elif control==1:
                res=res-i
                print(i,end=' ')
                if i==nim2:
                    print('=',end=' ')
                else:
                    print('+',end=' ')
                control=0
        print(res)
    elif num1>num2:
        res=0
        control=0
        for i in range(num1. num2-1,-1):
            if control==0:
                res=res+i
                print(i,end=' ')
                if i==num2:
                    print('=', end=' ')
                else:
                    print('-', end=' ')
                control=1
            elif control==1:
                res=res-i
                print(i,end=' ')
                if i==num2:
                    print('=',end=' ')
                else:
                    print('+',end=' ')
                control=0
            print(res)
list.replace("찾을 문자", "치환 문자" (,치환횟수))
                
                    
        
