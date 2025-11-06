## 2. Buatlah program Python yang meminta pengguna memasukkan sebuah kalimat. Program
# tersebut kemudian akan menampilkan menu untuk memilih salah satu operasi berikut:
# • Menghitung jumlah kata dalam kalimat
# • Menampilkan kalimat dalam huruf kapital semua
# • Membalik urutan kata dalam kalimat
# Setelah pengguna memilih salah satu operasi, hasilnya akan ditampilkan.

# NAMA : UTAMI TRISNA KINANTI 
# KELAS : 1B
# KELOMPOK : QUANTUM 
# KODE : QTM - 09

a = str(input("MASUKKAN SEBUAH KALIMAT : "))

while True :
    b = int(input("=== LANGKAH SELANJUTNYA === \n 1. HITUNG JUMLAH KATA \n 2. TAMPILKAN KALIMAT DALAM KAPITAL \n 3. BALIK URUTAN KATA DALAM KALIMAT \n 4. KELUAR \n PILIHAN KAMU (1/2/3/4): "))
    if b == 1 :
        print("======")
        print("JUMLAH KATA PADA KALIMATMU ADALAH", len(a))
        print("======")
    
    elif b == 2 :
        print("======")
        print(a.upper())
        print("======")
    
    elif b == 3 :
        c = a.split()
        c.reverse()
        d = " ".join(c)
        print("======")
        print(d)
        print("======")

    elif b == 4 :
        print("======")
        print("SAMPAI JUMPA LAGI!")
        print("======")
        break

    else :
        print("MAAF, INPUTAN KAMU SALAH")
