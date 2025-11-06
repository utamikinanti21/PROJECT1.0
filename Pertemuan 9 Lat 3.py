# Latihan 3

def hitung_selisih_waktu(jam_mulai, menit_mulai, detik_mulai, jam_selesai, menit_selesai, detik_selesai):

    total_mulai = jam_mulai * 3600 + menit_mulai * 60 + detik_mulai
    total_selesai = jam_selesai * 3600 + menit_selesai * 60 + detik_selesai
    selisih_detik = total_selesai - total_mulai

    jam = selisih_detik // 3600
    selisih_detik %= 3600 
    menit = selisih_detik // 60
    detik = selisih_detik % 60

    if jam < 0:
        jam_24 = jam + 24

    print(f"Selisih waktu: {jam_24} jam - {menit} menit - {detik} detik")

def input_waktu(waktu):
    print(f"\nInput waktu {waktu}")

    jam = int(input("Masukkan jam (0–23): "))
    while jam < 0 or jam > 23:
        print("Jam harus 0–23!")
        jam = int(input("Masukkan ulang jam (0–23): "))

    menit = int(input("Masukkan menit (0–59): "))
    while menit < 0 or menit > 59:
        print("Menit harus 0–59!")
        menit = int(input("Masukkan ulang menit (0–59): "))

    detik = int(input("Masukkan detik (0–59): "))
    while detik < 0 or detik > 59:
        print("Detik harus 0–59!")
        detik = int(input("Masukkan ulang detik (0–59): "))

    return jam, menit, detik

jam_mulai, menit_mulai, detik_mulai = input_waktu("mulai")
jam_selesai, menit_selesai, detik_selesai = input_waktu("selesai")

hitung_selisih_waktu(jam_mulai, menit_mulai, detik_mulai, jam_selesai, menit_selesai, detik_selesai)
