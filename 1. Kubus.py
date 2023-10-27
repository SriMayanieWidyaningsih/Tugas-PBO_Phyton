import math

print("Program Menghitung Luas dan Kubus")

#Programmer  : Sri Mayanie Widyaningsih
#NIM         : 220511178#Pertemuan   : 1x
#Tanggal     : 22 Oktober 2023

#input nilai
sisi = float(input("Masukkan panjang sisi: "))
tinggi = float(input("Masukkan tinggi limas segitiga: "))
sisi_tegak = float(input("Masukkan panjang sisi tegak limas segitiga: "))

#rumus
luas_alas = 0.5 * alas * tinggi
luas_tegak = 3 * (alas * sisi_tegak) / 2
luas = luas_alas + luas_tegak
volume = (luas_alas * tinggi) / 3

#output
print(f"Luas: {luas}")
print(f"Volume: {volume}")