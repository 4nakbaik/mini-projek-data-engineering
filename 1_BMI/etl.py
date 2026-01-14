def bmi_calcu(tb_cm,bb):
    tb_m = tb_cm / 100
    bmi = bb / (tb_m**2)
    
    if bmi <= 18.5:
        kategori = "Kurus"
    elif bmi <= 25:
        kategori = "Ideal"
    elif bmi <= 30:
        kategori = "Gemuk"
    else:
        kategori ="Obesitas"    
        
    return round(bmi,2), kategori
 
def valid_data(nama,umur,tb_cm,bb):
    if not nama:
        return False
    if umur <=0:
        return False
    if tb_cm <=0 or bb <=0:
        return False
    return True