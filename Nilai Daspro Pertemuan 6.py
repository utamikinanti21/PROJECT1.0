# ## Studi Kasus Daspro Pertemuan 6

# # Nilai A, B, C, D

# nilai = int(input("Masukan nilai: "))

# if nilai >= 90:
#     print("Nilai kamu A")
# elif nilai >= 80:
#     print("Nilai kamu B")
# elif nilai >= 70:
#     print("Nilai kamu C")
# else:
#     print("Nilai kamu D")

# # Model Catwalk

# gender = int(input("Apa kelamin kamu? (1. Pria / 2. Wanita): "))
# age = int(input("Berapa Umur kamu?: "))
# height = int(input("Berapa Tinggi kamu (cm)?: "))
# iq = int(input("Berapa IQ kamu?: "))

# if (gender == 1 and 18 <= age <= 25 and height >= 175 and iq >= 130):
#     print("Kamu Lolos Model Pria")
# elif (gender == 2 and 18 <= age <= 25 and height >= 170 and iq >= 130):
#     print("Kamu Lolos Model Wanita")
# else:
#     print("Kamu Tidak Lolos")

# Tarif Parkir

kendaraan = str(input("Jenis Kendaraan (Mobil/Motor): ")).lower()
waktu = int(input("Masukkan lama parkir (jam): "))
biaya = 0

if kendaraan == "motor":
    if waktu > 10:
        biaya = 20000
    elif waktu == 1:
        biaya = 3000
    else:
        biaya = 3000 + (waktu - 1) * 2000

elif kendaraan == "mobil":
    if waktu > 10:
        biaya = 30000
    elif waktu == 1:
        biaya = 5000
    else:
        biaya = 5000 + (waktu - 1) * 3000

else:
    print("Jenis kendaraan tidak valid.")

print(f"Total biaya parkir: Rp {biaya:,}")


# Kategori Pesan Hari

week = input("Masukkan hari (Senin-Minggu): ").capitalize()
kategori = input("Masukkan kategori penonton (Dewasa, Mahasiswa, Anak-anak): ")
weekend = ["Sabtu", "Minggu"]

harga = 0

if kategori == "Dewasa":
    if week in weekend:
        harga = 70000
    elif week in ["Senin", "Selasa", "Rabu", "Kamis", "Jumat"]:
        harga = 50000
    else:
        print("Hari tidak valid.")
elif kategori == "Mahasiswa":
    if week in weekend:
        harga = 60000
    elif week in ["Senin", "Selasa", "Rabu", "Kamis", "Jumat"]:
        harga = 40000
    else:
        print("Hari tidak valid.")
elif kategori == "Anak-anak":
    if week in weekend:
        harga = 40000
    elif week in ["Senin", "Selasa", "Rabu", "Kamis", "Jumat"]:
        harga = 30000
    else:
        print("Hari tidak valid.")
else:
    print("Kategori tidak valid.")

print(f"Harga tiket untuk {kategori} pada hari {week} adalah Rp {harga:,}")

# Harga Belanja