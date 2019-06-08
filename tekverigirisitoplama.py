def toplama():
	veriler=[]
	for i in range(2):
		veri=int(input())
		veriler.append(veri)
	sayi1=veriler[0]
	sayi2=veriler[1]
	toplam=sayi1+sayi2
	return toplam
print(toplama())
