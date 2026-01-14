import csv

def input_data():
    data =[]
    while True:
        try:
            nama = str(input("Nama : "))
            if nama.lower() == "stop": # Ketik "stop" untuk menghentikan input data
                break
            umur = int(input("Umur : "))
            tb = float(input(" Tinggi Badan : "))
            bb = float(input("Berat Badan : "))
            
            # tabel data
            data.append({
                "nama": nama,
                "umur": umur,
                "tinggi_badan": tb,
                "berat_badan": bb
            })
            print("Data berhasil ditambahkan.\n")
        
        except ValueError:
            print("Tidak valid, ulangi.\n")
    return data

# Dismpan ke file csv
def save_csv(data,filepath):
    fieldnames = [
        "nama",
        "umur",
        "tinggi_badan",
        "berat_badan",
        "bmi",
        "kategori"
    ]
    
    with open(filepath, "w", newline="", encoding= "utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader
        writer.writerows(data)
        