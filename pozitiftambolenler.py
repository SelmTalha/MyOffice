"""
Pozitif tam bolenleri Bulup ekrana yazdiralim.
Bunu yaparken islemler devamli olsun.
Biz klavyeden bir deger girdigimizde dongu bitsin program kapansin.
"""

def bolenleri_bul(sayi):
	bolen_listesi=[]
	for i in range(1,sayi+1):
		if(sayi%i==0):
			bolen_listesi.append(i)
	return bolen_listesi

while True:
	sayi=input("Bolenlerini bulmak istediginiz sayiyi giriniz (Cikmak icin 'q' tusuna basiniz !):")
	if(sayi=="q"):
		print("Programdan cikiliyor ...")
		break
	else:
		sayi=int(sayi)
		print(bolenleri_bul(sayi))
