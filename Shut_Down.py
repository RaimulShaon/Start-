from tkinter import *
import os

st = Tk()
st.title("Shutdown App")
st.geometry('450x200')
st.config(bg="#eeeedd")
def restart():
    os.system("Shutdown /r /t 1")
def sleep():
    os.system("Shutdown -1")
def shutdown():
    os.system("Shutdown /s /t 1")

R_Button= Button(st,text="RESTART", font=("Calibri", 20,"bold"), relief=RAISED,cursor='pirate', bg="#99ff99",command=restart )
R_Button.place(x=20,y=60,height=40, width=120,) # X,Y mane geometry box er hght wid

L_Button= Button(st,text="SLEEP", font=("Calibri", 20,"bold"), relief=RAISED,cursor='spraycan', bg="#0080ff",command=sleep )
L_Button.place(x=160,y=60,height=40, width=120, )

S_Button= Button(st,text="SHUTDOWN", font=("Calibri", 15,"bold",), relief=RAISED,cursor='heart', bg="#e60000", command=shutdown )
S_Button.place(x=300,y=60,height=40, width=120,)




st.mainloop()

