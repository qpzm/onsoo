#kimhaeun
#22100224
#problem3

Magic=[5*[0] for i in range(5)]

print(Magic)

n=1
row=0
col=2

Magic[row][col]=n

for i in range(24):
    n+=1
    row-=1
    col-=1

    if Magic[row][col]!=0:
        row+=2
        col+=1          
    elif row<0 and col<0:
        row+=2
        col+=1    
    elif row<0:
        row=4
    elif col<0:
        col=4
    Magic[row][col]=n

for i in range(5):
    print(Magic[i])
    
    

    
