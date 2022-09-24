'''
작성자 : 박성온
프로그램의 목적 : 키, 몸무게, 인종 등을 입력받아 그에 맞는 BMI를 계산하고 if,elif,else를 사용하여 출력된 BMI가 몸상태 중 어느 범주에 있는지 도출한다.
'''
height = float(input("키를 입력하시오(m기준): "))
weight = float(input("몸무게를 입력하시오(kg기준): "))
BMI = weight/(height*height)
nat =int(input("인종을 입력하시오(유럽인이면 1, 아시아인이면 2를 입력): "))
if nat==1:
    if BMI<18.5:
        print("BMI값은", BMI, "이며, 유럽인으로 저체중입니다.")
    elif BMI<23:
        print("BMI값은", BMI, "이며, 유럽인으로 정상1입니다.")
    elif BMI<25:
        print("BMI값은", BMI, "이며, 유럽인으로 정상2입니다.")
    elif BMI<30:
        print("BMI값은", BMI, "이며, 유럽인으로 과체중입니다.")
    elif BMI<40:
        print("BMI값은", BMI, "이며, 유럽인으로 비만1입니다.")
    else:
        print("BMI값은", BMI, "이며, 유럽인으로 비만2입니다.")
elif nat==2:
    if BMI<18.5:
        print("BMI값은", BMI, "이며, 아시아인으로 저체중입니다.")
    elif BMI<23:
        print("BMI값은", BMI, "이며, 아시아인으로 정상입니다.")
    elif BMI<25:
        print("BMI값은", BMI, "이며, 아시아인으로 과체중입니다.")
    elif BMI<30:
        print("BMI값은", BMI, "이며, 아시아인으로 비만1입니다.")
    elif BMI<40:
        print("BMI값은", BMI, "이며, 아시아인으로 비만2입니다.")
    else:
        print("BMI값은", BMI, "이며, 아시아인으로 심각한 비만입니다.")
else: 
    print("인종을 알 수 없으므로 BMI를 측정할 수 없습니다.")
