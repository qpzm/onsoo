wea = float(input("온도를 입력해주세요: "))
if wea <= -10:
    print("아주 추운 날씨입니다.")
elif wea > -10 and wea <= 0:
    print("추운 날씨 입니다.")
elif wea > 0 and wea <= 12:
    print("살짝 싸늘한 날씨 입니다.")
elif wea > 12 and wea <= 25:
    print("활동하기 좋은 날씨 입니다.")
elif wea > 25 and wea <= 32:
    print("더운 날씨 입니다.")
else :
    print("아주 더운 날씨입니다.")
