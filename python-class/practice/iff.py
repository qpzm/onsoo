bir = input("생년월일을 입력하세요 : ")
year = bir[0:4]
mon = bir[4:6]
day = bir[6:8]
if bir > "20220912" : 
    print("나이를 계산할 수 없습니다.")
else : 
    age = 2022 - int(year)
    if mon < "9" and day < "12" :
        age = age-1
    print("당신의 만나이는", age, "입니다.")