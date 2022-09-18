#Kimhaeun
#22100224
#phoneNumber
d={2:('A','B','C'),3:('D','E','F'),4:('G','H','I'),5:('J','K','L'),6:('M','N','O'),7:('P','Q','R','S'),8:('T','U','V'),9:('W','X','Y','Z')}
phoneNumber=[]
str=input("10자리 문자열을 입력하세요:")

while len(str) != 10:
    str=input("10자리 문자열을 입력하세요:")

str=str.upper()

for ch in str:
    for key in d.keys():
        if ch in d[key]:
            phoneNumber.append(key)

    
print(phoneNumber)
phoneNumber.insert(3,'-')
phoneNumber.insert(7,'-')

for i in range(len(phoneNumber)):
    print(phoneNumber[i],end='')


    
