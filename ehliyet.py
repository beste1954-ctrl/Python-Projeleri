print("****ehliyet alma programı****")
yas=input("yaşınızı giriniz:")
saglık=input("sürüş için engeliniz var mı? e/h")
ilksinav=input("teorik sınavdan kaç aldınız?")
uygulamasinavi=input("uygulamageçtiniz mi?e/h")
if yas>=18:
    print("yaşınız uygun")
    if saglık=="h":
        print("sağlık engeliniz vardır")
        if ilksinav>=70:
            print("teoriksınav notunuz uygundur")
            if uygulamasinavi=="e":
                print("ehliyet almaya hak kazandınız")
            else:
                print("uygulama sınavından kaldınız")
        else:
            print("teorik sınavındanyeterli not almadınız")
    else:
        print("sağlık durumunuz uygun değildir")
else:
    print("yaşınız küçük")                            

