import math

print("Program Menghitung Luas dan Volume Limas Segiempat")

#Programmer    : Sri Mayanie Widyaningsih
#NIM           : 220511178
#Pertemuan     : 1
#tanggal       : 22 Oktober 2023

#input nilai
alas = float(input("Memasukkan panjang alas limas segiempat: "))
tinggi = float(input("Memasukkan panjang tinggi limas segiempat: "))
sisi_tegak = float(input("Memasukkan panjang tinggi limas segiempat: "))

#rumus
luas_alas = alas * alas
luas_tegak = 4 * (alas * alas_tegak) / 2
luas = 4 * (alas * sisi_tegak / 2) + luas_alas
volume = (alas_alas * tinggi) / 3

#output
print(f"Luas: {luas}")
print(f"volume: {volume}")