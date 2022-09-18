result = ""
loc1 = input("도 : ")
if(loc1 != ""):
    result = result + loc1
loc2 = input("시 : ")
if(loc1 != ""):
    result = result + " " + loc2
loc3 = input("구 : ")
if(loc3 != ""):
    result = result + " " + loc3
loc4 = input("나머지 : ")
if(loc4 != ""):
    result = result + " " + loc4
print("저의 주소는", result, "입니다.")