# pwd = "????"
# count =1
# while pwd!="1111" and count<=3:
#     pwd = input("비밀번호 입력하세요: ")
#     count = count+1
# if pwd == "1234":
#     print("비밀번호가 정확합니다")
# elif count>3:
#     print("비밀번호를 3번 잘못 입력했습니다.")

# s = 1
# n = 1
# while s <10:
#     s=s+n
#     print("s=", s)


# x = 1.0
# y = 1.0
# i = 0
# while y<=1.5:
#     x=x/2
#     y=x+y
#     i=i+1
#     print("x=", x)
#     print("y=", y)
# print("i=", i)
# #왜 i가 1이 아니고 2지?

# numofnum = 0
# count = 1
# sum = 0
# while numofnum <= 0:
#     numofnum=int(input("정수의 개수: "))
# while count <= numofnum:
#     num = float(input("숫자를 입력하세요: "))
#     count=count+1
#     sum = sum+num
# print("입력받은 수들의 평균은" , sum/numofnum)
# #어떨 때 어떤 변수를 몇개를 써야할지 모르겠다!

# price = 0
# count = 0
# sum = 0
# while price <= 10000:
#     price = int(input("구매할 물건의 금액을 입력하세요."))
#     if price <= 10000:
#         count = count+1
#         sum = sum + price
# print("물건의 개수는", count, "이고 금액의 합계는", sum, "원입니다")
# #if문을 안 쓰면 10000원 넘어간 값도 합계에 계산 되기 때문에 if문 꼭 써야 함

name = 0
count = 0
while name != "김" or "최" or "이" and count <= 5:
    name = input("성을 입력하세요: ")
    count = count + 1
