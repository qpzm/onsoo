#수업 내 코딩 1번
str1 = input("문자를 입력하세요:")
str2 = input("문자를 입력하시오:")
if str1>str2:
    print(str1,"은", str2, "보다 크다")
elif str1<str2:
    print(str1,"은", str2, "보다 작다")
else:

    print(str1,"은", str2, "와 같다")

#수업 내 코딩 2번
num = int(input("input a positive integer : "))
prime_yes = True
for i in range(2, num):
    if num % i == 0:
        prime_yes = False
        break
if prime_yes == True:
    print(num, "is a prime number")
else:
    print(num, "is not a prime number")
