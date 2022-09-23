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

# 사용자가 종료를 요청할 때("y" 입력)까지 반복하기
quit = 'n'
while quit != 'y':
    quit = input("Do you want to quit")
#왜 처음에 n이지?

pwd = "????"
while pwd!="1234":
    pwd = input("비밀번호를 입력하세요: ")

pwd = "????"
count = 1
while pwd != "1111" and count<=5:
    pwd = input("비밀번호를 입력하세요: ")
    count = count+1
    if count > 5:
        print("비밀번호를 5회 이상 틀렸으므로 종료합니다")
#5번째 기회에서 "1111"을 입력했는데 종료가 안되고 line32로 되나?

#문제: 1부터 100미만의 짝수를 모두 출력하는 while, for문을 쓰시오
i = 1
n = 1
while n < 100:
    n = i*2
    i = i+1
    print(n)
#마지막 100을 안 출력하려면?