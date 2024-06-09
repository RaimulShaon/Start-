thislist= ["rai","mul ", 'sha', 'tanjila ', 'Akter ', 'keya']
listerrnam= ['tanjila ', 'Akter ', 'keya']
# list3= thislist+listerrnam
# print(list3)
for a in listerrnam:
    thislist.append(a)
    print(thislist)
thistup= ("rai","mul ", 'sha', 'tanjila ', 'Akter ', 'keya')
li = list(thislist)
li.append("sahon")
thistup= tuple(li)
print(thistup)



x=0
while x < len(thistup):
    print(thistup[x])
    x= x+1
print('sob  thik ace')
thisset= {"rai", "mul ", 'sha', 'tanjila ', 'Akter ', 'keya'}
thisset.add('raimul')
print(thisset)
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964}
x= thisdict.keys()
print(thisdict)
thisdict["cplor"]= "Black"
print(thisdict)
thisdict.update({"cplor": "White"})
print(thisdict)


a=20
b=20
if a<b:
    print('sksk')
elif a==b:
    print("ko")

elif a!=b:

    print('sob thik ace')

def choto(a,b):
    print("cchoto " + a ,b)
choto(a='sona', b="boro")


def inp(a):
    if a % 2 !=0:
        print("ODD")
    else:
        print("EVEN")
inp(31)


thisli = [["rai", 23],["mul ",54], ['sha', 43], ['tanjila ', 65],['Akter ',43], ['keya',98]]
new = []
for std in thisli:
 new.append(std[1])
 pr = sorted(set(new))

print(pr[1])



