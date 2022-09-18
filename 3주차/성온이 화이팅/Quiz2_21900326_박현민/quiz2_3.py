'''
작성자 : 21900326 박현민
quiz2 3번
'''

a='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
b='ZYXWVUTSRQPONMLKJIHGFEDCBAzyxwvutsrqponmlkjihgfedcba'
c=list(zip(a,b))

dic=dict(c)


def transfer(str):
    transfer=[]
    for letter in str:
        for i in letter:
            if i in dic:
                transfer.append(dic[i])
    a=''.join(transfer)
    print(a)



transfer('Apple')
transfer('Mom')
transfer('Python')



