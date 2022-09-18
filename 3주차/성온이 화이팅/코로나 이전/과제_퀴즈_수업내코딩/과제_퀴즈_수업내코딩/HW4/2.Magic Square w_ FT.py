#Kimhaeun
#22100224
#Magic Square 7X7

magic=[7*[0] for i in range(8)]

row=0
col=3
magic[row][col]=1

def below(row,col):
    row+=2
    col+=1
    return row,col

def out_of_table(row,col):
    if row<0:
        row=6
    elif col<0:
        col=6
    return row,col

for i in range(2,50):
    row-=1
    col-=1
    if row<0 and col<0:
        row,col=below(row,col)
        magic[row][col]=i
    elif magic[row][col]!=0:
        row,col=below(row,col)
        magic[row][col]=i
    else:
        row,col=out_of_table(row,col)
        magic[row][col]=i
        
    
for i in range(7):
    print(magic[i])
        
        
