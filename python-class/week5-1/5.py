# 입력 받은 패스워드가 1111이거나, 입력 받은 횟수가 5회 이상이면 반복문을 종료하는 코드를 쓰시오
pwd = "????"
count = 1
while pwd != "1111" and count<=5:
    pwd = input("비밀번호를 입력하세요: ")
    if count > 5 and pwd != "1111":
        print("비밀번호를 5회 이상 틀렸으므로 종료합니다")