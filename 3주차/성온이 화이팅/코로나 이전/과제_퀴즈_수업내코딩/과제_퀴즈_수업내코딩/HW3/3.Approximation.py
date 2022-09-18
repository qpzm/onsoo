#Kimhaeun
#22100224
#근사값을 구하는 함수

input_error_value=1

while input_error_value>0.01:
    input_error_value=float(input("오차값을 실수로 입력하세요:"))


i=1
pi=0
pi1=0
pi2=0
control=0
real_error_value=0

while i>=1:
    if control==0:
        pi1=4/i
        pi=pi+pi1
        real_error_value=pi-(pi-4/(i+2))
        if real_error_value<input_error_value:
            print(pi)
            break
        else:
            control=1
    if control==1:
        pi2=4/(i+2)
        pi=pi-pi2
        real_error_value=(pi-(pi+4/(i+4)))*(-1)
        if real_error_value<input_error_value:
            print(pi)
            break
        else:
            control=0
    i+=4

    
