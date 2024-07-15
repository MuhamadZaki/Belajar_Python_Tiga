""" Membaca Input Dari Pengguna dan Mencetaknya """

# Praktekan dan Pahami!

# Input Menggunakan String
nama = input("Masukan nama sobat : ")
print("Nama : ", nama) 

# Mengkonversi String to Integer
umur = input("Masukan umur sobat : ")
konversi_umur = int(umur)
print("Umur : ", konversi_umur) 

# Mengkonversi String to Float
berat_badan = input("Masukan berat badan sobat : ")
konversi_berat_badan = float(berat_badan)
print("Berat badan : ", konversi_berat_badan) 


# Beberapa Inputan Sekaligus
data = input("Masukan angka yang dipisahkan dengan koma : ")
angka_string = data.split(',')
angka = [int(tobrut) for tobrut in angka_string ]
print("Hasil angka : ", angka) 

# Inputan Menggunakan Validasi (di sini saya mengkonversi string to int)
while True: 
    try:  
        data_usia_string = input("Masukan Usia Sobat : ")
        usia = int(data_usia_string)
        break # keluar loop, jika konversi berhasil
    except ValueError:
        print("Input tidak benar! Masukan angka!") 
print("Usia sobat : ", usia ) 

# Note : Input merujuk pada data yang diterima oleh program dari luar (pengguna) atau mengambil data daari pengguna