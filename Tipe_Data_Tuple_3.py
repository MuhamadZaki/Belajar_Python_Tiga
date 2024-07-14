# Praktekan dan Pahami!

# Tipe Data Canggih atau Koleksi

# 1. List
# 2. Tuple
# 3. Set
# 4. Dictionary

""" Tipe Data Tuple (Ordered-Terurut) - (Unchnagble-Tidak Bisa diubah) """

# Cara Standar Tuple
standar_tuple = ('Laki-laki', 'Perempuan') # --> Inisialisasi variabel yang menyimpan data tuple, berisi 2 elemen data string
print(standar_tuple)                       # --> Mencetak variabel standar_tuple dan hasilnya adalah Laki-laki, Perempuan

# Tanpa Kurung Tuple
tanpa_kurung_tuple = 'Tobrut', 'Ukhti'   # --> Inisialisasi variabel yang menyimpan data tuple, berisi 2 elemen data string
print(tanpa_kurung_tuple)                # --> Mencetak variabel dan hasilnya adalah Tobrut, Ukhti

Ini_sting_bukan_tuple = 'Tobrut'         # --> Inisialisasi variabel yang menyimpan data string (Ingat yang ini bukan tuple)
print(Ini_sting_bukan_tuple)             # --> Mencetak variabel dan hasilnya adalah Tobrut

# Tuple Kosong
tuple_kosong = ()   # --> Inisialisasi variabel yang menyimpan data tuple, tidak berisi elemen apapun atau kosong
print(tuple_kosong) # --> Mencetak variabel tuple_kosong dan hasinya adalah  ()

# Tupel Tunggal (Hanya Berisi Satu Item)
tuple_tunggal = (10) #    --> Inisialisasi variabel yang menyimpan data integer (Akan tetapi di Anggap Integer)
print(tuple_tunggal) # 10 --> Mencetak variabel tupel_tunggal

tuple_tunggal = (10,) #    --> Inisialisasi variabel yang menyimpan data tuple, berisi 1 elemen data integer (Ini Baru dianggap Tuple)
print(tuple_tunggal)  # 10 --> Mencetak variabel tuple_tunggal

print('-------------')

# Cara Standar (Mengakses Nilai Tuple dengan Langsung Mendefinisikan Indeks)
cara_standar_tuple = ('Tobrut', 'Era') # --> Inisialisasi variabel yang menyimpan data tuple, berisi 2 elemen data string
print(cara_standar_tuple[1])           # Era       --> Mencetak variabel
print(cara_standar_tuple[0])           # Tobrut    --> Mencetak variabel

# Mengakses Nilai Tuple dengan Negatif Indeks
cara_standar_tuple = ('Tobrut', 'Era') # --> Inisialisasi variabel yang menyimpan data tuple, berisi 2 elemen data string
print(cara_standar_tuple[-1])          # Era    --> Mencetak vriabel
print(cara_standar_tuple[-2])          # Tobrut --> Mencetak variabel


# Slicing Tuple
tuple_buah = ('Anggur', 'Melon', 'Nanas', 'Semangka') # --> Inisialisasi variabel yang menyimpan data tuple, berisi 4 elemen data string
print(tuple_buah[0:])                                 # Anggur, Melon, Nanas, Semangka dan Tak-terbatas --> Mencetak variabel dan slicing
print(tuple_buah[0:2])                                # Anggur, Melon                                   --> Mencetak variabel dan slicing
print(tuple_buah[1:3])                                # Melon, Nanas                                    --> Mencetak variabel dan slicing
print(tuple_buah[0:-1])                               # Anggur, Melon, Nanas                            --> Mencetak variabel dan slicing
print(tuple_buah[-1:-3])                              # Kosong                                          --> Mencetak variabel dan slicing
print(tuple_buah[-1:3])                               # Kosong                                          --> Mencetak variabel dan slicing
print(tuple_buah[-3:-1])                              # Melon, Nanas                                    --> Mencetak variabel dan slicing

# Slicing Tanpa Batas
tuple_buah = ('Anggur', 'Melon', 'Nanas', 'Semangka') # --> Inisialisasi variabel yang menyimpan data tuple, berisi 4 elemen data string
print(tuple_buah[0:])                                 # Anggur, Melon, Nanas, Semangka   --> Mencetak variabel dan slicing
print(tuple_buah[1:])                                 # Melon, Nanas, Semangka           --> Mencetak variabel dan slicing
print(tuple_buah[2:])                                 # Nanas, Semangka                  --> Mencetak variabel dan slicing
print(tuple_buah[3:])                                 # Semangka dan Tak-terbatas        --> Mencetak variabel dan slicing
print(tuple_buah[:0])                                 # []                               --> Mencetak variabel dan slicing
print(tuple_buah[:1])                                 # Anggur                           --> Mencetak variabel dan slicing
print(tuple_buah[:2])                                 # Anggur, Melon                    --> Mencetak variabel dan slicing
print(tuple_buah[:3])                                 # Anggur, Melon, Nanas             --> Mencetak variabel dan slicing
print(tuple_buah[:4])                                 # Anggur, Melon, Nanas, Semangka   --> Mencetak variabel dan slicing

print('-------------')

# Squence Unpaking (Mengekstrak Isi Dari Tuple ke Dalam Variable-Variable Tunggal, Secara Berurutan)
siswi = (' Natasia Tobrut', 'Makassar', 22) # --> Inisialisasi variabel yang menyimpan data tuple, berisi 3 elemen data string, string dan integer

nama, asal, usia = siswi # Ekstrak Data atau Juga dinamakan Sequence Unpacking (Setiap Variable Akan Memiliki Nilai dari Variable siswi)- yang pertama, nama maka mempunyai indeks [0]
print('Nama :', nama)    # Natasia Tobrut --> siswi[0] -nama   --> Mencetak variabel (String di dalam cuma untuk pemanis)
print('Asal : ', asal)   # Makassar       --> siswi[1] -asal   --> Mencetak variabel (String di dalam cuma untuk pemanis)
print('Usia : ', usia)   # 22             --> siswi[2] -usia   --> Mencetak variabel (String di dalam cuma untuk pemanis)

print('-------------')

# Menggabungkan Dua Buat Tuple atau Lebih Menjadi Satu
a = (1,2,3)          # --> Inisialisasi variabel yang menyimpan data tuple, berisi 3 elemen data integer
b = (4,5,6)          # --> Inisialisasi variabel yang menyimpan data tuple, berisi 3 elemen data integer
c = a + b            # --> Menggabungkan data tuple pada variabel a dan b menggunaan operator penjumlahan dan tersimpan dalam variabel c
print('Hasil = ', c) # 1,2,3,4,5,6 --> Mencetak variabel c (String di dalam cuma untuk pemanis)

# FUNGSI - FUNGSI BAWAAN TUPLE
# 1. len() ---> Menghitung jumlah item pada tuple
# 2. max() ---> Mencari nilai paling besar dari sebuah tuple
# 3. min() ---> Mencari nilai paling kecil dari sebuah tuple