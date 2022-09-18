# #1번 문제
# for i in range(2,11,2):
#     print(i)

# i = 2
# while i < 11:
#     print(i)
#     i=i+2

# for i in range(2,11):
#     if i%2==0:
#         print(i)

# #2번 문제
# for i in range(0,50,7):
#     print(i)
#     print(i**2)

# #3번 문제
# string = input("문자 입력: ")
# for i in range(1,len(string),2):
#     print(string[i])

#4번 문제
count = 0
letter =input("문자 입력 : ")
vowels = "AEIOUaeiou"
for i in range(0, len(letter)):
    if letter[i] in "AEIOUaeiou":
        count=count+1
print(count)

