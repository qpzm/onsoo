score = float(input("당신의 점수를 입력하시오: "))
grade = input("성적 유형을 입력하시오(L or PF): ")
if grade == "PF":
    if score >= 90:
        print("PD(Pass with Distinction)")
    elif score >= 60:
        print("Pass")
    else:
        print("Fail")
elif grade == "L":
    if score >= 90:
        print("당신의 성적은 A입니다")
    elif score >= 80:
        print("당신의 성적은 B입니다")
    elif score >= 70:
        print("당신의 성적은 C입니다")
    elif score >= 60:
        print("당신의 성적은 D입니다")
    else: 
        print("당신의 성적은 F입니다")
else:
    print("성적 유형을 올바르게 입력하세요")
