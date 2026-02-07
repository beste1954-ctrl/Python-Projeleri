meyveleer=["elma","armut","kivi","kiraz","domates","muz","ananas"]
print("berivan en fazla" meyveler [2],"meyvesini seviyor")
print("taha en fazla", meyveler[-1],"meyvesini seviyor")
toptanci=input("hangi meyveyi almak istiyorsunuz?")
meyveler=append(toptanci)
print("meyveler")
ayarlar=("ses","türkçe","dark mode","deneme.com")
print("ayarlar[2]")
ayarlar.append("x.com")

kütüphane=[
    {

        "ad":"ali",
        "soyadı":"yılmaz",
        "yas":20,
        "şehir":"istanbul",
        "okul":"İstanbul üniversitesi",
        "tc": 12345678902
    },
    {
        "ad":"ayşe",
        "soyadı":"kaya",
        "yas":25,
        "şehir":"Ankara",
        "Okul":"ankara üniversitesi",
        "tc":12345678902
    }
    ] 
    kütüphane.remove("kütüphane"[1])
    print(kütüphane)
    add_user=input("yeni kulanıcı adı giriniz:")
    add_surname=input("yeni kulanıcı soyadınızı giriniz")
    add_age=int(input("yeni yaşınızı giriniz:"))
    add_school=input("yeni kulanıcı okulunuzu giriniz:")
    add_tc=input  ("kulanıcı tc kimlik numaranızı giriniz:")
    kütüphane.append({
            "ad":add_user,
            "soyadı":add_surname,
            "yas":add_age,
            "sehir":add_cıty,
            "okul":add_school,
            "tc":add_tc
    })
    print(kütüphane)