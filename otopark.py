times= float(input("otoparkta kalınan süre(dakika):"))
car_type=input("araç tipiniz nedir?(otomobil, motor, kamyon):")
vıp=input("vip misiniz?(e/h):")
no_ticket=input("kaıp bilet varmı?(e/h):")

if car_type=="otomobil":
    clock_price=30
elif car_type=="kamyon":
    clock_price=60
elif car_type=="motor":
    clock_price=20
else:
    print("hatalı giriş araç tipi bulunamadı")


if times<=1 and times>=0:
    total_price=0
    print("1 saaten az kaldınız için ucret ödemiyorsunuz")
elif times>1:
    if times<10:

    if vıp=="h" and no_ticket=="h":
        print("araban otoparkta çok kaldı bü yüzden")
        total_price=(times*clock_price)*0.70
        print(total_price)
    elif vıp=="h" and no_ticket=="h":
        total_price=times*clock_price
        print("toplam tutar:",total_price)
    elif no_ticket=="e":
    
        total_price=(times*clock_price)+200
        print("200 lira ceza kesildi",total_price)
    elif times > 10:
        if vıp=="h" and no_ticket=="h":
        print("araban otoparkata çok kladı bu yüzden %20 zam yapılacak")
        total_price=(times*clock_price)*1.20
        print("ödeneck tutar:",total_price) 

    
    else:
        print(" hatalı bir giriş yaptınız")

else:
    print("süre ile ilgili hatalı giriş yaptınız")



        






     
     
     
     
     
     
     
    



