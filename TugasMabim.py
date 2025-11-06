## Peserta diminta untuk membuat dua program sederhana:
# 1. Buatlah program Python yang meminta pengguna memasukkan Biodata. Program tersebut
# kemudian akan menampilkan menu pilihan:
# • Menginput biodata : Nama Lengkap, Nim, Kelas, Program Studi, Umur, No Telephone
# • Menampilkan Biodata
# jika user telah melakukan input biodata maka biodata sebelumnya akan tergantikan dengan
# Biodata terbaru.

# NAMA : UTAMI TRISNA KINANTI
# KELAS : 1 B 
# KELOMPOK : QUANTUM
# KOPES : QTM - 09

biodata = {}

while True : 
    a = int(input("Selamat datang, pilih menu selanjutnya : \n 1. Input Biodata \n 2. Tampilkan Biodata \n 3. Keluar \n Pilihan anda (1/2/3): "))
    
    if a == 1 :
        biodata = {
            "Nama" : str(input("Masukkan Nama Lengkap Anda: ")),
            "Nama Panggilan" : str(input("Masukkan Nama Panggilan: ")),
            "NIM" : str(input("Masukkan NIM Anda: ")),
            "Kelas" : str(input("Masukkan Kelas Anda: ")),
            "Prodi" : str(input("Masukkan Prodi Anda: ")),
            "Umur" : str(input("Masukkan Umur Anda: ")),
            "Nomor Telpon" : str(input("Masukkan Nomor Telepon Anda: ")),
        }
        print("=====")
        print("Biodata kamu telah tersimpan!")
        print("=====")

    elif a == 2 : 
        print(f"=== BIODATA {biodata['Nama Panggilan'].upper()} ===")
        for k, v in biodata.items() : 
            print(f"{k} : {v}")
            print("=====")

    elif a == 3 :
        print("PROGRAM SELESAI, TERIMA KASIH")
        break

    else :
        print("Input tidak valid, ulangi.")