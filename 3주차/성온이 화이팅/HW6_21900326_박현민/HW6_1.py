'''
작성자 : 박현민
프로그램의 목적 : 과일명과 색상을 dictionary로 제작하고 색상을 영문으로 입력
                  받은 후 해당 색상을 가지는 과일명을 모두 리스트에 저장하여
                  출력하는 프로그램
'''
dic={'apple':['red','pink','ivory','green'],'strawberry':['red','black','green'],'grape':['purple','green'],'blueberry':['purple','white'],'peach':['pink','ivory','white','yellow']}

a=input('색상을 영어로 입력하시오 : ')

lst=[]

b=list(dic.items())

for i in range(len(b)):
    if a in b[i][1]:
        lst.append(b[i][0])
        
print(lst)
   
