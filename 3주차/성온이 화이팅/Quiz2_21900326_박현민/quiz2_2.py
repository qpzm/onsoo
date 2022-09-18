'''
작성자 : 21900326 박현민
quiz2 3번
'''
import random

num_p=int(input('전체 인원 수를 입력하시오 : '))
lst=[]
for i in range(num_p):
    a=input('인원의 이름을 입력하시오 : ')
    lst.append(a)



randomlst=[]

def ladder(num,listname):
    if num<0:
        print('인원의 양수가 아닙니다')
    else:
        ladderlst=['심부름','5천원','7천원','1만원','500원']
        for i in range(num):
            randomlst.append(random.choice(ladderlst))

        a=list(zip(lst,randomlst))
        
        print(a)

        for i in range(len(a)):
            if a[i][1]=='심부름':
                print('심부름 할 사람은 ',a[i][0])


ladder(num_p,lst)
        
        
        
    
