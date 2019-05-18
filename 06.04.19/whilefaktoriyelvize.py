deger=int(input("Lutfen bir sayi giriniz :"))
def faktoriyel(sayi):
	sonuc = 1
	while sayi>=1:
		sonuc*=sayi
		sayi-=1
	return sonuc
print("Faktoriyel {}".format(faktoriyel(deger)))
