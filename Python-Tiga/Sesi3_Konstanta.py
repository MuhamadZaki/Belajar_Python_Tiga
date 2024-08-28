# Konstanta (Nilai Konstan) Adalah Sebuah Variabel Yang Nilainya Dideklarasikan Di Awal Dan Tidak Bisa Diubah Setelahnya

# Konstanta 

#  1. Anotasi Final Digunakan Untuk Menunjukkan Bahwa Suatu Variabel, Atribut, Atau Metode Tidak Boleh Diubah Atau Di-Override Setelah Didefinisikan

from typing import Final # --> Mengimpor anotasi tipe Final dari modul typing

PI: Final = 3.14         # --> Inisialisasi variabel yang menyimpan data konstanta float (tidak boleh diubah)
print("%f" % (PI))       # --> Mencetak variabel, menggunakan float standar, maka mencetak pesan 3.140000

# 2. Modul Import

# Keyword import Digunakan Untuk Meng-Import Sesuatu, Sedangkan Keyword from Digunakan Untuk Menentukan Dari Module Mana Sesuatu Tersebut Akan Di-Import

# Statement from typing import Final Artinya Adalah Meng-Import Tipe Final Dari Module Typing Yang Dimana Module Ini Merupakan Bagian Dari Python Standard Library (stdlib).


print("------")

# 3. Tipe Class typing.Final

# Anotasi Final Digunakan Untuk Menunjukkan Bahwa Suatu Variabel, Atribut, Atau Metode Tidak Boleh Diubah Atau Di-Override Setelah Didefinisikan

PI: Final = 3.14             # --> # tipe konstanta PI tidak ditentukan secara explisit, melainkan didapat dari tipe data nilai

TOTAL_MONTH: Final[int] = 12 # --> Tipe konstanta TOTAL_MONTH ditentukan secara explisit yaitu `int`


print("------")

# 4. Naming Convention Konstanta

#Mengacu ke dokumentasi PEP 8 – Style Guide for Python Code, nama konstanta harus dituliskan dalam huruf besar (UPPER_CASE).