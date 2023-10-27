print("Aplikasi Menghitung Luas dan Volume Selinder (Tabung)")

"""
Nama  : Sri Mayanie Widyaningsih
NIM   : 220511178
Kelas : K1
MK    : PBO
Tugas : Pertemuan ke 1

Keterangan:
L = Luas permukaan tabung
r = Jari - jari lingkaran tabung
T = Tinggi
phi = 3.14
"""

# Atur Nilai
phi = 3.14
r = 17
T = 40

# Rumus
luas_selimut = 2 * phi * r * T
luas_permukaan = (2 * phi * r * T) + (2 * phi * r**2)
volume = phi * r**2 * T

# output
print("Phi:", phi)
print("Jari - Jari Lingkaran Tabung:", r)
print("Tinggi:", T)
print("Luas Selimut:", luas_selimut)
print("Luas Permukaan:", luas_permukaan)
print("Volume:", volume)
