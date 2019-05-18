kelime=input("Bir kelime yaziniz :")

if(kelime == kelime[::-1]):
	print("{} palindrom bir kelimedir.".format(kelime))
else:
	print("Palindrom degildir.")
