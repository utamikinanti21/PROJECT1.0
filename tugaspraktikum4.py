# KASUS 1

print("KASUS 1 : HOBI MAHASISWA")
print()
# HOBI MAHASISWA 

hobi_A = {"membaca", "berenang", "musik", "traveling"}
hobi_B = {"musik", "gaming", "traveling", "fotografi"}

#1 Tampilkan semua hobi yang ada di kelas

semua_hobi = hobi_A.union(hobi_B)
print("SEMUA HOBI YANG ADA DIKELAS ADALAH", semua_hobi)

#2 Tampilkan hobi yang sama antara kelas A dan B 

hobi_sama = hobi_A.intersection(hobi_B)
print("HOBI YANG SAMA ADALAH", hobi_sama)

#3 Hobi yang hanya ada di kelas A, dan tidak ada di kelas B

c = hobi_A.difference(hobi_B)
print("HOBI YANG HANYA ADA DI KELAS A ADALAH", c)

#4 Apakah gaming ada di hobi A? 

print("Apakah ada gaming di hobi A?", "gaming" in hobi_A)
print()

# KASUS 2

print("KASUS 2 : MATA KULIAH YANG DIAMBIL")
print()

semester_1 = {"Matematika", "Pemrograman Dasar", "Bahasa Inggris", "Sistem Digital"}
semester_2 = {"Pemrograman Dasar", "Basis Data", "Bahasa Inggris", "Jaringan Komputer"}

#1 Cari mata kuliah yang diulang
print("MATA KULIAH YANG DIULANG ADALAH", semester_1.intersection(semester_2))

#2 Tampilkan semua daftar kuliah unik yang diambil
print("DAFTAR SEMYA MATA KULIAH UNIK ADALAH", semester_1.union(semester_2))

#3 Tampilkan mata kuliah yang hanya ada di semester 2
print("MATKUL YANG HANYA ADA DI SEMESTER 2 ADALAH", semester_2.symmetric_difference(semester_1))
print()


# KASUS 3 

print("KASUS 3 : KEHADIRAN SEMINAR")
print()

# CATATAN PESERTA SEMINAR

hari_pertama = {"Andi", "Budi", "Citra", "Dewi", "Eka"}
hari_kedua = {"Budi", "Citra", "Fajar", "Gita", "Andi"}

#1 Siapa saja yang hadir di kedua hari? 

hadir_kedua_hari = hari_pertama.intersection(hari_kedua)
print("PESERTA YANG HADIR DI KEDUA HARI ADALAH", hadir_kedua_hari)

#2 Siapa yang hanya hadir 1 hari saja?

hadir_satu_hari = hari_pertama.symmetric_difference(hari_kedua)
print("JUMLAH PESERTA YANG HADIR HANYA SATU HARI ADALAH", hadir_satu_hari)

#3 Hitung jumlah total peserta unik

total = hari_pertama.union(hari_kedua)
print("JUMLAH TOTAL PESERTA UNIK ADALAH", len(total))
print()


# KASUS 4 

print("KASUS 4 : KATA DALAM KALIMAT")
print()

kalimat = "python adalah bahasa pemograman yang mudah dan python sangat populer"

#1 Ubah kalimat menjadi set kata (hanya kata unik yang tersimpan)

variabel = set(kalimat.split())
print(variabel)

#2 Hitung jumlah kata unik

print("JUMLAH KATA UNIK ADALAH", len(variabel))

#3 Apakah kata java ada dalam set kata? 

print("APAKAH JAVA ADA DALAM SET?", "java" in variabel)
print()

# KASUS 5 

print("KASUS 5 : DAFTAR PRODUK TOKO")
print()

cabang_A = {"beras", "gula", "minyak", "kopi", "susu"}
cabang_B = {"beras", "gula", "teh", "kopi", "coklat"}

#1 Produk yang tersedia di semua cabang 

print("PRODUK YANG TERSEDIA DI SEMUA CABANG ADALAH", cabang_A.intersection(cabang_B))

#2 Produk yang hanya tersedia di cabang B 

print("PRODUK YANG TERSEDIA DI CABANG B ADALAH", cabang_A.difference(cabang_B))

#3 Buat set baru berisi semua produk yang dijual 

c = cabang_A.union(cabang_B)
print(c)

