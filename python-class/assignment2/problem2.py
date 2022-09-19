'''
반복문을 사용하여 factorial 결과 값을 예시와 같이 출력 하시오.
양의 정수를 입력 받아 num!, (num-1)!, …2!, 1! 을 계산하여 한 줄로 출력 하시오.
print(i, end=' ‘)를 사용하면 한 줄로 출력할 수 있다. 양의 정수가 아닌 값이 입력되면 “계산할 수 없는 값입니다” 출력한다.
<< 예시 >>   
5가 입력되면,  120,  24,  6,  2,  1
4가 입력되면,  24,  6,  2,  1
'''
# num = int(input("양의 정수를 입력하세요: "))
# if num>0:
#     for i in range(num,0,-1):
#         print(i, end=' ')
#     #각자 줄어드는 거 
#     #그 안에서 팩토리얼 계산하는 거5

# else:
    # print("계산할 수 없는 값입니다.")

    
n=int(input())
def recur(num):
    if num ==1:
        return 1
    else:
        return num*recur(num-1)