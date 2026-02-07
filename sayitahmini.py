from random import randint

tutulan_sayi= randint(1,10)
hak=3
while True:
    tahmin_sayi=int(input("1-10 Arasındaki Sayı Tahminizi Yapınız:"))
    if hak==0:
        print("Haknınız Kalmadı")
        print(tutulan_sayi)
        break
    else:
        hak=hak-1
    if tutulan_sayi==tahmin_sayi:
        print("Tahminiz Doğru Tebrikler")
        break
    elif tutulan_sayi>tahmin_sayi:
        print("Daha büyük sayı giriniz")
    elif tutulan_sayi<tahmin_sayi:
        print("Daha küçük sayı giriniz")
    print(hak,"hakınızkaldı")


    







