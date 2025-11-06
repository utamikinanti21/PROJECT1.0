### SOAL NOMOR 5 

Total = int(input("MASUKKAN TOTAL BELANJA KAMU HARI INI : "))
Member = str(input("APAKAH KAMU PUNYA MEMBER? (Y/N) : "))

if Total >= 500000 and Member == "Y":
    print("JUMLAH YANG KAMU BAYAR", Total * 85 / 100)
    if Member == "N" : 
        print("JUMLAH YANG KAMU BAYAR", Total * 90 / 100)

elif Total >= 200000 and Member == "Y":
    print("JUMLAH YANG KAMU BAYAR", Total * 95 / 100)
    if Member == "N" : 
        print("JUMLAH YANG KAMU BAYAR", Total * 90 / 100)

elif Total <= 200000 and Member == "Y" : 
    print("JUMLAH YANG KAMU BAYAR", Total * 95 / 100)

else :
    print("JUMLAH YANG KAMU BAYAR", Total)