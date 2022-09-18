#kimhaeun
#22100224
#problem1

fr=['Apple','Banana','Coconut','Lime','Blueberry','Zetberry','STRAWBERRY']
countList=[]

def V_count(listname):
    vowel=['a','e','i','o','u','A','E','I','O','U']
    for i in range(len(listname)):
        count=0
        for ch in listname[i]:
            if ch in vowel:
                count+=1
        countList.append(count)
    return countList

V_count(fr)
s=list(zip(fr,countList))
d=dict(s)

print(d)


'''               
fa=['music','rhythm','song','hymn']
V_count(fa)
t=list(zip(fa,countList))
dt=dict(t)

print(dt)
'''
