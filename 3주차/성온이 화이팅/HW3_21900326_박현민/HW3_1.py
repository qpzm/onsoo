'''
작성자 : 박현민
프로그램의 목적 : 단수명사들로 구성된 리스트의 단어들을 각 조건에 맞추어 복수명사로 출력하는 프로그램이다.
'''

word=['apple','axes','book','box','buzz','cat','cantus','church','dish','knife','lady','leaf','pitch','stimulus','taxi','wish','wolf']

#빈리스트를 만들어준다.
plural=[]


for wd in word:
    if wd[-1]=='y':
        #string을 바로 바꾸어줄수 없기에 list를 사용한다
        L=list(wd)
        del L[-1]
        L.append('ies')
        #.join을 이용하여 string으로 바꾼다.
        S=''.join(L)
        plural.append(S)

    elif wd[-1]=='f' or wd[-2]=='f' and wd[-1]=='e':
        if wd[-1]=='f':
            L=list(wd)
            del L[-1]
            L.append('ves')
            S=''.join(L)
            plural.append(S)
        else:
            L=list(wd)
            for i in range(2):
                del L[-1]
            L.append('ves')
            S=''.join(L)
            plural.append(S)

    elif wd[-1]=='s' and wd[-2]=='u':
        L=list(wd)
        for i in range(2):
            del L[-1]
        L.append('i')
        S=''.join(L)
        plural.append(S)

    elif wd[-1]=='s' or wd[-1]=='x' or wd[-1]=='z' or wd[-1]=='h' and wd[-2]=='c' or wd[-1]=='h' and wd[-2]=='s':
        L=list(wd)
        L.append('es')
        S=''.join(L)
        plural.append(S)

    else:
        L=list(wd)
        L.append('s')
        S=''.join(L)
        plural.append(S)
        

print(plural)
        
