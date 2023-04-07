import os
import json
import pro_crud as crud

data_file = crud.database.data_file

def showKonten():
    os.system('cls' if os.name == 'nt' else 'clear')
    crud.database.readData()
    
    # -> Head <-
    print('='*50)
    print('halaman showroom'.center(50, " ").upper())
    # -> Head <-
    try:
        with open(data_file, 'r') as file:
            data = json.load(file)
            
            
        # <body> 
        
        
        for i, d in enumerate(data["motor"]):
            print(f"{i+1:4} | {d['kendaraan']:15} | {d['harga']:20} | ")    
        #</body>
        
        #<footer>
        print('-'*50)
        #<footer>
        
    except json.decoder.JSONDecodeError:
        with open(data_file, 'w', encoding='utf-8') as file:
            data = {}
            json.dump(data,file, indent=4)
            
            
    except FileNotFoundError:
        with open(data_file, 'w') as f:
            data = {}
            json.dump(data, f)
        
            print('Mobil atau Motor tidak ditemukan')
            data = {}
    with open(data_file, 'w', encoding='utf-8') as file:
        json.dump(data,file, indent=4)
            
