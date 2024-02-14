import random as random
sayi = random.randint(1,10)
lives = 3
print("3 tahmin hakkınız var.")
while True:
	
	tahmin = int(input("1-10 arası bir sayı tahmin ediniz:	"))
	if tahmin == sayi:
		print("Doğru tahmin ettiniz!!!")
		break
	else:
		print("Yanlış tahmin ettiniz!!!")
		lives -= 1
		print(lives, "tahmin hakkınız kaldı.")
		if lives == 0:
			print("You died")
			break