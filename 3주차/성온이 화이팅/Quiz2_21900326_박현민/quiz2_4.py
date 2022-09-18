'''
작성자 : 박현민
quiz2 4번
'''

lst=[]
def fibo(n):
    if n==1 or n==2:
        return 1
    else:
        return fibo(n-1)+fibo(n-2)

a=int(input('피보나치 수열 원소 수를 입력하시오 : '))


while a!=0:
    lst.append(fibo(a))
    a-=1

lst.sort()

print(lst)
    
