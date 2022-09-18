#kimhaeun
#22100224
#2
from tkinter import *

root=Tk()

height_lbl=Label(root,text="height")
height_lbl.pack()
height_entry=Entry(root)
height_entry.pack()

weight_lbl=Label(root,text="weight")
weight_lbl.pack()
weight_entry=Entry(root)
weight_entry.pack()

cal_but=Button(root,text='calculate')
cal_but.pack()

def calculate(event):
    BMI=int(weight_entry.get())/(int(height_entry.get())*2)
    BMI_lbl=Label(root,text=BMI)
    BMI_lbl.pack()
    if BMI>=20 or BMI<25:
        result_lbl=Label(root,text='정상')
        result_lbl.pack()
    elif BMI>=25 or BMI<=29.9:
        result_lbl=Label(root,text='과체중(1도 비만)')
        result_lbl.pack()
    elif BMI>=30 or BMI<=40:
        result_lbl=Label(root,text='비만 (2도 비만)')
        result_lbl.pack()
    else:
        result_lbl=Label(root,text='고도비만')
        result_lbl.pack()


cal_but.bind('<Button-1>',calculate)

root.mainloop()
