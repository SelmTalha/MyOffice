#Basit Bir Hesap Makinasını def (fonksiyon) lerle yazalım.

secim=int(input("1-Toplama İşlemi\n2-Çıkarma İşlemi\n3-Çarpma İşlemi\n4-Bölme İşlemi\n"))

def topla(a,b):
    return a+b
def cikarma(a,b):
    return a-b
def carpma(a,b):
    return a*b
def bolme(a,b):
    return a/b

if secim==1:
    sayi1=float(input("Birinci sayiyi giriniz:"))
    sayi2=float(input("İkinci sayiyi giriniz:"))
    sonuc=topla(sayi1,sayi2)
if secim==2:
    sayi1=float(input("Birinci sayiyi giriniz:"))
    sayi2=float(input("İkinci sayiyi giriniz:"))
    sonuc=cikarma(sayi1,sayi2)
if secim==3:
    sayi1=float(input("Birinci sayiyi giriniz:"))
    sayi2=float(input("İkinci sayiyi giriniz:"))
    sonuc=carpma(sayi1,sayi2)
if secim==4:
    sayi1=float(input("Birinci sayiyi giriniz:"))
    sayi2=float(input("İkinci sayiyi giriniz:"))
    sonuc=bolme(sayi1,sayi2)
print("Sonuc :{}".format(sonuc))

