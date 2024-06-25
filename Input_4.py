""" Membaca Input Dari Pengguna dan Mencetaknya """

# Input Menggunakan String
nama = input("Masukan nama sobat : ")
print("Nama : ", nama) # Dinamis, sesuai inputas pengguna dan contoh inputan Muhamad Zaki

# Mengkonversi String to Integer
umur = input("Masukan umur sobat : ")
konversi_umur = int(umur)
print("Umur : ", konversi_umur) # Dinamis, sesuai inputan pengguna dan contoh inputan 20

# Mengkonversi String to Float
berat_badan = input("Masukan berat badan sobat : ")
konversi_berat_badan = float(berat_badan)
print("Berat badan : ", konversi_berat_badan) # Dinamis, sesuai inputan user dan contoh inputan 50


# Beberapa Inputan Sekaligus
data = input("Masukan angka yang dipisahkan dengan koma : ")
angka_string = data.split(',')
angka = [int(tobrut) for tobrut in angka_string ]
print("Hasil angka : ", angka) # Dinamis, sesuai inputan user dan contoh inputan 100, 200, 300, 400, 500

# Inputan Menggunakan Validasi (di sini saya mengkonversi string to int)
while True:
    try:
        data_usia_string = input("Masukan Usia Sobat : ")
        usia = int(data_usia_string)
        break # keluar loop, jika konversi berhasil
    except ValueError:
        print("Input tidak benar! Masukan angka!") # Dinamis, jika user memasukan angka, maka akan break (konversi berhasil), jika tidak akan mengulai lagi dan terdapat pesan
print("Usia sobat : ", usia )

# Note : Input merujuk pada data yang diterima oleh program dari luar (pengguna) atau mengambil data daari pengguna