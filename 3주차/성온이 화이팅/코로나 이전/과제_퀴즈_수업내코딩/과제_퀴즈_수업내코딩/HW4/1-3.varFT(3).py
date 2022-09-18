#Kimhaeun
#22100224
#def3

r_word=""
def reverse(string):
    for i in range(len(string)-1,-1,-1):
        global r_word
        r_word=r_word+string[i]
    return r_word

for i in range(2):
    word=input("단어를 입력하세요:")
    print(reverse(word))
    r_word=""

