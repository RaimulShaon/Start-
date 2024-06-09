from time import *
import random

def mistake (paratest, usertest):
    error = 0
    for i in range(len(paratest)):
        try:
            if paratest[1]!=usertest[1]:
                error += 1
        except:
            error += 1
    return error

def speed_time(start,stop,usetest):
    strt = stop-start
    r = round(strt,2)
    u = len(usetest)/r
    return round(u,2)



paragraph = ["Track your progress with the free My Learning program here at W3Schools.",
             "Log to your account and start earning points This is an optional feature.",
             " You can study at W3Schools without using My Learning."]
para = random.choice(paragraph)
print(para)
print("\n""\n")
print("typing tst""\n""\n")
st1 = time()
usinput = input("Type hare: " )
st2 = time()

print("Speed : ", speed_time(st1,st2,usinput), "WpS" )
print("Error : ", mistake(paragraph,usinput))