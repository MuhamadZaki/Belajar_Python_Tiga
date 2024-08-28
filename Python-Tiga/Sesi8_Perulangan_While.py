# Di Python, Selain keyword for Ada Juga Keyword while Yang Fungsinya Kurang Lebih Sama Yaitu Untuk Perulangan Dan Bedanya Perulangan Menggunakan while Terkontrol Via Operasi Logika Atau Nilai bool

# 1. Keyword while

# Cara Penerapan Perulangan Ini Adalah Dengan Menuliskan kyword while Kemudian Diikuti Dengan Nilai bool Atau Operasi Logika

lanjutkan = True                                       # --> Inisialisasi variabel yang menyimpan data boolean

while lanjutkan:                                       # --> Perulanga atau loop, yang akan terus berjalan selama variabel lanjutkan bernilai True
    input_konversi = int(input("Masukan bilnap: "))    # --> Meminta pengguna memasukan nilai sebagai string, lalu mengonversinya menjadi tipe data integer dan tersimpan pada variabel input_konversi

    if input_konversi <= 0 or input_konversi % 2 == 1: # --> Kondisi, memeriksa nilai input_konversi kurang dari atau sama dengan 0 atau merupakan bilangan ganjil, jika salah satu kondisi terpenuhi maka akan mengeksekusi kode di dalamnya dan jika kondisi tidak terpenuhi maka akan melanjutkan ke kondisi berikutnya
        print(input_konversi)                          # --> Jika kondisi benar atau terpenuhi, maka mencetak pesan angka ganjil (tergantung inputan pengguna)
        lanjutkan = False                              # --> Untuk mengakhiri perulangan atau loop, jika kondisi sebelumnya terpenuhi
    
    else:                                              # --> Kondisi, jika kondisi sebelumnya tidak terpenuhi maka blok kode ini dieksekusi
        print("Lol", input_konversi)                   # --> Jika kondisi sebelumnya salah atau tidak terpenuhi, maka mencetak pesan "Lol" dan (angka inputan pengguna)


