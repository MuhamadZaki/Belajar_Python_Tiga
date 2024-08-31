# List Adalah Tipe Data Kolektif Yang Disimpan Secara Urut Dan Bisa Diubah Nilainya (Istilah Lainnya Adalah Tipe Data Sequence)
# Pada Bahasa Pemrograman Umumnya Ada Tipe Data Array. List Di Python Ini Memiliki Banyak Kemiripan Dengan Array, Bedanya list Bisa Berisi Data Dengan Berbagai Macam Tipe Data, Jadi Tidak Harus Sejenis Tipe Datanya.

# 1. Pengenalan list
# Deklarasi  Atau Inisialisasi Variabel Dan Data list Adalah Menggunakan Literal list Dengan Notasi 

# List Dengan Satu Tipe Data

a_list = [1,2,3]                        # --> Inisialisasi variabel yang menyimpan data list, berisi 3 elemen data integer
print(a_list)                           # --> Mencetak variabel, maka akan mencetak pesan [1,2,3]
print(type(a_list))                     # --> Mencetak variabel dan mengecek tipe data, maka mencetak pesan <class 'list'>

# Deklarasi Elemen list Secara Vertikal

a_list = [
    "satu",
    "dua",
    "tiga"
]                                       # --> Inisialisasi variabel yang menyimpan data list, berisi 3 elemen data string
print(a_list)                           # --> Mencetak variabel, maka akan mencetak pesan ['satu', 'dua', 'tiga']
 
# List Yang Berisi Elemen Beberapa Tipe Data

a_list = [3.14, "satu", 2, True, False] # --> Inisialisasi variabel yang menyimpan data list, berisi 5 elemen data float, string, integer, boolean
print(a_list)                           # --> Mencetak variabel, maka akan mencetak pesan [3.14, 'satu', 2, True, False]

# List Kosong

a_list = []                             # --> Inisialisasi variabel yang menyimpan data list, berisi elemen kosong
print(a_list)                           # --> Mencetak variabel, maka akan mencetak pesan []

# Data Dalam list Bisa Disebut Dengan Elemen, Setiap Elemen Disimpan Dalam list Secara Terurut Dengan Penanda Urutan Yang disebut Index Dan Nilai Indek Dimulai Dari Angka 0

a_list = [10, 20, 30, 40, 50]           # --> Inisialisasi variabel yang menyimpan data list, berisi 5 elemen data integer
results = a_list[0]                     # --> Mengambil elemen pertama dari a_list (indeks 0) dan tersimpan dalam variabel results
print(results)                          # --> Mencetak variabel, maka akan mencetak pesan [10]


print("------")

# 2. Perulangan list
# List Adalah Salah Satu Tipe Data Yang Dapat Digunakan Langsung Pada Perulangan for

a_list = [10, 20, 30]  # --> Inisialisasi varibel yang menyimpan data list, berisi 3 elemen data integer

for ls in a_list:      # --> Perulangan atau loop, mengiterasi melalui setiap elemen dalam a_list (variabel ls akan mengambil nilai dari setiap elemen selama iterasi)
    print(ls)          # --> Mencetak variabe setiap iterasi, maka akan mencetak pesan 10, 20, 30
    print(type(ls))    # --> Mencetak variabel dan mengecek tipe data, maka mencetak pesan <class 'int'> <class 'int'> <class 'int'>

# Selain Itu, Perulangan list Bisa Juga Dilakukan Menggunakan Index

a_list = [10, 20, 30, 40]           # --> Inisialisasi variabel yang menyimpan data list, berisi 4 elemen data integer

for index in range(0, len(a_list)): # --> Perulangan atau loop, mencakup indeks 0 hingga panjang atau jumlah elemen a_list 
    print(index, a_list[index])     # --> Mencetak variabel, maka akan mencetak pesan 0 10 1 20 230 3 40

# Fungsi enumerate()
# Digunakan Untuk Membuat Data Sequence Menjadi Data enumerasi, Yang Jika Dimasukan Ke Perulangan Di Setiap Iterasinya Bisa Kita Akses Index Beserta Element-nya

a_list = [10, 20, 30]               # --> Inisialisasi variabel yang menyimpan data list, berisi 3 elemen data integer

for i, e in enumerate(a_list):      # --> Perulangan atau loop, mengiterasi melalui setiap elemen dalam a_list dan mengembalikan pasangan indeks dan nilai dari setiap elemen dalam a_list
    print(i, e)                     # --> Mencetak variabel, maka akan mencetak pesan 0 10 1 20 2 30


print("------")

# 3. Nested list

matrix = [
    [0, 1, 0, 1, 0],
    [1, 1, 1, 0, 0],
    [0, 0, 0, 1, 1],
    [0, 1, 1, 1, 0],
]                                   # --> Inisialisasi variabel yang menyimpan data list, berisi 4 baris 5 kolom dengan elemen data integer

for baris in matrix:                # --> Perulangan atau loop, mengiterasi melalui setiap baris dalam matrix
    for cel in baris:               # --> Perulangan atau loop bersarang, mengiterasi melalui setiap elemen dalam baris tersebut
        print(cel, end=" ")         # --> Menceta variabel dengan spasi sebagai pemisah (tanpa newline)
    print()                         # --> Mencetak pesan newline (baris baru) setelah mencetak variabel


print("------")

# Fungsi list()

# Konversi range Ke list
# Data range (Hasil Pemanggilan Fungsi range()) Bisa Dikonversi Ke Bentuk list Menggunakan Fungsi list() Dan Cara Ini Cukup Efisien Untuk Pembuatan Data list Yang Memiliki Pattern Atau Pola

a_range = range(6)         # --> Membuat sebuah range, rentang dari angka 0 hingga 5 dan tersimpan pada variabel a_range
a_list = list(a_range)     # --> Mengonversi variabel a_range menjadi sebuah list dan tersimpan pada variabel a_list
print(a_list)              # --> Mencetak variabel, maka akan mencetak pesan [0,1,2,3,4,5]

a_range = range(1, 6)      # --> Membuat sebuah range, rentang dari angka 1 hingga 5 dan tersimpan dalam variabel results
a_list = list(a_range)     # --> Mengonversi variabel a_range menjadi sebuah list dan tersimpan pada variabel a_list
print(a_list)              # --> Mencetak variabel, maka akan mencetak pesan [1, 2, 3, 4, 5]

a_range = range (0, 14, 3) # --> Membuat sebuah range, rentang dari angka 0 hingga 13 dengan langkah sebesar 3 dan tersimpan pada variabel a_range
a_list = list(a_range)     # --> Mengonversi variabek a_range menjadi sebuah list dan tersimpan pada variabel a_list
print(a_list)              # --> Mencetak variabel, maka akan mencetak pesan [0, 3, 6, 9, 12]

a_range = (100, 0, -10)    # --> Membuat sebuah range, rentang dari angka 100 hingga 0 dengan langkah sebesar -10 dan tersimpan pada variabel a_range
a_list = list(a_range)     # --> Mengonversi variabel a_range menjadi sebuah list dan tersimpan pada variabel a_list
print(a_list)              # --> mencetak variabel, maka akan mencetak pesan [100, 0, -10] (agak aneh!) harusnya [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]

# Selain Metode Ini, Ada Juga Cara Lainnya Untuk Membuat list, Yaitu Menggunakan Metode list Comprehension


print("------")

# Konversi string Ke list

