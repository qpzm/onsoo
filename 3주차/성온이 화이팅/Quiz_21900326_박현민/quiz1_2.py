'''
작성자 : 21900326 박현민
2번 문제 - 키와 몸무게, 유럽인이면1, 아시아인이면 2를 입력 받아
BMI 값을 계산하고, 아래 표에 있는 대로 현재 몸 상태를 출력 하시오
BMI=몸무게/(키*키), 이 때 키는 m기준
'''

weight=float(input('몸무게를 입력하시오(kg기준) : '))
height=float(input('키를 입력하시오(m기준) : '))

human=int(input('유럽인이면 1, 아시아인이면 2를 입력하시오 : '))

BMI=weight/(height*height)

if human==1:
    if BMI<18.5:
        print('저체중')
    elif BMI<23:
        print('정상 I')
    elif BMI<25:
        print('정상 II')
    elif BMI<30:
        print('과체중')
    elif BMI<40:
        print('비만 I')
    else:
        print('비만 II')

elif human==2:
    if BMI<18.5:
        print('저체중')
    elif BMI<23:
        print('정상')
    elif BMI<25:
        print('과체중')
    elif BMI<30:
        print('비만 I')
    elif BMI<40:
        print('비만 II')
    else:
        print('심각한 비만')

else:
    print('잘못된 입력입니다.')
    
