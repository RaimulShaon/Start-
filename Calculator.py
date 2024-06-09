from tkinter import *




window= Tk()
window.title("                      BASIC CALCULATOR")
window.geometry('400x500')
window.config(bg="gray")

def button_press(num):
    global equation_text

    equation_text=equation_text+str(num)
    equation_lebel.set(equation_text)

def equals():
    global equation_text
    total= str(eval(equation_text))
    equation_lebel.set(total)
    equation_text=total
def clear():
    global equation_text
    equation_lebel.set("")  #var.set(value)
    equation_text=""






equation_text= ""

equation_lebel= StringVar() #var = Tkinter_variable(master=None)


label = Label(window,textvariable= equation_lebel, font= ('consolas',20), bg="white", height=2, width=24)
label.pack()

frame = Frame(window)
frame.pack()

Button1 = Button(frame, text=1,height=4,width=8, font=('Arial',12,"bold"),bg="light gray", relief=RAISED, command=lambda: button_press(1))
Button1.grid(row=0,column=0)

Button2 = Button(frame, text=2,height=4,width=8, font= ('Arial',12,"bold"),bg="light gray", relief=RAISED, command=lambda: button_press(2))
Button2.grid(row=0,column=1)

Button3 = Button(frame, text=3,height=4,width=8, font= ('Arial',12,"bold"),bg="light gray", relief=RAISED, command=lambda: button_press(3))
Button3.grid(row=0,column=2)

Button4 = Button(frame, text=4,height=4,width=8, font= ('Arial',12,"bold"),bg="light gray", relief=RAISED, command=lambda: button_press(4))
Button4.grid(row=1,column=0)

Button5 = Button(frame, text=5,height=4,width=8, font= ('Arial',12,"bold"),bg="light gray", relief=RAISED, command=lambda: button_press(5))
Button5.grid(row=1,column=1)

Button6 = Button(frame, text=6,height=4,width=8, font= ('Arial',12,"bold"),bg="light gray", relief=RAISED, command=lambda: button_press(6))
Button6.grid(row=1,column=2)

Button7 = Button(frame, text=7,height=4,width=8, font= ('Arial',12,"bold"),bg="light gray", relief=RAISED, command=lambda: button_press(7))
Button7.grid(row=2,column=0)

Button8 = Button(frame, text=8,height=4,width=8, font= ('Arial',12,"bold"),bg="light gray", relief=RAISED, command=lambda: button_press(8))
Button8.grid(row=2,column=1)

Button9 = Button(frame, text=9,height=4,width=8, font= ('Arial',12,"bold"),bg="light gray", relief=RAISED, command=lambda: button_press(9))
Button9.grid(row=2,column=2)

Button0 = Button(frame, text=0,height=4,width=8, font= ('Arial',12,"bold"),bg="light gray", relief=RAISED, command=lambda: button_press(0))
Button0.grid(row=3,column=0)

Button_P = Button(frame, text=".",height=4,width=8, font= ('Arial',12,"bold"),bg="light gray", relief=RAISED, command=lambda: button_press("."))
Button_P.grid(row=3,column=1)

Button_ql = Button(frame, text="=",height=4,width=8, font= ('Arial',12,"bold"),bg="light gray", relief=RAISED, command=equals)
Button_ql.grid(row=3,column=2)

Button_pls = Button(frame, text="+",height=4,width=8, font= ('Arial',12,"bold"),bg="light gray", relief=RAISED, command=lambda: button_press("+"))
Button_pls.grid(row=0,column=3)

Button_mns = Button(frame, text="-",height=4,width=8, font= ('Arial',12,"bold"),bg="light gray", relief=RAISED, command=lambda: button_press("-"))
Button_mns.grid(row=1,column=3)

Button_Mlt = Button(frame, text="*",height=4,width=8, font= ('Arial',12,"bold"),bg="light gray", relief=RAISED, command=lambda: button_press("*"))
Button_Mlt.grid(row=2,column=3)

Button_dvd = Button(frame, text="/",height=4,width=8, font= ('Arial',12,"bold"),bg="light gray", relief=RAISED, command=lambda: button_press("/"))
Button_dvd.grid(row=3,column=3)

Button_clr = Button(window, text="CLEAR",height=4,width=35, font= ('Arial',12,"bold"),bg="light gray", relief=RAISED, command=clear)
Button_clr.pack()


window.mainloop()