# Tuple Merupakan Tipe Data Sequence Yang Ideal Digunakan Untuk Menampung Nilai Kolektif yang isinya Tidak Akan Berubah (Immutable), Berbeda Dengan list yang cocok Untuk Data Yang Bisa Berubah Nilai atau Elemennya (Mutable)

# Urutan Elemen    : Terurut Sesuai Indeks
# Akses Elemen     : Menggunakan Indeks Dan Perulangan 
# Mutability       : Elemen Tidak Bisa Diubah
# Duplikasi Elemen : Elemen Bisa Diduplikat
# Tipe Data Eemen  : Bisa Sejenis, Maupun Berbeda Satu Sama Lain

# 1 . Pengenalan tuple
# Deklarasi Atau Inisialisasi tuple Menggunakan Literal () Dengan Delimiter Tanda Koma ,
# Tuple bisa menampung element yang tipe datanya bisa sejenis atau tidak, sama seperti list

a_tuple = (1,2,3, "Zaki", True) # --> Inisialisasi variabel yang menyimpan data tuple, berisi 5 elemen data integer, string dan boolean
print(a_tuple)                  # --> Mencetak variabel, maka akan mencetak pesan (1, 2, 3, 'Zaki', True)
print(len(a_tuple))             # --> Mencetak variabel dan menghirung panjang atau jumlah elemen dari a_tuple, maka akan mencetak pesan 5
print(type(a_tuple))            # --> Mencetak variabel dan mengecek tipe data, maka akan mencetak pesan <class 'tuple'>



print("------")

# 2. Mengakses Element tuple Menggunakan index
# Element tuple Bisa Diakses Menggunakan Notasi tuple[index]
# Pengaksesan Elemen Menggunakan index Di Luar Kapasitas Data Akan Menyebabkan Error

a_tuple = (1,2,3,4,5)           # --> Inisialisasi variabel yang menyimpan data tuple, berisi 5 elemen data integer
results = a_tuple[4]            # --> Mengakses elemen menggunakan index dan tersimpan pada variabel results
print(results)                  # --> Mencetak variabel, maka akan mencetak pesan 5


print("------")

# 3. Perulangan tuple
# Tuple Merupakan Salah Satu Tipe Data Yang Bisa Digunakan Secara langsung Pada Perulangan Menggunakan Keyword for

a_tuple = (1,2,3,4,5)   # --> Inisialisasi variabel yang menyimpan data tuple, berisi 5 elemen data integer
for e in a_tuple:       # --> Perulangan atau loop, mengiterasi melalui setiap element e dalam variabel a_list 
    print(e)            # --> Mencetak variabel setiap iterasi, maka akan mencetak pesan 1,2,3,4,5


# Perulangan Di Ekuvalen

a_tuple = (1,2,3,4,5)            # --> Inisialisasi variabel yang menyimpan data tuple, berisi 5 elemen data integer
for i in range(0, len(a_tuple)): # --> Perulangan atau loop, mengiterasi nilai i mulai rentang 0 hingga panjang a_tuple 
    print(i, a_tuple[i])         # --> Mencetak variabel dan mencetak index juga elemen dari a_tuple, maka akan mencetak pesan  01 12 23 34 45


# Fungsi enumerate()
# Fungsi Ini Digunakan Untuk Membuat Data Sequence Menjadi Data enumrasi, Yang Jika Dimasukan Ke Perulangan Di Setiap Iterasinya Bisa Kisa Akses Index Berserta Elemennya

a_tuple = (1,2,3,4,5)            # --> Inisialisasi variabel yang menyimpan data tuple, berisi 5 elemen data integer

for i, n in enumerate(a_tuple):  # --> Perulangan atau loop, mengiterasi setiap index dan elemen dari a_tuple
    print(i, n)                  # --> Mencetak variabel dan mencetak index juga elemen dari a_tuple, maka akan mencetak pesan 01 12 23 34 45


print("------")

#  4. Mencek Apakah Elemen Ada Pada tuple
# Kombinasi keyword if Dan in Bisa Digunakan Untuk Mengidentifikasi Apakah Suatu Element Merupakan bagian Dari tuple Atau Tidak

a_tuple = (1,2,3,4,5)  # --> Inisialisasi variabel yang menyimpan data tuple, berisi 5 elemen data integer
e = 1                  # --> Inisialisasi variabel yang menyimpan data integer

if e in a_tuple:       # --> Kondisi, memerikasa apakah nilai e, terdapat pada variabel a_tuple, jika kondisi terpenuhi maka akan mengeksekusi kode di dalamnya dan jika kondisi tidak terpenuhi maka akan melanjutkan ke kondisi berikutnya
    print(True)        # --> Jika kondisi benar atau terpenuhi, maka akan mencetak pesan True
else:                  # --> Kondisi, jika kondisi sebelumnya tidak terpenuhi maka blok kode ini dieksekusi
    print(False)       # --> Jika kondisi salah atau tidak terpenuhi, maka akan mencetak pesan False


print("------")

# Nested tuple
# Dibuat Dengan Menuliskan Data tuple Sebagai ELemen tuple
# Penulisan data literal nested tuple bisa dalam bentuk horizontal atau vertikal

a_tuple = ((0,1), (1,1), (2,2), (3,3)) # --> Inisialisasi variabel yang menyimpan data tuple, berisi 4 sub tuple

for row in a_tuple:                    # --> Perulangan atau loop, mengiterasi setiap row dari a_tuple
    for cell in row:                   # --> Perulangan bersarang, mengiterasi melalui setiap index dan elemen cell
        print(cell, end=" ")           # --> Menceta variabel dengan spasi sebagai pemisah (tanpa newline)
    print()                            # --> Mencetak pesan newline (baris baru) setelah mencetak variabel

# Horizontal

a_tuple = ((0,1), (1,1), (2,2), (3,3)) # --> Inisialisasi variabel yang menyimpan data tuple, berisi 4 sub tuple

# Vertikal

a_tuple = (
    (0,1),
    (1,1),
    (2,2),
    (3,3)
)                                      # --> Inisialisasi variabel yang menyimpan data tuple, berisi 4 sub tuple



print("------")

# 5. List Dan tuple
# Tipe Data list Dan tuple Umum Dikombinasikan, Keduanya Sangat Mirip Tapi Memiliki Perbedaan Yang Jelas, Yaitu Nilai tuple Tidak Bisa Dimodifikasi Sedangkan list Bisa

# Deklarasi Atau Inisialisasi Data list Berisi Elemen tuple

data = [
    ("Meow", 18, False, ["satu", "dua"])
]                                        # --> Inisialisasi vairabel yang menyimpan data list, berisi data tuple

# append tuple Ke list

data.append((
    "Semlohe",
    10,
    True,
    ["Indah", "Sekali"]
))                                       # --> Menambakkan tupel ke dalam vairbel data


for row in data:                         # --> Perulangan atau loop, mengiterasi melalui setiap row (tuple) dalam data
    for cell in row:                     # --> Perulangan bersarang, Mengiterasi melalui setiap elemen cell dalam row (tuple)
        print(cell, end=" ")             # --> Menceta variabel dengan spasi sebagai pemisah (tanpa newline)
    print()                              # --> Mencetak pesan newline (baris baru) setelah mencetak variabel



print("------")

# 6. Fungsi tuple()
# Fungsi Ini Bisa Digunakan Untuk Konversi Data string Ke tuple dan Dan Hasilnya Nilai tuple Dengan Elemen Berisi Setiap Karakter Yang Ada Di string

sudahlah = tuple("Mahkota") # --> Inisialisasi varaiabel yang menyimpan data tuple, berisi elemen data string
print(sudahlah)             # --> Mencetak variabel, maka akan mencetak pesan ('M', 'a', 'h', 'k', 'o', 't', 'a')

# mengonversi list Ke tuple
# Ini Bisa Dilakukan Dengan Mudah Menggunakan fungsi tuple()

nums = tuple([1,2,3,4,5])   # --> Inisialisasi variabel yang menyimpan data tuple, berisi data list
print(nums)                 # --> Mencetak variabel, maka akan mencetak pesan (1, 2, 3, 4, 5)

# Mengonversi range ke tuple
# range Juga Bisa Dikonversi Ke tuple Menggunakan Fungsi tuple()

r = range(0, 3)             # --> Inisialisasi variabel yang menyimpan rentang nilai 0 hingga 2
r_tuple = tuple(r)          # --> Mengonversi rentang dengan fungsi tuple, agar menjadi data tuple
print(r_tuple)              # --> Mencetak variabel, maka akan mencetak pesan (0, 1, 2)



print("------")

# 7. Tuple packing Dan unpacking

# Tuple packing
# Packing Merupakan Istilah Untuk Menggabungkan Beberapa Data Menjadi Satu Data Kolektif
# Tulis Saja Data Atau Variabel Yang Ingin Di-pack Dalam Notasi tuple, Kemudian Gunakan Sebagai Nilai Pada Operasi assignment
# Penulisan tuple Boleh Juga Dituliskan Tanpa Menggunakan karkter () Dan Pastikan Berhati-Hati, Bisa Jadi Salah Paham Karena Metode ini Pada Saat Menggunakan tuple Sebagaii Nilai Argumen Pemanggil fungsi, Karena Intrepreter Akan Menganggapnya Sebagai banyak Argumen!

satu = "Natashia"             # --> Inisialisasi variabel yang menyimpan data string
dua = 12                      # --> Inisialisasi variabel yang menyimpan data intager
tiga = True                   # --> Inisialisasi variabel yang menyimpan data boolean

# Menggunakan ()
row_data = (satu, dua, tiga)  # --> Menggabungkan variabel ke dalam sebuah tuple dan tersimpan pada variabel row_data

# Tidak Menggunakan ()
row_data = satu, dua, tiga    # --> Menggabungkan variabel ke dalam sebuah tuple dan tersimpan pada variabel row_data
print(row_data)               # --> Mencetak variabel, maka akan mencetak pesan ('Natashia', 12, True)


# Tuple unpacking
# Unpacking Merupakan Istilah Untuk Menyebar Isi Suatu Data kolektif Ke Beberapa Variabel Dan unpacking Merupakan Kebalikan Dari unpacking

row_data = ("Laura", 17, True)  # --> Inisialisasi variabel yang menyimpan data tuple, berisi 3 elemen data string, integer dan boolean

name, age, yes = row_data       # --> Mengambil nilai atau elemen dari variabel row_data (tuple), dan menetapkannya ke variabel terpisah
print(name, age, yes)           # --> Mencetak variabel, maka akan mencetak pesan Laura 17 True



print("------")

# Tuple Kosong
# Tuple Bisa Saja Tidak Berisi Apapun, Contoh Data (), Yang Cukup Umum Digunakan Untuk Mempresentasikan data Kolektif Yang Isinya Bisa Saja Kosong

empty_tuple = ()    # --> Inisialisasi variabel yang menyimpan data tuple, berisi elemen kosong
print(empty_tuple)  # --> Mencetak variabel, maka akan mencetak pesan ()

# Berikut Proses Penerapannya, Misalkan Ada Data Kolektif Yang Didapat Dari Database Berbentuk Array Object Dan Data Tersebut Perlu Disimpan Oleh Variabel list, Yang elemennya Adalah tuple Dengan Spesifikasi

# Tuple Elemen index 0 Berisi nama
# Tuple Elemen index 1 Berisi age
# Tuple Elemen index 2 Berisi yes
# Tuple Elemen index 3 Berisi kimochi, Dimana kimochi Bisa Saja Kosong

my_data = [
    ("Meow", 18, True, ("satu", "dua")),
    ("Gug", 17, True, ("Tiga", "Empat")),
    ("Kimochiah", 10, False, ())
]

# Bisa Dilihat Dari my_data kimochiah Tidak Memiliki kimochi, Karena Terisi Dengan Nilai tuple () 