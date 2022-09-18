'''
작성자 : 박현민
프로그램의 목적 : 화학식을 입력받아 분자량 계산하는 프로그램이다.
'''
#화학식을 입력받는다
sentence=input('화학식을 입력 하시오 : ')


#각 화학식을 하나씩 list에 추가한다.
lst=[]
for i in sentence:
    lst.append(i)

#초기값들을 설정해준다.
a=0.0
b=0.0

c=0.0
d=0.0

e=0.0
f=0.0

g=0.0
h=0.0

i=0.0
j=0.0

k=0.0
l=0.0

m=0.0
n=0.0

o=0.0
p=0.0

q=0.0
r=0.0

s=0.0
t=0.0

#lst의 길이에 따라 if문으로 나누어 출력한
if len(lst)==1:
    if lst[0]=='O':
        a=15.9994
    elif lst[0]=='S':
        a=32.066
    elif lst[0]=='C':
        a=12.011
    elif lst[0]=='H':
        a=1.00794
    elif lst[0]=="N":
        a=14.00674
    b=1.0

elif len(lst)==2:
    if lst[0]=='O':
        a=15.9994
    elif lst[0]=='S':
        a=32.066
    elif lst[0]=='C':
        a=12.011
    elif lst[0]=='H':
        a=1.00794
    elif lst[0]=="N":
        a=14.00674

    if lst[1] in 'OSCHN':
        b=1.0
        if lst[1]=='O':
            c=15.9994
        elif lst[1]=='S':
            c=32.066
        elif lst[1]=='C':
            c=12.011
        elif lst[1]=='H':
            c=1.00794
        elif lst[1]=="N":
            c=14.00674
        d=1.0

    elif lst[1] not in 'OSCHN':
        float(lst[1])
        b=lst[1]

elif len(lst)==3:
    if lst[0]=='O':
        a=15.9994
    elif lst[0]=='S':
        a=32.066
    elif lst[0]=='C':
        a=12.011
    elif lst[0]=='H':
        a=1.00794
    elif lst[0]=="N":
        a=14.00674

    if lst[1] in 'OSCHN':
        b=1.0
        if lst[1]=='O':
            c=15.9994
        elif lst[1]=='S':
            c=32.066
        elif lst[1]=='C':
            c=12.011
        elif lst[1]=='H':
            c=1.00794
        elif lst[1]=="N":
            c=14.00674
        d=1.0

    elif lst[1] not in 'OSCHN':
        float(lst[1])
        b=lst[1]

    if lst[2] in 'OSCHN':
        if lst[2]=='O':
            e=15.9994
        elif lst[2]=='S':
            e=32.066
        elif lst[2]=='C':
            e=12.011
        elif lst[2]=='H':
            e=1.00794
        elif lst[2]=="N":
            e=14.00674
        f=1.0
    elif lst[2] not in 'OSCHN':
        float(lst[2])
        d=lst[2]

elif len(lst)==4:
    if lst[0]=='O':
        a=15.9994
    elif lst[0]=='S':
        a=32.066
    elif lst[0]=='C':
        a=12.011
    elif lst[0]=='H':
        a=1.00794
    elif lst[0]=="N":
        a=14.00674

    if lst[1] in 'OSCHN':
        b=1.0
        if lst[1]=='O':
            c=15.9994
        elif lst[1]=='S':
            c=32.066
        elif lst[1]=='C':
            c=12.011
        elif lst[1]=='H':
            c=1.00794
        elif lst[1]=="N":
            c=14.00674
        d=1.0

    elif lst[1] not in 'OSCHN':
        float(lst[1])
        b=lst[1]

    if lst[2] in 'OSCHN':
        if lst[2]=='O':
            e=15.9994
        elif lst[2]=='S':
            e=32.066
        elif lst[2]=='C':
            e=12.011
        elif lst[2]=='H':
            e=1.00794
        elif lst[2]=="N":
            e=14.00674
        f=1.0
    elif lst[2] not in 'OSCHN':
        float(lst[2])
        d=lst[2]

    if lst[3] in 'OSCHN':
        if lst[3]=='O':
            g=15.9994
        elif lst[3]=='S':
            g=32.066
        elif lst[3]=='C':
            g=12.011
        elif lst[3]=='H':
            g=1.00794
        elif lst[3]=="N":
            g=14.00674
        h=1.0
    elif lst[3] not in 'OSCHN':
        float(lst[3])
        f=lst[3]

elif len(lst)==5:
    if lst[0]=='O':
        a=15.9994
    elif lst[0]=='S':
        a=32.066
    elif lst[0]=='C':
        a=12.011
    elif lst[0]=='H':
        a=1.00794
    elif lst[0]=="N":
        a=14.00674

    if lst[1] in 'OSCHN':
        b=1.0
        if lst[1]=='O':
            c=15.9994
        elif lst[1]=='S':
            c=32.066
        elif lst[1]=='C':
            c=12.011
        elif lst[1]=='H':
            c=1.00794
        elif lst[1]=="N":
            c=14.00674
        d=1.0

    elif lst[1] not in 'OSCHN':
        float(lst[1])
        b=lst[1]

    if lst[2] in 'OSCHN':
        if lst[2]=='O':
            e=15.9994
        elif lst[2]=='S':
            e=32.066
        elif lst[2]=='C':
            e=12.011
        elif lst[2]=='H':
            e=1.00794
        elif lst[2]=="N":
            e=14.00674
        f=1.0
    elif lst[2] not in 'OSCHN':
        float(lst[2])
        d=lst[2]

    if lst[3] in 'OSCHN':
        if lst[3]=='O':
            g=15.9994
        elif lst[3]=='S':
            g=32.066
        elif lst[3]=='C':
            g=12.011
        elif lst[3]=='H':
            g=1.00794
        elif lst[3]=="N":
            g=14.00674
        h=1.0
    elif lst[3] not in 'OSCHN':
        float(lst[3])
        f=lst[3]

    if lst[4] in 'OSCHN':
        if lst[4]=='O':
            i=15.9994
        elif lst[4]=='S':
            i=32.066
        elif lst[4]=='C':
            i=12.011
        elif lst[4]=='H':
            i=1.00794
        elif lst[4]=="N":
            i=14.00674
        j=1.0
    elif lst[4] not in 'OSCHN':
        float(lst[4])
        h=lst[4]
    

elif len(lst)==6:
    if lst[0]=='O':
        a=15.9994
    elif lst[0]=='S':
        a=32.066
    elif lst[0]=='C':
        a=12.011
    elif lst[0]=='H':
        a=1.00794
    elif lst[0]=="N":
        a=14.00674

    if lst[1] in 'OSCHN':
        b=1.0
        if lst[1]=='O':
            c=15.9994
        elif lst[1]=='S':
            c=32.066
        elif lst[1]=='C':
            c=12.011
        elif lst[1]=='H':
            c=1.00794
        elif lst[1]=="N":
            c=14.00674
        d=1.0

    elif lst[1] not in 'OSCHN':
        float(lst[1])
        b=lst[1]

    if lst[2] in 'OSCHN':
        if lst[2]=='O':
            e=15.9994
        elif lst[2]=='S':
            e=32.066
        elif lst[2]=='C':
            e=12.011
        elif lst[2]=='H':
            e=1.00794
        elif lst[2]=="N":
            e=14.00674
        f=1.0
    elif lst[2] not in 'OSCHN':
        float(lst[2])
        d=lst[2]

    if lst[3] in 'OSCHN':
        if lst[3]=='O':
            g=15.9994
        elif lst[3]=='S':
            g=32.066
        elif lst[3]=='C':
            g=12.011
        elif lst[3]=='H':
            g=1.00794
        elif lst[3]=="N":
            g=14.00674
        h=1.0
    elif lst[3] not in 'OSCHN':
        float(lst[3])
        f=lst[3]

    if lst[4] in 'OSCHN':
        if lst[4]=='O':
            i=15.9994
        elif lst[4]=='S':
            i=32.066
        elif lst[4]=='C':
            i=12.011
        elif lst[4]=='H':
            i=1.00794
        elif lst[4]=="N":
            i=14.00674
        j=1.0
    elif lst[4] not in 'OSCHN':
        float(lst[4])
        h=lst[4]

    if lst[5] in 'OSCHN':
        if lst[5]=='O':
            k=15.9994
        elif lst[5]=='S':
            k=32.066
        elif lst[5]=='C':
            k=12.011
        elif lst[5]=='H':
            k=1.00794
        elif lst[5]=="N":
            k=14.00674
        l=1.0
    elif lst[5] not in 'OSCHN':
        float(lst[5])
        j=lst[5]
        
elif len(lst)==7:
    if lst[0]=='O':
        a=15.9994
    elif lst[0]=='S':
        a=32.066
    elif lst[0]=='C':
        a=12.011
    elif lst[0]=='H':
        a=1.00794
    elif lst[0]=="N":
        a=14.00674

    if lst[1] in 'OSCHN':
        b=1.0
        if lst[1]=='O':
            c=15.9994
        elif lst[1]=='S':
            c=32.066
        elif lst[1]=='C':
            c=12.011
        elif lst[1]=='H':
            c=1.00794
        elif lst[1]=="N":
            c=14.00674
        d=1.0

    elif lst[1] not in 'OSCHN':
        float(lst[1])
        b=lst[1]

    if lst[2] in 'OSCHN':
        if lst[2]=='O':
            e=15.9994
        elif lst[2]=='S':
            e=32.066
        elif lst[2]=='C':
            e=12.011
        elif lst[2]=='H':
            e=1.00794
        elif lst[2]=="N":
            e=14.00674
        f=1.0
    elif lst[2] not in 'OSCHN':
        float(lst[2])
        d=lst[2]

    if lst[3] in 'OSCHN':
        if lst[3]=='O':
            g=15.9994
        elif lst[3]=='S':
            g=32.066
        elif lst[3]=='C':
            g=12.011
        elif lst[3]=='H':
            g=1.00794
        elif lst[3]=="N":
            g=14.00674
        h=1.0
    elif lst[3] not in 'OSCHN':
        float(lst[3])
        f=lst[3]

    if lst[4] in 'OSCHN':
        if lst[4]=='O':
            i=15.9994
        elif lst[4]=='S':
            i=32.066
        elif lst[4]=='C':
            i=12.011
        elif lst[4]=='H':
            i=1.00794
        elif lst[4]=="N":
            i=14.00674
        j=1.0
    elif lst[4] not in 'OSCHN':
        float(lst[4])
        h=lst[4]

    if lst[5] in 'OSCHN':
        if lst[5]=='O':
            k=15.9994
        elif lst[5]=='S':
            k=32.066
        elif lst[5]=='C':
            k=12.011
        elif lst[5]=='H':
            k=1.00794
        elif lst[5]=="N":
            k=14.00674
        l=1.0
    elif lst[5] not in 'OSCHN':
        float(lst[5])
        j=lst[5]

    if lst[6] in 'OSCHN':
        if lst[6]=='O':
            m=15.9994
        elif lst[6]=='S':
            m=32.066
        elif lst[6]=='C':
            m=12.011
        elif lst[6]=='H':
            m=1.00794
        elif lst[6]=="N":
            m=14.00674
        n=1.0
    elif lst[6] not in 'OSCHN':
        float(lst[6])
        l=lst[6]

elif len(lst)==8:
    if lst[0]=='O':
        a=15.9994
    elif lst[0]=='S':
        a=32.066
    elif lst[0]=='C':
        a=12.011
    elif lst[0]=='H':
        a=1.00794
    elif lst[0]=="N":
        a=14.00674

    if lst[1] in 'OSCHN':
        b=1.0
        if lst[1]=='O':
            c=15.9994
        elif lst[1]=='S':
            c=32.066
        elif lst[1]=='C':
            c=12.011
        elif lst[1]=='H':
            c=1.00794
        elif lst[1]=="N":
            c=14.00674
        d=1.0

    elif lst[1] not in 'OSCHN':
        float(lst[1])
        b=lst[1]

    if lst[2] in 'OSCHN':
        if lst[2]=='O':
            e=15.9994
        elif lst[2]=='S':
            e=32.066
        elif lst[2]=='C':
            e=12.011
        elif lst[2]=='H':
            e=1.00794
        elif lst[2]=="N":
            e=14.00674
        f=1.0
    elif lst[2] not in 'OSCHN':
        float(lst[2])
        d=lst[2]

    if lst[3] in 'OSCHN':
        if lst[3]=='O':
            g=15.9994
        elif lst[3]=='S':
            g=32.066
        elif lst[3]=='C':
            g=12.011
        elif lst[3]=='H':
            g=1.00794
        elif lst[3]=="N":
            g=14.00674
        h=1.0
    elif lst[3] not in 'OSCHN':
        float(lst[3])
        f=lst[3]

    if lst[4] in 'OSCHN':
        if lst[4]=='O':
            i=15.9994
        elif lst[4]=='S':
            i=32.066
        elif lst[4]=='C':
            i=12.011
        elif lst[4]=='H':
            i=1.00794
        elif lst[4]=="N":
            i=14.00674
        j=1.0
    elif lst[4] not in 'OSCHN':
        float(lst[4])
        h=lst[4]

    if lst[5] in 'OSCHN':
        if lst[5]=='O':
            k=15.9994
        elif lst[5]=='S':
            k=32.066
        elif lst[5]=='C':
            k=12.011
        elif lst[5]=='H':
            k=1.00794
        elif lst[5]=="N":
            k=14.00674
        l=1.0
    elif lst[5] not in 'OSCHN':
        float(lst[5])
        j=lst[5]

    if lst[6] in 'OSCHN':
        if lst[6]=='O':
            m=15.9994
        elif lst[6]=='S':
            m=32.066
        elif lst[6]=='C':
            m=12.011
        elif lst[6]=='H':
            m=1.00794
        elif lst[6]=="N":
            m=14.00674
        n=1.0
    elif lst[6] not in 'OSCHN':
        float(lst[6])
        l=lst[6]

    if lst[7] in 'OSCHN':
        if lst[7]=='O':
            o=15.9994
        elif lst[7]=='S':
            o=32.066
        elif lst[7]=='C':
            o=12.011
        elif lst[7]=='H':
            o=1.00794
        elif lst[7]=="N":
            o=14.00674
        p=1.0
    elif lst[7] not in 'OSCHN':
        float(lst[7])
        n=lst[7]

elif len(lst)==9:
    if lst[0]=='O':
        a=15.9994
    elif lst[0]=='S':
        a=32.066
    elif lst[0]=='C':
        a=12.011
    elif lst[0]=='H':
        a=1.00794
    elif lst[0]=="N":
        a=14.00674

    if lst[1] in 'OSCHN':
        b=1.0
        if lst[1]=='O':
            c=15.9994
        elif lst[1]=='S':
            c=32.066
        elif lst[1]=='C':
            c=12.011
        elif lst[1]=='H':
            c=1.00794
        elif lst[1]=="N":
            c=14.00674
        d=1.0

    elif lst[1] not in 'OSCHN':
        float(lst[1])
        b=lst[1]

    if lst[2] in 'OSCHN':
        if lst[2]=='O':
            e=15.9994
        elif lst[2]=='S':
            e=32.066
        elif lst[2]=='C':
            e=12.011
        elif lst[2]=='H':
            e=1.00794
        elif lst[2]=="N":
            e=14.00674
        f=1.0
    elif lst[2] not in 'OSCHN':
        float(lst[2])
        d=lst[2]

    if lst[3] in 'OSCHN':
        if lst[3]=='O':
            g=15.9994
        elif lst[3]=='S':
            g=32.066
        elif lst[3]=='C':
            g=12.011
        elif lst[3]=='H':
            g=1.00794
        elif lst[3]=="N":
            g=14.00674
        h=1.0
    elif lst[3] not in 'OSCHN':
        float(lst[3])
        f=lst[3]

    if lst[4] in 'OSCHN':
        if lst[4]=='O':
            i=15.9994
        elif lst[4]=='S':
            i=32.066
        elif lst[4]=='C':
            i=12.011
        elif lst[4]=='H':
            i=1.00794
        elif lst[4]=="N":
            i=14.00674
        j=1.0
    elif lst[4] not in 'OSCHN':
        float(lst[4])
        h=lst[4]

    if lst[5] in 'OSCHN':
        if lst[5]=='O':
            k=15.9994
        elif lst[5]=='S':
            k=32.066
        elif lst[5]=='C':
            k=12.011
        elif lst[5]=='H':
            k=1.00794
        elif lst[5]=="N":
            k=14.00674
        l=1.0
    elif lst[5] not in 'OSCHN':
        float(lst[5])
        j=lst[5]

    if lst[6] in 'OSCHN':
        if lst[6]=='O':
            m=15.9994
        elif lst[6]=='S':
            m=32.066
        elif lst[6]=='C':
            m=12.011
        elif lst[6]=='H':
            m=1.00794
        elif lst[6]=="N":
            m=14.00674
        n=1.0
    elif lst[6] not in 'OSCHN':
        float(lst[6])
        l=lst[6]

    if lst[7] in 'OSCHN':
        if lst[7]=='O':
            o=15.9994
        elif lst[7]=='S':
            o=32.066
        elif lst[7]=='C':
            o=12.011
        elif lst[7]=='H':
            o=1.00794
        elif lst[7]=="N":
            o=14.00674
        p=1.0
    elif lst[7] not in 'OSCHN':
        float(lst[7])
        n=lst[7]

    if lst[8] in 'OSCHN':
        if lst[8]=='O':
            q=15.9994
        elif lst[8]=='S':
            q=32.066
        elif lst[8]=='C':
            q=12.011
        elif lst[8]=='H':
            q=1.00794
        elif lst[8]=="N":
            q=14.00674
        r=1.0
    elif lst[8] in 'OSCHN':
        float(lst[8])
        p=lst[8]

elif len(lst)==10:
    if lst[0]=='O':
        a=15.9994
    elif lst[0]=='S':
        a=32.066
    elif lst[0]=='C':
        a=12.011
    elif lst[0]=='H':
        a=1.00794
    elif lst[0]=="N":
        a=14.00674

    if lst[1] in 'OSCHN':
        b=1.0
        if lst[1]=='O':
            c=15.9994
        elif lst[1]=='S':
            c=32.066
        elif lst[1]=='C':
            c=12.011
        elif lst[1]=='H':
            c=1.00794
        elif lst[1]=="N":
            c=14.00674
        d=1.0

    elif lst[1] not in 'OSCHN':
        float(lst[1])
        b=lst[1]

    if lst[2] in 'OSCHN':
        if lst[2]=='O':
            e=15.9994
        elif lst[2]=='S':
            e=32.066
        elif lst[2]=='C':
            e=12.011
        elif lst[2]=='H':
            e=1.00794
        elif lst[2]=="N":
            e=14.00674
        f=1.0
    elif lst[2] not in 'OSCHN':
        float(lst[2])
        d=lst[2]

    if lst[3] in 'OSCHN':
        if lst[3]=='O':
            g=15.9994
        elif lst[3]=='S':
            g=32.066
        elif lst[3]=='C':
            g=12.011
        elif lst[3]=='H':
            g=1.00794
        elif lst[3]=="N":
            g=14.00674
        h=1.0
    elif lst[3] not in 'OSCHN':
        float(lst[3])
        f=lst[3]

    if lst[4] in 'OSCHN':
        if lst[4]=='O':
            i=15.9994
        elif lst[4]=='S':
            i=32.066
        elif lst[4]=='C':
            i=12.011
        elif lst[4]=='H':
            i=1.00794
        elif lst[4]=="N":
            i=14.00674
        j=1.0
    elif lst[4] not in 'OSCHN':
        float(lst[4])
        h=lst[4]

    if lst[5] in 'OSCHN':
        if lst[5]=='O':
            k=15.9994
        elif lst[5]=='S':
            k=32.066
        elif lst[5]=='C':
            k=12.011
        elif lst[5]=='H':
            k=1.00794
        elif lst[5]=="N":
            k=14.00674
        l=1.0
    elif lst[5] not in 'OSCHN':
        float(lst[5])
        j=lst[5]

    if lst[6] in 'OSCHN':
        if lst[6]=='O':
            m=15.9994
        elif lst[6]=='S':
            m=32.066
        elif lst[6]=='C':
            m=12.011
        elif lst[6]=='H':
            m=1.00794
        elif lst[6]=="N":
            m=14.00674
        n=1.0
    elif lst[6] not in 'OSCHN':
        float(lst[6])
        l=lst[6]

    if lst[7] in 'OSCHN':
        if lst[7]=='O':
            o=15.9994
        elif lst[7]=='S':
            o=32.066
        elif lst[7]=='C':
            o=12.011
        elif lst[7]=='H':
            o=1.00794
        elif lst[7]=="N":
            o=14.00674
        p=1.0
    elif lst[7] not in 'OSCHN':
        float(lst[7])
        n=lst[7]

    if lst[8] in 'OSCHN':
        if lst[8]=='O':
            q=15.9994
        elif lst[8]=='S':
            q=32.066
        elif lst[8]=='C':
            q=12.011
        elif lst[8]=='H':
            q=1.00794
        elif lst[8]=="N":
            q=14.00674
        r=1.0
    elif lst[8] in 'OSCHN':
        float(lst[8])
        p=lst[8]

    if lst[9] in 'OSCHN':
        if lst[9]=='O':
            s=15.9994
        elif lst[9]=='S':
            s=32.066
        elif lst[9]=='C':
            s=12.011
        elif lst[9]=='H':
            s=1.00794
        elif lst[9]=="N":
            s=14.00674
        t=1.0
    elif lst[9] not in 'OSCHN':
        float(lst[9])
        r=lst[9]
        

#최종 출력문이다.
print(sentence,'의 분자량은',float(a)*float(b)+float(c)*float(d)+float(e)*float(f)+float(g)*float(h)+float(i)*float(j)+float(k)*float(l)+float(m)*float(n)+float(o)*float(p)+float(q)*float(r)+float(s)*float(t))

    

    
   
        
        




        
    
            
    
        
        


    




        
