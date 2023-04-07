import os
import json
import time
import pro_crud as crud

data_file = 'D:/MAIN Python/Project-CRUD-1/pro_crud/data/data.json'
data_fileAkun ='D:/MAIN Python/Project-CRUD-1/pro_crud/data/dataAkun.json'

def readData():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("="*100)
    print("halaman data".upper().center(100," "))
    print("="*100)
    indeks = 'No'
    MOTOR = 'MOTOR'
    MOBIL = 'MOBIL'
    HARGA = "HARGA"
    
    if not os.path.isfile(data_file):   
        with open(data_file, 'w') as file:
            json.dump({}, file, indent=4)
            
    with open(data_file, 'r') as file:
        data = json.load(file)
        if len(data) == 0:
            print("Data masih kosong, silahkan masukan data!")
            createData()
        else:
            print(f"Jam {time.strftime('%H:%M:%S %p')}")
            print('-'*100)
            print(f"|{indeks:4} | {MOTOR:20} {HARGA:20} | {MOBIL:20} {HARGA:20} |")
            print('-'*100)
            
            for kendaraan in (["motor","mobil"]):
                for i, dataKendaraan in enumerate(data[kendaraan]):
                    if kendaraan == "motor":
                        print(f"|{i+1:4} | {dataKendaraan['nama']:20} {dataKendaraan['harga']:20} | {'-':20} {'-':20} |")
                    else:
                        print(f"|{i+1:4} | {'-':20} {'-':20} | {dataKendaraan['nama']:20} {dataKendaraan['harga']:20} |")
            print('-'*100)
            
            
def deleteData():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("="*100)
    print("halaman hapus data".upper().center(100," "))
    print("="*100)
    bacaData()
    with open(data_file, 'r') as file:
        data = json.load(file)
    try:    
        userDelete = input("Ingin menghapus nomor?: ")
        userDelete = int(userDelete) - 1
    
        userPilihan = input("1.motor\n2.mobil\n3.No tidak jadi menghapus data\nPilihan: ").lower()
        
        if userPilihan == "1":
            if userDelete > len(data["motor"]) or userDelete < 0:
                print("nomor tidak tersedia!")
            else:
                del data["motor"][userDelete]
                print("Data berhasil dihapus")
                
        elif userPilihan == "2":
            if userDelete > len(data["mobil"]) or userDelete < 0:
                print("nomor tidak tersedia!")
            else:
                del data["mobil"][userDelete]
                print("Data berhasil dihapus")
                
        elif userPilihan == "n" or userPilihan == "no" or userPilihan == '3':
            crud.mydashBoard()
            print("Tidak jadi menghapus data")
            
        time.sleep(1.3)
        
    
        
    except IndexError:
        print("nomor tidak tersedia!")
        
    with open(data_file, 'w') as file:
        json.dump(data, file, indent=4)


def createData():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("="*100)
    print("halaman membuat data".upper().center(100," "))
    print("="*100)
    print("Jam",time.strftime("%H:%M:%S %p"))
    if not os.path.isfile(data_file):   
        with open(data_file, 'w') as file:
            json.dump({}, file, indent=4)
            
    with open(data_file, 'r') as file:
        data = json.load(file)
        if len(data) == 0:
            data.setdefault("motor", [])        
            data.setdefault("mobil", []) 
            inputData = input("1.motor\n2.mobil\nPilihan (1-2):  ")
            
            if inputData == '1':
                namaMotor = input("masukan nama motor: ")
                hargaMotor = input("masukan harga motor: ")
                data["motor"].append({"nama": namaMotor, "harga": hargaMotor})
                
            elif inputData == '2':
                namaMobil = input("masukan nama mobil: ")
                hargaMobil = input("masukan harga mobil: ")
                data["mobil"].append({"nama": namaMobil, "harga": hargaMobil})
        else:
            inputData = input("1.motor\n2.mobil\nPilihan (1-2):  ")
            
            if inputData == '1':
                namaMotor = input("masukan nama motor: ")
                hargaMotor = input("masukan harga motor: ")
                data["motor"].append({"nama": namaMotor, "harga": hargaMotor})
                print("data motor telah ditambah")
                time.sleep(1.3)
                
            elif inputData == '2':
                namaMobil = input("masukan nama mobil: ")
                hargaMobil = input("masukan harga mobil: ")
                data["mobil"].append({"nama": namaMobil, "harga": hargaMobil})
                print("data mobil telah ditambah")
                time.sleep(1.3)
                
    with open(data_file, 'w') as file:
        json.dump(data, file, indent=4)
        
    try:
        with open(data_file, 'r') as file:
            data = json.load(file)
            
    except FileNotFoundError:
        data = {}
        with open(data_file, 'w') as file:
            json.dump(data, file, indent=4)  

            
def updateData():
    while True:
        os.system("cls" if os.name == 'nt' else "clear")
        print("="*100)
        print("halaman ubah data atau update data".upper().center(100," "))
        print("="*100)
        bacaData()
        with open(data_file, 'r') as file:
            data = json.load(file)
            
        userKendaraan = int(input("Ingin menganti atau update data? \n1.motor\n2.mobil\n3.Tidak jadi\nPilihan: "))
        print(len(data["motor"]))
        if userKendaraan == 3:
            print("Tidak jadi update data")
        
        elif userKendaraan == 1:
            userIndex = int(input("Pilih nomor atau indeks: ")) - 1
            if userIndex >= len(data["motor"]):
                print("indeks atau nomor tersebut tidak tersedia")
                time.sleep(1.4)
                continue
            userJenis = input("Ganti nama motor: ")
            userHarga = input("Ganti harga motor: ")
            if (userJenis == "" and userHarga == "") or (userJenis == "no" and userHarga == "no") or (userJenis == "No" and userHarga == "No"):
                print("data tidak update")
        
            else:
                data["motor"][userIndex]["nama"] = userJenis
                data["motor"][userIndex]["harga"] = userHarga
                print("data berhasil di update")
                
        elif userKendaraan == 2:
            userIndex = int(input("Pilih nomor atau indeks: ")) - 1
            if userIndex >= len(data["mobil"]):
                print("indeks atau nomor tersebut tidak tersedia")
                time.sleep(1.4)
                continue
            userJenis = input("Ganti nama mobil: ")
            userHarga = input("Ganti harga mobil: ")
            
            if (userJenis == "" and userHarga == "") or (userJenis == "no" and userHarga == "no") or (userJenis == "No" and userHarga == "No"):
                print("Nama tidak diganti")
            
            else:
                data["mobil"][userIndex]["nama"] = userJenis
                data["mobil"][userIndex]["harga"] = userHarga
                print("data berhasil di update")
        else:
            print("Menu tidak tersedia")    
                
        time.sleep(1.5)       
        with open(data_file, 'w') as file:
            json.dump(data, file, indent=4)

   
def bacaData():
    indeks = 'No'
    MOTOR = 'MOTOR'
    MOBIL = 'MOBIL'
    HARGA = "HARGA"
    
    if not os.path.isfile(data_file):   
        with open(data_file, 'w') as file:
            json.dump({}, file, indent=4)
            
    with open(data_file, 'r') as file:
        data = json.load(file)
        if len(data) == 0:
            print("Data masih kosong, silahkan masukan data!")
            createData()
        else:
            print(f"Jam {time.strftime('%H:%M:%S %p')}")
            print('-'*100)
            print(f"|{indeks:4} | {MOTOR:20} {HARGA:20} | {MOBIL:20} {HARGA:20} |")
            print('-'*100)
            
            for kendaraan in (["motor","mobil"]):
                for i, dataKendaraan in enumerate(data[kendaraan]):
                    if kendaraan == "motor":
                        print(f"|{i+1:4} | {dataKendaraan['nama']:20} {dataKendaraan['harga']:20} | {'-':20} {'-':20} |")
                    else:
                        print(f"|{i+1:4} | {'-':20} {'-':20} | {dataKendaraan['nama']:20} {dataKendaraan['harga']:20} |")
            print('-'*100)
            
