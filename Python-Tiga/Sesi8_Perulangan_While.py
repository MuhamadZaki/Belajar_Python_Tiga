# Di Python, Selain keyword for Ada Juga Keyword while Yang Fungsinya Kurang Lebih Sama Yaitu Untuk Perulangan Dan Bedanya Perulangan Menggunakan while Terkontrol Via Operasi Logika Atau Nilai bool

# 1. Keyword while

# Cara Penerapan Perulangan Ini Adalah Dengan Menuliskan kyword while Kemudian Diikuti Dengan Nilai bool Atau Operasi Logika

#lanjutkan = True                                       # --> Inisialisasi variabel yang menyimpan data boolean, dengan nilai True

#while lanjutkan:                                       # --> Perulanga atau loop, yang akan terus berjalan selama variabel lanjutkan bernilai True
    #input_konversi = int(input("Masukan biljil: "))    # --> Meminta pengguna memasukan nilai sebagai string, lalu mengonversinya menjadi tipe data integer dan tersimpan pada variabel input_konversi

    #if input_konversi <= 0 or input_konversi % 2 == 1: # --> Kondisi, memeriksa nilai input_konversi kurang dari atau sama dengan 0 atau merupakan bilangan ganjil, jika salah satu kondisi terpenuhi maka akan mengeksekusi kode di dalamnya dan jika kondisi tidak terpenuhi maka akan melanjutkan ke kondisi berikutnya
        #print(input_konversi)                          # --> Jika kondisi benar atau terpenuhi, maka mencetak pesan angka ganjil (tergantung inputan pengguna)
        #lanjutkan = False                              # --> Untuk mengakhiri perulangan atau loop, jika kondisi sebelumnya terpenuhi  atau variabel lanjutkan diubah menjadi False
    
    #else:                                              # --> Kondisi, jika kondisi sebelumnya tidak terpenuhi maka blok kode ini dieksekusi
        #print("Lol", input_konversi)                   # --> Jika kondisi sebelumnya salah atau tidak terpenuhi, maka mencetak pesan "Lol" dan (angka inputan pengguna)



#input_konversi = int(input("Masukan angka: "))  # --> Meminta pengguna memasukan nilai sebagai string, lalu mengonversinya menjadi tipe data integer dan tersimpan pada variabel input_konversi
#index = 0                                       # --> Inisialisasi variabel yang menyimpan data integer, dengan nilai 0

#while index < input_konversi:                   # --> Perulangan atau loop, selama nilai index kurang dari nilai yang dimasukan oleh pengguna (input_konversi), jika kondisi terpenuhi maka akan mengeksekusi kode di dalamnya
    #print(index)                                # --> Jika kondisi benar atau terpenuhi, maka mencetak pesan (tergantung inputan pengguna, jika 5 maka 0 1 2 3 4)
    #index += 1                                  # --> Menambahkan 1 pada nilai variabel index, setiap iterasi (increment)



#input_konversi = int(input("Masukan angka: "))  # --> Meminta pengguna memasukan nilai sebagai string, lalu mengonversinya menjadi tipe data integer dan tersimpan pada variabel input_konversi
#index = 0                                       # --> Inisialisasi variabel yang menyimpan data integer, dengan nilai 0

#while index > input_konversi:                   # --> Perulangan atau loop, selama nilai index lebih besar dari nilai yang dimasukan oleh pengguna (input_konversi), jika kondisi terpenuhi maka akan mengeksekusi kode di dalamnya
    #print(index)                                # --> Jika kondisi benar, atau terpenuhi, maka mencetak pesan (tergantung inputan pengguna, jika -5 maka 0 -1 -2 -3 -4 )
    #index -= 1                                  # --> Mengurangi 1 pada nilai variabel index, setiap iterasi (decrement)

# Operasi Increment Dan Decrement

# Python Tidak Mengenal Operator Unary ++ Dan --, Solusi Untuk Melakukan Operasi Increment Dan Decrement Bisa Menggunakan Cara Ini

# Increment --> index += 1

# Decrement --> index -= 1


print("------")

# 2. Perulangan while VS for
# Operasi while Cocok Digunakan Untuk Perulangan Yang Dimana Kontrolnya Adalah Operasi Logika Atau Nilai Boolean Yang Tidak Ada Kaitannya Dengan Sequence
# Perulangan Akan Menjadi Lebih Ringkas Dengan Pengaplikasian Keyword for, Silakan Lihat Perbandingannya 

#input_konversi = int(input("Masukan angka: "))  # --> Meminta pengguna memasukan nilai sebagai string, lalu mengonversinya menjadi tipe data integer dan tersimpan pada variabel input_konversi
#index = 0                                       # --> Inisialisasi variabel yang menyimpan data integer, dengan nilai 0

#while index < input_konversi:                   # --> Perulangan atau loop, selama nilai index kurang dari nilai yang dimasukan oleh pengguna (input_konversi), jika kondisi terpenuhi maka akan mengeksekusi kode di dalamnya
    #print(index)                                # --> Jika kondisi benar atau terpenuhi, maka mencetak pesan (tergantung inputan pengguna, jika 5 maka 0 1 2 3 4)
    #index += 1                                  # --> Menambahkan 1 pada nilai variabel index, setiap iterasi (increment)


#input_konversi = int(input("Masukan nilai: "))  # --> Meminta pengguna memasukan nilai sebagai string, lalu mengonversinya menjadi tipe data integer dan tersimpan pada variabel input_konversi

#for index in range(input_konversi):             # --> Perulangan atau loop, sebanyak nilai yang dimasukan oleh pengguna input_konversi dan (variabel index akan mengambil nilai dari 0 hingga input_konveri -1)
    #print(index)                                # --> Setiap iterasi nilai index akan dicetak (tergantung inputan pengguna, jika 5 maka 0 1 2 3 4)


# Sedangkan Keyword for Lebih Pas Digunakan Pada Perulangan Yang Kontrolnya Adalah Data Sequence, Contohnya Seperti range Dan list


print("------")

# 3. Perulangan Bercabang (Bersarang) / Nested while

#input_konversi = int(input("Masukan nilai: "))  # --> Meminta pengguna memasukan nilai sebagai string, lalu mengonversinya menjadi tipe data integer dan tersimpan pada variabel input_konversi
#index = 0                                       # --> Inisialisasi variabel yang menyimpan data integer, dengan nilai 0

#while index < input_konversi:                   # --> Perulangan atau loop, selama nilai index kurang dari nilai yang dimasukan oleh pengguna (input_konversi), jika kondisi terpenuhi maka akan mengeksekusi kode berikutnya
    #jidex = 0                                   # --> Inisialisasi variabel yang menyimpan data integer, dengan nilai 0

    #while jidex < input_konversi - index:       # --> Perulangan atau loop bersarang, selama nilai jidex kurang dari nilai input_konversi - index, jika kondisi terpenuhi maka akan mengeksekusi kode di dalamnya atau berikutnya
        #print("*", end=" ")                     # --> Jika kondisi benar atau terpenuhi, maka mencetak pesan karakter bintang dengan spasi sebagai pemisah (tanpa newline)
        #jidex += 1                              # --> Menambahkan 1 pada nilai variabel jidex, setiap iterasi (increment)
    
    #print()                                     # --> Maka mencetak pesan newline (baris baru) setelah mencetak bintang sejumlah yang sesuai
    #index += 1                                  # --> Menambahkan 1 pada nilai variabel index, setiap iterasi (increment)


print("------")

# 4. Kombinasi while Dan for
# Kedua Keyword Perulangan Yang Sudah Dipelajari, Yaitu for Dan while Bisa Dikombinasikan Untuk Membuat Suatu Nested Loop Atau Perulangan Bercabang

input_konversi = int(input("Masukan angka: "))  # --> Meminta pengguna memasukan nilai sebagai string, lalu mengonversinya menjadi tipe data integer dan tersimpan pada variabel input_konversi
index = 0                                       # --> Inisialisasi variabel yang menyimpan data integer, dengan nilai 0

for index in range(input_konversi):             # --> Perulangan atau loop, sebanyak nilai yang dimasukan oleh pengguna (input_konversi) dan (variabel index akan mengambil nilai dari 0 hingga input_konveri -1)
    jidex = 0                                   # --> Inisialisasi variabel yang menyimpan data integer, dengan nilai 0

    while jidex < input_konversi - index:       # --> Perulangan atau loop bersarang, selama nilai jidex kurang dari nilai input_konversi - index, jika kondisi terpenuhi maka akan mengeksekusi kode di dalamnya atau berikutnya 
        print("*", end=" ")                     # --> Jika kondisi benar atau terpenuhi, maka mencetak pesan karakter bintang dengan spasi sebagai pemisah (tanpa newline)
        jidex += 1                              # --> Menambahkan 1 pada nilai variabel jidex, setiap iterasi (increment)
    
    print()                                     # --> Maka mencetak pesan newline (baris baru) setelah mencetak bintang sejumlah yang sesuai