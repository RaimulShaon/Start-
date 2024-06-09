# from tkinter import *
# import speedtest
#
# def speedcheck():
#     SP = speedtest.Speedtest()
#     SP.get_servers()
#     download_speed = str(round(SP.download() /(10**6),3))+" Mbps"  # Convert to Mbps
#     upload_speed = str(round(SP.upload() /(10**6),3))+" Mbps" # Convert to Mbps
#     lab_down.config(text= download_speed)
#     lab_upload.config(text=upload_speed)
#
# st = Tk()
# st.title("Speed Test")
# st.geometry('400x500')
# st.config(bg="#eeeedd")
#
# lab= Label(st,text="Internet Speed Test", font=("Calibri", 20,"bold"), bg="#99ff99",fg="black")
# lab.place(x=80, y=70)
#
# lab= Label(st,text="DOWNLOAD", font=("Calibri", 20,"bold"), bg="#99ff99",fg="black")
# lab.place(x=80, y=160, height=40, width=220,)
#
# lab_down= Label(st,text="00", font=("Calibri", 20,"bold"), bg="#99ff99",fg="black")
# lab_down.place(x=80, y=250,height=40, width=220,)
#
# lab= Label(st,text="UPLOAD", font=("Calibri", 20,"bold"), bg="#99ff99",fg="black")
# lab.place(x=80, y=330,height=40, width=220,)
#
# lab_upload= Label(st,text="00", font=("Calibri", 20,"bold"), bg="#99ff99",fg="black")
# lab_upload.place(x=80, y=400,height=40, width=220,)
#
# R_Button= Button(st,text="TEST", font=("Calibri", 20,"bold"), relief=RAISED,cursor='pirate', bg="red", command=speedcheck)
# R_Button.place(x=120,y=10,height=40, width=120,) # X,Y mane geometry box er hght wid
#
# st.mainloop()

from tkinter import *
import speedtest

def speedcheck():
    sp = speedtest.Speedtest()
    sp.get_servers()
    download_speed = str(round(sp.download() / (10**6), 3)) + " Mbps"  # Convert to Mbps
    upload_speed = str(round(sp.upload() / (10**6), 3)) + " Mbps"  # Convert to Mbps
    lab_down.config(text=download_speed)
    lab_upload.config(text=upload_speed)

st = Tk()
st.title("Speed Test")
st.geometry('400x500')
st.config(bg="#eeeedd")

lab_title = Label(st, text="Internet Speed Test", font=("Calibri", 20, "bold"), bg="#99ff99", fg="black")
lab_title.place(x=80, y=70)

lab_download = Label(st, text="DOWNLOAD", font=("Calibri", 20, "bold"), bg="#99ff99", fg="black")
lab_download.place(x=80, y=160, height=40, width=220)

lab_down = Label(st, text="00", font=("Calibri", 20, "bold"), bg="#99ff99", fg="black")
lab_down.place(x=80, y=250, height=40, width=220)

lab_upload = Label(st, text="UPLOAD", font=("Calibri", 20, "bold"), bg="#99ff99", fg="black")
lab_upload.place(x=80, y=330, height=40, width=220)

lab_upload_speed = Label(st, text="00", font=("Calibri", 20, "bold"), bg="#99ff99", fg="black")
lab_upload_speed.place(x=80, y=400, height=40, width=220)

test_button = Button(st, text="TEST", font=("Calibri", 20, "bold"), relief=RAISED, cursor='pirate', bg="red", command=speedcheck)
test_button.place(x=120, y=10, height=40, width=120)

st.mainloop()
