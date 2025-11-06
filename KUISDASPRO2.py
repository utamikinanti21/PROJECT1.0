### UTAMI TRISNA KINANTI 2501782 1C RPL

### SOAL NOMOR 2 

# BU RINDA ATLET MANTAN LARI 
# Running track berukuran Panjang 100 meter, lebar 48 meter
# Buat program menghitung total jarak lari bu rinda, gunakan rumus keliling persegi panjang (2P + 2L)

# PROGRAM KHUSUS UNTUK BU RINDA DENGAN RUNNING TRACK SAMA SETIAP LARI

a = 2 * 100 + 2 * 48
b = int(input("Masukkan jumlah putaran lari hari ini : "))

c = a * b 
d = c / 1000

print("JUMLAH JARAK YANG KAMU TEMPUH HARI INI ADALAH", d, "KILOMETER")

# PROGRAM DENGAN RUNNING TRACK BERBEDA 

e = int(input("Masukkan panjang lapangan hari ini (satuan meter): "))
f = int(input("Masukkan lebar lapangan hari ini (satuan meter): "))
g = int(input("Masukkan jumlah putaran hari ini : "))
h = 2 * e + 2 * f
i = h * g
j = i / 1000

print("JUMLAH JARAK YANG KAMU TEMPUH HARI INI ADALAH", j, "KILOMETER")