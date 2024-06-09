from time import *
import random as r

def mistake(paratest,usertest):     #pararagraph r usertest
    error=0
    for i in range(len(paratest)):
        try:
            if paratest[i]!=usertest[i]:
                error=error+1
        except:
            error=error+1
    return error
def speed_time(time_s,time_e, userinput):
    time_delay = time_e - time_s
    time_R = round(time_delay,2)
    speed = len(userinput)/time_R
    return round(speed,2)



Test = ["Track your progress with the free My Learning program here at W3Schools.","Log to your account and start earning points This is an optional feature."," You can study at W3Schools without using My Learning."]
Test1 = r.choice(Test)  #random module use kora hoice
print("        *****Speed Test*****       ")
print(Test1)
print()
print()
time_1 = time()
testinput = input("Enter : ")
time_2 = time()
print("Speed: ",speed_time(time_1,time_2,testinput), "W/Sec." )
print("Error : ", mistake(Test1,testinput))
