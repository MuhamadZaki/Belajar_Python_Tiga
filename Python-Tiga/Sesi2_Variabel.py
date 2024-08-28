# Dalam Konsep Programming, Variabel Adalah Suatu Nama Yang Dikenali Komputer Sebagai Penampung Nilai/Data Yang Disimpan Di Memory. Sebagai Contoh Nilai 3.14 Disimpan Di Variabel Bernama Pi.

# Variabel

print("------")

# 1. Deklarasi Atau Inisialisasi Variabel

names = "Natashia"       # --> 'names' nama variabel, '=' operator assignment, dan 'Natashia' adalah nilai

a_string = "Natashia"    # --> Inisialisasi variabel yang menyimpan data string
print(a_string)          # --> Mencetak variabel, maka menctak pesan Natashia

a_integer = 26           # --> Inisialisasi variabel yang menyimpan data integer
print(a_integer)         # --> Mencetak variabel, maka mencetak pesan 26

a_float = 9.0            # --> Inisialisasi variabel yang menyimpan data float
print(a_float)           # --> Mencetak variabel, maka mencetak pesan 9.0

a_boolean = True         # --> Inisialisasi variabel yang menyimpan data boolean
print(a_boolean)         # --> Mencetak variabel, maka mencetak pesan True


print("------")

# 2.  String Formatting

# %s Untuk String (a_string)
# %d Untuk Integer (a_integer)
# %.1f Untuk Float Dengan Satu Angka Desimal (a_float)
# %f Untuk Float standar (a_float)
# %r Untuk Representasi Objek (a_boolean)

a_string = "Natashia"    # --> Inisialisasi variabel yang menyimpan data string
a_integer = 26           # --> Inisialisasi variabel yang menyimpan data integer
a_float = 9.0            # --> Inisialisasi variabel yang meyimpan data float
b_float = 8.0            # --> Inisialisasi variabel yang meyimpan data float    
a_boolean = True         # --> Inisialisasi variabel yang menyimpan dat aboolean

print("1 : %s, 2 : %d, 3 : %.1f, 4 : %f, 5 : %r" % (a_string, a_integer, a_float, b_float, a_boolean)) # --> Mencetak variabel, dengan format string --> 1 : Natashia, 2 : 26, 3 : 9.0, 4 : 8.000000, 5 : True


print("------")

# 3.  Naming Convention Variabel

# Normal
nama = "Zaki"            # --> Inisialisasi variabel yang menyimpan data string
print(nama)              # --> Mencetak variabel, maka mencetak pesan Zaki

# Snake_Case

nama_saya = "Zaki"       # --> Inisialisasi variabel yang menyimpan data string
print(nama_saya)         # --> Mencetak variabel, maka mencetak pesan Zaki

# CamelCase

namaSaya = "Zaki"        # --> Inisialisasi variabel yang menyimpan data string
print(namaSaya)          # --> Mencetak variabel, maka mencetak pesan Zaki

namaSayaSiapa = "Zaki"   # --> Inisialisasi variabel yang menyimpan data string
print(namaSayaSiapa)     # --> Mencetak variabel, maka mencetak pesan Zaki

# Pascal Case

NamaSaya = "Zaki"        # --> Inisialisasi variabel yang menyimpan data string
print(NamaSaya)          # --> Mencetak variabel, maka mencetak pesan Zaki


print("------")

# 4. Operasi Assignment

a_string = "Laura"       # --> Inisialisasi variabel yang menyimpan data string
print(a_string)          # --> Mencetak variabel, maka mencetak pesan Laura

a_integer = 17           # --> Inisialisasi variabel yang menyimpan data integer
print(a_integer)         # --> Mencetak variabel, maka mencetak pesan 17

a_float = 5.0            # --> Inisialisasi variabel yang menyimpan data float
print(a_float)           # --> Mencetak variabel, maka mencetak pesan 5.0

a_boolean = False        # --> Inisialisasi variabel yang menyimpan data boolean
print(a_boolean)         # --> Mencetak variabel, maka mencetak pesan False


print("------")

# 5. Deklarasi Atau Inisialisasi Variabel Beserta Tipe Data

a_string = "Isabella"    # --> Inisialisasi variabel yang menyimpan data string
print(a_string)          # --> Mencetak variabel, maka mencetak pesan Isabella

a_integer = 18           # --> Inisialisasi variabel yang menyimpan data integer
print(a_integer)         # --> Mencetak variabel, maka mencetak pesan 18

a_float = 7.0            # --> Inisialisasi variabel yang menyimpan data float
print(a_float)           # --> Mencetak variabel, maka mencetak pesan 7.0

a_boolean = False        # --> Inisialisasi variabel yang menyimpan data boolean
print(a_boolean)         # --> Mencetak variabel, maka mencetak pesan False


print("------")

# 6. Deklarasi Banyak Variabel Sebaris

# %s Untuk String (a_string)
# %d Untuk Integer (a_integer)
# %.1f Untuk Float Dengan Satu Angka Desimal (a_float)
# %r Untuk Representasi Objek (a_boolean)

satu, dua, tiga, empat, lima = 80, 60, 40, 20, 10   # --> Inisialisasi lima variabel yang menyimpan data integer
results = (satu + dua + tiga + empat + lima) / 2    # --> Menjumlahkan semua variabel dan membagi hasilnya dengan 2 dan tersimpan dalam variabel results
print("%f" % (results))                             # --> Mencetak variabel, menggunakan float standar, maka mencetak pesan 105.000000
print("%.1f" % (results))                           # --> Mencetak variabel, menggunakan float satu angka desimal, maka mencetak pesan 105.0

