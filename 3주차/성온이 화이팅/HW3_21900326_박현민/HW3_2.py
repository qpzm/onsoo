'''
작성자 : 21900326 박현민
프로그램의 목적 : 오차 값을 입력받아 해당 오차가 발생하는 시점을 출력하는 프로그램이다.
'''

#float를 통해 입력받은 값을 실수형으로 변환한다
a=float(input("오차값을 실수로 입력하세요 : "))

#시작값을 1로 설정한다
n=1

total=0

#입력받은 값이 0.01보다 크다면 다음을 출력한다.
if a>0.01:
    print("0.01 이하 값만 입력하세요.")
else:
    while True:
        if n%2==1:
            total+=4/(2*n-1)
            c=total-4/(2*(n+1)-1)

        else:
            total-=4/(2*n-1)
            c=total+4/(2*(n+1)-1)
        n+=1

        if -a<total-c<a:
            print(total)
            break
