import random

can=3
oyun=["taş","kağıt","makas"]


wahile=("can"!=0)
x=random.randint(0,2)
bilgisayar=secenekler=[x]
kulanıcı=input("taş,kağıt, makas")

if ("bilgisayar"==kulanıcı):
    print("kulanıcı","taş"and bilgisayar=="taş")
    can=can-1
    print("berabere")
    print("kalan canınız",can)
    
elif("kulanıcı","makas"and bilgisayar=="kağıt"):
    ("bilgisayar kazandı")
    can=can-1
    print("kalan canınız",can)

elif("kualnıcıc","taş"and bilgisayar=="taş"):
    print("bilgisayar kazandı")
    print(  "oyunu kaybetiniz")
    can=can-1
elif("kulanıcı","taş"and bilgisayar=="makas"):
    can=can-1

    print("kulanıcı kazandı")
    print("kalan can:",can)
else:
    print("tebrikler oyunu kazandınız")
    print("oyun bitti")




     




 

 
    
    




