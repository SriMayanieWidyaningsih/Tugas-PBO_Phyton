print("Aplikasi Menghitung Luas dan volume kerucut")
"""
Nama  : Sri Mayanie Widyaningsih
NIM   : 220511178
Kelas : K1
MK    : PBO
Tugas : Pertemuan ke 1

Keterangan:
L = Luas permukaan kerucut
r = Jari-jari
T = Tinggi
s = Garis pelukis
phi = 3,14
"""
# Atur Nilai
phi = 3.14
r = 8
s = 9
T = 10

# Rumus
luas_selimut = phi * r * s
luas_permukaan = (phi * r * s) + (phi * r**2)
volume = 1/3 * phi * r**2 * T

# Output
print("Phi:", phi)
print("Jari-Jari:", r)
print("Tinggi:", T)
print("Garis Pelukis:", s)
print("Luas Selimut:", luas_selimut)
print("Luas Permukaan:", luas_permukaan)
print("Volume:", volume)
