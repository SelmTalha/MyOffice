import random,time


corba = ["Çorba","Domates Çorbası", "Mercimek Çorbası", "Düğün Çorbası", "Yayla Çorbası", "Tarhana Çorbası", "Ezogelin Çorbası", "Tavuklu Şehriye Çorbası", "Bal kabağı çorbası",
"Brokoli çorbası"]
zeytinyagli = ["Zeytinyağlı","Bamya", "Barbunya", "Kabak yemeği", "Kereviz", "Pırasa", "Enginar", "Şakşuka", "Fava", "Taze Fasulye", "Patlıcan Salatası", "Piyaz", "Sarma"]
etsiz = ["Etsiz","Mücver", "Kapuska", "Türlü", "Dolma", "Lahana Sarması", "Karnabahar", "Enginar", "Menemen","Mercimek Köfte"]
karbon_yan = ["Karbon_yan","Pirinç Pilavı", "Bulgur Pilavı", "Makarna", "Mantı", "Hamburger"]
etli = ["Etli","Et Köfte", "Orman Kebabı", "Fırında Tavuk Kanat", "Arnavut Ciğeri", "Kadınbudu Köfte", "Kağıt Kebabı", "Tas kebabı", "Patlıcan Musakka","Et Sote","Karnıyarık","Hünkar Beğendi",
"Sulu Köfte", "Alinazik", "Et Kavurma", "Patates Yemeği", "Kuru Fasulye", "Mantarlı Et Sote", "Özbek Pilavı"]

def listeden_soru_cek():
    listen=[corba,zeytinyagli,etsiz,karbon_yan,etli]
    for i in listen:
        deneme=i[0]
        secimin = str(input(f"{deneme} düşünüyor musun ? E/H :"))
        otomatik(secimin,i)

def otomatik(secimin,i):
    secilmis=i[0:]
    if secimin == "E" or secimin == "e" :
            x = str(input("Senin yerine ben seçebilir miyim? E/H"))
            if x == "E" or x == "e" :
                y = random.randint(1,len(secilmis)+1)
                print(secilmis[y])
            else:
                print(secilmis)
    elif secimin == "H" or secimin =="h":
            pass
    else:
        print("Geçersiz değer girdiniz.")
        
while True:
    print("#################")
    print("1-Yemek seçim")
    print("2-Çıkış")
    secim=int(input("Seçiminizi yapınız: "))
    if secim==1:
        listeden_soru_cek()
    elif secim==2:
        print("Çıkış yapılıyor..")
        time.sleep(2)
        break