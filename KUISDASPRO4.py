### UTAMI TRISNA KINANTI 2501782 1C RPL

### SOAL NOMOR 4 

mobil = { 
    "Merk" : "Honda",
    "Tipe" : "HRV",
    "Warna" : "Hitam",
    "Tahun" : "2018",
    "No. Polisi" : "D 1234 ABC",
    "Bensin" : "Pertalite",
    "Transmisi" : "Manual"
}

print("Mobil lama pak Oki adalah : ")

for k,v in mobil.items() : 
    print(k, ":", v)

print()

mobil_baru = { 
    "Merk" : str(input("Masukkan merk mobil baru : ")),
    "Tipe" : str(input("Masukkan tipe mobil baru : ")),
    "Warna" : str(input("Masukkan warna mobil baru : ")),
    "Tahun" : str(input("Masukkan tahun mobil baru : ")),
    "No. Polisi" : str(input("Masukkan No. Polisi mobil baru : ")),
    "Bensin" : str(input("Masukkan bensin mobil baru : ")),
    "Transmisi" : str(input("Masukkan transmisi mobil baru : ")),
}

print()
print("Mobil baru pak Oki adalah :")
for k,v in mobil_baru.items() : 
    print(k, ":", v)