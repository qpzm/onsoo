'''
작성자 : 박현민 21900326
프로그램의 목적 : tkinter을 이용하여 회문을 인식하는 GUI프로그램을 구현한다
'''
from tkinter import *
from tkinter import ttk


def isPalindrome(str):
    a=''
    b=''
    str=str.lower()
    for word in str:
        if word.isalpha()==True:
            a=a+word
    for i in range(len(a)-1,-1,-1):
        b=b+a[i]
    if a==b:
        return "True"
    else:
        return "False"





def press():
    label2['text']=isPalindrome(entry.get())
    label2.grid()

root=Tk()

root.title("isPalindrome")

label=Label(root,text='Input a string to check palindrome or not')
label.grid()

entry=Entry(root)
entry.grid()

button=Button(root,text='Check',command=press)
button.grid()

label2=Label(root,text='')
label2.grid()


root.mainloop()
