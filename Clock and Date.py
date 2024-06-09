from tkinter import *
import datetime


def date_time ():
    time = datetime.datetime.now()
    hr = time.strftime("%I")
    mi = time.strftime("%M")
    se = time.strftime("%S")
    am =  time.strftime("%p")
    date = time.strftime("%d")
    mon = time.strftime("%b")
    yr = time.strftime ("%Y")
    dy = time.strftime("%a")




    lab_hr.config(text=hr)
    lab_min.config(text= mi)
    lab_sec.config(text=se)
    lab_ap.config(text=am)
    lab_dd.config(text=date)
    lab_mm.config(text=mon)
    lab_yy.config(text=yr)
    lab_day.config(text=dy)


    lab_hr.after(200,date_time)





td= Tk()
td.title("TIME & DATE")
td.geometry("750x350")
td.config(bg="#936c6c")






lab_time = Label(td, text="Time :", font=("Arial",30,"bold"),bg="black", fg="gray" )
lab_time.place(x=30,y=30,height=100 , width=150)

lab_hr = Label(td, text="00", font=("Arial",30,"bold"),bg="black", fg="gray" )
lab_hr.place(x=210,y=30,height=100 , width=100)

lab_min = Label(td, text="01", font=("Arial",30,"bold"),bg="black", fg="gray" )
lab_min.place(x=340,y=30,height=100 , width=100)

lab_sec = Label(td, text="02", font=("Arial",30,"bold"),bg="black", fg="gray" )
lab_sec.place(x=480,y=30,height=100 , width=100)

lab_ap = Label(td, text="03", font=("Arial",30,"bold"),bg="black", fg="gray" )
lab_ap.place(x=610,y=30,height=100 , width=100)

lab_date = Label(td, text="Date :", font=("Arial",30,"bold"),bg="black", fg="gray" )
lab_date.place(x=30,y=200,height=100 , width=150)

lab_dd = Label(td, text="DD", font=("Arial",30,"bold"),bg="black", fg="gray" )
lab_dd.place(x=210,y=200,height=100 , width=100)

lab_mm = Label(td, text="MM", font=("Arial",30,"bold"),bg="black", fg="gray" )
lab_mm.place(x=340,y=200,height=100 , width=100)

lab_yy = Label(td, text="YYYY", font=("Arial",30,"bold"),bg="black", fg="gray" )
lab_yy.place(x=480,y=200,height=100 , width=100)

lab_day = Label(td, text="DAY", font=("Arial",30,"bold"),bg="black", fg="gray" )
lab_day.place(x=610,y=200,height=100 , width=100)





date_time()


td.mainloop()

