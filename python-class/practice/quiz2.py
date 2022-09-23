year = int(input("년도 입력 : "))
if year < 1:
    print("처리할 수 없는 년도로, 에러입니다")
else:
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        leap = True
        print(year, "년은 윤년입니다")
    else:
        leap = False
        print(year, "년은 평년입니다")

