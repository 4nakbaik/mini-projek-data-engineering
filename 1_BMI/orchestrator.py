from config.setting import (
    RAW_DATA_FILE, 
    CLEAN_DATA_FILE, 
    INVALID_DATA_FILE
    )
from etl import bmi_calcu, valid_data
from io_utils import input_data, save_csv

OUTPUT_FILE = "1_BMI/output/bmi_hasil.csv"

def main():
    data_raw = input_data()
    data_clean = []
    
    for row in data_raw:
        nama = row["nama"]
        umur = row["umur"]
        tb = row["tinggi_badan"]
        bb = row["berat_badan"]
        
        if not valid_data(nama,umur,tb,bb):
            continue
    
        bmi, kategori = bmi_calcu(tb,bb)
        
        data_clean.append({
            "nama": nama,
            "umur": umur,
            "tinggi_badan": tb,
            "berat_badan": bb,
            "bmi":round (bmi, 2),
            "kategori": kategori
        })
    
    save_csv(data_clean, OUTPUT_FILE)
    print(f"Data berhasil disimpan ke {OUTPUT_FILE}")
        
if __name__ == "__main__" :
    main()     
