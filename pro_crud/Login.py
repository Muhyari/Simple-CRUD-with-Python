import os
import time
import json
import pro_crud as crud

data_fileAkun = crud.database.data_fileAkun

def loginAkun():
    count = 0
    Main = True
    while Main:
        os.system("cls" if os.name == "nt" else "clear")
        print("="*50)
        print("halaman login".center(50, " ").upper())
        print("="*50)
        print("Belum punya akun? Tulis b\nMau melihat konten? Tulis k\n")
        inputUser = input("Login admin? [y/n/b/k]: ").lower()
                
        if not os.path.isfile(data_fileAkun):   
            with open(data_fileAkun, 'w') as file:
                json.dump({}, file, indent=4)
        
        with open(data_fileAkun, 'r') as file:
            data = json.load(file)
        
            
        if inputUser == "n":
            print("Login user")
            if len(data) == 0:
                data.setdefault("username", [])
                data.setdefault("password", [])
                print("anda belum memiliki akun\nsilahkan buat akun terlebih dahulu!")
                time.sleep(2.5)
                createAkun()
                
            elif len(data["username"]) == 0 and len(data["password"]) == 0:
                print("anda belum memiliki akun\nsilahkan buat akun terlebih dahulu!")
                time.sleep(2.5)
                createAkun()
                
            username = input("username: ").lower()
            password = input("password: ").lower()
            if username in data["username"] and password in data["password"]:
                print("login berhasil")
                crud.database.readData()
                Main = False
            else:
                print("Username atau Password salah!")
                time.sleep(2)
                
        elif inputUser == "b":
            createAkun()
            
        elif inputUser == "k":
            crud.konten.showKonten()
            
        elif inputUser == "y":
            print("login sebagai admin")
            with open(data_fileAkun, 'w') as file:
                json.dump(data, file, indent=4)
            
            username = input("username: ").lower()
            password = input("password: ").lower()
            if username == "admin" and password == "admin123":
                time.sleep(1.5)
                crud.adminDasboard.mydashBoard()
                
                    
        else:
            print("Pilihan tidak tersedia!")
            time.sleep(1)   

def createAkun():
    if not os.path.isfile(data_fileAkun):   
        with open(data_fileAkun, 'w') as file:
            json.dump({}, file, indent=4)
        
    with open(data_fileAkun, 'r') as file:
        data = json.load(file)
        
        if len(data) == 0:
            data.setdefault("username", [])
            data.setdefault("password", [])
            
    with open(data_fileAkun, 'w') as file:
        json.dump(data, file, indent=4)
            
    os.system("cls" if os.name == "nt" else "clear")
    print("halaman buat akun".center(50, "=").upper())
    print("Sudah punya akun? Tulis n\nMau melihat konten? Tulis k\n")
    username = input("Buat username: ").lower()
    password = input("Buat password: ").lower()
    match username or password:
        case "n":
            loginAkun()
        case "k":
            pass
    match username and password:
        case "n":
            loginAkun()
        case "k":
            pass
          
    try:
        with open(data_fileAkun, 'r') as file:
            data = json.load(file)
            
    except json.decoder.JSONDecodeError:
        data = {}
        with open(data_fileAkun, 'w') as file:
            json.dump(data, file, indent=4)
            
    data["username"].append(username)        
    data["password"].append(password)        
    
    with open(data_fileAkun, 'w') as file:
        json.dump(data, file, indent=4)

    print("Akun telah dibuat")
    time.sleep(1.3)
    