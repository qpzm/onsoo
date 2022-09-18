#Kimhaeun
#22100224
#Problem1
count=0
word=['Apple','box','buzz','CANTUS','dish','knife','lady','pitch','stimulus','wish','wolf']
t=[]

for i in word:
    count=0
    t=[]
    for char in i:
        #if ch in ['a','A',...]:
        if char=='a' or char=='A'or char=='e' or char=='E' or char=='i' or char=='I' or char=='o' or char=='O' or char=='u' or char=='U':
            count=count+1
            t.append(char)
    print(i,',',t,"로 모음",count,"개")
    
#자음을 세는 경우 not in ['a','A',...]
#단,스페이스랑 특수 문자를 제외해야 하는 경우 다른 조건문을 입력 
