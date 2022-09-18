'''
작성자 : 21900326 박현민
1번 문제 - 입력받은 정수의 특성에 따라서 다음과 같이 출력 하시오
'''

num=int(input('정수를 입력하시오 : '))

if num<=0:
    print('양수가 아닙니다')
elif num%5==0 and num%2==0:
    print('5의 배수인 짝수')
elif num%5==0 and not num%2==0:
    print('5의 배수인 홀수')
elif num%2==0:
    print('짝수입니다')
else:
    print('홀수입니다')
