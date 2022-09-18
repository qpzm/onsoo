'''
name=input("name:")
age=input("age:")

do=input("도:")
si=input("시:")
gu=input("구:")
other=input("나머지:")

print("저의 주소는",do, si, gu, other,"입니다")

score = float(input("Inpur your score:"))
type=input("Input Letter(L) or PF(PF):")

if type=="L":
    if score<60:
        print("your grade is F")
    elif score<70:
        print("your grade is D")
    elif score<80:
        print("your grade is C")
    elif score<90:
        print("your grade is B")
    else:
        print("your grade is A")

elif type=="PF":
    if score<60:
        print("Fail")
    elif score<90:
        print("Pass")
    else:
        print("PD(Pass with Distinction)")

n1=int(input("n1:"))
n2=int(input("n2:"))
n3=int(input("n3:"))
n4=int(input("n4:"))
n5=int(input("n5:"))
n6=int(input("n6:"))
n7=int(input("n7:"))

n=[n1,n2,n3,n4,n5,n6,n7]
b=n1
b2=n1

if n1==n2==n3==n4==n5==n6==n7:
    print("동일한 수")
else:
    for i in n:
        if i>b:
            b=i
    for i in n:
        if i<b2:
            b2=i
    for i in n:
        if i<b and i>b2:
            b2=i
    print("두번째로 큰 수는",b2,"입니다.")


word=input("word:")
a=len(word)-1

if word[a]=="y":
    word=word.replace("y","ies")
elif word[a]=="f":
    word=word.replace("f","ves")
elif word[a-1]=="fe":
    word=word.replace("fe","ves")
elif word[a-1:]=="us":
    word=word.replace("us","i")
elif word[a]=="s" or word[a]=="x" or word[a]=="z" or word[a-1:]=="ch" or word[a-1:]=="sh":
    word=word+"es"
else:
    word=word+"s"

print(word)


num_list=[]
count_list=[0 for i in range(30)]
most_count=0
most_num=[]
most_count_list=[]

for i in range(30):
    num=int(input("숫자:"))
    num_list.append(num)

for i in range(30):
    for j in range(30):
        if num_list[i]==num_list[j]:
            count_list[i]+=1
for i in range(29):
    if count_list[i]>count_list[i+1] and count_list[i]>most_count:
        most_count=count_list[i]
        if num_list[i] not in most_num:
            most_num.append(num_list[i])
            most_count_list.append(count_list[i])
print("가장 많이 반복된 수와 빈도수:", end=' ')

for i in range(len(most_num)):
    print(most_num[i],most_count_list[i],"회", end=' ')

print(' ')

largest=num
for i in range(30):
    if num_list[i]>num:
        largest=num_list[i]

print("가장 큰 수:", largest)
        

n=int(input("정수입력:"))
print("*"*n)

n=int(input("양의 정수를 입력하세요:"))

if n>0:
    for i in range(1,n+1):
        print(i*'*')

n1=int(input("양의 정수를 입력하세요:"))
n2=int(input("양의 정수를 입력하세요:"))
sum=0
if n1<=0 or n2<=0:
    print("양의 정수가 아니라서 입력에러 입니다")
else:
    if n1<n2:
        for i in range(n1,n2+1):
            sum=sum+i
            if i==n2:
                print(i,"=",end='')
            else:
                print(i,"+",end='')
        print(sum)
    elif n1>n2:
        for i in range(n1,n2-1,-1):
            sum=sum+i
            if i==n2:
                print(i,'=',end='')
            else:
                print(i,'+',end='')
        print(sum)
    else:
        print("동일한 수 입니다")


n=int(input("양의 정수를 입력하세요:"))
prime=True

for i in range(2,n):
    if n%i==0:
        prime=False
        break

if prime==True:
    print(n,"은 소수입니다")
else:
    print(n,"은 소수가 아닙니다. 약수는",end=' ')
    for i in range(1,n+1):
        if n%i==0:
            print(i, end=' ')
    print("입니다")

n=int(input("양의 정수를 입력하세요:"))
prime=True
t1=[1]

for i in range(2,n):
    if n%i==0:
        prime=False
        t1.append(i)
t1.append(n)
if prime==True:
    print(n,"은 소수입니다.")
else:
    print(n, "은 소수가 아닙니다. 약수는 ",t1,"입니다.")



wordstr=''
bword=''
word=input("단어를 입력하세요:")

word=word.lower()
for ch in word:
    if ch.isalpha()==True:
        wordstr=wordstr+ch

for i in range(len(wordstr)-1,-1,-1):
    bword=bword+wordstr[i]
if bword==wordstr:
    print("palindrome")

year=input("태어난 년도:")
month=input("태어난 월:")
date=input("태어난 날짜:")

birth=year+month+date
print(birth)


year=input("태어난 년도:")
month=input("티어난 월:")
date=input("태어난 날짜:")
age=0
birth=year+month+date

if birth>"20210423":
    print("잘못된 정보 입니다.")
else:
    age=2021-int(year)
    if month>"04":
        age=age-1
    elif month=="04" and date>"23":
        age=age-1
print("만 나이:",age)


n1=int(input("정수입력:"))
n2=int(input("정수입력:"))
n3=int(input("정수입력:"))
n=[n1,n2,n3]

n_sort=[]
n_sort=n.sort()
reverse_n=[]

n=int(input("정수:"))
sum=0
ave=0

for i in range(1,n+1):
    sum=sum+i

ave=sum/n

print(sum, ave)

fac=1
n=int(input("양의 정수를 입력하세요:"))

if n<=0:
    print("계산할 수 없는 값입니다.")
else:
    print(n,"가 입력되면,",end=' ')
    for i in range(n,0,-1):
        fac=1
        for j in range(1,i+1):
            fac=fac*j
        print(fac, end=' ')

        if fac==1:
            print(fac)
        else:
            print(fac,end=',')
'''

t=['apple','banana']
for i in t:
    print(i)
