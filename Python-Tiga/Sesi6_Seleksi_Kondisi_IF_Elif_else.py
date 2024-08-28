# Seleksi Kondisi Merupakan Suatu Blok Kode Yang Dieksekusi Hanya ketika Kriteria Yang Ditentukan Terpenuhi Dan Biasanya Digunakan Untuk Kontrol Alur Program

# 1. Block Identation 

# Di Python, Suatu Blok Kondisi Ditandai Dengan Indentation Atau Spasi, Yang Menjadikan Kode Semakin Menjorok Ke Kanan.

#umur = 16                           
#pendapatan = 9000                   

#if umur <=16 and pendapatan <=9000:
    #print("Pinjol diterima!")           # --> Sesuai aturan PEP 8 – Style Guide for Python Code, indentation di Python menggunakan 4 karakter spasi dan bukan karakter tab.


print("------")

# 2. Fungsi input()

# Untuk Menampilkan Suatu Pesan Text (Yang Disisipkan Saat Fungsi Dipanggil) Dan Mengembalikan Nilai Inputan User Dalam Bentuk String

#string_input = input("Masukan Angka: ") # --> Meminta pengguna memasukan nilai sebagai string
#print(string_input)                     # --> Mencetak variabel, maka mencetak pesan tergantung inputan user
#print(type(string_input))               # --> Mencetak variabel dan mengencek tipe data, maka mencetak pesan <class 'str'>


print("------")

# 3. Fungsi type()

# Untuk Melihat Informasi Tipe Data Dari Suatu Nilai Atau Variabel Dan Fungsi Ini Mengembalikan String Dalam Format <class 'tipe_data'>

#cek_tipe_data = True       # --> Inisialisasi variabel yang menyimpan data boolean
#print(type(cek_tipe_data)) # --> Mencetak variabel dan mengecek tipe data, maka mencetak pesan <class 'bool'>


print("------")

# 4. Type Conversion / Konversi Tipe Data

# konversi Tipe Data String ke Int Dilakukan Menggunakan Fungsi int(), Dengan Menggunakan Fungsi Tersebut Data String Yang Disisipkan Pada Parameter, Tipe Datanya Berubah menjadi Integer

#string_input = input("Masukan Angka: ") # --> Meminta pengguna memasukan nilai sebagai string
#Konversi = int(string_input)            # --> Mengonversi variabel string_input menjadi integer
#print(type(Konversi))                   # --> Mencetak variabel dan mengecek tipe data, maka mencetak pesan <class 'int'>


print("------")

# 5. Keyword if

# Kondisi Ini Akan Dieksekusi Jika Kondisi terpenuhi Atau Bernilai True

#umur = 16                           # --> Inisialisasi variabel yang menyimpan data integer
#pendapatan = 9000                   # --> Inisialisasi variabel yang menyimpan data integer

#if umur <=16 and pendapatan <=9000: # --> Kondisi, memeriksa apakah umur kurang dari atau sama dengan 16 dan pendapatan kurang dari atau sama dengan 9000, jika kedua kondisi terpenuhi maka akan mengeksekusi kode di dalamnya dan jika kondisi tidak terpenuhi maka akan melanjutkan ke kondisi berikutnya
    #print("Pinjol diterima!")       # --> Jika kedua kondisi benar atau terpenuhi, maka mencetak pesan "Pinjol diterima!"


print("------")

# 6. Keyword elif

# Kondisi Ini Akan Diprikas Jika Kondisi Sebelumnya Tidak Terpenuhi

# nilai = int(input("Masukan nilai: "))  # --> Bisa juga seperti ini

#string_input = input("Masukan Nilai: ") # --> Meminta pengguna memasukan nilai sebagai string
#nilai = int(string_input)               # --> Mengonversi variabel string_input menjadi integer


#if nilai == 100:                        # --> Kondisi, memeriksa apakah nilai sama dengan 100, jika kondisi terpenuhi maka akan mengeksekusi kode di dalamnya dan jika kondisi tidak terpenuhi maka akan melajutkan ke kondisi berikutnya
    #print("A")                          # --> Jika kondisi benar atau terpenuhi, maka mencetak pesan "A"

#elif nilai >= 90 and nilai < 100:       # --> Kondisi, memeriksa apakah nilai lebih besar dari atau sama dengan 90 dan nilai kurang dari 100, jika kedua kondisi terpenuhi maka akan mengeksekusi kode di dalamnya dan jika kondisi tidak terpenuhi maka akan melanjutkan ke kondisi berikutnya
    #print("B")                          # --> Jika kedua kondisi benar atau terpenuhi, maka mencetak pesan "B"

#elif nilai >= 0 and nilai < 90:         # --> Kondisi, memeriksa apakah nilai lebih besar dari atau sama dengan 0 dan nilai kurang dari 90, jika kedua kondisi terpenuhi maka akan mengeksekusi kode di dalamnya dan jika kondisi tidak terpenuhi maka akan melanjutkan ke kondisi berikutnya
    #print("C")                          # --> Jika kedua kondisi benar atau terpenuhi, maka mencetak pesan "C"


print("------")

# 7. Keyword else

# Digunakan Sebagai Blok Seleksi Kondisi Penutup Ketika Blok if Atau elif Dalam Satu Chain Tidak Ada Yang Terpenuhi

#string_input = input("Masukan Nilai: ") # --> Meminta pengguna memasukan nilai sebagai string
#nilai = int(string_input)               # --> Mengonversi variabel string_input menjadi integer

#if nilai >= 90 and nilai <= 100:        # --> Kondisi, memeriksa apakah nilai lebih besar dari atau sama dengan 90 dan nilai kurang dari atau sama dengan 100, jika kedua kondisi terpenuhi maka akan mengeksekusi kode di dalamnya dan jika kondisi tidak terpenuhi maka akan melanjutkan ke kondisi berikutnya
    #print("A")                          # --> Jika kedua kondisi benar atau terpenuhi, maka mencetak pesan "A"

#elif nilai >= 80 and nilai < 90:        # --> Kondisi, memeriksa apakah nilai lebih besar dari atau sama dengan 80 dan nilai kurang dari 90, jika kedua kondisi terpenuhi maka akan mengeksekusi kode di dalamnya dan jika kondisi tidak terpenuhi maka akan melanjutkan ke kondisi berikutnya
    #print("B")                          # --> Jika kedua kondisi benar atau terpenuhi, maka mencetak pesan "B"

#elif nilai >= 70 and nilai < 80:        # --> Kondisi, memeriksa apakah nilai lebih besar dari atau sama dengan 70 dan nilai kurang dari 80, jika kedua kondisi terpenuhi maka akan mengeksekusi kode di dalamnya dan jika kondisi tidak terpenuhi maka akan melanjutkan ke kondisi berikutnya
    #print("C")                          # --> Jika kedua kondisi benar atau terpenuhi, maka mencetak pesan "C"

#elif nilai < 70 and nilai >= 50:        # --> Kondisi, memeriksa apakah nilai kurang dari 70 dan nilai lebih besar dari atau sama dengan 50, jika kedua kondisi terpenuhi maka akan mengeksekusi kode di dalamnya dan jika kondisi tidak terpenuhi maka akan melanjutkan ke kondisi berikutnya
    #print("D")                          # --> Jika kedua kondisi benar atau terpenuhi, maka mencetak pesan "D"

#else:                                   # --> Kondisi, jika semua kondisi tidak terpenuhi maka blok kode ini dieksekusi (jika nilai kurang dari 50)
    #print("Tidak Lulus!")               # --> Jika semua kondisi salah atau tidak terpenuhi, maka mencetak pesan "Tidak lulus!"


print("------")

# 8. Seleksi Kondisi Bercabang (Bersarang) / Nested

# Seleksi Kondisi Bisa Saja Berada Di Dalam Suatu Blok Seleksi Kondisi Dan Gunakan Identation Yang Lebih Ke kanan Untuk Seleksi Kondisi Terdalam

#string_input = input("Masukan Value: ") # --> Meminta pengguna memasukan nilai sebagai string
#nilai= int(string_input)                # --> Mengonversi variabel string_input menjadi integer

#if nilai >= 90 and nilai <=100:         # --> Kondisi, memeriksa apakah nilai lebih besar dari atau sama dengan 90 dan nilai kurang dari atau sama dengan 100, jika kedua kondisi terpenuhi maka akan mengeksekusi kode di dalamnya dan jika kondisi tidak terpenuhi maka akan melanjutkan ke kondisi berikutnya
    #print("A")                          # --> Jika kedua kondisi benar atau terpenuhi, maka akan mencetak pesan "A"

#elif nilai >= 80 and nilai < 90:        # --> Kondisi, memeriksa apakah nilai lebih besar dari atau sama dengan 80 dan nilai kurang dari 90, jika kedua kondisi terpenuhi maka akan mengeksekusi kode di dalamnya dan jika kondisi tidak terpenuhi maka akan melanjutkan ke kondisi berikutnya
    #print("B")                          # --> Jika kedua kondisi benar atau terpenuhi, maka akan mencetak pesan "B"

#elif nilai >= 70 and nilai < 80:        # --> Kondisi, memeriksa apakah nilai lebih besar dari atau sama dengan 70 dan nilai kurang dari 80, jika kedua kondisi terpenuhi maka akan mengeksekusi kode di dalamnya dan jika kondisi tidak terpenuhi maka akan melanjutkan ke kondisi berikutnya
    #print("C")                          # --> Jika kedua kondisi benar atau terpenuhi, maka akan mencetak pesan "C"

#elif nilai >=60 and nilai < 70:         # --> Kondisi, memeriksa apakah nilai lebih besar dari atau sama dengan 60 dan nilai kurang dari 70, jika kedua kondisi terpenuhi maka akan mengeksekusi kode di dalamnya dan jika kondisi tidak terpenuhi maka akan melanjutkan ke kondisi berikutnya
    #print("D")                          # --> Jika kedua kondisi benar atau terpenuhi, maka akan mencetak pesan "D"

#elif nilai < 60:                        # --> Kondisi, memeriksa apakah nilai kurang dari 60, jika kondisi terpenuhi maka akan mengeksekusi kode di dalamnya dan jika kondisi tidak terpenuhi maka akan melanjutkan ke kondisi berikutnya
    #print("Mendapatkan Nilai")          # --> Jika kondisi benar atau terpenuhi, maka akan mencetak pesan "Mendapatkan Nilai"
    #if nilai >=50:                      # --> Kondisi bersarang, memeriksa apakah nilai lebih besar dari atau sama dengan 50, jika kondisi terpenuhi maka akan mengeksekusi kode di dalamnya dan jika kondisi tidak terpenuhi maka akan melanjutkan ke kondisi berikutnya
        #print("E")                      # --> Jika kondisi benar atau terpenuhi, maka akan mencetak pesan "E"
    #else:                               # --> Kondisi bersarang, jika semua kondisi tidak terpenuhi maka blok kode ini dieksekusi (jika nilai kurang dari 50)
        #print("Belajra lagi!")          # --> Jika semua kondisi salah atau tidak terpenuhi, maka mencetak pesan "Belajar lagi!"


print("------")

# 9. Seleksi Kondisi Dengan Operasi Logika

# Keyword and, or, Dan not Bisa Digunakan Dalam Seleksi Kondis

string_input = input("Masukan nilai: ")                  # --> Meminta pengguna memasukan nilai sebagai string

if not string_input:                                     # --> Kondisi, memeriksa apakah string input kosong, jika kondisi terpenuhi maka akan mengeksekusi kode di dalamnya dan jika konidak terpenuhi maka akan melanjutkan ke kondisi berikutnya
    print("Input harus berupa angka!")                   # --> Jika kondisi benar atau terpenuhi, maka akan mencetak pesan "Input harus berupa angka!"

else:                                                    # --> Kondisi, jika kondisi sebelumnya tidak terpenuhi maka blok kode ini dieksekusi (jika string_input tidak kosong atau angka)
    nilai = int(string_input)                            # --> Mengonversi variabel string_input menjadi integer
    
    string_input_prev = input("Masukan nilai prev: ")    # --> Meminta pengguna memasukan nilai sebelumnya/prev sebagai string

    if not string_input_prev:                            # --> Kondisi, memeriksa apakah string input_prev kosong, jika kondisi terpenuhi maka akan mengeksekusi kode di dalamnya dan jika konidak terpenuhi maka akan melanjutkan ke kondisi berikutnya
        print("Input harus berupa angka!")               # --> Jika kondisi benar atau terpenuhi, maka akan mencetak pesan "Input harus berupa angka!" 
    
    else:                                                # --> Kondisi, jika kondisi sebelumnya tidak terpenuhi maka blok kode ini dieksekusi (jika string_input_prev tidak kosong atau angka)
        prev = int(string_input_prev)                    # --> Mengonversi variabel string_input_prev menjadi integer

        if nilai >= 90 and prev <=100:                   # --> kondisi bersarang, memeriksa apakah nilai lebih besar dari atau sama dengan 90 dan prev kurang dari atau sama dengan 100, jika kedua kondisi terpenuhi maka akan mengeksekusi kode di dalamnya dan jika kondisi tidak terpenuhi maka akan melanjutkan ke kondisi berikutnya
            print("A")                                   # --> Jika kedua kondisi benar atau terpenuhi, maka akan mencetak pesan "A"
        
        elif nilai >= 80 and prev < 90:                  # --> Kondisi bersarang, memeriksa apakah nilai lebih besar dari atau sama dengan 90 dan prev kurang dari 90, jika kedua kondisi terpenuhi maka akan mengeksekusi kode di dalamnya dan jika kondisi tidak terpenuhi maka akan melanjutkan ke kondisi berikutnya
            print("B")                                   # --> Jika kedua kondisi benar atau terpenuhi, maka akan mencetak pesan "B"
        
        elif nilai >= 50 and prev < 80:                  # --> Kondisi bersarang, memeriksa apakah nilai lebih besar dari atau sama dengan 50 dan prev kurang dari 80, jika kedua kondisi terpenuhi maka akan mengeksekusi kode di dalamnya dan jika kondisi tidak terpenuhi maka akan melanjutkan ke kondisi berikutnya
            print("C")                                   # --> Jika kedua kondisi benar atau terpenuhi, maka akan mencetak pesan "C"
        
        else:                                            # --> Kondisi bersarang, jika semua kondisi tidak terpenuhi maka blok kode ini dieksekusi (jika nilai kurang dari 50)
            print("Tidak Lulus!")                        # --> Jika semua kondisi salah atau tidak terpenuhi, maka mencetak pesan "Tidak Lulus!"

        
        if not (0 <= nilai <=100 and 0 <= prev <= 100):            # --> Kondisi bersarang, apakah nilai atau prev di luar rentang 0-100, jika kedua kondisi terpenuhi maka akan mengeksekusi kode di dalamnya dan jika kondisi tidak terpenuhi maka akan melanjutkan ke kondisi berikutnya
            print("Nilai berada di luar rentang yang diharapkan!") # --> Jika kedua kondisi benar atau terpenuhi, maka mencetak pesan "Nilai berada di luar rentang yang diharapkan!

""" Note! """

# Berikut Adalah Contoh Bagaimana Kondisi Ini Bekerja


# if not (0 <= nilai <=100 and 0 <= prev <= 100): --> Akan bernilai True, jika salah satu dari nilai atau prev berada di luar rentang 0 hingga 100.

# 0 <= nilai <= 100                               --> Memeriksa apakah nilai berada dalam rentang 0 hingga 100 (inklusif)

# 0 <= prev <= 100                                --> Memeriksa apakah prev berada dalam rentang 0 hingga 100 (inklusif)

# Operator not membalikkan nilai ekspresi dalam kurung. Jika ekspresi dalam kurung bernilai True, maka not akan membuatnya menjadi False, dan sebaliknya.

# Jika Pengguna Malakukan Input

"""
Jika nilai = 80 dan prev = 75:

0 <= 80 <= 100 adalah True.

0 <= 75 <= 100 adalah True.

True and True adalah True.

not True adalah False, sehingga kondisi tidak terpenuhi dan blok kode di dalamnya tidak akan dieksekusi

"""

"""
Jika nilai = 105 dan prev = 75:

0 <= 105 <= 100 adalah False.

0 <= 75 <= 100 adalah True.

False and True adalah False.

not False adalah True, sehingga kondisi terpenuhi dan blok kode di dalamnya akan dieksekusi.

"""


print("------")

# 10. Seleksi Kondisi Sebaris & Ternary

# One-Line / Sebaris

# Metode Penulisan Sebaris Ini Cocok Diterapkan Pada Situasi Dimana Seleksi Kondisi Hanya memiliki 1 Kondisi Saja

#string_input = input("Masukan Nilai: ") # --> Meminta pengguna memasukan nilai sebagai string
#nilai = int(string_input)               # --> Mengonversi variabel string_input menjadi integer

#if nilai >=0: print(True)               # --> Kondisi, memeriksa apakah nilai lebih besar dari atau sama dengan 0, jika kondisi terpenuhi maka akan mencetak True

#string_input = input("Masukan Nilai: ") # --> Meminta pengguna memasukan nilai sebagai string
#nilai = int(string_input)               # --> Mengonversi variabel_string menjadi integer

#if nilai < 0 : print(True)              # --> Kondisi, memeriksa apakah nilai kurang dari 0, jika kondisi terpenuhi maka akan mencetak True

# Ternary

# Metode Penulisan Ternary Umum Diterapkan Pada Blok Kode Seleksi Kondisi Yang Memiliki 2 Kondisi (True dan False)

#string_input = input("Masukan Nilai: ")     # --> Meminta pengguna memasukan nilai sebagai string
#nilai = int(string_input)                   # --> Mengonversi variabel string_input menjadi integer

#print(True) if nilai >= 0 else print(False) # --> Kondisi, memeriksa apakah nilai lebih besar atau sama dengan 0, jika kondisi terpenuhi maka akan mengeksekusi kode di dalamnya dan jika kondisi tidak terpenuhi maka akan melanjutkan ke kondisi berikutnya

# Ternary Dengan Nilai Balik

# Metode Penulisan Ini Sebenarnya Adalah Sama Seperti Penerapan Ternary Sebelumnya, Perbedaannya Pada Metode Ini Setiap Kondisi Menghasilkan Nilai Balik Yang Umumnya Ditampung Oleh Variabel

#string_input = input ("Memasukan nilai: ") # --> Meminta pengguna memasukan nilai sebagai string
#nilai = int(string_input)                  # --> Mengonversi variabel string_input menjadi integer

#pesan = True if nilai < 0 else False       # --> Kondisi, memeriksa apakah nilai kurang dari 0, ika kondisi terpenuhi maka akan mengeksekusi kode di dalamnya dan jika kondisi tidak terpenuhi maka akan melanjutkan ke kondisi berikutnya dan tersimpan pada variabel pesan
#print(pesan)                               # --> Mencetak variabel, jika kondisi benar atau terpenuhi, maka akan mencetak pesan "True"


print("------")

# 11. Pattern Matching

# Selain Keyword if, Python Menyediakan Keyword Lain Yaitu match Dan case Yang Kegunaannya Adalah Untuk Pattern Matching. Pattern Matching Sendiri Merupakan Teknik Seleksi Kondisi Yang Cukup Advance, Mendukung Banyak Variasi Pencocokan Pola