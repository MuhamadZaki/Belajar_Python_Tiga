# List Adalah Tipe Data Kolektif Yang Disimpan Secara Urut Dan Bisa Diubah Nilainya (Istilah Lainnya Adalah Tipe Data Sequence)
# Pada Bahasa Pemrograman Umumnya Ada Tipe Data Array. List Di Python Ini Memiliki Banyak Kemiripan Dengan Array, Bedanya list Bisa Berisi Data Dengan Berbagai Macam Tipe Data, Jadi Tidak Harus Sejenis Tipe Datanya.

# Urutan Elemen    : Terurut Sesuai Indeks
# Akses Elemen     : Menggunakan Indeks Dan Perulangan 
# Mutability       : Elemen Bisa Diubah
# Duplikasi Elemen : Elemen Bisa Diduplikat
# Tipe Data Eemen  : Bisa Sejenis, Maupun Berbeda Satu Sama Lain

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

# 4. Fungsi list()

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
print(a_list)              # --> Mencetak variabel, maka akan mencetak pesan [100, 0, -10] (agak aneh!) harusnya [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]

# Selain Metode Ini, Ada Juga Cara Lainnya Untuk Membuat list, Yaitu Menggunakan Metode list Comprehension


# Konversi string Ke list
# Selain Untuk Konversi Data range Ke list, Fungsi list() Bisa Digunakan Untuk Konversi Data string Ke List, Dengan Hasil Adalah Setiap Karakter string Menjadi Elemen list

a_string = "Zaki"         # --> Inisialisasi variabel yang menyimpan data string
a_list = list(a_string)   # --> Mengonversi variabel a_string menjadi sebuah list dan tersimpan pada variabel a_list
print(a_list)             # --> Mencetak variabel, maka akan mencetak pesan ['Z', 'a', 'k', 'i']


# Konversi tuple Ke list
# Tipe Data tuple Bisa Diubah Bentuknya Menjadi list Dengan Menggunakan Fungsi list()

a_tuple = (1,2,3,4,5)    # --> Inisialisasi variabel yang menyimpan data tuple, berisi 5 elemen data integer
a_list = list(a_tuple)   # --> Mengonversi variabel a_tuple menjadi sebuah list dan tersimpan pada variabel a_list
print(a_list)            # --> Mencetak variabel, maka akan mencetak pesan [1, 2, 3, 4, 5]


print("------")

# 5. Operasi Pada list
# Nilai Elemen list Bisa Diakses Menggunakan Notasi list[index]

a_list = [1,2,3,4,5,6]   # --> Inisialisasi variabel yang menyimpan data list, berisi 6 elemen data integer
elemenSatu = a_list[0]   # --> Mengambil elemen pertama dari a_list (indeks 0) dan tersimpan pada variabel elemenSatu
elemenDua = a_list[1]    # --> Mengambil elemen kedua dari a_list (indeks 1) dan tersimpan pada variabel elemenDua
elemenTiga = a_list[2]   # --> Mengambil elemen ketiga dari a_list (indeks 2) dan terismpan pada variabel elemenTiga
print(elemenSatu, elemenDua, elemenTiga) # --> Mencetak variabel, makan akan mencetak pesan 1 2 3

#  Jangan Gunakan Ini, Pengaksesan Elemen Menggunakan Index Di-Luar Kapasitas Data
#a_list = [1,2,3,4]
#a_list[2]
#print(a_list)


# Mengecek Apakah Elemen Ada
# Kombinasi Keyword if Dan in Bisa Digunakan Untuk Mengidentifikasi Apakah Suatu Elemen Merupakan Bagian Dari list Atau Tidak

a_list = [1,2,3,4,5]     # --> Inisialisasi variabel yang menyimpan data list, berisi 5 elemen data integer
a_int = 5                # --> Inisialisasi variabel yang menyimpan data integer

if a_int in a_list:                 # --> Kondisi, memeriksa apakah nilai variabel a_int terdapat pada variabel a-list, jika kondisi terpenuhi maka akan mengeksekusi kode di dalamnya dan jika kondisi tidak terpenuhi maka akan melajutkan ke kondisi berikutnya
    print(a_int, "Termasuk!")       # --> Jika kondisi benar atau terpenuhi, maka mencetak pesan Termasuk!

else:                               # --> Kondisi, jika kondisi sebelumnya tidak terpenuhi maka blok kode ini dieksekusi
    print(a_int, "Tidak termasuk!") # --> Jika kondisi salah atau tidak terpenuhi, maka mencetak pesan Tidak termasuk!



# Slicing list
# Merupakan Metode Pengaksesan list Menggunakan notasi slice, Notasi Ini Mirip Seperti array, Namun Mengembalikan Data Bertipe Tetap slice

a_list = [1,2,3,4,5,6]   # --> Inisialisasi variabel yang menyimpan data list, berisi 6 elemen data integer
a_slice = a_list[1:3]    # --> Membuat irisan, mencakup elemen dari indeks 1 hingga 2 (3 tidak termasuk)
print(a_slice)           # --> Mencetak variabel, maka akan mencetak pesan [2, 3]

a_list = [1,2,3,4,5,6]   # --> Inisialisasi variabel yang menyimpan data list, berisi 6 elemen data integer
a_slice = a_list[:4]     # --> Membuat irisan, mencakup elemen dari indeks 0 hingga 3 (4 tidak termasuk)
print(a_slice)           # --> Mencetak variabel, maka akan mencetak pesan [1, 2, 3, 4]

a_list = [1,2,3,4,5,6]   # --> Inisialisasi variabel yang menyimpan data list, berisi 6 elemen data integer
a_slice = a_list[3:]     # --> Membuat irisan, mencakutp elemen dari indeks 3 hingga akhir
print(a_slice)           # --> Mencetak variabel, maka akan mencetak pesan [4, 5, 6]

a_list = [1,2,3,4,5,6]   # --> Inisialisasi variabel yang menyimpan data list, berisi 6 elemen data integer
a_slice = a_list[:]      # --> Membuat irisan, mencakup semua elemen atau isi dari list
print(a_slice)           # --> Mencetak variabel, maka akan mencetak pesan [1, 2, 3, 4, 5, 6]

a_list = [1,2,3,4,5,6]   # --> Inisialisasi variabel yang menyimpan data list, berisi 6 elemen data integer
a_slice = a_list[::-1]   # --> Membuat irisan, mencakpt semua elemen atau isi dari list dengan urutan terablik (dari belakang kedepan)
print(a_slice)           # --> Mencetak variabel, maka akan mencetak pesan [6, 5, 4, 3, 2, 1]

a_list = [1,2,3,4,5,6]   # --> Inisialisasi variabel yang menyimpan data list, berisi 6 elemen data integer
a_slice = a_list[0::2]   # --> Membuat irisan, mencakup elemen indeks genap (0 2 4 dll)
print(a_slice)           # --> Mencetak variabel, maka akan mencetak pesan [1, 3, 5]

a_list = [1,2,3,4,5,6]   # --> Inisialisasi variabel yang menyimpan data list, berisi 6 elemen data integer
a_slice = a_list[1::2]   # --> Membuat irisan, mencakup elemen indeks ganjil (1 3 5 dll)
print(a_slice)           # --> Mencetak variabel, maka akan mencetak pesan [2, 4, 6]


# Mengubah Nilai Elemen list
# Cara Mengubah Nilai Element list Dengan Cara Mengakses Nilai Element Menggunakan Index, Kemudian Diikuti Operator assignment = Dan Nilai Baru

a_list = [1,2,3,4,5]    # --> Inisialisasi variabel yang menyimpan data list, berisi 5 elemen data integer
a_list[0] = 10          # --> Mengganti elemen pertama (indeks 0) dari variabel a_list dengan nilai 10
print(a_list)           # --> Mencetak variabel, maka akan mencetak pesan [10, 2, 3, 4, 5]


# Menambah Elemen append() Pada list
#Operasi append Atau Menambahkan Element Baru Setelah Index Terakhir, Bisa Menggunakan 2 Cara

# Menggunakan Method append()

a_list = [1,2,3,4,5]    # --> Inisialisasi variabel yang menyimpan data list, berisi 5 elemen data integer
a_list.append(6)        # --> Menambahkan elemen baru, setelah indeks terakhir
print(a_list)           # --> Mencetak variabel, maka akan mencetak pesan [1, 2, 3, 4, 5, 6]

# Menggunakan Slicing

a_list = [1,2,3,4,5]              # --> Inisialisasi variabel yang menyimpan data list, berisi 5 elemen data integer
a_list[len(a_list):] = [50], [60] # --> Menghitung panjang (jumlah elemen) dari a_list, lalu mengambil irisan dari a_list mulai dari indeks 5 (setelah elemen terakhir - karena ini irisan kosong, kita menambahkan elemen baru ke akhir list) hingga akhir list dan menambahkan 2 elemen
print(a_list)                     # --> Mencetak variabel, maka akan mencetak pesan [1, 2, 3, 4, 5, [50], [60]]

a_list = [1,2,3,4,5]              # --> Inisialisasi variabel yang menyimpan data list, berisi 5 elemen data integer
a_list[len(a_list):] = [50, 100]  # --> Menghitung panjang (jumlah elemen) dari a_list, lalu mengambil irisan dari a_list mulai dari indeks 5 (setelah elemen terakhir - karena ini irisan kosong, kita menambahkan elemen baru ke akhir list) hingga akhir list dan menambahkan 2 elemen
print(a_list)                     # --> Mencetak variabel, maka akan mencetak pesan [1, 2, 3, 4, 5, 50, 100]


# Extend/concat/union Element
#Operasi extend (Atau concat / union) Adalah Operasi Penggabungan Dua Data list dan Ada Beberapa Metode Yang Tersedia
