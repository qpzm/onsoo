#Kimhaeun
#22100224
#[tkinter 활용] isPalindrome

from tkinter import *
from tkinter import Tk

def ispal(string):
    wordstr=""
    bword=""
    string=string.lower() 
    for ch in string:
        if ch.isalpha()==True:
            wordstr=wordstr+ch
    for i in range(len(wordstr)-1,-1,-1):
        bword=bword+wordstr[i]
    if wordstr==bword:
        return "True"
    else:
        return "False"

root=Tk()
root.title("2.isPalindrome")
lbl=Label(root,text="Input a string to check palindrome or not")
lbl.pack()

txt=Entry(root)
txt.pack()

check_but=Button(root,text="Check")
check_but.pack()

check_lbl=Label(root,text="")
check_lbl.pack()
    
def checking(event):
    check_lbl['text']=ispal(txt.get())
    check_lbl.pack()
    
check_but.bind('<Button-1>',checking)

root.mainloop()

