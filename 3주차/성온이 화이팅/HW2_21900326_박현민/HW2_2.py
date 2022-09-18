'''
작성자 : 박현민(21900326)
프로그램의 목적 : 반복문을 사용하여 factorial의 결과값을 한줄에 출력하는 프로그램이다.
'''

num=int(input("양의 정수를 입력하시오 : "))

#0보다 작거나 같은 값은 계산할수 없기때문에 if문으로 나누어 처리한다.
if num>0:
    #num이 1일때는 값이 1이된다.
    if num==1:
        print(num)
    #result라는 변수를 따로 설정하여 while반복문을 사용해 계산하였다.
    else:
        result=1
        n=num
        while n>1:
            result=result*n
            n-=1
        print(result,end=" ")
        while num>1:
            print(int(result/num),end=" ")
            result=result/num
            num-=1
        
    
else:
    print("계산할 수 없는 값입니다.")
    
    




