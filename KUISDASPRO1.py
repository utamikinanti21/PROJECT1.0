### UTAMI TRISNA KINANTI 2501782 1C RPL

### SOAL NOMOR 1 

# PAK ABI INGIN MEMBUAT RUMAH
# DENGAN PANJANG 8M TINGGI 4M DAN LEBAR 10M
# BUAT PROGRAM UNTUK MEMBUAT BANGUNAN DENGAN BIAYA 450.000/M2

a = int(input("Masukkan panjang rumah : "))
b = int(input("Masukkan tinggi rumah : "))
c = int(input("Masukkan lebar rumah : "))

d = 2 * a * b + 2 * c * b 
e = 450000 * d 

print("Biaya pembuatan rumahmu adalah Rp.", e)