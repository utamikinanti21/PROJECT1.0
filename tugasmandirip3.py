#### Nomor 1

# Diketahui list dengan nilai 10 mahasiswa sebagai berikut : 

nilai = [88, 75, 63, 97, 82, 74, 91, 80, 81, 63]

# Tampilkan data maksimum 
print("Data maksimum adalah", (max(nilai)))

# Tampilkan data minimum 
print("Data minimum adalah", (min(nilai)))

# Tampilkan nilai rata rata 
print("Rata - rata nilai adalah", int(sum(nilai)/len(nilai)))

# Tampilkan data nilai terbesar kedua 
nilai.sort()
nilai.reverse()
print(nilai[1])
print()


#### Nomor 2

# Diketahui tuple yang berisi daftar pasangan (latitude, longitude) sebuah lokasi : 

Kordinat = (
    ("Jakarta", (-6.2088, 106.8456)),
    ("Bandung", (-6.9175, 107.6191)),
    ("Surabaya", (-7.2575, 112.7521))
)

# Tampilkan data kordinat untuk kota bandung 
print("Koordinat kota Bandung", Kordinat[1][1])
print("Jumlah lokasi yang tersimpan adalah", len(Kordinat))
