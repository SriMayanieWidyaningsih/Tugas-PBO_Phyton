import math

print("Program Menghitung Luas dan Volume Balok")

#Programmer   : Sri Mayanie Widyaningsih
#NIM          : 220511178
#Pertemuan    : 1
#Tanggal      : 22 Oktober 2023


#input nilai
panjang = float(input("Masukkan panjang balok:"))
lebar = float(input("Masukkan lebar balok:"))
tinggi = float(input("Masukkan tinggi balok:"))

#rumus
luas = 2 * (lebar * tinggi + lebar * tinggi)
volume = panjang * lebar *  tinggi

#output
print(f"Luas: {luas}")
print(f"volume: {volume}")