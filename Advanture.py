Name = input("Ener Ur Name: ")
print("Welcome", Name, "TO New Adventure Game!!!")

qsn = input(" DO u Want to restart ur life? Y/N : ")

if qsn == 'Y':
    print("Good Luck")

    qsn = input(" DO u Want to Go School? Y/N : ")
    if qsn == 'Y':
        print("Read Well And Pass the EXM")
        qsn= input(" do u want to complite ur stady?: ")
        if qsn == 'Y':
            print("u r getting a job with high pay salary..")
        elif qsn== 'N':
            print("you lose!!! go n fuck ur self...")
    else:
        print("u can't do anything")

elif qsn == 'N':
    quit()

print("****Game Over****")
