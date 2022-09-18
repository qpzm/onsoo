#Kimhaeun
#22100224
#복수명사를 만든 후 출력

word=['apple','axes','book','box','buzz','cat','cantus','church','dish','knife','lady','leaf','pitch','stimulus','taxi','wish','wolf']
plural=[]

for w in word:

    if w[len(w)-1]=='y':
        w=list(w)
        w.pop()
        w.append('ies')
        delimiter=''
        str=delimiter.join(w)
        plural.append(str)
        
    elif w[len(w)-1]=='f':
        w=list(w)
        w.pop()
        w.append('ves')
        delimiter=''
        str=delimiter.join(w)
        plural.append(str)
        
    elif w[len(w)-2:]=='fe':
        w=list(w)
        w.pop()
        w.pop(-1)
        w.append('ves')
        delimiter=''
        str=delimiter.join(w)
        plural.append(str)
        
    elif w[len(w)-2:]=='us':
        w=list(w)
        w.pop()
        w.pop(-1)
        w.append('i')
        delimiter=''
        str=delimiter.join(w)
        plural.append(str)
        
    elif w[len(w)-1]=='s':
        w=list(w)
        w.append('es')
        delimiter=''
        str=delimiter.join(w)
        plural.append(str)

    elif w[len(w)-1]=='x':
        w=list(w)
        w.append('es')
        delimiter=''
        str=delimiter.join(w)
        plural.append(str)
        
    elif w[len(w)-1]=='z':
        w=list(w)
        w.append('es')
        delimiter=''
        str=delimiter.join(w)
        plural.append(str)

    elif w[len(w)-2:]=='ch':
        w=list(w)
        w.append('es')
        delimiter=''
        str=delimiter.join(w)
        plural.append(str) 

    elif w[len(w)-2:]=='sh':
        w=list(w)
        w.append('es')
        delimiter=''
        str=delimiter.join(w)
        plural.append(str)

    else:
        w=list(w)
        w.append('s')
        delimiter=''
        str=delimiter.join(w)
        plural.append(str)
print(plural)
        
