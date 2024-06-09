Email= input("Enter your email:")  #g@g.com  raimul@gmail.com
D, k, U = 0, 0, 0
if len(Email)>=6:
    if Email[0].isalpha():
        if ("@" in Email) and (Email.count("@")==1):
            if (Email[-4]=='.') ^ (Email[-3]=='3'):
                for i in Email:
                    if i == i.isspace():
                         D=1
                    elif i.isalpha():
                        if i==i.upper():
                            k=1
                    elif i.isdigit():
                        continue
                    elif i=='_' or i=='.' or i== '@':
                        U=1
                    if D==1:
                        print("wrong mail 5 ")
            else:
                print("wrong mail 4")
        else:
            print("wrong mail 3 ")
    else:
        print("wrong mail 2 ")
else:
    print("wrong mail 1 ")
