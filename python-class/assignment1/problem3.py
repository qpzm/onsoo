name = input("이름: ")
HGD = [name]
print (HGD[0][0])
print (HGD[0][0 : 2])
print (HGD[0][0:])
print (HGD[0][1 : ])
print (HGD[0][2])

# name[0:1] -> 박
# name[0:2] -> 박성
# name[0:3] -> 박성온
# name[1:0] -> 성온
# name[2:0] -> 온
name = input("이름: ")
print(name[0:1])
print(name[0:2])
print(name[0:3])
print(name[1:3])
print(name[2:3])