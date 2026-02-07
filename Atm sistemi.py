kulanicilar=[
    {
        "name":"Berivan:",
        "usarname":"berivan",
        "şifre":"123",
        "bakiye":2000,
    },
    {
        "name":"mizgin":,
        "usarname":"mizgin47",
        "şifre":"1234",
        "bakiye":15000
    },
    {
        "name":"kerem":,
        "usarname":"kerem47",
        "şifre":"4380",
        "bakiye":19
    }
]

while True:
    kulanici=input("kulanıcı adınızı giriniz")
    for user in kulanicilar:
        if user["username"]==kulanici:
            password=input("lutfen şifrenizi tuşlayınız:")
            if user["şifre"]==password:
                print(user["name"],"hoş geldiniz")


