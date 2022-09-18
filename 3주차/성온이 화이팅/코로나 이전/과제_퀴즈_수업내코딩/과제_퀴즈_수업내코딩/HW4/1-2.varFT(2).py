#Kimhaeun
#22100224
#def2

a=0
def countVowels(string):
    global a
    string=string.lower()
    vowels=['a','e','i','o','u']
    for i in range(len(string)):
        if string[i] in vowels:
            a+=1
    return a

for i in range(2):
    sent=input("문장을 입력하세요:")
    print("모음의 총 개수:",countVowels(sent))
    a=0
