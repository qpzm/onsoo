#Kimhaeun
#22100224
#easyCrypto

k_alpha='abcdefghijklmnopqrstuvwxyz '
key_alpha=k_alpha+k_alpha.upper()

v_alpha='badcfehgjilknmporqtsvuxwzy '
value_alpha=v_alpha+v_alpha.upper()

alpha=dict(zip(key_alpha,value_alpha))

def crypt(str):
    password=''
    for i in range(len(str)):
        password+=alpha.get(str[i])
    return password

def decrypt(str):
    encode=''
    for i in range(len(str)):
        for key in alpha.keys():
            if str[i]==alpha[key]:
                encode+=key
    return encode

code=input("암호화 할 문장을 입력하시오:")

print('암호화 한 문장은',crypt(code))
print('복호화 한 문장은',decrypt(crypt(code)))
