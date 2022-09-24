i =1 
n =1
while n<100:
    n= i*5
    i = i+1
    print(n)
#i와 n이 들어갈 자리 잘 구분하기

num = int(input("정수 입력: "))
if num != 99999:
    i = 0
    while i < num:
        print(num)
        i=i+1
print("num=", num)

pwd = "????"
while pwd!="1234":
    pwd = input("비밀번호를 입력하세요: ")