bas = int(input("Başlangıç değeri:	"))
bit = int(input("Bitiş değeri:	"))

tek_sayilar = []
cift_sayilar = []

for num in range(bas,bit):
	if num % 2:
		tek_sayilar.append(num)
	else:
		cift_sayilar.append(num)
print("Tek Sayılar:" , tek_sayilar )
print("Çift Sayılar: " , cift_sayilar)