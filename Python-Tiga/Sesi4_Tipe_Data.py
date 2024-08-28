# Python Mengenal Cukup Banyak Tipe Data, Mulai Dari Yang Built-In (Bawaan) Maupun Custom Type. Pada Chapter Ini Kita Akan Mempelajari High-Level Overview Tipe-Tipe Tersebut.

# Tipe Data Numrik

# 1. Integer --> Menamoung Bilangan Bulat
# 2. Float   --> Menampung Bilangan Desimal Atau Floating Point
# 3. complex --> Menampung Nilai Berisi Kombinasi Bilangan Real Dan Imajiner

# Tipe Data

# 1. Tipe Data String Atau str

# Menggunakan Tanda Petik Dua "", '' (Sebaris) Dan """ """. ''' ''' (Multi-baris)

a_string = "Laura"    # --> Inisialisasi variabel yang menyimpan data string sebaris
print(a_string)       # --> Mencetak variabel, maka mencetak pesan Laura
print(type(a_string)) # --> Mencetak variabel dan mengecek tipe data, maka mencetak pesan <class 'str'>

a_string = 'Laura'    # --> Inisialisasi variabel yang menyimpan data string sebaris
print(a_string)       # --> Mencetak variabel, maka mencetak pesan Laura
print(type(a_string)) # --> Mencetak variabel dan mengecek tipe data, maka mencetak pesan <class 'str'>

a_string = """
Satu baris
Dua baris
Tiga baris
"""                   # --> Inisialisasi variabel yang menyimpan data string multi-baris
print(a_string)       # --> Mencetak variabel, maka mencetak pesan Satu baris Dua baris Tiga baris
print(type(a_string)) # --> Mencetak variabel dan mengecek tipe data, maka mencetak pesan <class 'str'>

a_string = '''
Satu baris
Dua baris
Tiga baris  
'''                   # --> Inisialisasi variabel yang menyimpan data string multi-baris
print(a_string)       # --> Mencetak variabel, maka mencetak pesan Satu baris Dua baris Tiga baris
print(type(a_string)) # --> Mencetak variabel dan mengecek tipe data, maka mencetak pesan <class 'str'>


print("------")

# 2. Tipe Data Boolean

# Literal Untuk Tipe Data Boolean adalah True Untuk Nilai Benar, Dan False Untuk Nilai Salah.

a_boolean = True       # --> Inisialisasi variabel yang menyimpan data boolean
print(a_boolean)       # --> Mencetak variabel, maka mencetak pesan True
print(type(a_boolean)) # --> Mencetak variabel dan mengecek tipe data, maka mencetak pesan <class 'bool'>

b_boolean = False      # --> Inisialisasi variabel yang menyimpan data boolean
print(b_boolean)       # --> Mencetak variabel, maka mencetak pesan False
print(type(a_boolean)) # --> Mencetak variabel dan mengecek tipe data, maka mencetak pesan <class 'bool'>


print("------")

# 3. Tipe Data None

# Tipe Data None Merepresentasikan Nilai Kosong (Seperti Nilai Null Atau Nil). 

a_none = None          # --> Inisialisasi variabel yang menyimpan data boolean
print(a_none)          # --> Mencetak variabel, maka mencetak pesan None
print(type(a_none))    # --> Mencetak variabel dan mengecek tipe data, maka mencetak pesan <class 'NoneType'>


print("------")

# 4. Tipe Data List

# Urutan Elemen    : Terurut Sesuai Indeks
# Akses Elemen     : Menggunakan Indeks Dan Perulangan 
# Mutability       : Elemen Bisa Diubah
# Duplikasi Elemen : Elemen Bisa Diduplikat
# Tipe Data Eemen  : Bisa Sejenis, Maupun Berbeda Satu Sama Lain

a_list = [1,2,3]                 # --> Inisialisasi variabel yang menyimpan data list, berisi 3 elemen data integer
print(a_list)                    # --> Mencetak variabel, maka mencetak pesan [1,2,3]
print(type(a_list))              # --> Mencetak variabel dan mengecek tipe data, maka mencetak pesan <class 'list'>

a_list = ["Kucing", "Ikan"]      # --> Inisialisasi variabel yang menyimpan data list, berisi 3 elemen data integer
print(a_list)                    # --> Mencetak variabel, maka mencetak pesan ['Kucing', 'Ikan']

a_list = [18, "Ikan", False]     # --> Inisialisasi variabel yang menyimpan data list, berisi 3 elemen data integer, string, dan boolean
print(a_list)                    # --> Mencetak variabel, maka mencetak pesan [18, 'Ikan', False]

# Akses Elemen List
a_list = [1,2,3]                 # --> Inisialisasi variabel yang menyimpan data list, berisi 3 elemen data integer
results = a_list[0]              # --> Mengambil elemen pertama dari list, dan tersimpan pada variabel results
print(results)                   # --> Mencetak variabel, maka mencetak pesan 1


print("------")

# 5. Tipe Data Tuple

# Urutan Elemen    : Terurut Sesuai Indeks
# Akses Elemen     : Menggunakan Indeks Dan Perulangan 
# Mutability       : Elemen Tidak Bisa Diubah
# Duplikasi Elemen : Elemen Bisa Diduplikat
# Tipe Data Eemen  : Bisa Sejenis, Maupun Berbeda Satu Sama Lain

a_tuple = (1,2,3)                # --> Inisialisasi variabel yang menyimpan data tuple, berisi 3 elemen data integer
print(a_tuple)                   # --> Mencetak variabel, maka mencetak pesan (1,2,3)
print(type(a_tuple))             # --> Mencetak variabel dan mengecek tipe data, maka mencetak pesan <class 'tuple'>

a_tuple = ("Natashia", "Laura")  # --> Inisialisasi variabel yang menyimpan data tuple, berisi 2 elemen data string
print(a_tuple)                   # --> Mencetak variabel, maka mencetak pesan ('Natashia', 'Laura')

a_tuple = (5, "Zaki", True)      # --> Inisialisasi variabel yang menyimpan data tuple, berisi 2 elemen integer, string, dan boolean
print(a_tuple)                   # --> Mencetak variabel, maka mencetak pesan (5, 'Zaki', True)

# Akses Elemen Tuple

a_tuple = (1,2,3)                # --> Inisialisasi variabel yang menyimpan data tuple, berisi 3 elemen data integer
results = a_tuple[2]             # --> Mengambil elemen ketiga dari tuple, dan tersimpan pada variabel results
print(results)                   # --> Mencetak variabel, maka mencetak pesan 3



print("------")

# 6. Tipe Data Dictionary

# %s Untuk String (a_string)
# %d Untuk Integer (a_integer)
# %.1f Untuk Float Dengan Satu Angka Desimal (a_float)
# %f Untuk Float standar (a_float)
# %r Untuk Representasi Objek (a_boolean)

# Tipe Data Dict Atau Dictionary Berguna Untuk Menyimpan Data Kolektif Terstruktur Berbentuk Key-Value

a_dict = {
    "nama":"Zaki",
    "male":False,
    "umur":25,
    "hobi":["Baca", "Belajar"]
}                               # --> Inisialisasi variabel yang menyimpan data dict, berisi 4 key-value
print(a_dict)                   # --> Mencetak variabel, maka mencetak pesan {'nama': 'Zaki', 'male': False, 'umur': 25, 'hobi': ['Baca', 'Belajar']}
print(type(a_dict))             # --> Mencetak variabel dan mengecek tipe data, maka mencetak pesan <class 'dict'>

# Pengaksesan Property Dictionary Menggunakan Notasi Dict [Property_Name]

a_dict = {
    "nama":"Zaki",
    "male":False,
    "umur":"25",
    "hobi":["Baca", "Belajar"]
}                                # --> Inisialisasi variabel yang menyimpan data dict, berisi 4 key-value
print("%s" % (a_dict["nama"]))   # --> Mencetak variabel, dengan format string, maka mencetak pesan Zaki

# Penulisan Dictionary Diperbolehkan Horizontal

a_dict = {"nama":"Zaki", "umur": 26} # --> Inisialisasi variabel yang menyimpan data dict, berisi 2 key-value
print(a_dict)                        # --> Mencetak variabel, maka mencetak pesan {'nama': 'Zaki', 'umur': 26}


print("------")

# 7. Tipe Data Set

# Urutan Elemen    : Tidak urut
# Akses Elemen     : Hanya Menggunakan Perulangan
# Mutability       : Elemen Bisa Diubah
# Duplikasi Elemen : Elemen Selalu Unik
# Tipe Data Eemen  : Bisa Sejenis, Maupun Berbeda Satu Sama Lain

# Selalu Berubah-Rubah Posisi Elemen, Stiap Dijalankan

a_set = {1,2,3}                # --> Inisialisasi variabel yang menyimpan data set, berisi 3 elemen data integer
print(a_set)                   # --> Mencetak variabel, maka mencetak pesan {1,2,3}
print(type(a_set))             # --> Mencetak variabel dan mengecek tipe data, maka mencetak pesan <class 'set'>

a_set = {"Natashia", "Laura"}  # --> Inisialisasi variabel yang menyimpan data set, berisi 2 elemen data string
print(a_set)                   # --> Mencetak variabel, maka mencetak pesan {'Natashia', 'Laura'}

a_set = {5, "Zaki", True}      # --> Inisialisasi variabel yang menyimpan data set, berisi 2 elemen integer, string, dan boolean
print(a_set)                   # --> Mencetak variabel, maka mencetak pesan {5, 'Zaki', True} 


print("------")

# 7. Tipe Data Lainnya

# Selain Tipe-Tipe Di Atas Ada Juga Beberapa Tipe Data Lainnya, Seperti Frozenset, Bytes, Memoryview, Range Dan Kesemuanya Akan Dibahas Satu Per Satu Di Chapter Terpisah.

