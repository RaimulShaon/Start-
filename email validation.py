import re
email_condition = "^[a-z]+[\._]?+[a-z 0-9]+[@]\w+[.]\w{2,3}$"
email= input('Enter ur email :')
if re.search(email_condition, email):
    print("Right Email ")
else:
    print("Wrong email " )
    # valo vabe RegEx dekhte ebong porte hobe sateh practice korte hobe. sokol kicur bekkha ache regEx a gele paoa jabe.