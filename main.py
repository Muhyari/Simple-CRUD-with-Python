import pro_crud as crud
import os
import time


if __name__ == "__main__":

    run = True
    while run:
        os.system("cls" if os.name == "nt" else "clear")
        print("=" * 50)
        print("selamat datang".title().center(50, " "))
        print("Showroom Mobil & Motor".center(50, " "))
        print("=" * 50)
        
        print("1.Login")
        print("2.Buat akun")
        print("3.Preview konten")
        print("-" * 50)
        try:
            inputUser = int(input("Pilihan: "))
            match inputUser:
                case 1:
                    crud.Login.loginAkun()
                case 2:
                    crud.Login.createAkun()
                case 3:
                    crud.database.readData()
                case _:
                    print("Menu tidak tersedia!")
        except ValueError:
            print('Input berupa angka')
            time.sleep(1)
            continue
        
        user = input("Exit Program? [y/n]: ").lower()
        run = False if user == "y" else True
        if user == "y":
            print("Terima kasih!")
        
