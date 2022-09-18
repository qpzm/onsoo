'''
작성자 : 박현민
프로그램의 목적: 10개의 정수를 입력받아 리스트를 만들고
모든 element를 한칸씩 오른쪽으로 이동한 출력값과
10개의 아이템 중 중간에 위치한 2개의 element를 제거한 출력값,
전체 element중 제일 큰 수를 찾아 출력
전체 element중 중복되는 값 찾기, 합계와 평균을 출력하는 프로그램이다.
'''

#10개의 정수를 입력받아 list에 추가한다.
lst=[]
a=int(input('1 번째 정수를 입력하시오 : '))
lst.append(a)
b=int(input('2 번째 정수를 입력하시오 : '))
lst.append(b)
c=int(input('3 번째 정수를 입력하시오 : '))
lst.append(c)
d=int(input('4 번째 정수를 입력하시오 : '))
lst.append(d)
e=int(input('5 번째 정수를 입력하시오 : '))
lst.append(e)
f=int(input('6 번째 정수를 입력하시오 : '))
lst.append(f)
g=int(input('7 번째 정수를 입력하시오 : '))
lst.append(g)
h=int(input('8 번째 정수를 입력하시오 : '))
lst.append(h)
i=int(input('9 번째 정수를 입력하시오 : '))
lst.append(i)
j=int(input('10 번째 정수를 입력하시오 : '))
lst.append(j)

#입력받은 리스트를 출력한다.
print('리스트 : ',lst)

#오른쪽으로 한칸씩 이동후 출력한다.
lst.pop()
lst.insert(0,j)
print('오른쪽으로 한 칸씩 이동 : ',lst)

#중간의 위치한 2개의 element를 제거한 후 출력한다.
for i in range(2):
    del lst[4]
print('중간에 위치한 2개의 element 제거 : ',lst)

#sorted를 이용하여 정렬 후 가장 큰 수를 출력한다.
k=sorted(lst)
print('전체 element 중 가장 큰 수 : ', k[-1])

#중복 여부를 체크한다.
result=[]
for value in lst:
    if value not in result:
        result.append(value)

if result==lst:
    print('중복 여부 체크 : no duplicate elements')
else:
    if a==b:
        rest_list=list(filter(lambda x: lst[x]==a,range(len(lst))))
        print('중복 여부 체크 : exist duplicate elements',rest_list)
    elif a==c:
        rest_list=list(filter(lambda x: lst[x]==a,range(len(lst))))
        print('중복 여부 체크 : exist duplicate elements',rest_list)
    elif a==f:
        rest_list=list(filter(lambda x: lst[x]==a,range(len(lst))))
        print('중복 여부 체크 : exist duplicate elements',rest_list)
    elif a==g:
        rest_list=list(filter(lambda x: lst[x]==a,range(len(lst))))
        print('중복 여부 체크 : exist duplicate elements',rest_list)
    elif a==h:
        rest_list=list(filter(lambda x: lst[x]==a,range(len(lst))))
        print('중복 여부 체크 : exist duplicate elements',rest_list)
    elif a==i:
        rest_list=list(filter(lambda x: lst[x]==a,range(len(lst))))
        print('중복 여부 체크 : exist duplicate elements',rest_list)
    elif a==j:
        rest_list=list(filter(lambda x: lst[x]==a,range(len(lst))))
        print('중복 여부 체크 : exist duplicate elements',rest_list)
    elif b==c:
        rest_list=list(filter(lambda x: lst[x]==b,range(len(lst))))
        print('중복 여부 체크 : exist duplicate elements',rest_list)
    elif b==f:
        rest_list=list(filter(lambda x: lst[x]==b,range(len(lst))))
        print('중복 여부 체크 : exist duplicate elements',rest_list)
    elif b==g:
        rest_list=list(filter(lambda x: lst[x]==b,range(len(lst))))
        print('중복 여부 체크 : exist duplicate elements',rest_list)
    elif b==h:
        rest_list=list(filter(lambda x: lst[x]==b,range(len(lst))))
        print('중복 여부 체크 : exist duplicate elements',rest_list)
    elif b==i:
        rest_list=list(filter(lambda x: lst[x]==b,range(len(lst))))
        print('중복 여부 체크 : exist duplicate elements',rest_list)
    elif b==j:
        rest_list=list(filter(lambda x: lst[x]==b,range(len(lst))))
        print('중복 여부 체크 : exist duplicate elements',rest_list)
    elif c==f:
        rest_list=list(filter(lambda x: lst[x]==c,range(len(lst))))
        print('중복 여부 체크 : exist duplicate elements',rest_list)
    elif c==g:
        rest_list=list(filter(lambda x: lst[x]==c,range(len(lst))))
        print('중복 여부 체크 : exist duplicate elements',rest_list)
    elif c==h:
        rest_list=list(filter(lambda x: lst[x]==c,range(len(lst))))
        print('중복 여부 체크 : exist duplicate elements',rest_list)
    elif c==i:
        rest_list=list(filter(lambda x: lst[x]==c,range(len(lst))))
        print('중복 여부 체크 : exist duplicate elements',rest_list)
    elif c==j:
        rest_list=list(filter(lambda x: lst[x]==c,range(len(lst))))
        print('중복 여부 체크 : exist duplicate elements',rest_list)
    elif f==g:
        rest_list=list(filter(lambda x: lst[x]==f,range(len(lst))))
        print('중복 여부 체크 : exist duplicate elements',rest_list)
    elif f==h:
        rest_list=list(filter(lambda x: lst[x]==f,range(len(lst))))
        print('중복 여부 체크 : exist duplicate elements',rest_list)
    elif f==i:
        rest_list=list(filter(lambda x: lst[x]==f,range(len(lst))))
        print('중복 여부 체크 : exist duplicate elements',rest_list)
    elif f==j:
        rest_list=list(filter(lambda x: lst[x]==f,range(len(lst))))
        print('중복 여부 체크 : exist duplicate elements',rest_list)
    elif g==h:
        rest_list=list(filter(lambda x: lst[x]==g,range(len(lst))))
        print('중복 여부 체크 : exist duplicate elements',rest_list)
    elif g==i:
        rest_list=list(filter(lambda x: lst[x]==g,range(len(lst))))
        print('중복 여부 체크 : exist duplicate elements',rest_list)
    elif g==j:
        rest_list=list(filter(lambda x: lst[x]==g,range(len(lst))))
        print('중복 여부 체크 : exist duplicate elements',rest_list)
    elif h==i:
        rest_list=list(filter(lambda x: lst[x]==h,range(len(lst))))
        print('중복 여부 체크 : exist duplicate elements',rest_list)
    elif h==j:
        rest_list=list(filter(lambda x: lst[x]==h,range(len(lst))))
        print('중복 여부 체크 : exist duplicate elements',rest_list)
    elif i==j:
        rest_list=list(filter(lambda x: lst[x]==i,range(len(lst))))
        print('중복 여부 체크 : exist duplicate elements',rest_list)
        

#합계와 평균을 출력한다.
s=sum(lst)
print('저장된 값들의 합계는',s,'평균은',s/len(lst))




    


