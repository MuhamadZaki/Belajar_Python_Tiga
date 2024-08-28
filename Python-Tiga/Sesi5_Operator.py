""" All Operator """

# Operator Adalah Suatu Karakter Yang Memiliki Kegunaan Khusus Contohnya Seperti + Untuk Operasi Aritmatika Tambah, Dan and Untuk operasi logika AND


print("-------->") 

# 1. Operator Aritmatika --> Untuk Melakukan Operasi Matematika Dasar

# Penjumlahan

a = 5            # --> Inisialisasi variabel yang menyimpan data integer
b = 3            # --> Inisialisasi variabel yang menyimpan data integer
results = a + b  # --> Menjumlahkan nilai variabel a, b menggunakan operator + dan tersimpan pada variabel results
print("Penjumlahan(+) = ", results)   # --> Mencetak variabel --> 8

a = 5.5          # --> Inisialisasi variabel yang menyimpan data float
b = 3.3          # --> Inisialisasi variabel yang menuimpan data float
results = a + b  # --> Menjumlahkan nilai variabel a, b menggunakan operator + dan tersimpan pada variabel results
print("Penjumlahan(+) = ", results)   # --> Mencetak variabel --> 8.8

a = 5j           # --> Inisialisasi variabel yang menyimpan data complex
b = 3j           # --> Inisialisasi variabel yang menyimpan data complex
results = a + b  # --> Menjumlahkan nilai variabel a, b mengguanakan operator + dan tersimpan pada variabel results
print("Penjumlahan(complex) = ", results) # --> Mencetak variabel --> 8j

a = 5 + 3j      # --> Inisialisasi variabel yang menyimpan data complex
b = 5 + 3j      # --> Inisialisasi vriabel yang menyimpan data complex
results = a + b # --> Menjumlahkan nilai variabel a, b menggunakan operator + dan tersimpan pada variabel results
print("Penjumlahan(complex) = ", results) # --> Mencetak variabel --> (10+6j)

a = "Muhamad"          # --> Inisialisasi variabel yang menyimpan data string
b = "Zaki"             # --> Inisialisasi variabel yang menyimpan data string
results = a + " " + b  # --> Menggabungkan (concatenation) nilai vriabel a, b menggunakan operator + dan tersimpan pada variabel results
print("Penjumlahan(+) = ", results)       # --> Mencetak vriabel --> Muhamad Zaki

a = [1,2,3]     # --> Inisialisasi varirbel yang menyimpan data list, berisi 3 elemen data integer
b = [4,5,6]     # --> Inisialisasi variabel yang menyimpan data list, berisi 3 elemen data integer
results = a + b # --> Menggabungkan (concatenation) nilai variabel a, b menggunakan operator + dam tersimpan pada variabel results
print("Penjumlahan(+) = ", results)       # --> Mencetak variabel --> [1,2,3,4,5,6]

a = (1,2,3)     # --> Inisialisasi variabel yang menyimpan data tuple, berisi 3 elemen data integer
b = (4,5,6)     # --> Inisialisasi variabel yang menyimpan data tuple, berisi 3 elemen data integer
results = a + b # --> Menggabungkan (concatenation) nilai variabel a, b mengguakan operator + dan tersimpan pada variabel results
print("Penjumlahan(+) = ", results)       # --> Mencetak variabel --> (1,2,3,4,5,6)

a = b"Muhamad"  # --> Inisialisasi variabel yang menyimpan data bytes
b = b"Zaki"     # --> Inisialisasi variabel yang menyimpan data bytes
results = a + b # --> Menggabungkan (concatenation) nilai variabel a, b menggunakan operator + dan tersimpan pada variabel results
print("Penjumlahan(+) = ", results)       # --> Mencetak variabel --> b'MuhamadZaki'

a = bytearray(b"mantap")   # --> Inisialisasi variabel yang menyimpan data bytearray
b = bytearray(b'gede')     # --> Inisialisasi variabel yang menyimpan data bytearray
results = a + b            # --> Menggabungkan (concatenation) nilai vairbel a, b menggunakan operator + dan tersimpan pada variabel results
print("Penjumlahan(+) = ", results)       # --> Mencetak variabel --> bytearray(b'mantapgede')


print("-------->")      

# Pengurangan

a = 5            # --> Inisialisasi variabel yang menyimpan data integer
b = 3            # --> Inisialisasi variabel yang menyimpan data integer
results = a - b  # --> Mengurangi nilai variabel a, b menggunakan operatpr - dan tersimpan pada variabel results
print("Pengurangan(-) = ", results)    # --> Mencetak variabel --> 2

a = 5.5          # --> Inisialisasi variabel yang menyimpan data float
b = 3.3          # --> Inisialisasi variabel yang menyimpan data float
results = a - b  # --> Mengurangi nilai variabel a, b menggunakan operator - dan tersimpan pada variabel results
print("Pengurangan(-) = ", results)    # --> Mencetak variabel --> 2.2

a = 5j           # --> Inisialisasi variabel yang menyimpan data complex
b = 3j           # --> Inisialisasi variabel yang menyimpan data complex
results = a - b  # --> Mengurangi nilai variabel a, b menggunakan operator - dan tersimpan pada variabel results
print("Pengurangan(-) = ", results)    # --> Mencetak variabel --> 2j

a = 5 + 3j       # --> Inisialisasi variabel yang menyimpan data complex
b = 5 + 3j       # --> Inisialisasi variabel yang menyimpan data complex
results = a - b  # --> Mengurangi nilai variabel a, b menggunakan operator - dan tersimpan pada variabel results
print("Pengurangan(-) = ", results)    # --> Mencetak variabel --> (0j)

# --> Tidak bisa menggunakan tipe data string
# --> Tidak bisa menggunakan tipe data list
# --> Tidak bisa menggunakan tipe data tuple
# --> Tidak bisa menggunakan tipe data bytes
# --> Tidak bisa menggunakan tipe data bytearray
 

print("-------->")      

# Perkalian

a = 5           # --> Inisialisasi variabel yang menyimpan data integer
b = 3           # --> Inisialisasi variabel yang menyimpan data integer
results = a * b # --> Mengalikan nilai variabel a, b menggunakan operator * dan terimpan pada variabel results
print("Perkalian(*) = ", results)          # --> Mencetak variabel --> 15

a = 5.5         # --> Inisialisasi variabel yang menyimpan data float
b = 3.3         # --> Inisialisasi variabel yang menyimpan data float
results = a * b # --> Mengalikan nilai variabel a, b menggunakan operator * dan tersimpan pada variabel results
print("Perkalian(*) = ", results)       # --> Mencetak variabel --> 18.15

a = 5j          # --> Inisialisasi variabel yang menyimpan data complex
b = 3j          # --> Inisialisasi variabel yang menyimpan data complex
results = a * b # --> Mengalikan nilai variabel a, b menggunakan operator * dan tersimpan pada variabel results
print("Perkalian(*) = ", results)       # --> Mencetak variabel --> (-15j+0j)

a = 5 + 3j      # --> Inisialisasi variabel yang menyimpan data complex
b = 5 + 3j      # --> Inisialisasi variabel yang menyimpan data complex
results = a * b # --> Mengalikan nilai variabel a, b menggunakan operator * dan tersimpan pada variable results
print("Perkalian(*) = ", results)       # --> Mencetak variabel --> (16+30j)

a ="Aduhai"     # --> Inisialisasi variabel yang menyimpan data string
results = a * 3 # --> Mengalikan (pengulangan) nilai variabel a dengan angka 3 menggunakan operator * dan tersimpan pada variabel results
print("Perkalian(*) = ", results)       # --> Mencetak variabel --> AduhaiAduhaiAduhai

a = [1,2,3]     # --> Inisialisasi variabel yang menyimpan data list, berisi 3 elemen data integer
results = a * 2 # --> Mengulangi (pengulangan) nilai variabel sebanyak 2x menggunakan operator * dan tersimpan pada variabel results
print("Perkalian(*) = ", results)         # --> Mencetak variabel --> [1,2,3,1,2,3]

a = (1,2,3)     # --> Inisialisasi variabel yang menyimpan data tuple, berisi 3 elemen data integer
results = a * 2 # --> Mengulangi (pengulangan) nilai variabel sebanyak 2x menggunakan operator * dan tersimpan pada variabel results
print("Perkalian(*) = ", results)         # --> Mencetak variabel --> (1,2,3,1,2,3)

a = b"Nenen"    # --> Inisialisasi variabel yang menyimpan data bytes
results= a * 2  # --> Mengulangi (pengulangan) nilai variabel sebanyak 2x menggunakan operator * dan tersimpan pada variabel results
print("Perkalian(*) = ", results)         # --> Mencetak variabel --> b'NenenNenen'

a = bytearray(b"gede") # --> Inisialisasi variabel yang menyimpan data bytearray
results = a * 2        # --> Mengulangi (pengulangan) nilai variabel sebanyak 2x menggunakan operator * dan tersimpan pada variabel results
print("Perkalian(*) = ", results)         # --> Mencetak variabel --> bytearray(b'gedegede')
 

print("-------->")    

# Pembagian (Float)

a = 5            # --> Inisialisasi variabel yang menyimpan data integer
b = 3            # --> Inisialisasi variabel yang menyimpan data integer
results = a / b  # --> Membagi milai variabel a, b menggunakan operator / (float) dan tersimpan pada variabel results
print("Pembagian(/) = ", results)   # --> Mencetak variabel --> 1.6

a = 5.5          # --> Inisialisasi variabel yang menyimpan data float
b = 3.3          # --> Inisialisasi variabel yang menyimpan data float
results = a / b  # --> Membagi nilai variabel a, b menggunakan operator / dan tersimpan pada variabel results
print("Pembagian(/) = ", results)   # --> Mencetak variabel --> 1.6

a = 5j           # --> Inisialisasi variabel yang menyimpan data complex
b = 3j           # --> Inisialisasi variabel yang menyimpan data complex
results = a / b
print("Pembagian(/) = ", results)   # --> Mencetak variabel --> (1.6+0j)

a = 5 + 3j       # --> Inisialisasi variabel yang menyimpan data complex
b = 5 + 3j       # --> Inisialisasi variabel yang menyimpan data complex
results = a / b  # --> Membagi nilai vriabel a, b menggunakan operator / dan tersimpan pada variabel results
print("Pembagian(/) = ", results)   # --> Mencetak vriabel --> (1+0j)

# --> Tidak bisa menggunakan tipe data string
# --> Tidak bisa menggunakan tipe data list
# --> Tidak bisa menggunakan tipe data tuple
# --> Tidak bisa menggunakan tipe data bytes
# --> Tidak bisa menggunakan tipe data bytearray


print("-------->")      

# Pembagian Integer

a = 5            # --> Inisialisasi variabel yang menyimpan data integer
b = 3            # --> Inisialisasi variabel yang menyimpan data integer
results = a // b # --> Membagi nilai variabel a, b menggunakan operator // (integer) dan tersimpan pada variabel results
print("Pembagian(//) = ", results)     # --> Mencetak variabel --> 1

a = 5.5          # --> Inisialisasi variabel yang menyimpan data float
b = 3.3          # --> Inisialisasi variabel yang menyimpan data float
results = a // b # --> Membagi nilai variabel a, b menggunakan operator // dan tersimpan pada variabel results
print("Pembagian(//) = ", results)              # --> Mencetak variabel -->  1.0

# --> Tidak bisa menggunakan tipe data complex
# --> Tidak bisa menggunakan tipe data string
# --> Tidak bisa menggunakan tipe data list
# --> Tidak bisa menggunakan tipe data tuple
# --> Tidak bisa menggunakan tipe data bytes
# --> Tidak bisa menggunakan tipe data bytearray


print("-------->")      

# Modulo Atau Sisa Bagi

a = 5           # --> Inisialisasi variabel yang menyimpan data integer
b = 3           # --> Inisialisasi variabel yang menyimpan data integer
results = a % b # --> Sisa bagi nilai variabel a, b menggunakan operator % dan tersimpan pada variabel results
print("Modulo(%) = ", results)             # --> Mencetak variabel --> 2

a = 5.5         # --> Inisialisasi variabel yang menyimpan data float
b = 3.3         # --> Inisialisasi variabel yang menyimpan data float
results = a % b # --> Sisa bagi nilai variabel a, b menggunakan operator % dan tersimpan pada variabel results
print("Modulo(%) = ", results)             # --> Mencetak variabel --> 2.2

# --> Tidak bisa menggunakan tipe data complex
# --> Tidak bisa menggunakan tipe data string
# --> Tidak bisa menggunakan tipe data list
# --> Tidak bisa menggunakan tipe data tuple
# --> Tidak bisa menggunakan tipe data bytes
# --> Tidak bisa menggunakan tipe data bytearray


print("-------->")     

# Pemangkatan

a = 5            # --> Inisialisasi variabel yang menyimpan data integer
b = 3            # --> Inisialisasi variabel yang menyimpan data integer
results = a ** b # --> Memangkatkan nilai variabel a, b menggunakan operator ** dan tersimpan pada variabel results
print("Pemangkatan = ", results)        # --> Mencetak variabel --> 125

a = 5.5          # --> Inisialisasi variabel yang menyimpan data float
b = 3.3          # --> Inisialisasi variabel yang menyimpan data float
results = a ** b # --> Memangkatkan nilai variabel a, b menggunakan operator ** dan tersimpan pada variabel results
print("Pemangkatan(**) = ", results)    # --> Mencetak variabel --> 277

a = 5j           # --> Inisialisasi variabel yang menyimpan data complex
b = 3j           # --> Inisialisasi variabel yang menyimpan data complex
results = a ** b # --> Memangkatkan vriabel a, b mengguakan operator ** dan tersimpan pada variabel results
print("Pemangkatan(**) = ", results)    # --> Mencetak vriabel --> (0.0010390549422230513-0.00892299738862152j)

a = 5 + 3j       # --> Inisailisasi variabel yang menyimpan data complex
b = 5 + 3j       # --> Inisialisasi variabel yang menyimpan data complex
results = a ** b # --> Memangkatkan variabel a, b menggunakan operator ** dan tersimpan pada variabel results
print("Pemangkatan(**) = ", results)    # --> Mencetak vriabel --> (-182.81777310243447+1319.6714172143916j)

# --> Tidak bisa menggunakan tipe data string
# --> Tidak bisa menggunakan tipe data list
# --> Tidak bisa menggunakan tipe data tuple
# --> Tidak bisa menggunakan tipe data bytes
# --> Tidak bisa menggunakan tipe data bytearray


print("-------->")

# 2. Operator Perbandingan --> Pasti Menghasilkan Nilai Kebenaran bool Dengan Kemungkinannya Hanya Dua Nilai , Yaitu True Atau False

# Sama Dengan (==)

a = True         # --> Inisialisasi variabel yang menyimpan data boolean
b = False        # --> Inisialisasi variabel yang menyimpan data boolean
results = a == b # --> Menggunakan operator ==, apakah nilai variabel a sama dengan nilai variabel b dan tersimpan pada variabel results
print("Sama dengan(==) = ", results)   # --> Mencetak variabel --> False

a = 5            # --> Inisialisasi variabel yang menyimpan data integer
b = 3            # --> Inisialisasi variabel yang menyimpan data integer
results = a == b # --> Menggunakan operator ==, apakah nilai variabel a sama dengan nilai variabel b dan tersimpan pada variabel results
print("Sama dengan(==) = ", results)   # --> Mencetak variabel --> False

a = 5.5          # --> Inisialisasi variabel yang menyimpan data float
b = 3.3          # --> Inisialisasi variabel yang menyimpan data float
results = a == b # --> Menggunakan operator ==, apakah nilai variabel a sama dengan nilai variabel b dan tersimpan pada variabel results
print("Sama dengan(==) = ", results)   # --> Mencetak variabel --> False

a = "Jawa"       # --> Inisialisasi variabel yang menyimpan data string
b = "Tengah"     # --> Inisialisasi variabel yang menyimpan data string
results = a == b # --> Menggunakan operator ==, apakah nilai variabel a sama dengan nilai variabel b dan tersimpan pada variabel results
print("Sama dengan(==) = ", results)   # --> Mencetak variabel --> False

a = [1,2,3]      # --> Inisialisasi variabel yang menyimpan data list, berisi 3 elemen data integer
b = [1,2,3]      # --> Inisialisasi variabel yang menyimpan data list, berisi 3 elemen data integer
results = a == b # --> Menggunakan operator ==, apakah nilai variabel a sama dengan nilai variabel b dan tersimpan pada variabel results
print("Sama dengan(==) = ", results)   # --> Mencetak variabel --> True

a = (1,2,3)      # --> Inisialisasi variabel yang menyimpan data tuple, berisi 3 elemen data integer
b = (1,2,3)      # --> Inisialisasi variabel yang menyimpan data tuple, berisi 3 elemen data integer
results = a == b # --> Menggunakan operator ==, apakah nilai variabel a sama dengan nilai variabel b dan tersimpan pada variabel results
print("Sama dengan(==) = ", results)   # --> Mencetak variabel --> True

a = {"a":1, "b":2} # --> Inisialisasi variabel yang menyimpan data dict, berisi 2 key-value --> Note: Hanya untuk kesetaraan atau ketidaksamaan
b = {"a":1, "b":2} # --> Inisialisasi vraiabel yang menyimpan data dict, berisi 2 key-value
results = a == b   # --> Menggunakan operator ==, apakah nilai variabel a sama dengan nilai variabel b dan tersimpan pada variabel results
print("Sama dengan(==) = ", results)   # --> Mencetak variabel --> True

a = {1,2,3}      # --> Inisialisasi varibael yang menyimpan data set, berisi 3 elemen data integer --> Note: Hanya untuk pengecekan kesetaraan atau ketidaksamaan
b = {1,2,3}      # --> Inisialisasi variabel yang menyimpan data set, berisi 3 elemen data integer
results = a == b # --> Menggunakan operator ==, apakah nilai variabel a sama dengan nilai variabel b dan tersimpan pada variabel results
print("Sama dengan(==) = ", results)   # --> Mencetak variabel --> True

a = None         # --> Inisialisasi variabel yang menyimpan data None --> Note: Hanya untuk pengecekan kesetaraan atau ketidaksamaan
b = None         # --> Inisialisasi variabel yang menyimpan data None
results = a == b # --> Menggunakan operator ==, apakah nilai variabel a sama dengan nilai variabel b dan tersimpan pada variabel results
print("Sama dengan(==) = ", results)   # --> Mencetak variabel --> True

a = b"aki"       # --> Inisialisasi variabel yang menyimpan data bytes
b = b"aki"       # --> Inisialisasi variabel yang menyimpan data bytes
results = a == b # --> Menggunakan operator ==, apakah nilai variabel a sama dengan nilai variabel b dan tersimpan pada variabel results
print("Sama dengan(==) = ", results)   # --> Mencetak variabel --> True

a = bytearray(b"aki") # --> Inisialisasi variabel yang menyimpan data bytearray
b = bytearray(b"aki") # --> Inisialisasi variabel yang menyimpan data bytearray
results = a == b      # --> Menggunakan operator ==, apakah nilai variabel a sama dengan nilai variabel b dan tersimpan pada variabel results
print("Sama dengan(==) = ", results)   # --> Mencetak variabel --> True


print("-------->")

# Tidak Sama Dengan (!=)

a = True         # --> Inisialisasi variabel yang meyimpan data boolean
b = False        # --> Inisialisasi variabel yang menyimpan data boolean
results = a != b # --> Menggunakan operator !=, apakah nilai variabel a tidak sama dengan nilai variabel b dan tersimpan pada variabel results
print("Tidak sama dengan(!=) = ", results)   # --> Mencetak variabel --> True

a = 5            # --> Inisialisasi variabel yang menyimpan data integer
b = 3            # --> Inisialisasi variabel yang menyimpan data integer
results = a != b # --> Menggunakan operator !=, apakah nilai vaiabel a tidak sama dengan nilai variabel b dan tersimpan pada variabel results
print("Tidak sama dengan(!=) = ", results)   # --> Mencetak variabel --> True

a = 5.5          # --> Inisialisasi variabel yang menyimpan data float
b = 3.3          # --> Inisialisasi variabel yang menyimpan data float
results = a != b # --> Menggunakan operator !=, apakah nilai variabel a tidak sama dengan nilai variabel b dan tersimpan pada variabel results
print("Tidak sama dengan(!=) = ", results)   # --> Mencetak variabel --> True

a = "Jawa"       # --> Inisialisasi variabel yang menyimpan data string
b = "Tengah"     # --> Inisialisasi variabel yang menyimpan data string
results = a != b # --> Menggunakan operator !=, apakah nilai variabel a tidak sama dengan nilai variabel b dan tersimpan pada variabel results
print("Tidak sama dengan(!=) = ", results)   # --> Mencetak variabel --> True

a = [1,2,3]      # --> Inisialisasi variabel yang menyimpan data list, berisi 3 elemen data integer
b = [1,2,3]      # --> Inisialisasi variabel yang menyimpan data list, berisi 3 elemen data integer
results = a != b # --> Menggunakan operator !=, apakah nilai variabel a tidak sama dengan nilai variabel b dan tersimpan pada variabel results
print("Tidak sama dengan(!=) = ", results)   # --> Mencetak variabel --> False

a = (1,2,3)      # --> Inisialisasi variabel yang menyimpan data tuple, berisi 3 elemen data integer
b = (1,2,3)      # --> Inisialisasi variabel yang menyimpan data tuple, berisi 3 elemen data integer
results = a != b # --> Menggunakan operator !=, apakah nilai variabel a tidak sama dengan nilai variabel b dan tersimpan pada variabel results
print("Tidak sama dengan(!=) = ", results)   # --> Mencetak variabel --> False

a = {"a":1, "b":2} # --> Inisialisasi variabel yang menyimpan data dict, berisi 2 key-value --> Note: Hanya untuk pengecekan kesetaraan atau ketidaksamaan
b = {"a":1, "b":2} # --> Inisialisasi variabel yang menyimpan data dict, berisi 2 key-value
results = a != b   # --> Menggunakan operator !=, apakah nilai variabel a tidak sama dnegan nilai variabel b dan tersimpan pada variabel results
print("Tidak sama dngan(!=) = ", results)    # --> Mencetak variabel --> False

a = {1,2,3}      # --> Inisialisasi variabel yang mennyimpan data set, berisi 3 elemen data integer --> Note: Hanya untuk pengecekan kesetaraan atau ketidaksamaan
b = {1,2,3}      # --> Inisialisasi variabel yang menyimpan data set, berisi 3 elemen data integer
results = a != b # --> Menggunakan operator !=, apakah nilai vriabel a tidak sama dengan nilai variabel b dan tersimpan pada variabel results
print("Tidak sama dengan(!=) = ", results)   # --> Mencetak variabel --> False

a = None         # --> Inisialisasi variabel yang menyimpan data None --> Note: Hanya untuk pengecekan kesetaraan atau ketidaksamaan
b = None         # --> Inisialisasi variabel yang menyimpan data None 
results = a != b # --> Menggunakan operator !=, apakah nilai variabel a tidak sama dengan nilai variabel b dan tersimpan pada variabel results
print("Tidak sama dnegan(!=) = ", results)   # --> Mencetak variabel --> False

a = b"aki"       # --> Inisialisasi variabel yang menyimpan data bytes
b = b"aki"       # --> Inisialisasi variabel yang menyimpan data bytes
results = a != b # --> Menggunakan operator !=, apakah nilai variabel a tidak sama dengan nilai variabel b dan tersimpan pada variabel results
print("Tidak sama dengan(!=) = ", results)   # --> Mencetak variabel --> False

a = bytearray(b"aki") # --> Inisialisasi variabel yang menyimpan data bytearray
b = bytearray(b"aki") # --> Inisialisasi variabel yang menyimpan data bytearray
results = a != b      # --> Menggunakan operator !=, apakah nilai variabel a tidak sama dengan nilai variabel b dan tersimpan pada variabel results
print("Tidak sama dengan(!=) = ", results)   # --> Mencetak variabel --> False


print("-------->")

# Lebih Besar Dari (>)

a = True        # --> Inisialisasi variabel yang menyimpan data boolean
b = False       # --> Inisialisasi variabel yang menyimpan data boolean 
results = a > b # --> Menggunakan operator >, apakah nilai variabel a lebih besar dari nilai variabel b dan tersimpan pada variabel results 
print("Lebih besar dari(>) = ", results)  # --> Mencetak variabel --> True

a = 5           # --> Inisialisasi vriabel yang menyimpan data integer
b = 3           # --> Inisialisasi variabel yang menyimpan data integer
results = a > b # --> Menggunakan operator >, apakah nilai variabel a lebih besar dari nilai variabel b dan tersimpan pada variabel results
print("Lebih besar dari(>) = ", results)  # --> Mencetak variabel --> True

a = 5.5         # --> Inisialisasi variabel yang menyimpan data float
b = 3.3         # --> Inisialisasi variabel yang menyimpan data float
results = a > b # --> Menggunakan operator >, apakah nilai variabel a lebih besar dari nilai variabel b dan tersimpan pada variabel results
print("Lebih besar dari(>) = ", results)  # --> Mencetak variabel --> True

a = "Jawa"      # --> Inisialisasi variabel yang menyimpan data string
b = "Tengah"    # --> Inisialisasi variabel yang menyimpan data string
results = a > b # --> Menggunakan operator >, apakah nilai variabel a lebih besar dari nilai variabel b (dibandingkan berdasarkan urutan leksikografis atau panjang teks dan besar kecil huruf paling depan) dan tersimpan pada variabel results
print("Lebih besar dari(>) = ", results)   # --> Mencetak variabel --> False

a = [1,2,3]      # --> Inisialisasi variabel yang menyimpan data list, berisi 3 elemen data integer
b = [4,5,6]      # --> Inisialisasi variabel yang menyimpan data list, berisi 3 elemen data integer
results = a > b  # --> Menggunakan operator >, apakah nilai variabel a lebih besar dari nilai variabel b (dibandingkan elemen per-elemen, nilai elemen besar paling depan diutamakan) dan tersimpan pada variabel results
print("Lebih besar dari(>) = ", results)   # --> Mencetak variabel --> False

a = (1,2,3)      # --> Inisialisasi variabel yang menyimpan data tuple, berisi 3 elemen data integer
b = (4,5,6)      # --> Inisialisasi variabel yang menyimpan data tuple, berisi 3 elemen data integer
results = a > b  # --> Menggunakan operator >, apakah nilai variabel a lebih besar dari nilai variabel b (dibandingkan elemen-perelemen, nilai elemen besar paling depan diutamakan) dan tersimpan pada variabel results
print("Lebih besar dari(>) = ", results)   # --> Mencetak variabel --> False

a = b"jawa"      # --> Inisialisasi variabel yang menyimpan data bytes
b = b"jateng"       # --> Inisialisasi variabel yang menyimpan data bytes
results = a > b  # --> Menggunakan operator >, apakah nilai variabel a lebih besar dari nilai variabel b (huruf depan  harus sama kecil/besar, lalu selanjutnya boleh huruf besar dan panjang teks, beda teks tidak mempengaruhinya) dan tersimpan pada variabel results
print("Lebih besar dari(>) = ", results)      # --> Mencetak variabel --> True

print("Memek lala")

a = bytearray(b"aki")  # --> Inisialisasi variabel yang menyimpan data bytearray
b = bytearray(b"jaki") # --> Inisialisasi variabel yang menyimpan data bytearray
results = a > b        # --> Menggunakan operator >, apakah nilai vairiabel a lebih besar dari nilai variabel b dan tersimpan pada variabel results
print("Lebih besar dari(>) = ", results)      # --> Mencetak variabel --> False

# --> Tidak bisa menggunakan tipe data None
# --> Tidak bisa menggunakan tipe data set
# --> Tidak bisa menggunakan tipe data dict


print("-------->")    

# Lebih Kecil Dari (<)

a = True        # --> Inisialisasi variabel yang menyimpan data boolean
b = False       # --> Inisialisasi variabel yang menyimpan data boolean
results = a < b # --> Menggunakan operator <, apakah nilai variabel a lebih kecil dari nilai variabel b dan tersimpan pada variabel results
print("Lebih kecil dari(<) = ", results)  # --> Mencetak variabel --> False

a = 5           # --> Inisialisasi variabel yang menyimpan data integer
b = 3           # --> Inisialisasi variabel yang menyimpan data integer
results = a < b # --> Menggunakan operator <, apakah nilai variabel a lebih kecil dari nilai variabel b dan tersimpan pada variabel results
print("Lebih kecil dari(<) = ", results)  # --> Mencetak variabel --> False

a = 5.5         # --> Inisialisasi variabel yang menyimpan data float
b = 3.3         # --> Inisialisasi variabel yang menyimpan data float
results = a < b # --> Menggunakan operator <, apakah nilai variabel a lebih kecil dari nilai variabel b dan tersimpan pada variabel results
print("Lebih kecil dari(<) = ", results)  # --> Mencetak variabel --> False

a = "Jawa"      # --> Inisialisasi variabel yang menyimpan data string
b = "Tengah"    # --> Inisialisasi variabel yang menyimpan data string
results = a < b # --> Menggunakan operator <, apakah nilai variabel a lebih kecil dari nilai variabel b (dibandingkan berdasarkan urutan lekssikografis atau panjang teks) dan tersimpan pada variabel results
print("Lebih kecil dari(<) = ", results)  # --> Mencetak variabel --> True

a = [1,2,3]     # --> Inisialisasi variabel yang menyimpan data list, berisi 3 elemen data integer
b = [4,5,6]     # --> Inisialisasi variabel yang menyimpan data list, berisi 3 elemen data integer
results = a < b # --> Menggunakan operator <, apakah nilai variabel a lebih kecil dari nilai variabel b (dibandingkan elemen per-elemen, nilai elemen kecil paling depan diutamakan) dan tersimpan pada variabel results
print("Lebih kecil dari(<) = ", results)  # --> Mencetak variabel --> True

a = (1,4,7)     # --> Inisialisasi variabel yang menyimpan data tuple, berisi 3 elemen data integer
b = (1,5,6)     # --> Inisialisasi variabel yang menyimpan data tuple, berisi 3 elemen data integer
results = a < b # --> Menggunakan operator <, apakah nilai variabel a lebih kecil dari nilai variabel b (dibandingkan elemen-perelemen, nilai elemen kecil paling depan diutamakan) dan tersimpan pada variabel results
print("Lebih kecil dari(<) = ", results)   # --> Mencetak variabel --> True

a = b"zAki"      # --> Inisialisasi variabel yang menyimpan data bytes
b = b"aki"       # --> Inisialisasi variabel yang menyimpan data bytes
results = a < b  # --> Menggunakan operator >, apakah nilai variabel a lebih kecil dari nilai variabel b (huruf depan  harus sama kecil/besar, lalu selanjutnya boleh huruf besar dan panjang teks, beda teks tidak mempengaruhinya) dan tersimpan pada variabel results
print("Lebih kecil dari(>) = ", results)      # --> Mencetak variabel --> True

a = bytearray(b"aki")  # --> Inisialisasi variabel yang menyimpan data bytearray
b = bytearray(b"jaki") # --> Inisialisasi variabel yang menyimpan data bytearray
results = a < b        # --> Menggunakan operator >, apakah nilai vairiabel a lebih kecil dari nilai variabel b dan tersimpan pada variabel results
print("Lebih kecil dari(>) = ", results)      # --> Mencetak variabel --> False


# --> Tidak bisa menggunakan tipe data None
# --> Tidak bisa menggunakan tipe data set
# --> Tidak bisa menggunakan tipe data dict


print("-------->")   

# Lebih Besar Atau Sama Dengan (>=)

a = True         # --> Inisialisasi variabel yang menyimpan data boolean
b = False        # --> Inisialisasi variabel yang menyimpan data boolean
results = a >= b # --> Menggunakan operator >=, apakah nilai variabel a lebih besar atau sama dengan nilai variabel b dan tersimpan pada variabel results 
print("Lebih besar atau sama dengan(>=) = ", results)   # --> Mencetak variabel --> True

a = 5            # --> Inisialisasi variabel yang menyimpan data integer
b = 3            # --> Inisialisasi variabel yang menyimpan data integer
results = a >= b # --> Menggunakan operator >=, apakah nilai variabel a lebih besar atau sama dengan nilai variabel b dan tersimpan pada variabel results
print("Lebih besar atau sama dengan(>=) = ", results)   # --> Mencetak variabel --> True

a = 5.5          # --> Inisialisasi variabel yang menyimpan data float
b = 3.3          # --> Inisialisasi variabel yang menyimpan data float
results = a >= b # --> Menggunakan operator >=, apakah nilai variabel a lebih besar atau sama dengan nilai variabel b dan tersipan pada variabel results
print("Lebih besar atau sama dengan(>=) = ", results)   # --> Mencetak variabel --> True

a = "Tengah"     # --> Inisialisasi variabel yang menyimpan data string
b = "Tengah"     # --> Inisialisasi variabel yang menyimpan data string
results = a >= b # --> Menggunakan operator >=, apakah nilai variabel a lebih besar atau sama dengan nilai variabel b (dibandingkan berdasarkan urutan lekssikografis atau teks sama dan lebih panjang) dan tersimpan pada variabel results
print("Lebih besar atau sama dengan(>=) = ", results)   # --> Mencetak variabel --> True

a = [4,2,3]      # --> Inisialisasi variabel yang menyimpan data list, berisi 3 elemen data integer
b = [4,5,6]      # --> Inisialisasi variabel yang menyimpan data list, berisi 3 elemen data integer
results = a >= b # --> Menggunakan operator >=, apakah nilai variabel a lebih besar atau samadengan nilai variabel b (dibandingkan elemen per-elemen, nilai elemen besar paling depan diutamankan) dan tersimpan pada variabel results
print("Lebih besar atau sama dengan(>=) = ", results)   # --> Mencetak varibel --> False

a = (1,2,3)      # --> Inisialisasi variabel yang menyimpan data tuple, berisi 3 elemen data integer
b = (1,2,3)      # --> Inisialisasi variabel yang menyimpan data tuple, berisi 3 elemen data integer
results = a >= b # --> Menggunakan operator >=, apakah nilai variabel a lebih besar atau samadengan nilai variabel b (dibandingkan elemen per-elemen, nilai elemen besar paling depan diutamakan) dan tersimpan pada variabel results
print("Lebih besar atau sama dengan(>=) = ", results)   # --> Mencetak variabel --> True   

a = b"zAki"      # --> Inisialisasi variabel yang menyimpan data bytes
b = b"aki"       # --> Inisialisasi variabel yang menyimpan data bytes
results = a >= b  # --> Menggunakan operator >, apakah nilai variabel a lebih besar atau sama dengan nilai variabel b (huruf depan  harus sama kecil/besar, lalu selanjutnya boleh huruf besar dan panjang teks, beda teks tidak mempengaruhinya) dan tersimpan pada variabel results
print("Lebih besar atau sama dengan(>=) = ", results)   # --> Mencetak variabel --> True

a = bytearray(b"aki")  # --> Inisialisasi variabel yang menyimpan data bytearray
b = bytearray(b"jaki") # --> Inisialisasi variabel yang menyimpan data bytearray
results = a >= b        # --> Menggunakan operator >, apakah nilai vairiabel a lebih besar atau sama dengan nilai variabel b dan tersimpan pada variabel results
print("Lebih besar atau sama dengan(>=) = ", results)   # --> Mencetak variabel --> False


# --> Tidak bisa menggunakan tipe data None
# --> Tidak bisa menggunakan tipe data set
# --> Tidak bisa menggunakan tipe data dict


print("-------->")     

# Lebih Kecil Atau Sama Dengan (<=)

a = True         # --> Inisialisasi variabel yang menyimpan data boolean
b = False        # --> Inisialisasi variabel yang menyimpan dat bolean
results = a <= b # --> Mengghunakan operator <=, apakah nilai variabel a lebih kecil sama dengan nilai variabel b dan tersimpan pada variabel results 
print("Lebih kecil atau sama dengan(<=) = ", results)  # --> Mencetak variabel --> False

a = 5            # --> Inisialisasi variabel yang menyimpan data integer
b = 3            # --> Inisialisasi variabel yang menyimpan data integer
results = a <= b # --> Menggunakan operator <=, apakah nilai variabel a lebih kecil sama dengan nilai variabel b dan tersimpan pada variabel results
print("Lebih kecil atau sama dengan(<=) = ", results)  # --> Mencetak variabel --> False

a = 5.5          # --> Inisialisasi variabel yang menyimpan data float
b = 3.3          # --> Inisialisasi variabel yang menyimpan data float
results = a <= b # --> Menggunakan operator <=, apakah nilai variabel a lebih kecil sama dengan nilai variabel b dan tersimpan pada variabel results
print("Lebih kecil atau sama dengan(<=) = ", results)  # --> Mencetak variabel --> False

a = "Tengah"     # --> Inisialisasi variabel yang menyimpan data string
b = "Tengah"     # --> Inisialisasi variabel yang menyimpan data string
results = a <= b # --> Menggunakan operator <=, apakah nilai variabel a lebih kecil sama dengan nilai variabel b (dibandingkan berdasarkan urutan leksikografis atau teks sama dan lebih pendek) dan tersimpan pada variabel results
print("Lebih kecil atau sama dengan(<=) = ", results)   # --> Mencetak variabel --> True

a = [1,2,3]      # --> Inisialisasi variabel yang menyimpan data list, berisi 3 elemen data integer
b = [4,5,6]      # --> Inisialisasi variabel yang menyimpan data list, berisi 3 elemen data integer
results = a <= b # --> Menggunakan operator <=, apakah nilai variabel a lebih kecil sama dengan nilai variabel b (dibandingkan elemen per-elemen, nilai elemen kecil paling depan diutamakan) dan tersimpan pada variabel results
print("Lebih kecil atau sama dengan(<=) = ", results)   # --> Mencetak variabel --> True

a = (1,2,3)      # --> Inisialisasi variabel yang menyimpan data tuple, berisi 3 elemen data integer
b = (1,2,3)      # --> Inisialisasi variabel yang menyimpan data tuple, berisi 3 elemen data integer
results = a <= b # --> Menggunakan operator <=, apakah nilai vriabel a lebih kecil sama dengan nilai variabel b (dibandingkan elemen per-elemen, nilai elemen kecil paling depan diutamakan) dan tersimpan pada variabel results
print("Lebih kecil atau sama dengan(<=) = ", results)   # --> Mencetak variabel --> True

a = b"zAki"      # --> Inisialisasi variabel yang menyimpan data bytes
b = b"aki"       # --> Inisialisasi variabel yang menyimpan data bytes
results = a <= b  # --> Menggunakan operator >, apakah nilai variabel a lebih besar atau sama dengan nilai variabel b (huruf depan  harus sama kecil/besar, lalu selanjutnya boleh huruf besar dan panjang teks, beda teks tidak mempengaruhinya) dan tersimpan pada variabel results
print("Lebih kecil atau sama dengan(<=) = ", results)   # --> Mencetak variabel --> False

a = bytearray(b"aki")  # --> Inisialisasi variabel yang menyimpan data bytearray
b = bytearray(b"jaki") # --> Inisialisasi variabel yang menyimpan data bytearray
results = a <= b        # --> Menggunakan operator >, apakah nilai vairiabel a lebih besar atau sama dengan nilai variabel b dan tersimpan pada variabel results
print("Lebih kecil atau sama dengan(<=) = ", results)   # --> Mencetak variabel --> True


# --> Tidak bisa menggunakan tipe data None
# --> Tidak bisa menggunakan tipe data set
# --> Tidak bisa menggunakan tipe data dict



print("-------->") 

# 3. Operator Logika --> Untuk Melakukan Operasi Logis Pada Ekspresi Boolean (True Atau False) Dan Biasanya Digunakan Dalam Kondisi if, while Atau Pernyataan Logika Lainnya

# And (Mengembalikan True Jika Kedua Kondisi Bernilai True)

a = True          # --> Inisialisasi variabel yang menyimpan data boolean
b = False         # --> Inisialisasi variabel yang menyimpan data boolean
results = a and b # --> Menggunakan operator and, menggabungkan variabel a, b lalu jika salah satu nilai vriabel False maka akan menghasilkan False dan tersimpan pada variabel results
print("And = ", results)    # --> Mencetak variabel --> False

a = True          # --> Inisialisasi variabel yang menyimpan data boolean
b = True          # --> Inisialisasi variabel yang menyimpan data boolean
results = a and b # --> Menggunakan operator and, menggbaungkan variabel a, b lalu jika kedua nilai variabel True maka akan menghasilkan True dan terimpan pada variabel results
print("And = ", results)    # --> Mencetak variabel --> True

a = False         # --> Inisialisasi variabel yang menyimpan data boolean
b = False         # --> Inisialisasi variabel yang menyimpan data boolean
results = a and b # --> Menggunakan operator and, menggbungkan variabel a, b lalu jika kedua nilai variabel False maka akan menghasilkan False dan tersimpan pada variabel results
print("And = ", results)    # --> Mencetak variabel --> False

a = 0             # --> Inisialisasi variabel yang menyimpan data integer
b = 5             # --> Inisialisasi variabel yang menyimpan data integer
results = a and b # --> Menggunakan operator and, menggabungkan variabel a, b lalu jika salah satu nilai variabel False maka akan menghasilkan False dan tersimpan pada variabel results
print("And = ", results)   # --> Mencetak variabel --> 0 False

a = 0.0           # --> Inisialisasi variabel yang menyimpan data float
b = 5.5           # --> Inisialisasi variabel yang menyimpan data float
results = a and b # --> Menggunakan operator and, menggabungkan variabel a, b lalu jika salah satu nilai vairbel False maka akan menghasilkan False dan tersimpan pada variabel results
print("And = ", results)   # --> Mencetak variabel --> 0.0 False

a = ""            # --> Inisialisasi variabel yang menyimpan data string kosong
b = "Zaki"        # --> Inisialisasi variabel yang menyimpan data string
results = a and b # --> Menggunakan operator and, menggabungkan variabel a, b lalu jika salah satu nilai variabel False maka akan menghasilkan False dan tersimpan pada variabel results
print("And = ", results)     # --> Mencetak variabel --> "" False

a = []            # --> Inisialisasi variabel yang menyimpan data list, berisi elemen kosong
b = [1,2,3,4,5]   # --> Inisialisasi variabel yang menyimpan data list, berisi 5 elemen data integer
results = a and b # --> Menggunakan operator and, menggabungkan variabel a, b lalu jika salah satu nilai variabel False maka akan menghasilkan False dan tersimpan pada varibel results
print("And = ", results)    # --> Mencetak variabel --> [] False

a = ()            # --> Inisialisasi variabel yang menyimpan data tupel, berisi elemen kosong
b = (1,2)         # --> Inisialisasi variabel yang menyimpan data tupel, berisi 2 elemen data integer
results = a and b # --> Menggunakan operator and, menggabungkan variabel a, b lalu jika salah satu nilai variabel False maka akan menghasilkan False dan tersimpan pada variabel results
print("And = ", results)     # --> Mencetak variabel --> () False

a = {}              # --> Inisialisasi variabel yang menyimpan data dict, tidak berisi key-value
b = {"key":"value"} # --> Inisialisasi variabel yang menyimpan data dict, berisi 1 key-value
results = a and b   # --> Menggunakan operator and, menggbaungkan variabel a, b lalu jika salah satu nilai variabel False maka akan menghasilkan False dan tersimpan pada variabel results
print("And = ", results)     # --> Mencetak variabel --> {} False

a = set()           # --> Inisialisasi variabel yang menyimpan data set, berisi elemen kosong
b = {1,2,3,4,5}     # --> Inisialisasi variabel yang menyimpan data set, berisi 5 elemen data integer
results = a and b   # --> Menggunakan operator and, menggabungkan variabel a, b lalu jika salah satu nilai variabel False maka akan menghasilkan False dan tersimpan pada variabel results
print("And = ", results)     # --> Mencetak variabel --> set() False

a = None            # --> Inisialisasi variabel yang menyimpan data None
b = "Python"        # --> Inisialisasi variabel yang menyimpan data string
results = a and b   # --> Menggunakan operator and, menggabungkan variabel a, b lalu jika salah satu nilai variabel False maka akan menghasilkan False dan tersimpan pada variabel results
print("And = ", results)     # --> Mencetak variabel --> None False

a = b""             # --> Inisialisasi variabel yang menyimpan data bytes
b = b"satu"         # --> Inisialisasi variabel yang menyimpan data bytes
results = a and b   # --> Menggunakan operator and, menggabungkan variabel a, b lalu jika salah satu nilai variabel False maka akan menghasilkan False dan tersimpan pada variabel results
print("And = ", results)     # --> Mencetak variabel --> b'' False

a = bytearray(b"")     # --> Inisialisasi variabel yang menyimpan data byteaaray
b = bytearray(b"satu") # --> Inisialisasi variabel yang menyimpan data bytearray
results = a and b      # --> Menggunakan operator and, menggabungkan variabel a, b lalu jika salah satu nilai variabel False maka akan menghasilkan False dan tersimpan pada variabel results
print("And = ", results)     # --> Mencetak variabel --> bytearray(b'')


print("-------->") 

# Or (Mengembalikan True Jika Salah Satu Kondisi Bernilai True)

a = True          # --> Inisialisasi variabel yang menyimpan data boolean
b = False         # --> Inisialisasi variabel yang menyimpan data boolean
results = a or b  # --> Menggunakan operator or, menggabungkan nilai variabel a, b lalu jika salah satu nilai variabel True maka akan menghasilkan True dan tersimpan pada variabel results
print("Or = ", results)    # --> Mencetak variabel --> True

a = True          # --> Inisialisasi variabel yang menyimpan data boolean
b = True          # --> Inisialisasi variabel yang menyimpan data boolean
results = a or b  # --> Menggunakan operator or, menggabungkan nilai variabel a, b lalu jika kedua nilai variabel True maka akan menghasilkan True dan tersimpan pada variabel results
print("Or = ", results)   # --> Mencetak variabel --> True

a = False         # --> Inisialisasi variabel yang menyimpan data boolean
b = False         # --> Inisialisasi variabel yang menyimpan data boolean
results = a or b  # --> Menggunakan operator or, menggabungkan nilai variabel a, b lalu jika kedua nilai variabel False maka akan menghasilkan False dan tersimpan pada variabel results
print("Or = ", results)    # --> Mencetak variabel --> False

a = 0             # --> Inisialisasi variabel yang menyimpan data integer
b = 5             # --> Inisialisasi variabel yang menyimpan data integer
results = a or b  # --> Menggunakan operator or, menggabungkan nilai variabel a, b lalu jika salah satu nilai variabel True maka akan mengembalikan True dan tersimpan pada variabel results
print("Or = ", results)   # --> Mencetak variabel --> 5 True

a = 0.0           # --> Inisialisasi variabel yang menyimpan data float
b = 5.5           # --> Inisialisasi variabel yang menyimpan data float
results = a or b  # --> Menggunakan operator or, menggabungkan nilai variabel a, b lalu jika salah satu nilai variabel True maka akan mengembalikan True dan tersimpan pada variabel results
print("Or = ", results)   # --> Mencetak variabel --> 5.5 True

a = ""            # --> Inisialisasi variabel yang menyimpan data string kosong
b = "Zaki"        # --> Inisialisasi variabel yang menyimpan data string
results = a or b  # --> Menggunakan operator or, menggabungkan nilai variabel a, b lalu jika salah satu nilai variabel True maka akan mengembalikan True dan tersimpan pada variabel results
print("Or = ", results)   # --> Mencetak variabel --> Zaki True

a = []            # --> Inisialisasi variabel yang menyimpan data list, berisi elemen kosong
b = [1,2,3,4,5]   # --> Inisialisasi variabel yang menyimpan data list, berisi 5 elemen data integer
results = a or b  # --> Menggunakan operator or, menggabungkan nilai variabel a, b lalu jika salah satu nilai variabel True maka akan mengembalikan True dan tersimpan pada variabel results
print("Or = ", results)   # --> Mencetak variabel --> [1,2,3,4,5] True

a = ()            # --> Inisialisasi variabel yang menyimpan data tuple, berisi elemen kosong
b = (1,2)         # --> Inisialisasi variabel yang menyimpan data tuple, berisi 2 elemen data integer
results = a or b  # --> Menggunakan operator or, Menggabungkan nilai variabel a, b lalu jika salah satu nilai variabel True maka akan mengembalikan True dan tersimpan pada variabel results
print("Or = ", results)    # --> Mencetak variabel --> (1,2) True

a = {}              # --> Inisialisasi variabel yang menyimpan data dict, tidak berisi key-value
b = {"key":"value"} # --> Inisialisasi variabel yang menyimpan data dict, berisi 1 key-value
results = a or b    # --> Menggunakan operator or, menggbungkan nilai variabel a, b jika salah satu nilai variabel True maka akan mengembalikan True dan tersimpan pada variabel results
print("Or = ", results)    # --> Mencetak variabel --> {"key":"value"} True

a = set()         # --> Inisialisasi variabel yang menyimpan data set, berisi elemen kosong
b = {1,2,3,4,5}   # --> Inisialisasi variabel yang menyimpan data set, berisi 5 elemen data integer
results = a or b  # --> Menggunakan operator or, menggabungkan nilai variabel a, b jika salah satu nilai variabel True maka akan mengembalikan True dan tersimpan pada variabel results
print("Or = ", results)   # --> Mencetak variabel --> {1,2,3,4,5} True

a = None          # --> Inisialisasi variabel yang menympan data None
b = "Python"      # --> Inisialisasi variabel yang meyimpan data string
results = a or b  # --> Menggunakan operator or, menggabungkan nilai variabel a, b jika salah satu nilai variabel True maka akan mengembalikan True dan tersimpan pada variabel results
print("Or = ", results)   # --> Mencetak variabel --> Python True

a = b""           # --> Inisialisasi variabel yang menyimpan data bytes
b = b"satu"       # --> Inisialisasi variabel yang menyimpan data bytes
results = a or b  # --> Menggunakan operator or, menggabungkan nilai variabel a, b jika salah satu nilai variabel True maka akan mengembalikan True dan tersimpan pada variabel results
print("Or = ", results)   # --> Mencetak variabel --> b'sat' True

a = bytearray(b"")     # --> Inisialisasi variabel yang menyimpan data bytearray
b = bytearray(b"satu") # --> Inisialisasi variabel yang menyimpan data bytearray
results = a or b       # --> Menggunakan operator or, menggabungkan nilai variabel a, b jika salah satu nilai variabel True makan akan mengahsilkan True dan tersimpan pada variabel results
print("Or = ", results)   # --> Mencetak variabel --> bytearray(b'sat') True


print("-------->") 

# Not (Membalikan Nilai Kondisi)

a = False       # --> Inisialisasi variabel yang menyimpan daya boolean
results = not a # --> Menggunakan operator not, membalikan nilai variabel a lalu jika nilai variabel False maka akan menghasilkan True dan tersipan pada variabel results
print("Not = ", results)  # --> Mencetak variabel --> True

a = 0           # --> Inisialisasi variabel yang meyimpan data integer
results = not a # --> Menggunakan operator not, membalikan nilai variabel a lalu jika nilai variabel False maka akan menghasilkan True dan tersimpan pada variabel results
print("Not = ", results)  # --> Mencetak variabel --> True

a = 0.0         # --> Inisialisasi variabel yang menyimpan data float
results = not a # --> Menggunakan operator not, membalikan nilai variabel a lalu jika nilai variabel False maka akan menghasilkan True dan tersimpan pada variabel results
print("Not = ", results)  # --> Mencetak variabel --> True

a = ""          # --> Inisialisasi vriabel yang menyimpan data string kosong
results = not a # --> Menggunakan operator not, membalikan nilai variabel a lalu jika nilai variabel False maka akan menghasilkan True dan tersimpan pada variabel results
print("Not = ", results)  # --> Mencetak variabel --> True

a = []          # --> Inisialisasi variabel yang menyimpan data list, berisi elemen kosong
results = not a # --> Menggunakan operator not, membalikan nilai variabel a lalu jika nilai variabel False maka akan menghasilkan True dan tersimpan pada variabel results
print("Not = ", results)  # --> Mencetak variabel --> True

a = ()          # --> Inisialisasi variabel yang menyimpan data tupel kosong
results = not a # --> Menggunakan operator not, membalikan nilai variabel a lalu jika nilai variabel False maka akan menghasilkan True dan tersimpan pada variabel results
print("Not = ", results)  # --> Mencetak variabel --> True

a = {}          # --> Inisialisasi variabel yang menyimpan data dict, tidak berisi key-value
results = not a # --> Menggunakan operator not, membalikan nilai variabel a lalu jika nilai variabel False maka akan menghasilkan True dan tersimpan pada variabel results
print("Not = ", results)  # --> Mencetak variabel --> True

a = set()       # --> Inisialisasi variabel yang menyimpan data set, berisi elemen kosong
results = not a # --> Menggunakan operator not, membalikan nilai variabel a lalu jika nilai variabel False maka akan menghasilkan True dan tersimpan pada variabel results
print("Not = ", results)  # --> Mencetak variabel --> True

a = None        # --> Inisialisasi variabel yang menyinpan data None
results = not a # --> Menggunakan operator not, membalikan nilai variabel a lalu jika nilai variabel False maka akan menghasilkan Treu dan tersimpan pada variabel results
print("Not = ", results)  # --> Mencetak variabel --> True

a = b""         # --> Inisialisasi variabel yang menyimpan data bytes
results = not a # Menggunakan operator not, membalikan nilai variabel a lalu jika nilai variabel False maka akan menghasilkan True dan tersimpan pada vriabel results
print("Not = ", results)  # --> Mencetak variabel --> True


print("-------->")

# 4. Operator Penugasan Atau Assignment --> Untuk menetapkan nilai ke variabel

names = "Natashia"           # --> 'names' nama variabel, '=' operator assignment, dan 'Natashia' adalah nilai

print("-------->")

a = 5                        # --> Inisialisasi variabel yang menyimpan data integer
print("Penugasan(=) = ", a)  # --> Mencetak variabel --> 5

a = 5.5                      # --> Inisialisasi variabel yang menyimpan data float
print("Penugasan(=) = ", a)  # --> Mencetak variabel --> 5.5

a = "5"                      # --> Inisialisasi variabel yang menyimpan data string
print("Penugasan(=) = ", a)  # --> Mencetak variabel --> 5 string

a = [1, 2, 3, 4, 5]         # --> Inisialisasi variabel yang menyimpan data list, berisi 5 elemen data integer
print("Penugasan(=) = ", a)  # --> Mencetak variabel --> [1, 2, 3, 4, 5]

a = {"key1":"value1", "key2":"value2"}  # --> Inisialisasi variabel yang menyimpan data dict, berisi 2 key-value data string
print("Penugasan(=) = ", a)             # --> Mencetak variabel --> {"key1":"value1", "key2":"value2"}

a = {"a": 1, "b":2}                     # --> Inisialisasi variabel yang menyimpan data dict, berisi 2 key-value data integer
a ["a"] = "Ganti"                       # --> Mengganti value key a pada variabel a
a ["c"] = "Tambah"                      # --> Menambah key-value baru
print("Penugasan(=) = ", a)             # --> Mencetak variabel -->  {'a': 'Ganti', 'b': 2, 'c': 'Tambah'}

a = {1, 2, 3, 4, 5}          # --> Inisialisasi variabel yang menyimpan data set, berisi 5 elemen data integer
print("Penugasan(=) = ", a)  # --> Mencetak variabel --> {1, 2, 3, 4, 5}

a = (10, )                   # --> Inisialisasi variabel yang menyimpan data tuple, berisi 1 elemen data integer
print("Penugasan(=) = ", a)  # --> Mencetak variabel --> (10,)


print("-------->")

# Penugasan (+=, Menambahkan Nilai Ke Variabel Dan Menetapkan Hasilnya)

a = 5    # --> Inisialisasi variabel yang menyimpan data integer
a += 3   # --> Menambahkan nilai variabel a dan menetapkan hasilnya ke variabel itu sendiri
print("Penambahan(+=) = ", a)  # --> Mencetak variabel --> 8

a = 5.5  # --> Inisialisasi variabel yang menyimpan data float
a += 3.3 # --> Menambahkan nilai variabel a dan menetapkan hasilnya ke variabel itu sendiri
print("Penambahan(+=) = ")     # --> Mencetak variabel --> 8.8

a = "Coin "  # --> Inisialiasai variabel yang menyimpan data string
a += "Memew" # --> Menambahkan nilai variabel a dan menetapkan hasilnya ke variabel itu sendiri
print("Penambahan(+=) = ", a)  # --> Mencetak variabel --> Coin Memew

a = [1, 2, 3, 4, 5] # --> Inisialisasi variabel yang menyimpan data list, berisi 5 elemen data integer
a += [6]            # --> Menambahkan elemen data integer ke variabel a yang menyimpan data list dan menetapkan hasilnya ke variabel itu sendiri
print("Penambahan(+=) = ", a)  # --> Mencetak variabel --> [1, 2, 3, 4, 5]


print("-------->") 

# Penugasan (-=, Mengurangi Nilai Ke Variabel Dan Menetapkan Hasilnya)

a = 5    # --> Inisialisasi variabel yang menyimpan data integer
a -= 3   # --> Mengurangi nilai variabel a dan menetapkan hasilnya ke variabel itu sendiri
print("Pengurangan(-=) = ", a) # --> Mencetak variabel --> 2

a = 5.5  # --> Inisialisasi variabel yang menyimpan data float
a -= 3.3 # --> Mengurangi nilai variabel a dan menetapkan hasilnya ke variabel itu sendiri
print("Pengurangan(-=) = ", a) # --> Mencetak variabel --> 2.2

a = {1, 2, 3, 4, 5} # --> Inisialisasi variabel yang menyimpan data set, berisi 5 elemen data integer
a -= {2}            # --> Menghilangkan elemen 2 pada variabel a dan menetapkan hasilnya ke variabel itu sendiri
print("Pengurangan(-=) = ", a) # --> Mencetak variabel --> {1, 3, 4, 5}


print("-------->")

# Penugasan (*=, Mengalikan Nilai Ke Variabel Dan Menetapkan Hasilnya)

a = 5    # --> Inisialisasi variabel yang menyimpan data integer
a *= 3   # --> Mengalikan nilai variabel a dan menetapkan hasilnya ke variabel itu sendiri
print("Perkalian(*=) = ", a) # --> Mencetak variabel --> 15

a = 5.5  # --> Inisialisasi variabel yang menyimpan data float
a *= 3.3 # --> Mengalikan nilai variabel a dan menetapkan hasilnya ke variabel itu sendiri
print("Perkalian(*=) = ", a) # --> Mencetak variabel --> 18.15

a = [1, 2, 3, 4, 5] # --> Inisialisasi variabel yang menyimpan data list, berisi 5 elemen data integer
a *= 2              # --> Mengalikan elemen dalam vriabel a dan menetapkan hasilnya ke variabel itu sendiri
print("Perkalian(*=) = ", a) # --> Mencetak variabel --> [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]


print("-------->")

# Penugasan (/=, Membagi Nilai Ke Variabel Dan Menetapkan Hasilnya)-(Float)

a = 5    # --> Inisialisasi variabel yang menyimpan data integer
a /= 3   # --> Mebagi nilai variabel a dan menetapkan hasilnya ke variabel itu sendiri (hasil pembagian float)
print("Pembagian(/=) = ", a) # --> Mencetak variabel --> 1.6

a = 5.5  # --> Inisialisasi variabel yang menyimpan data float
a /= 3.3 # --> Membagi nilai variabel a dan menetapkan hasilnya ke variabel itu sendiri
print("Pembagian(/=) = ", a) # --> Mencetak variabel --> 1.6


print("-------->") 

# Penugasan (//=, Membagi Nilai Ke Variabel Dan Menetapkan Hasilnya)-(Integer)

a = 5     # --> Inisialisasi variabel yang menyimpan data integer
a //= 3   # --> Mebagi nilai variabel a dan menetapkan hasilnya ke variabel itu sendiri (hasil pembgian integer)
print("Pembagian(//=) = ", a)  # --> Mencetak variabel --> 1

a = 5.5   # --> Inisialisasi variabel yang menyimpan data float
a //= 3.3 # --> Membagi nilai variabel a dan menetapkan hasilnya ke variabel itu sendiri
print("Pembagian(//=) = ", a)  # --> Mencetak variabel --> 1.1


print("-------->") 

# Penugasan (%=, Sisa Hasil Pembagian Nilai Ke Variabel Dan Menetapkan Hasilnya)

a = 5    # --> Inisialisasi variabel yang menyimpan data integer
a %= 3   # --> Sisa hasil pembagian nilai variabel a dan menetapkan hasilnya ke variabel itu sendiri
print("Modulo(%=) = ", a) # --> Mencetak variabel --> 2

a = 5.5  # --> Inisialisasi variabel yang menyinpan data float
a %= 3.3 # --> Sisa hasil pembagian nilai variabel a dan menetapkan hasilnya ke variabel itu sendiri
print("Modulo(%=) = ", a) # --> Mencetak variabel --> 2.2


print("-------->")

# Penugasan (**=, Memangkatkan Nilai Ke Variabel Dan Menetapkan Hasilnya) 

a = 5    # --> Inisialisasi variabel yang menyimpan data inetegr
a **= 3  # --> Memangkatkan nilai variabel a dan menetapkan hasilnya ke variabel itu sendiri
print("Pemangkatan(**=) = ", a) # --> Mencetak variabel --> 125

a = 5.5  # --> Inisialisasi variabel yang menyimpan data float
a **= 2  # --> Memangkatkan nilai variabel a dan menetapkan hasilnya ke variabel itu sendiri
print("Pemangkatan(**=) = ", a) # --> Mencetak variabel --> 30.25


print("-------->")

# 5. Operator Bitwise --> Untuk operasi bit per bit pada angka biner (digunakan pada tipe data integer, bytearray dan boolean)

# AND Bitwise (&)

a = 5           # --> Inisialisasi variabel yang menyimpan data integer (bit 0101)
b = 3           # --> Inisialisasi variabel yang menyimpan data integer (bit 0011)
results = a & b # --> Melakukan operasi AND dan tersimpan pada variabel results
print("And(&) = ", results)  # --> Mencetak variabel --> 1

a = bytearray([0b10101010])  # --> Inisialisasi variabel yang menyimpan data bytearray (byte dengan nilai biner 10101010)
b = bytearray([0b11001100])  # --> Inisialisasi variabel yang menyimpan data bytearray (byte dengan nilai biner 11001100)
results = a[0] & b[0]        # --> Melakukan Operasi AND dan tersimpan pada variabel results
print("And(&) = ", results)  # --> Mencetak variabel --> 136

a = True        # --> Inisialisasi variabel yang menyimpan data boolean (Treu atau 1)
b = False       # --> Inisialisasi variabel yang menyimpan data boolean (False atau 0)
results = a & b # --> Melakukan operasi AND dan tersimpan pada variabel results
print("And(&) = ", results)  # --> Mencetak variabel --> False


print("-------->") 

# OR Bitwise (|) 

a = 5           # --> Inisialisasi variabel yang menyimpan data integer (bit 0101)
b = 3           # --> Inisialisasi variabel yang menyimpan data integer (bit 0011)
results = a | b # --> Melakukan operasi OR dan tersimpan pada variabel results
print("Or(|) = ", results)   # --> Mencetak variebl --> 7

a = bytearray([0b10101010])  # --> Inisialisasi variabel yang menyimpan data bytearray (byte dengan nilai biner 10101010)
b = bytearray([0b11001100])  # --> Inisialisasi variabel yang menyimpan data bytearray (byte dengan nilai biner 11001100)
results = a[0] | b[0]        # --> Melakukan Operasi OR dan tersimpan pada variabel results
print("Or(|) = ", results)   # --> Mencetak variabel --> 238

a = True        # --> Inisialisasi variabel yang menyimpan data boolean (Treu atau 1)
b = False       # --> Inisialisasi variabel yang menyimpan data boolean (False atau 0)
results = a | b # --> Melakukan operasi OR dan tersimpan pada variabel results
print("Or(|) = ", results)   # --> Mencetak variabel --> True


print("-------->")  

# XOR Bitwise (^)

a = 5           # --> Inisialisasi variabel yang menyimpan data integer (bit 0101)
b = 3           # --> Inisialisasi variabel yang menyimpan data integer (bit 0011)
results = a ^ b # --> Melakukan operasi XOR dan tersimpan pada variabel results
print("Xor(^) = ", results)  # --> Mencetak variabel --> 6

a = bytearray([0b10101010])  # --> Inisialisasi variabel yang menyimpan data bytearray (byte dengan nilai biner 10101010)
b = bytearray([0b11001100])  # --> Inisialisasi variabel yang menyimpan data bytearray (byte dengan nilai biner 11001100)
results = a[0] ^ b[0]        # --> Melakukan Operasi XOR dan tersimpan pada variabel results
print("Xor(^) = ", results)  # --> Mencetak variabel --> 102

a = True        # --> Inisialisasi variabel yang menyimpan data boolean (Treu atau 1)
b = False       # --> Inisialisasi variabel yang menyimpan data boolean (False atau 0)
results = a ^ b # --> Melakukan operasi XOR dan tersimpan pada variabel results
print("Xor(^) = ", results)  # --> Mencetak variabel --> True


print("-------->") 

# NOT Bitwise (~) 

a = 5           # --> Inisialisasi variabel yang menyimpan data integer (bit 0101)
results = ~ a   # --> Melakukan operasi NOT dan tersimpan pada variabel results
print("Not(~) = ", results)  # --> Mencetak variabel --> -6

a = bytearray([0b10101010])  # --> Inisialisasi variabel yang menyimpan data bytearray (byte dengan nilai biner 10101010)
results = ~a[0]              # --> Melakukan Operasi NOT dan tersimpan pada variabel results
print("Not(~) = ", results)  # --> Mencetak variabel --> -171

#a = True        # --> Inisialisasi variabel yang menyimpan data boolean (Treu atau 1)
#b = False       # --> Inisialisasi variabel yang menyimpan data boolean (False atau 0)
#results = ~ a   # --> Melakukan operasi NOT dan tersimpan pada variabel results (ingat sering tidak digunakan untuk yang ini)
#print("Not(~) = ", results)  # --> Mencetak variabel


print("-------->")

# Shift Kiri Bitwise (<<)

a = 5             # --> Inisialisasi variabel yang menyimpan data integer (bit 0101)
results = a << 1  # --> Melakukan operasi Shift left atau menggeser bit ke kiri dan tersimpan pada variabel results
print("Shift kiri(<<) = ", results)    # --> Mencetak variabel --> 10

a = bytearray([0b10101010])  # --> Inisialisasi variabel yang menyimpan data bytearray (byte dengan nilai biner 10101010)
b = bytearray([0b11001100])  # --> Inisialisasi variabel yang menyimpan data bytearray (byte dengan nilai biner 11001100)
results = a[0] << b[0]       # --> Melakukan Operasi shift left dan tersimpan pada variabel results
print("Shift kiri(<<) = ", results)    # --> Mencetak variabel --> 43708+++

a = True          # --> Inisialisasi variabel yang menyimpan data boolean (Treu atau 1)
b = False         # --> Inisialisasi variabel yang menyimpan data boolean (False atau 0)
results = a << 1  # --> Melakukan operasi Shift dan tersimpan pada variabel results
print("Shift kiri(<<) = ", results)    # --> Mencetak variabel --> 2


print("-------->") 

# Shift Kanan Bitwise (>>)

a = 5             # --> Inisialisasi variabel yang menyimpan data integer (bit 0101)
results = a >> 1  # --> Melakukan operasi Shift right atau menggeser bit ke kanan dan tersimpan pada variabel results
print("Shift kanan(>>) = ", results)    # --> Mencetak variabel --> 2

a = bytearray([0b10101010])  # --> Inisialisasi variabel yang menyimpan data bytearray (byte dengan nilai biner 10101010)
b = bytearray([0b11001100])  # --> Inisialisasi variabel yang menyimpan data bytearray (byte dengan nilai biner 11001100)
results = a[0] >> b[0]       # --> Melakukan Operasi shift right dan tersimpan pada variabel results
print("Shift kanan(>>) = ", results)    # --> Mencetak variabel --> 0

a = True          # --> Inisialisasi variabel yang menyimpan data boolean (Treu atau 1)
b = False         # --> Inisialisasi variabel yang menyimpan data boolean (False atau 0)
results = a >> 1  # --> Melakukan operasi Shift right bit per bit yang tersimpan pada variabel results
print("Shift kanan(>>) = ", results)    # --> Mencetak variabel --> 0

# 6. Operator Keanggotaan Atau Membership --> Untuk Mengecek Apakah Suatu Nilai Merupakan Bagian Dari Data Kolektif Atau Tidak Dan Biasanya Digunakan Pada Semya Tipe Data Kolektif, Seperti Dict, Set, Tuple, Dan List
 

print("-------->") 

# In (Mengembalikan True Jika Elemen Ada Dalam koleksi Dan Jika Elemen Tidak Ada Dalam Koleksi Maka Mengembalikan False)

my_list = [1, 2, 3, 4, 5]   # --> Inisialisasi variabel yang menyimpan data list, berisi 5 elemen data integer
results = 2 in my_list      # --> Apakah elemen angka 2 berada dalam variabel my_list, jika ada maka mengembalikan True dan tersimpan pada variabel results
print("In = ", results)     # --> Mencetak variabel --> True

my_tuple = (1, 2, 3, 4, 5)  # --> Inisialisasi variabel yang menyimpan data tuple, berisi 5 elemen data integer
results = 2 in my_tuple     # --> Apakah elemen angka 2 berada dalam variabel my_tuple, jika ada maka mengembalikan True dan tersimpan pada variabel results
print("In = ", results)     # --> Mencetak variabel --> True

my_set = {1, 2, 3, 4, 5}    # --> Inisialisasi variabel yang menyimpan data set, berisi 5 elemen data integer
results = 2 in my_set       # --> Apakah angka 2 berada dalam variabel my_set, jika ada maka mengembalikan True dan tersimpan pada variabel results
print("In = ", results)     # --> Mencetak variabel --> True

my_dictionary = {"nama":"Zaki", "Asal": "Rusia"} # --> Inisialisasi variabel yang menyimpan data dict, berisi 2 key-value data string
results = "nama" in my_dictionary                # --> Apakah key nama dalam variabel my_dictionary, jika ada maka mengembalikan True dan tersimpan pada variabel results
print("In = ", results)                          # --> Mencetak variabel --> True

my_string = " Jangan Pernah Membuat Sakit Hati Seseorang Menggunakan kata " # --> Inisialisasi variabel yang menyimpan data string
results = "Hati" in my_string                                               # --> Apakah hati berada dalam variabel my_string, jika ada maka mengembalikan True dan tersimpan pada variabel results
print("In = ", results)                                                     # --> Mencetak variabel --> True

my_range = range(1, 5)  # --> Inisialisasi variabel yang menyimpan fungsi range atau urutan, berisi atau mencakup data integer 1 - 4
results = 2 in my_range # --> Apakah, anka 2 berada dalam cakupan fungsi range di variabel my_range, jika ada maka mengembalikan True dan tersimpan pada variabel results
print("In = ", results) # --> Mencetak variabel --> True


print("-------->") 

# Not In (Mengembalikan True Jika Elemen Tidak Ada Dalam Koleksi Dan Mengembalikan False Jika Elemen Berada Dalam Koleksi)

my_list = [1, 2, 3, 4, 5]   # --> Inisialisasi variabel yang menyimpan data list, berisi 5 elemen data integer
results = 6 not in my_list  # --> Apakah elemen angka 5 berada dalam variabel my_list, jika tidak ada maka mengembalikan True dan tersimpan pada variabel results
print("Not in = ", results) # --> Mencetak variabel --> True

my_tupel = (1, 2, 3, 4, 5)  # --> Inisialisasi variabel yang menyimpan data tuple, berisi 5 elemen data integer
results = 6 not in my_tuple # --> Apakah elemen angka 6 berada dalam variabel my_tuple, jika tidak ada maka mengembalikan True dan tersimpan pada variabel results
print("Not in = ", results) # --> Mencetak variabel --> True

my_set = {1, 2, 3, 4, 5}    # --> Inisialisasi variabel yang menyimpan data set, berisi 5 elemen data integer
results = 6 not in my_set   # --> Apakah elemen angka 6 berada dalam variabel my_set, jika tidak ada maka mengembalikan True dan tersimpan pada variabel results
print("Not in = ", results) # --> Mencetak variabel --> True

my_dictionary = {"nama":"Muhamad", "pets":"Anjing"} # --> Inisialisasi variabel yang menyimpan data dict, berisi 2 key-value data string dan tersimpan pada variabel results
results = "monyet" not in my_dictionary             # --> Apakah key monyet berada dalam variabel my_dictionary, jika tidak ada maka mengembalikan True dan tersimpan pada variabel result
print("Not in = ", results)                         # --> Mencetak variabel --> True

my_string = " Jaga Mulutmu Kalau Tidak Ingin Saya Balas " # --> Inisialisasi variabel yang menyimpan data string
results = "Fitnah" not in my_string                       # --> Apakah Fitnah berada dalam variabel my_string, jika tidak ada maka mengembalikan True dan tersimpan pada variabel results
print("Not in = ", results)                               # --> Mencetak variabel --> True

my_range = range(1, 5)      # --> Inisialisasi variabel yang menyimpan fungsi range, berisi atau mencakup data integer 1 hingga 4
results = 5 not in my_range # --> Apakah angka 5 berada dalam cakupan fungsi range di variabel my_range, jika tidak ada maka mengembalikan True dan tersimpan pada variabel results
print("Not in = ", results) # --> Mencetak variabel --> True


print("-------->") 

# 7. Opreator Identitas --> Untuk memeriksa apakah dua variabel mengacu pada objek yang sama di dalam memori dan membalik hasil dari ekpresi 

# Is (Untuk Memeriksa Apakah Dua Variabel Mengacu Pada Objek Yang Sama Di Dalam Memori, Maka Mengembalikan True)

my_integer1 = 97                     # --> Inisialisasi variabel yang menyimpan data integer
my_integer2 = 97                     # --> Inisialisasi variabel yang menyimpan data integer
results = my_integer1 is my_integer2 # --> Pada tipe data integer, python memperlakukan setiap inisialisasi data int dengan nilai yang sama sebagai objek yang sama di dalam memori maka mengembalikan True dan tersimpan pada variabel results
print("Is = ", results)              # --> Mencetak variabel --> True

my_boolean1 = True                   # --> Inisialisasi variabel yang menyimpan data boolean
my_boolean2 = True                   # --> Inisialisasi variabel yang menyimpan data boolean
results = my_boolean1 is my_boolean2 # --> Pada tipe data, boolean, python memperlakukan setiap inisialisasi data bool dengan nilai yang sama sebagai objek yang sama di dalam memori maka mengembalikan True dan tersimpan pada variabel results
print("Is = ", results)              # --> Mencetak variabel --> True

my_float1 = 5.5                      # --> Inisialisasi variabel yang menyimpan data float
my_float2 = 5.5                      # --> Inisialisasi variabel yang menyimpan data float
results = my_float1 is my_float2     # --> Pada tipe data float, python memperlakukan setiap inisialisasi data float dengan nilai yang sama sebagai objek yang sama di dalam memori maka mengembalikan True dan tersimpan pada variabel results
print("Is = ", results)              # --> Mencetak variabel --> True

my_string1 = "Zaki"                  # --> Inisialisasi variabel yang menyimpan data string
my_string2 = "Zaki"                  # --> Inisialisasi variabel yang menyimpan data string
results = my_string1 is my_string2   # --> Pada tipe data string, python memperlakukan setiap inisialisasi data string dengan nilai yang sama sebagai objek yang sama di dalam memori maka mengembalikan True dan tersimpan pada variabel results
print("Is = ", results)              # --> Mencetak variabel --> True

my_set1 = {1, 2, 3, 4, 5}            # --> Inisialisasi variabel yang menyimpan data set, berisi 5 elemen data integer
my_set2 = {1, 2, 3, 4, 5}            # --> Inisialisasi vairabel yang menyimpan data set, berisi 5 elemen data integer
results = my_set1 is my_set2         # --> Pada tipe data set python memperlakukan setiap inisialisasi data set sebagai objek yang berbeda di dalam memori, bahkan jika elemennya sama maka hasilnya False dan tersimpan pada variabel results
print("Is = ", results)              # --> Mencetak variabel --> False

my_list1 = [1, 2, 3, 4, 5]           # --> Inisialisasi variabel yang menyimpan data list, berisi 5 elemen data integer
my_list2 = [1, 2, 3, 4, 5]           # --> Inisialisasi variabel yang menyimpan data list, berisi 5 elemen data integer
results = my_list1 is my_list2       # --> Karena tipe data list bersifat mutable, python memperlakukan setiap inisialisasi data list sebagai objek yang berbeda di dalam memori, bahkan jika elemennya sama maka hasilnya False dan tersimpan pada variabel results
print("Is = ", results)              # --> Mencetak variabel --> False

my_tuple1 = (1, 2, 3, 4, 5)          # --> Inisialisasi variabel yang menyimpan data tuple, berisi 5 elemen data integer
my_tuple2 = (1, 2, 3, 4, 5)          # --> Inisialisasi variabel yang menyimpan data tuple, berisi 5 elemen data integer
results = my_tupel is my_tuple2      # --> Pada tipe data tuple, python memperlakukan setiap inisialisasi data tuple dengan elemen yang sama sebagai objek yang sama di dalam memori maka mengembalikan True dan tersimpan pada variabel results
print("Is = ", results)              # --> Mencetak variabel --> True

my_dict1 = {"key1":"value1", "key2":"value2"} # --> Inisialisasi variabel yang menyimpan data dict, berisi 2 key-value data string
my_dict2 = {"key1":"value1", "key2":"value2"} # --> Inisialisasi variabel yang menyimpan data dict, berisi 2 key-value data sting
results = my_dict1 is my_dict2                # --> Karena tipe data dict bersifat mutable, Python memperlakukan setiap inisialisasi data dict sebagai objek yang berbeda di dalam memori, bahkan jika key-value nya sama maka hasinya False dan tersimpan pada variabel results
print("Is = ", results)                       # --> Mencetak variabel --> False

class MyClass:                       # --> Membuat class dengan nama Myclass
    pass                             # --> Tidak ada kode yang dieksekusi, sehingga melajutkan mengeksekusi code berikutnya
obj1 = MyClass()                     # --> Inisialisasi variabel yang menyimpan data MyClass atau membuat objek(instance) dari kelas MyClass
obj2 = MyClass()                     # --> Inisialisasi variabel yang menyimpan data MyClass atau membuat objek(instance) dari kelas MyClass
results = obj1 is obj2               # --> Python memperlakukan setiap inisialisasi sebagai objek yang berbeda di dalam memori, bahkan jika keduanya dari class yang sama maka mengembalikan False dan tersimpan pada variabel results
print("Is = ", results)              # --> Mencetak variabel --> False


print("-------->")

# Is Not (Membalik Hasil Dari Ekspresi Is) 

my_int1 = 10                         # --> Inisialisasi variabel yang menyimpan data integer
my_int2 = 10                         # --> Inisialisasi variabel yang menyimpan data integer
results = my_int1 is not my_int2     # --> Pada tipe data integer, python memperlakukan setiap inisialisasi data int dengan nilai yang sama sebagai objek yang sama di dalam memori maka mengembalikan False karena not kebalikan dari is dan tersimpan pada variabel results
print("Is not = ", results)          # --> Mencetak variabel --> False

my_bool1 = True                      # --> Inisialisasi variabel yang menyimpan data boolean
my_bool2 = True                      # --> Inisialisasi variabel yang menyimpan data boolean
results = my_bool1 is not my_bool2   # --> Pada tipe data boolean, python memperlakukan setiap inisialisasi data boolean dengan nilai yang sama sebagai objek yang sama di dalam memori maka mengembalikan False karena not kebalikan dari is dan tersimpan pada variabel results
print("Is not = ", results)          # --> Mencetak variabel --> False

my_float1 = 2.2                      # --> Inisialisasi variabel yang menyimpan data float
my_float2 = 2.2                      # --> Inisailisasi variabel yang menyimpan data float
results = my_float1 is not my_float2 # --> Pada tipe data float, python memperlakukan setiap inisialisasi data float dengan nilai yang sama sebagai objek yang sama di dalam memori maka mengembalikan False karena not kebalikan dari is dan tersimpan pada variabel results
print("Is not = ", results)          # --> Mencetak variabel --> False

my_str1 = "Lala"                     # --> Inisialisasi variabel yang menyimpan data string
my_str2 = "Lala"                     # --> Inisialisasi variabel yang menyimpan data string
results = my_str1 is not my_str2     # --> Pada tipe data string, python memperlakukan setiap inisialisasi data string dengan nilai yang sama sebagai objek yang sama di dalam memori maka mengembalikan False karena not kebalikan dari is dan tersimpan pada variabel results
print("Is not = ", results)          # --> Mencetak variabel --> Flase

my_set1 = {1, 2, 3, 4, 5}            # --> Inisialisasi variabel yang menyimpan data set, berisi 5 elemen data integer
my_set2 = {1, 2, 3, 4, 5}            # --> Inisialisasi vairabel yang menyimpan data set, berisi 5 elemen data integer
results = my_set1 is not my_set2     # --> Pada tipe data set python memperlakukan setiap inisialisasi data set sebagai objek yang berbeda di dalam memori, bahkan jika elemennya sama maka hasilnya True karena not kebalikan dari is dan tersimpan pada variabel results
print("Is not = ", results)          # --> Mencetak variabel --> True

my_list1 = [1, 2, 3, 4]              # --> Inisialisasi variabel yang menyimpan data list, berisi 4 elemen data integer
my_list2 = [1, 2, 3, 4]              # --> Inisialisasi variabel yang menyimpan data list, berisi 4 elemen data integer
results = my_list1 is not my_list2   # --> Karena tipe data list bersifat mutable, python memperlakukan setiap inisialisasi data list sebagai objek yang berbeda di dalam memori, bahkan jika elemennya sama maka hasilnya True karena not kebalikan dari is dan tersimpan pada variabel results
print("Is not = ", results)          # --> Mencetak variabel --> True

my_tuple1 = (1, 2, 3, 4)             # --> Inisialisasi variabel yang menyimpan data tuple, berisi 4 elemen data integer        
my_tuple2 = (1, 2, 3, 4)             # --> Inisialisasi variabel yang menyimpan data tuple, berisi 4 elemen data integer
results = my_tuple1 is not my_tuple2 # --> Pada tipe data tuple, python memperlakukan setiap inisialisasi tuple dengan elemen yang sama sebagai objek yang sama di dalam memori maka mengembalikan False dan tersimpan pada variabel results
print("Is not = ", results)          # --> Mencetak variabel --> False

my_dict1 = {"key1": "valu11", "key2": "value2"} # --> Inisialisasi variabel yang menyimpan data dict, berisi 2 key-value data string
my_dict2 = {"key1": "value1", "key2": "value2"} # --> Inisialisasi variabel yang menyimpan data dict, berisi 2 key-value data string
results = my_dict1 is not my_dict2              # --> Karena tipe data dict bersifat mutable, Python memperlakukan setiap inisialisasi data dict sebagai objek yang berbeda di dalam memori, bahkan jika key-value nya sama maka hasinya True karena not kebalikan dari is dan tersimpan pada variabel results
print("Is not = ", results)                     # --> Mencetak variabel --> True

class MyClass:                       # --> Membuat kelas bernama MyClass
    pass                             # --> Tidak ada code yang dieksekusi, sehingga maelajutkan mengeksekusi code berikutnya
obj1 = MyClass()                     # --> Inisialisasi variabel yang menyimpan data MyClass atau membuat objek(instance) dari kelas MyClass
obj2 = MyClass()                     # --> Inisialisasi variabel yang menyimpan data Myclass atau membuat objek(instance) dari kelas MyClass
results = obj1 is not obj2           # --> Python memperlakukan setiap inisialisasi sebagai objek yang berbeda di dalam memori, bahkan jika keduanya dari class yang sama maka mengembalikan True karena not kebalikan dari is dan tersimpan pada variabel results
print("Is not = ", results)          # --> Mencetak variabel --> True


# 8. Fungsi print() Tanpa String Formating --> 

print("Pesan: %s %s %s" % ("Hi", "Python", "Telu")) # --> Menggunakan string formating
print("Pesan:", "Hi", "Python", "Telu")             # --> Tidak menggunakan string formating

# 9. Fungsi id() --> Digunakan Untuk Mengambil Nilai Identitas atau ID suatu Data

data = "Zaki"      # --> Inisialisasi variabel yang menyimpan data string
id_data = id(data) # --> Mengambil identitas unik (alamat memori) dari objek data
print(data)        # --> Mencetak variabel --> Zaki
print(id_data)     # --> Mencetak variabel --> 2535914452864 (ini nilai integer yang unik)


""" Note! """

# --> 1. Operator bitwise tidak bisa menggunakan bytes karena sifat tidak bisa diubah (immutable) 
# --> 2. Operator bitwise bisa menggunakan bytearray karena sifat dapat diubah (mutable)
# --> 3. Operator bitwise tidak berlaku untuk tipe data string, float, list, set, tuple dan dict
# --> 4. Operator perbandingan ==, != dapat digunakan pada semua tipe data untuk mengecek kesetaraan atau ketidaksamaan
# --> 5. Operator perbandingan >, <, >=, <= dapat digunakan pada tipe data yang mendukung urutan atau perbandingan langsung seperti angka, string, list dan tuple
# --> 6. Pengecekan nilai kosong (atau None) dianjurkan untuk selalu dilakukan menggunakan operator is, dan menghindari penggunaan operator == ...
# -->    Hal ini karena operator is membandingkan identitas data dan identitas data None selalu valid. Sedangkan operator == perbandingannya dilakukan dengan via special method __eq__() yang default method tersebut bisa di-override isinya
# --> 7. 