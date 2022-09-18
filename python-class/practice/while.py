# #연습문제1
# value = 50
# while value < 100:
#     value = value + 10
#     print(value)
# print("last value =", value)

# #연습문제2
# value = 100
# while value > 0:
#     value = value - 5
#     print(value)
# print("last value=", value)

# #연습문제3
# i =1
# while i < 2**10:
#     print(i)
#     i=i*2
# print("last i =", i)

# #연습문제 4
# i = 2**10
# while i > 1 :
#     print(i)
#     i=i//2
# print("last i=", i)

#연습문제 1
# 7
# 14
# 21
# 28 
i = 7 # 초기화
while i < 1000: # i 조건 검사
    print(i) # 수행
    i += 7 # i 값 변경
# x         i
# 7  = 7 * 1
# 14 = 7 * 2
# 21 = 7 * 3 
print("=" * 10)
i = 1
while (i * 7) < 1000:
    print(i * 7)
    i += 1