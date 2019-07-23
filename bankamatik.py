#Console çalışması bankamatik yapımı:
#Para çekme ,para yatırma ve bakiye sorgulama işlemlerinin yapıldığı bir bankamatik programı yazınız.


hesap_1=1000
hesap_2=0

def bakiyesorgulama():
    print("...............")
    print("1.Hesap Bakiyeniz :",hesap_1)
    print("2.Hesap Bakiyeniz :",hesap_2)

def paracekme():
    global hesap_1,hesap_2
    secim=int(input("Hangi hesaptan para çekmek istiyorsunuz ?(1/2) :"))
    miktar=int(input("Ne kadar çekmek istiyorsunuz ?:"))
    if secim == 1:
        hesap_1-=miktar
    elif secim == 2:
        hesap_2-=miktar
    else:
        print("YANLIŞ SEÇİM !")

def parayatirma():
    global hesap_1,hesap_2
    secim=int(input("Hangi hesaptan para çekmek istiyorsunuz ?(1/2) :"))
    miktar=int(input("Ne kadar çekmek istiyorsunuz ?:"))
    if secim == 1:
        hesap_1+=miktar
    elif secim == 2:
        hesap_2+=miktar
    else:
        print("YANLIŞ SEÇİM !")

while(True):
    print("----------SeTBankamatik---------")
    print("-----------Hoşgeldiniz-----------")
    print("1.Bakiye Sorgulama")
    print("2.Para Çekme")
    print("3.Para Yatırma")
    print("4.Çıkış")

    secim = int(input("İşlem seçimini yapınız :"))

    if secim == 1 :
        bakiyesorgulama()
    elif secim == 2 :
        paracekme()
    elif secim == 3 :
        parayatirma()
    elif secim == 4 :
        print("Çıkış Yapıldı !")
        break
    else:
        print("Hatalı secim yaptınız !")