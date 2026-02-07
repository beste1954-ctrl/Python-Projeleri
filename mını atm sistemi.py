kulanicilar={
    "kerem":{"şifre":"123","bakiye":160},
    "berivan":{"şifre":"6057","bakiye":2000},
    "mizgin":{"şifre":"1946","bakiye":10000},


}

username=input("kulanıcı adınızı giriniz:")
if username in kulanicilar:
    hak=3
    while hak>0:
        sifre=input("şifrenizi giriniz")
        if sifre==kulanicilar[username]["şifre"]:
            break
        else:
            print("şifreniz yanlış")
            hak=hak-1
    if hak==0:
        print("kartınız bloke olmuştur hayırlı ogurlu olsun")
    else:       
        


        print("""
        (1) bakiye görüntüle
        (2) para çek
        (3) para yatırma
        (4) çıkış
        """)
        secim=input("seçiminiziyapınız")
        if secim=="1":
            bakiye=kulanicilar[username]["bakiye"]
            print("bakiyenizi",bakiye)
        elif secim=="2":
            miktar=input(int(" kaç para çekmek istiyorsunuz:"))
            bakiye=kulanicilar[username]["bakiye"]
            if miktar<=bakiye: 
                bakiye=bakiye-miktar
                print("kalan bakiyeniz:",bakiye)
            else:
                print("bakiyeniz yeterli  değil")
        elif secim=="3":
            miktar=int(input("kaç para yatırmak istersiniz"))
            bakiye=bakiye=+miktar
            print("toplam bakiyeniz",bakiye)
            

            

        


        

    