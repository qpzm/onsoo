#kimhaeun
#22100224
#CountFile

import sys

try:
    problem = open('problem.txt','r')
    outf = open('output.txt','w')

except IOError as err:
    print("Error: can't find file or read data")
problem.close()
outf.close()

w_count=0
ch_count=0
ch_s_count=0
l_count=0

def CountFile(filename):
    
    global w_count
    global ch_count
    global ch_s_count
    global l_count
    slist=[]
    s=filename.readlines()
    l_count=len(s)       #줄 수 
    for i in range(len(s)):
        s2=s[i].strip("\n")
        w_count+=len(s[i].split())   #단어 수
        slist.append(s2)
                      
    s_str=''.join(slist)
    ch_s_count=len(s_str)   #문자 수 (공백포함)
    
    s_list=s_str.split()
    s_str2=''.join(s_list)
    ch_count=len(s_str2)   #문자 수 (공백제외)
            
    return w_count,ch_count,ch_s_count,l_count

problem = open('problem.txt','r')
output = open('output.txt','w')
CountFile(problem)

result="단어 수:"+str(w_count)+"\n문자 수(공백제외):"+str(ch_count)+"\n문자 수(공백포함):"+str(ch_s_count)+"\n줄 수:"+str(l_count)

output.write(result)

problem.close()
output.close()

try:
    output=open('output.txt','r')
except IOError as err:
    print("Error: can't find file or read data")

print(output.read())

output.close()
