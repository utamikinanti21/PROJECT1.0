# Latihan 2

def login():
    tries = 0
    print("Login dengan 3 kesempatan admin\nusername: Daspro2023")
    password = str(input("password: "))

    while tries < 3:
        if password == "Latihan":
            print("Password diterima!")
            break
        else:
            tries += 1
            if tries == 3:
                print(f"Password ditolak!")
                break
            password = str(input(f"Password salah {3 - tries}x kesempatan lagi, coba lagi: "))
        
login()