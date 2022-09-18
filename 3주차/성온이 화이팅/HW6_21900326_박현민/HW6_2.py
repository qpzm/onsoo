'''
작성자 : 박현민
프로그램의 목적 : 텍스트 파일을 읽어서 단어 수, 문자 수(공백제외), 문자수(공백포함)
                  줄수를 리턴하는 함수를 작성하고 생성한 함수를 호출하여 그 결과를
                  output.txt에 저장하고 파일을 다시 읽어 그 내용을 출력하는 프로그램
'''

import sys

try:
    input_file=open('input.txt','r')
    output_file=open('output.txt','w')

except IOError as err:
    print("ERROR : can't read the file")



def CountFile(filename):
    global wc
    global cc
    global ccs
    global line
    
    wc=0
    cc=0
    ccs=0
    line=0


    lines=filename.readlines()
    line=len(lines)

    lst=[]
    for i in range(len(lines)):
        b=lines[i].strip('\n')
        wc+=len(lines[i].split())
        lst.append(b)

    c=''.join(lst)
    ccs=len(c)

    d=c.split()
    e=''.join(d)
    cc=len(e)

    return wc,cc,ccs,line

input_file=open('input.txt','r')
output_file=open('output.txt','w')
CountFile(input_file)

wc=str(wc)
cc=str(cc)
ccs=str(ccs)
line=str(line)

value="단어 수:"+wc+"\n문자 수(공백제외):"+cc+"\n문자 수(공백포함):"+ccs+"\n줄 수:"+line

output_file.write(value)
input_file.close()
output_file.close()

try:
    output_file=open('output.txt','r')

except IOError as err:
    print("ERROR : can't read the file")

print(output_file.read())
output_file.close()


