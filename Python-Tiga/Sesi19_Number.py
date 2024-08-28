# Python Mengenal Cukup Banyak Tipe Data, Mulai Dari Yang Built-In (Bawaan) Maupun Custom Type. Pada Chapter Ini Kita Akan Mempelajari High-Level Overview Tipe-Tipe Tersebut.

# Tipe Data Numrik

# 1. Integer --> Menamoung Bilangan Bulat
# 2. Float   --> Menampung Bilangan Desimal Atau Floating Point
# 3. complex --> Menampung Nilai Berisi Kombinasi Bilangan Real Dan Imajiner


print("------")

# 1. Integer

a_int = 20               # --> Inisialisasi variabel yang menyimpan data integer
b_int = 20               # --> Inisialisasi variabel yang menyimpan data integer
results = a_int + b_int  # --> Menjumlahkan nilai a_int dan b_int dan tersimpan dalam variabel results
print(results)           # --> Mencetak variabel --> 40
print(type(results))     # --> Mencetak variabel dan mengecek tipe data --> <class 'int'> 

a_int = 18_12_98         # --> Inisialisasi variabel yang menyimpan data integer
print(a_int)             # --> Mencetak variabel --> 181298
print(type(a_int))       # --> Mencetak variabel dan mengecek tipe data --> <class 'int'> 


print("------")

# Prefix literal untuk hexadesimal 0x
# Prefix literal untuk oktal 0o
# Prefix literal untuk biner 0b

a_int = 24               # --> Inisialisasi variabel yang menyimpan data integer
print(a_int)             # --> Mencetak variabel --> 24

a_int_hexa = 0x8c        # --> Inisialisasi variabel yang manyimpan data integer dalam bentuk hexadecimal
print(a_int_hexa)        # --> Mencetak variabel --> 140

a_int_octal = 0o214      # --> Inisialisasi variabel yang menyimpan data integer dalam bentuk octal
print(a_int_octal)       # --> Mencetak variabel --> 140

a_int_biner = 0b10001100 # --> Inisialisasi variabel yang menyimpan data integer dalam bentuk binary
print(a_int_biner)       # --> Mencetak variabel --> 140


print("------")

# Stirng Formating f"" Dengan Menambahkan d Atau Tanpa Suffix
# Stirng Formating f"" Dengan Menambahkan Suffix x
# Stirng Formating f"" Dengan Menambahkan Suffix o
# Stirng Formating f"" Dengan Menambahkan Suffix b

a_int = 24                # --> Inisialisasi variabel yang menyimpan data integer
print(f"{a_int:d}")       # --> Mencetak variabel --> 24

a_int_hexa = 0x8c         # --> Inisialisasi variabel yang manyimpan data integer dalam bentuk hexadecimal
print(f"{a_int_hexa:x}")  # --> Mencetak variabel tanpa prefix 0x --> 8c

a_int_octal = 0o214       # --> Inisialisasi variabel yang menyimpan data integer dalam bentuk octal
print(f"{a_int_biner:o}") # --> Mencetak variabel tanpa prefix 0o --> 214

a_int_biner = 0b10001100  # --> Inisialisasi variabel yang menyimpan data integer dalam bentuk binary
print(f"{a_int_biner:b}") # --> Mencetak variabel tanpa prefix 0b --> 10001100


print("------")

# Operasi Perbandingan Antar Basis

a_int = 140                    # --> Inisialisasi variabel yang menyimpan data integer
b_int = 140                    # --> Inisialisasi variabel yang menyimpan data integer
results = a_int == b_int       # --> Membandingkan apakah nilai a_int sama dengan nilai b_int, dan tersimpan pada variabel results
print(results)                 # --> Mencetak variabel --> True

a_int = 140                    # --> Inisialisasi variabel yang menyimpan data integer
a_int_hexa = 0x8c              # --> Inisialisasi variabel yang manyimpan data integer dalam bentuk hexadecimal
results = a_int == a_int_hexa  # --> Membandingkan apakah nilai a_int sama dengan nilai a_int_hexa, dan tersimpan pada variabel results
print(results)                 # --> Mencetak variabel --> True

a_int = 140                    # --> Inisialisasi variabel yang menyimpan data integer
a_int_octal = 0o214            # --> Inisialisasi variabel yang menyimpan data integer dalam bentuk octal
results = a_int == a_int_octal # --> Membandingkan apakah nilai a_int sama dengan nilai a_int_octal, dan tersimpan pada variabel results
print(results)                 # --> Mencetak variabel --> True

a_int = 140                    # --> Inisialisasi variabel yang menyimpan data integer
a_int_biner = 0b10001100       # --> Inisialisasi variabel yang menyimpan data integer dalam bentuk binary
results = a_int == a_int_biner # --> Membandingkan apakah nilai a_int sama dengan nilai a_int_biner, dan tersimpan pada variabel results
print(results)                 # --> Mencetak variabel --> True


print("------")

# Nilai Numrik Dalam Basis Tertentu Menggunakan Suffix

a_int = 140         # --> Inisialisasi variabel yang menyimpan data integer
print(f"{a_int:d}") # --> Mencetak variabel --> 140
print(f"{a_int:x}") # --> Mencetak variabel --> 8c
print(f"{a_int:o}") # --> Mencetak variabel --> 214
print(f"{a_int:b}") # --> Mencetak variabel --> 10001100

a_int_hexa = 0x8c         # -->Inisialisasi variabel yang manyimpan data integer dalam bentuk hexadecimal
print(f"{a_int_hexa:d}")  # --> Mencetak variabel --> 140
print(f"{a_int_hexa:x}")  # --> Mencetak variabel --> 8c
print(f"{a_int_hexa:o}")  # --> Mencetak variabel --> 214
print(f"{a_int_hexa:b}")  # --> Mencetak variabel --> 10001100

a_int_octal = 0o214       # --> Inisialisasi variabel yang menyimpan data integer dalam bentuk octal
print(f"{a_int_octal:d}") # --> Mencetak variabel --> 140
print(f"{a_int_octal:x}") # --> Mencetak variabel --> 8c
print(f"{a_int_octal:o}") # --> Mencetak variabel --> 214
print(f"{a_int_octal:b}") # --> Mencetak variabel --> 10001100

a_int_biner = 0b10001100  # --> Inisialisasi variabel yang menyimpan data integer dalam bentuk binary
print(f"{a_int_biner:d}") # --> Mencetak variabel --> 140
print(f"{a_int_biner:x}") # --> Mencetak variabel --> 8c
print(f"{a_int_biner:o}") # --> Mencetak variabel --> 214
print(f"{a_int_biner:b}") # --> Mencetak variabel --> 10001100


print("------")

# Operasi Aritmatika Antar basis

a_int = 140               # --> Inisialisasi variabel yang menyimpan data integer
a_int_hexa = 0x8c         # --> Inisialisasi variabel yang manyimpan data integer dalam bentuk hexadecimal
a_int_octal = 0o214       # --> Inisialisasi variabel yang menyimpan data integer dalam bentuk octal
a_int_biner = 0b10001100  # --> Inisialisasi variabel yang menyimpan data integer dalam bentuk binary

total_results = a_int + a_int_hexa + a_int_octal + a_int_biner                                           # --> Menjumlahkan nilai berbagai variabel menggunakan operator + dan tersimpan pada vriabel tota_results
print(f"{total_results} = ({total_results:d}, {total_results:x}, {total_results:o}, {total_results:b})") # --> Mencetak variabel --> 560 = (560, 230, 1060, 1000110000)


print("------")

# Nilai Numrik Dalam Basis Data Tertentu Menggunakan Fungsi

# Fungsi oct() Niai Numrik Dalam Bentuk Octal Dalam Tipe Data String
# Fungsi hex() Nilai Numerik Dalam Bentuk Hexadecimal Dalam Tipe Data String
# Fungsi bin() Nilai Numerik Dala Bentuk Binary Dalam Tipe Data String
# Fungsi int() Mengonversi Data String Berisi Angka Numerik Apapun, Selama Basisnya 0-36 Ke Tipe Data Integer

a_int = oct(140)          # --> Mengonversi nilai integer ke bentuk string oktal, dan tersimpan pada variabel a_int
print(a_int)              # --> Mencetak variabel --> 0o214

a_int = oct(0x8c)         # --> Mengonversi nilai integer dalam bentuk hexa ke bentuk string oktal, dan tersimpan pada variabel a_int
print(a_int)              # --> Mencetak variabel --> 0o214

a_int = oct(0b10001100)   # --> Mengonversi nilai integer dalam bentuk binary 140 ke bentuk string oktal, dan tersimpan pada variabel a_int
print(a_int)              # --> Mencetak variabel --> 0o214

#-----

a_int = hex(140)          # --> Mengonversi nilai integer ke bentuk string hexadecimal, dan tersimpan pada variabel a_int
print(a_int)              # --> Mencetak variabel --> 0x8c

a_int = hex(0o214)        # --> Mengonversi nilai integer dalam bentuk octal ke bentuk string hexadecimal, dan tersimpan pada variabel a_int
print(a_int)              # --> Mencetak variabel --> 0x8c

a_int = hex(0b10001100)   # --> Mengonversi nilai integer dalam bentuk binary ke bentuk string hexadecimal, dan tersimpan pada variabel a_int
print(a_int)              # --> Mencetak variabel --> 0x8c

#----

a_int = bin(140)          # --> Mengonversi nilai intager 140 ke bentuk string binary, dan tersimpan pada variabel a_int
print(a_int)              # --> Mencetak variabel --> 0b1000110

a_int = bin(0x8c)         # --> Mengonversi nilai intager dalam bentuk hexa ke bentuk string binary, dan tersimpan pada variabel a_int
print(a_int)              # --> Mencetak variabel --> 0b1000110

a_int = bin(0o214)        # --> Mengonversi nilai intager dalam bentuk octal ke bentuk string binary, dan tersimpan pada variabel a_int
print(a_int)              # --> Mencetak variabel --> 0b1000110

#----

a_int = int("140", base= 10)       # --> Mengonversi string integer ke integer dengan basis 10, dan tersimpan pada variabel a_int
print(a_int)                       # --> Mencetak variabel --> 140

a_int = int("0x8c", base = 16)     # --> Mengonversi string hexa ke integer dengan basis 16, dan tersimpan pada variabel a_int
print(a_int)                       # --> Mencetak variabel --> 140

a_int = int("0o214", base= 8)      # --> Mengonversi string octal ke integer dengan basis 8, dan tersimpan pada variabel a_int
print(a_int)                       # --> Mencetak variabel --> 140

a_int = int("0b10001100", base= 2) # --> Mengonversi string biner ke integer dengan basis 2, dan tersimpan pada variabel a_int
print(a_int)                       # --> Mencetak variabel --> 140


print("------")

# 2. Floating Point (float)

a_float = 3.14       # --> Inisialisasi variabel yang menyimpan data float
print(a_float)       # --> Mencetak variabel --> 3.14
print(type(a_float)) # --> Mencetak variabel dan mengecek tipe data --> <class 'float'>

a_float = 3.         # --> Inisialisasi variabel yang menyimpan data float
print(a_float)       # --> Mencetak variabel --> 3.0
print(type(a_float)) # --> Mencetak variabel dan mengecek tipe data --> <class 'float'>


print("------")

# Pembulatan Atau Rounding

pi = 3.145789          # --> Inisialisasi variabel yang menyimpan data float
a_float = round(pi, 2) # --> Membulatkan nilai pi hingga 2 angka di belakang koma, dan tersimpan pada variabel a_float
print(a_float)         # --> Mencetak variabel --> 3.15

pi = 3.145789
a_float = round(pi, 4) # --> Membulatkan nilai pi hingga 4 angka di belakang koma, dan tersimpan pada variabel a_float
print(a_float)         # --> Mencetak variabel --> 3.1458

# Pembulatan Ke Atas (Mengembalikan Tipe Data Int)

import math              # --> Mengimpor modul math yang menyediakan fungsi matematika
a_float = math.floor(pi) # --> Membulatkan nilai pi ke bawah (ke integer terdekat yang lebih kecil), dan tersimpan pada variabel a_float
print(a_float)           # --> Mencetak variabel --> 3

# Pembulatan Ke Bawah (Mengembalikan Tipe Data Int)

import math              # --> Mengimpor modul math yang menyediakan fungsi matematika
a_float = math.ceil(pi)  # --> Membulatkan nilai pi ke atas (ke integer terdekat yang lebih besar), dan tersimpan pada variabel a_float
print(a_float)           # --> Mencetak variabel --> 4


print("------")

# Pembulatan Float Dalam String Formating f""

a_float = -3.145789     # --> Inisialisasi variabel yang menyimpan data float
print(f"{a_float:.2f}") # --> Mencetak variabel, dengan pembulatan hingga 2 angka di belakang koma --> -3.15

a_float = -3.145789     # --> Inisialisasi variabel yang menyimpan data float
print(f"{a_float:.3f}") # --> Mencetak variabel, dengan pembulatan hingga 3 angka di belakang koma --> -3.146

a_float = -3.145789     # --> Inisialisasi variabel yang menyimpan data float
print(f"{a_float:.4f}") # --> Mencetak variabel, dengan pembulatan hingga 4 angka di belakang koma --> -3.1458


print("------")

# Karateristik Float (Memiliki Satu Sifat Unik Dimana Angka Belakang Koma Tidak Tersimpan Secara Pasti Informasinya Digitnya Atau Tidak Pasti, Tidak Fixed)

a_float = 3.14               # --> Inisialisasi variabel yang menyimpan data float
b_float = 3.8                # --> Inisialisasi variabel yang menyimpan data float
results = a_float + b_float  # --> Menjumlahkan nilai a_float dan b_float, menggunakan operator + dan tersimpan pada variabel results
print(results)               # --> Mencetak variabel --> 6.9399999999999995

# Karateristik Float Untuk Menampilkan Angka Fixednya Menggunakan Suffix :f Dan :.2f

a_float = 3.14               # --> Inisialisasi variabel yang menyimpan data float
b_float = 3.8                # --> Inisialisasi variabel yang menyimpan data float
results = a_float + b_float  # --> Menjumlahkan nilai a_float dan b_float, menggunakan operator + dan tersimpan pada variabel results
print(f"{results:f}")        # --> Mencetak variabel --> 6.940000

a_float = 3.14               # --> Inisialisasi variabel yang menyimpan data float
b_float = 3.8                # --> Inisialisasi variabel yang menyimpan data float
results = a_float + b_float  # --> Menjumlahkan nilai a_float dan b_float, menggunakan operator + dan tersimpan pada variabel results
print(f"{results:.2f}")      # --> Mencetak variabel, dengan 2 angka di belakang koma --> 6.94


print("------")

# Konversi Tipe Data Menggunakan Fungsi float()

# Fungsi float() digunakan untuk mengkonversi suatu nilai menjadi float

nums = 12345678       # --> Inisialisasi variabel yang menyimpan data integer
a_float = float(nums) # --> Mengonversi nilai integer nums ke float, dan tersimpan pada variabel a_float
print(a_float)        # --> Mencetak variabel --> 12345678.0

text = "12345678"     # --> Inisialisasi variabel yang menyimpan data string
a_float = float(text) # --> Mengonversi nilai string text ke float, dan tersimpan pada variabel a_float
print(a_float)        # --> Mencetak variabel --> 12345678.0

print("------")

# Notasi Float Exponential

# Notasi 2e0 Artinya Adalah 2.0 * (10 ^ 0). Nilai Tersebut Ekuivalen Dengan 2.0
# Notasi 577e2 Artinya Adalah 577.0 * (10 ^ 2). Nilai Tersebut Ekuivalen Dengan 57700.0
# Notasi 68277e+6 Artinya Adalah 68277.0 * (10 ^ 6). Nilai Tersebut Ekuivalen Dengan 68277000000.0
# Notasi 6e-3 Artinya Adalah 6 * (10^-3). Nilai Tersebut Ekuivalen Dengan 0.006

a_float = 2e0        # --> Inisialisasi variabel yang menyimpan data float, dengan nilai 2 dalam notasi ilmiah (2e0 berarti 2 * 10^0, yang setara dengan 2.0)
print(a_float)       # --> Mencetak variabel --> 2.0 

a_float = 577e2      # --> Inisialisasi variabel yang menyimpan data float, dengan nilai 577 dalam notasi ilmiah (577e2 berarti 577 * 10^2, yang setara dengan 57700.0)
print(a_float)       # --> Mencetak variabel --> 57700.0

a_float = 68277e+6   # --> Inisialisasi variabel yang menyimpan data float, dengan nilai 68277 dalam notasi ilmiah (68277e+6 berarti 68277 * 10^6, yang setara dengan 68277000000.0)
print(a_float)       # --> Mencetak variabel --> 68277000000.0

a_float = 6e-3       # --> Inisialisasi variabel yang menyimpan data float, dengan nilai 6 dalam notasi ilmiah (6e-3 berarti 6 * 10^-3, yang setara dengan 0.006)
print(a_float)       # --> Mencetak variabel --> 0.006


print("------")

# 3. Complex

a_complex = 120+3j       # --> Inisialisasi variabel yang menyimpan data complex (120 adalah bagian real, dan 3j adalah bagian imajiner)
print(a_complex)         # --> Mencetak variabel --> (120+3j)
print(type(a_complex))   # --> Mencetak variabel, dan mengecek tipe data --> <class 'complex'>

# Bisa Mengguanakan property (.real .imag) Untuk Informasi Bilangan Rean Dan Imagernya

a_complex = 120+3j       # --> Inisialisasi variabel yang menyimpan data complex (120 adalah bagian real, dan 3j adalah bagian imajiner)
results = a_complex.real # --> Mengambil bagian real dari bilangan complex, dan tersimpan pada variabel results
print(results)           # --> Mencetak variabel --> 120.0

a_complex = 120+3j       # --> Inisialisasi variabel yang menyimpan data complex (120 adalah bagian real, dan 3j adalah bagian imajiner)
results = a_complex.imag # --> Mengambil bagian imajiner dari bilangan complex, dan tersimpan pada variabel results
print(results)           # --> Mencetak variabel --> 3.0


print("------")

# Fungsi Complex

# Fungsi complex() Digunakan Sebagai Alternatif Cara Membuat Bilangan Complex (Ditulis 120+3j Dan Jika Ditulis Menggunakan Fungsi complex())

a_complex = complex(120, 3)      # --> Inisialisasi variabel yang menyimpan data complex
print(a_complex)                 # --> Mencetak variabel --> (120+3j)


print("------")

# Operasi Artimatika Bilangan Complex
a_complex = 120-2j               # --> Inisialisasi variabel yang menyimpan data complex (120 adalah bagian real, dan -2j adalah bagian imajiner)
b_complex = -19+4j               # --> Inisialisasi variabel yang menyimpan data complex (-19 adalah bagian real, dan 4j adalah bagian imajiner)
results = a_complex + b_complex  # --> Menjumlahkan dua bilangan kompleks, (120-19) + (-2j+4j) 
print(results)                   # --> Mencetak variabel --> (101+2j)

a_complex = 120-2j                   # --> Inisialisasi variabel yang menyimpan data complex (120 adalah bagian real, dan -2j adalah bagian imajiner)    
b_complex = -19+4j                   # --> Inisialisasi variabel yang menyimpan data complex (-19 adalah bagian real, dan 4j adalah bagian imajiner)
results = a_complex + b_complex + 20 # --> Menjumlahkan dua bilangan kompleks dan bilangan real 20, (120-19+20) + (-2j+4j)
print(results)                       # --> Mencetak variabel --> (121+2j)