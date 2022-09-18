# count = 9
# if count>=10 : 
#     count = 0
#     print("=" * 25)
#     print("다시 처음부터 시작합니다")
#     print("=" * 25)

# else :
#     count = count + 1
#     print("다음단계가 실행됩니다")

# x = int(input("정수를 입력하시오 : "))
# if x % 2==0 : 
#     print(x, "는 짝수입니다.")
# else :
#     print(x, "는 홀수입니다.")

# a = 4
# b = 5
# c = 6
# if a<b :
#     print("a is less than b")
# if a>b :
#     print("a is greater than b")
# if a<=b : 
#     print("a is less than or equal to b")
# else : 
#     print("a is greater than b")
# if a==b : 
#     print("a is equal to b")
# else : 
#     print("a and b are not equal")
    
from re import X


# x = 5
# y = 10
# if x < y :
#     print(x  "is less than", y)
# else : 
#     print(x "is greater than or equal to", y)

# x = input("첫번째 정수 입력 : ")
# y = input("두번째 정수 입력 : ")
# if x < y :
#     print(x, "is less than", y)
# elif x > y :
#     print(x, "is greater than", y)
# else :
#     print

# score = 70
# if score >= 90: 
#     print("Your grade is A")
# elif score >= 80: 
#     print("Your grade is B")
# elif score >=70:
#     print("Your grade is C")
# else :
#     print("Your grade is F")

# fruit = ["apple", "mango", "grape", "banana", "melon"]
# fru = input("좋아하는 과일을 입력하시오 : ")
# if fru in fruit : 
#     print("과일이 목록에 있습니다.")
# elif fru == "없음" :
#     print("과일을 먹어보세요.")
# else : 
#     print("과일이 목록에 없습니다.")
    
kor = float(input("국어 점수 입력 : "))
eng = float(input("영어 점수 입력 : "))
math = float(input("수학 점수 입력 : "))
avg = (kor+eng+math)/3
if avg >= 60:
    print("성적 평균은", avg, "이며, 합격입니다.")
else : 
    print("성적 평균은", avg, "이며, 불합격입니다.")
if avg>=60 and kor>=50 and eng>=50 and math>=50 :
    print("성적 평균은", avg, "이며, 과락 과목도 없기 때문에 합격입니다.")
else :
    if avg>=60:
        print("성적 평균은", avg, "이지만 과락 과목이 있어서 불합격입니다.")
    else : 
        print("성적 평균은", avg, "이며, 불합격입니다.")

if avg>=60 :
    if kor>=50 and eng>=50 and math>=50 :
        print("평균은", avg, "이고 과락 과목도 없기 때문에 합격입니다.")
    else : 
        print("평균은", avg, "이지만 과락과목이 있기 때문에 불합격입니다.")
else :
    print("평균이", avg, "이기 때문에 불합격입니다.")
#line 90이 틀린 이유: 국, 영, 수 중 하나만 충족이 안되어도 불합격이라 and말고 or을 써야 한다.
#fix-> if kor<50 or eng<50 or math<50 :
#           print("평균은", avg, "이지만 과락 과목이 있어서 불합격입니다.")

#BMI지수
height = float(input("키를 입력하시오 : "))
weight = float(input("몸무게를 입력하시오 : "))
BMI = weight/(height * height)
if BMI < 18.5 :
    print("당신의 BMI지수는", BMI, "이며, 저체중입니다.")
elif BMI < 23 :
    print("당신의 BMI지수는", BMI, "이며, 정상입니다.")
elif BMI < 25 :
    print("당신의 BMI지수는", BMI, "이며, 과체중입니다.")
elif BMI < 30 :
    print("당신의 BMI지수는", BMI, "이며, 비만1입니다.")
elif BMI < 40 :
    print("당신의 BMI지수는", BMI, "이며, 비만2입니다.")
else : 
    print("당신의 BMI지수는", BMI, "이며, 심각한 비만3입니다.")