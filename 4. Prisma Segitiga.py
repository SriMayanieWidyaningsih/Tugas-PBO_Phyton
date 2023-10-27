print("Aplikasi Menghitung Luas dan Volume Prisma Segitiga")
"""
Nama  : Sri Mayanie Widyaningsih
NIM   : 220511178
Kelas : K1
MK    : PBO
Tugas : Pertemuan ke 1
Keterangan:
S = Sisi
T = Tinggi prisma
a = Alas
t = Tinggi
"""
# Atur Nilai
S_1 = 4
S_2 = 9
S_3 = 7
T = 7
a = 8 
t = 11
# Rumus
keliling_segitiga = S_1 + S_2 + S_3
luas_segitiga = keliling_segitiga * T
luas_prisma = keliling_segitiga * T + a * t
volume = 1/2 * a * t * T
# Output
print("Sisi 1:", S_1)
print("Sisi 2:", S_2)
print("Sisi 3:", S_3)
print("Tinggi Prisma:", T)
print("Alas:", a)
print("Tinggi:", t)
print("Keliling Segitiga: ", keliling_segitiga)
print("Luas Segitiga: ", luas_segitiga)
print("Luas Prisma: ", luas_prisma)
print("Volume: ", volume)