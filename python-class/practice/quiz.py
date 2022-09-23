kor = float(input("국어성적: "))
eng = float(input("영어성적: "))
math = float(input("수학성적: "))
avg = ((kor+eng+math)/3)
print("세 과목의 평균은", avg, "입니다.")

name = input("이름을 입력하세요: ")
print(name[0]*5)
print(name[1]*5)
print(name[2]*5)

name = input("이름 : ")
aff = input("소속기관: ")
birth = int(input("출생년도: "))
age = 2017-birth
print("제 이름은", name, aff, "출신이고 나이는", age, "살입니다.")
# 왜 2017년 기준인데 2019-year 이지?

pri = int(input("상품 가격: "))
pric = int(input("낼 금액: "))
print("거스름 돈은", pric-pri, "원입니다.")