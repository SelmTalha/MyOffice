a=int(input("Bir sayi giriniz :"))
i=1
sonuc=0
while (i<a):
	if(a%i==0):
		sonuc+=i
	i+=1
if(sonuc==a):
	print("{} sayisi mukemmel sayidir.".format(a))
else:
	print("{} sayisi mukemmel sayi degildir.".format(a))

