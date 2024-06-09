from cryptography.fernet import Fernet


pws = input("what is the pass? : ")

def view():
    with open('password.txt', 'r') as f:
        for line in f.readline():
            data = line.rstrip()
            name, pws = data.split()
            print(line)
def add():
    name = input('Acc Name: ')
    pas = input('enter ur pass: ')

    with open('password.txt', 'a') as f:
        f.write(name + "" + pws + "\n")


while True:
    inp = input(" Would u like to add pass or view pass? add or view: ").lower()
    if inp == "q":
        quit()

    if inp == "add":
        add()
    elif inp == 'view':
        view()
    else:
        print("invalid")

