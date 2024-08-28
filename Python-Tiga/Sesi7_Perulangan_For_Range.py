# Perulanga Atau Loop Merupakan Teknik Untuk Mengulang-Ulang Eksekusi Suatu Blok Kode, Atau Mengitrasi Elemen Milik Tipe Data Kolektif Seperti List Dan Lain-Lain

# 1. Keyword for Dan Fungsi range()

# Perulangan Di Python Bisa Dibuat Menggunakan Kombinasi Keyword for Dan Fungsi range()
# Keyword for Adalah Keyword Untuk Perulangan, Dalam Penerapannya Diikuti Dengan Keyword in
# Fungsi range() Digunakan Untuk Membuat Object range, Yang Umumnya Dipakai Sebagai Kontrol Perulangan

for index in range(6): # --> Inisialisasi perulangan, yang melakukan iterasi sebanya 6 kali (variabel index digunakan sebagai penghitung iterasi dan ada setiap iterasi, nilai index akan berubah)
    print(index)       # --> Mencetak variabel pada setiap iterasi, maka mencetak pesan 0 1 2 3 4 5

# Statement print(index) Muncul 6 Kali, Karena Perulangan Dilakukan Dengan Kontrol range(6) Dimana Statement Tersebut Menghasilkan Object range Dengan Isi Deret Angka Sejumlah 6 Dimulai Dari Angka 0 Hingga 5
# Statement for index in range(6): Adalah Contoh Penulisan Perulangan Menggunakan for dan range(). Variabel a Berisi Nilai Counter Setiap Iterasi, Yang Pada Konteks Ini Adalah Angka 0 Hingga 5
# Statement print(index) Wajib Ditulis Menjorok Ke Kanan Karena Merupakan Isi Dari Blok Perulangan for imdex in range(6):


# Fungsi list()

# Fungsi range() Menghasilkan Object Sequence, Yaitu Jenis Data Yang Strukturnya Mirip Seperti list (Tapi Bukan list) Yang Kegunaan Utamanya Adalah Untuk Kontrol Perulangan

# Object Sequence Bisa Dikonversi Bentuk list Dengan Cara Dibungkus Menggunakan Fungsi list()

a_range = range(6)      # --> Menghitung dari 0 hingga 5 dan tersimpan pada variabel a_range
results = list(a_range) # --> Mengonversi object a_range menjadi sebuah list
print(results)          # --> Mencetak variabel, maka mencetak pesan [0,1,2,3,4,5]
print(type(results))    # --> Mencetak variabel dan mengecek tipe data, maka mencetak pesan <class 'list'>


print("------")

# 2. Penerapan fungsi range()

# Statement range(n) Menghasilkan Data range Sejumlah n Yang Isinya Dimulai Dari Angka 0. Syntax range(n) Adalah Bentuk Paling Sederhana Penerapan Fungsi Ini

# Selain range(n) Ada Juga Beberapa Cara Penulisan Lainnya:
# Menggunakan range(start, stop), Hasilnya Data range Dimulai Dari start Dan Hingga stop -1. Sebagai Contoh range(1,6) Menghasilkan Data range [1,2,3,4,5]
# Mengunakan renge(start, stop, step), Hasilnya Data range Dimulai dari strat Dan Hingga stop -1, Dengan Nilai Increment Sejumlah step. Sebagai Contoh, range(1, 10, 3) Menghasilkan Data range [1, 4, 7]

# range(nilai)

for index in range(4):         # --> Inisialisasi perulangan, yang melakukan iterasi sebanyak 4 kali (variabel index digunakan sebagai penghitung iterasi dan ada setiap iterasi, nilai index akan berubah)
    print(index)               # --> Mencetak variabel pada setiap iterasi, maka mencetak pesan 0 1 2 3
    

# range(start, stop)

for index in range(1, 4):      # --> Inisialisasi perulangan, yang melakukan iterasi dari angka 1 hingga 3 (variabel index digunakan sebagai penghitung iterasi dan ada setiap iterasi, nilai index akan berubah)
    print(index)               # --> Mencetak variabel pada setiap iterasi, maka mencetak pesan 1 2 3

# range(start, stop, step)

for index in range(0, 6, 2):   # --> Inisialisasi perulangan, yang melakukan itersi dari angka 0 hingga 5 dengan langkah sebesar 2 (variabel index digunakan sebagai penghitung iterasi dan ada setiap iterasi, nilai index akan berubah)
    print(index)               # --> Mencetak variabel pada setiap iterasi, maka mencetak pesan 0 2 4

print("---")
for index in range(6, -6, -1): # --> Inisialisasi perulangan, yang melakukan iterasi dari angka 6 hingga -5 dengan langkah sebesar -1 (variabel index digunakan sebagai penghitung iterasi dan ada setiap iterasi, nilai index akan berubah)
    print(index)               # --> Mencetak variabel pada setiap iterasi, maka mencetak pesan 6 5 4 3 2 1 0 -1 -2 -3 -4 -5


print("------")

# 3. Iterasi Elemen Data Kolektif

# Perulangan Menggunakan for Bisa Dilakukan Pada Beberapa Jenis Tipe Data (Seperti list, string, tuple, dan lainnya) Caranya Dengan Langsung Menuliskan Saja Variabel Atau Data Tersebut Pada Statement for
# Tipe Data Yang Bisa Digunakan Pada Keyword for Biasa Disebut Dengan Tipe iterator

# Iterasi Data List

pesan_list = ["Zaki", 26]    # --> Inisialisasi variabel yang menyimpan data list, berisi 2 elemen data string dan integr (yang akan di itersi)
for p in pesan_list:         # --> Melakukan perulangan atau loop melalui setip elemen dalam list pesan_list (variabel p digunakan untuk menyimpan nilai setiap elemen selama iterasi)
    print(p)                 # --> Mencetak variabel pada setiap iterasi, maka mencetk pesan Zaki 26
    print(type(p))           # --> Mencetak variabel pada setiap iterasi dan mengecek tipe data, maka mencetak pesan <class 'str'> <class 'int'>

# Iterasi Data Tuple

pesan_tuple = ("Zaki", 26)   # --> Inisialisasi variabel yang menyimpan data tuple, besiri 2 elemen data string dan integer (yang akan di iterasi)
for p in pesan_tuple:        # --> Melakukan perulangan atau loop melalui setiap elemen dalam tuple pesan_tuple (variabel p digunakan untuk menyimpan nilai setiap elemen selama iterasi)
    print(p)                 # --> Mencetak variabel pada setiap iterasi, maka mencetak pesan Zaki 26
    print(type(p))           # --> Mencetak variabel pada setiap iterasi dan mengecek tipe data, maka mencetak pesan <class 'str'> <class 'int'>

# Iterasi Data String

pesan_string = "Natashia"    # --> Inisialisasi variabel yang menyimpan data string (yang akan di iterasi)
for char in pesan_string:    # --> Melakukan perulangan atau loop melalui setiap karakter dalam string pesan_string (variabel char digunakan untuk menyimpan karakter setiap iterasi)
    print(char)              # --> Mencetak variabel pada setiap iterasi, maka mencetak pesan Natashia
    print(type(char))        # --> Mencetak variabel pada setiap iterasi dan mengecek tipe data, maka mencetak pesan <class 'str'>

# Iterasi Data Dictionary
# Penggunaan Keyword for Pada Tipe Data dict Akan Mengiterasi key-nya. Dari key Tersebut Value Bisa Diambil Dengan Mudah Menggunakan Notasi dict[key]

pesan_dict = {
    "nama":"Laura",
    "umur": 17
}                               # --> Inisialisasi variabel yang menyimpan data dict, berisi 2 key-value (yang akan di iterasi)
for key in pesan_dict:          # --> Melakukan perulangan atau loop melalui setiap key dalam dictionary pesan_dict (variabel key digunakan untuk menyimpan key setiap iterasi)
    print(key, pesan_dict[key]) # --> Mencetak variabel pada setiap iterasi, maka mencetak pesan nama Laura umur 17
    print(type(key))            # --> Mencetak variabel pada setiap iterasi dan mengecek tipe data, maka mencetak pesan <class 'str'> <class 'str'>

 
# Iterasi Data Set
pesan_set = {"Jaki", 25}        # --> Inisialisasi variabel yang menyimpan data set, berisi 2 elemen data string dan integer (yang akan di iterasi)
for p in pesan_set:             # --> Melakukan perulangan atau loop melalui setiap elemen dalam set pesan_set (variabel p digunakan untuk menyimpan nilai setiap elemen selama iterasi)
    print(p)                    # --> Mencetak variabel pada setiap iterasi, maka mencetak pesan Jaki 25 (posisi berubah setiap dijalankan)
    print(type(p))              # --> Mencetak variabel pada setiap iterasi dan mengecek tipe data, maka mencetak pesan <class 'str'> <class 'int'>


print("------")

# 4. Perulangan Bercabang / Nested for
# Cara Penerapan Nested Loop Adalah Cukup Dengan Menuliskan Statement for Sebagai Isi Dari Statement for Atasnya


string_input = input("Masukan jumlah *: ") # --> Meminta pengguna memasukan nilai sebagai string
stars = int(string_input)                  # --> Mengonversi variabel string_input menjadi integer

for index in range(stars):                 # --> Inisialisasi perulangan atau loop dan melakukan iterasi sebanyak nilai yang dimasukan oleh pengguna
    for j in range(0, stars - index):      # --> Perulangan bersarang, inisialisasi perulangan atau loop kedua dengan jumlah yang berkurang setiap iterasi
        print("*", end=" ")                # --> Mencetak karakter *, dengan spasi sebagai pemisah (tanpa new-line)
    print()                                # --> Mencetak new-line (baris baru) setelah mencetak bintang sejumlah yang sesuai


# Parameter Opsional end Pada Fungsi print()
# Fungsi print() Memiliki Parameter Opsional Bernama end, Kegunaannya Untuk Mengubah Karakter Akhir Yang Muncul Setelah Data String Di-print. Default Nilai Paramter end Ini Adalah \n Atau Karakter Baris Baru, Itulah kenapa Setiap Selesai print Pasti Ada Baris Baru
# Statement print("*", end=" ") Akan Menghasilkan Pesan * Yang Di-Akhiri Dengan Karakter Spasi Karena Nilai Parameter end Di-set Dengan Nilai Karakter Spasi


# Fungsi print() Tanpa Parameter
# Pemanggilan Fungsi print() Argument/Parameter Menghasilkan Baris Baru
