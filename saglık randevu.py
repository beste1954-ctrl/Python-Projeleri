yaa=int(input("yaşınız:"))
kronik=input("kronik raharsızlığınız var mı ?(e/h)")
hamile=input("hamile misiniz ?(e/h)")
acil=input("acil bir durmunuz var mı ?(e/h)")

if acil=="e":
    print("1.seviye öncelikli hastasınız")
elif hamile=="e":
    print("2. seviye öncelikli hastasınız")
elif yas>=65 or kronik=="e":
    print("3.seviye hastasınız")
else:
    print("4. seviye hastasınız")


    

        