'''
작성자 : 박현민
프로그램의 목적:7*7로 구성된 리스트를 생성하여 magic square을 작성하여 출력하는 프로그램이다.
'''

Magicsquare=[7*[0] for i in range(7)]


n=1
row=0
col=3
Magicsquare[row][col]=n

for i in range(48):
    n+=1
    row-=1
    col-=1

    if Magicsquare[row][col]!=0:
        row+=2
        col+=1
        
    elif row<0 and col<0:
        row+=2
        col+=1
        
    elif row<0:
        row=6
        
    elif col<0:
        col=6
        
    Magicsquare[row][col]=n

for i in range(7):
    print(Magicsquare[i])
    
