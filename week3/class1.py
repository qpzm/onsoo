kor = float(input("국어 점수 입력 : "))
eng = float(input("영어 점수 입력 : "))
math = float(input("수학 점수 입력 : "))
avg = (kor + eng + math) / 3
if avg >= 60:
    print("성적 평균은", avg, "이며, 합격입니다.")
else:
    print("성적 평균은", avg, "이며, 불합격입니다.")