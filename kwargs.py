#fungsi biasa
def fungsi(nama,tinggi,berat):
    print(f"{nama} memiliki tinggi badan {tinggi} dan berat badan {berat}")

fungsi("armin",170,50)


#fungsi kwargs
def fungsi(**kwargs):
    nama = kwargs["nama"]
    tinggi = kwargs["tinggi"]
    berat = kwargs["berat"]
    
    print(f"\n{nama} memiliki tinggi badan {tinggi} dan berat badan {berat}")

fungsi(nama = "armin",tinggi = 170, berat = 50)


#kasus
def math(*args,**kwargs):
    output = 0
    if kwargs["option"] == "tambah":
        for angka in args:
            output += angka
    
    elif kwargs["option"] == "kali":
        output = 1
        for angka in args:
            output *= angka

    else:
        print("Tidak Ada Operasi")
        
    return output
        

hasil = math(1,2,3,4,option="tambah")
print(f"\nhasi tambah  {hasil}")

hasil = math(1,2,3,4,option="kali")
print(f"\nhasil kali {hasil}")
