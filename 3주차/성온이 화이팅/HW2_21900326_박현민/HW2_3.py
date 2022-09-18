'''
작성자 : 박현민(21900326)
프로그램의 목적 : 서로 다른 양의 정수 두개를 입력받아 계산하고
                   계산 과정과 결과를 한줄로 출력하는 프로그램이다.
'''

n1=int(input("양의 정수를 입력하시오 : "))
n2=int(input("양의 정수를 입력하시오 : "))

#양의 정수 두개 중 n1이 n2보다 크고 n1,n2모두 0보다 클때를 처리한다.
if n1>n2 and n1>0 and n2>0:
    a=n1
    #계산값을 출력하기 위해 value라는 변수를 설정해준다.
    value=n1
    #for 반복문을 이용해 처리한다.
    for i in range(n1-n2):
        if not a==n2:
            print(a,end=' ')
            print('-',end=' ')
            a-=1
            value-=a
            if a==n2:
                print(a,'=',end=' ')
            else:
                print(a,end=' ')
                print('+',end=' ')
                a-=1
                value+=a
                if a==n2:
                    print(a,'=',end=' ')
                    #반복문을 중지한다.
                    break
                    
    print(value)

#양의 정수 두개 중 n2가 n1보다 크고 n1,n2모두 0보다 클때를 처리한다.       
elif n1<n2 and n1>0 and n2>0:
    a=n1
    value=n1
    for i in range(n2-n1):
        if not a==n2:
            print(a,end=' ')
            print('-',end=' ')
            a+=1
            value-=a
            if a==n2:
                print(a,'=',end=' ')
            else:
                print(a,end=' ')
                print('+',end=' ')
                a+=1
                value+=a
                if a==n2:
                    print(a,'=',end=' ')
                    break
                    
    print(value)

#같은 숫자가 입력되었을 때를 처리한다.   
else:
    print("입력 에러입니다")
    






















#두개의 정수를 한번에 input받아야 하는가?
