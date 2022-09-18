#Kimhaeun
#22100224
#Quiz1
#Problem1

birthdate=input("태어난 년도를 입력하시오(YYYYMMDD):")

year=birthdate[0:4]
month=birthdate[4:6]
date=birthdate[6:]

if birthdate>"2021301":
    print("잘못된 정보를 입력하셨습니다.")
else:
    age=2021-int(year)
    if month>"03":
        age=age-1
    elif month=="03" and date>"01":
        age=age-1

print("당신의 만 나이는",age,"입니다.")
