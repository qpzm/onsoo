#kimhaeun
#22100224
#1

outf=open("score.txt","w")

for i in range(10):
    name=input("name:")
    kor=int(input("kor:"))
    eng=int(input("eng:"))
    math=int(input("math:"))
    s=name+','+str(kor)+','+str(eng)+','+str(math)+'\n'
    outf.write(s)

outf.close()

inf=open("score.txt",'r')
s=inf.readlines()
sum=0
result=[]
for i in range(len(s)):
    sm=s[i].split(',')
    sum=int(sm[1])+int(sm[2])+int(sm[3])
    avg=sum/3
    result.append((sum,avg))

print(result)

inf.close()


    
