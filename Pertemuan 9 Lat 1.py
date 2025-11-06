# Latihan 1

def deret_fibonacci(n):
    a, b = 0, 1
    hasil = []
    for i in range(n):
        hasil.append(a)
        a, b = b, a + b
    return hasil

def volume_tabung(jari_jari, tinggi):
    volume = 3.14 * (jari_jari ** 2) * tinggi
    return volume

def hitung_total_dan_rata():
    nilai = []
    while True:
        data = input("Masukkan nilai (atau ketik 'selesai' untuk berhenti): ")
        if data.lower() == 'selesai':
            break
        try:
            nilai.append(float(data))
        except ValueError:
            print("Input tidak valid, masukkan angka atau 'selesai'.")

    if len(nilai) == 0:
        print("Tidak ada nilai yang dimasukkan.")
        return
        total = sum(nilai)

    total = sum(nilai)
    rata = total / len(nilai)
    print(f"\nTotal nilai = {total}")
    print(f"Rata-rata = {rata:.2f}")

n = int(input("Masukkan banyak suku: "))
print(f"Deret Fibonacchi {deret_fibonacci(n)}")

r = float(input("Masukkan jari-jari tabung: "))
t = float(input("Masukkan tinggi tabung: "))
print(f"Volume tabung = {volume_tabung(r, t):.2f} cm³")

hitung_total_dan_rata()

