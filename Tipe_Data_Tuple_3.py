# Praktekan dan Pahami!

# Tipe Data Canggih atau Koleksi

# 1. List
# 2. Tuple
# 3. Set
# 4. Dictionary

""" Tipe Data Tuple (Ordered-Terurut) - (Unchnagble-Tidak Bisa diubah) """

# Cara Standar Tuple
standar_tuple = ('Laki-laki', 'Perempuan')
print(standar_tuple)        # Laki-laki, Perempuan

# Tanpa Kurung Tuple
tanpa_kurung_tuple = 'Tobrut', 'Ukhti'
print(tanpa_kurung_tuple)   # Tobrut, Ukhti

# Tuple Kosong
tuple_kosong = ()
print(tuple_kosong) # Kosong

# Tupel Tunggal (Hanya Berisi Satu Item)
tuple_tunggal = (10)
print(tuple_tunggal) # 10 --> Akan tetapi di Anggap Integer

tuple_tunggal = (10,)
print(tuple_tunggal) # 10 --> Ini Baru dianggap Tuple

print('-------------')

# Cara Standar (Mengakses Nilai Tuple dengan Langsung Mendefinisikan Indeks)
cara_standar_tuple = ('Tobrut', 'Era')
print(cara_standar_tuple[1]) # Era
print(cara_standar_tuple[0]) # Tobrut

# Mengakses Nilai Tuple dengan Negatif Indeks
cara_standar_tuple = ('Tobrut', 'Era')
print(cara_standar_tuple[-1]) # Era
print(cara_standar_tuple[-2]) # Tobrut


# Slicing Tuple
tuple_buah = ('Anggur', 'Melon', 'Nanas', 'Semangka')
print(tuple_buah[0:])    # Anggur, Melon, Nanas, Semangka dan Tak-terbatas
print(tuple_buah[0:2])   # Anggur, Melon
print(tuple_buah[1:3])   # Melon, Nanas
print(tuple_buah[0:-1])  # Anggur, Melon, Nanas
print(tuple_buah[-1:-3]) # Kosong
print(tuple_buah[-1:3])  # Kosong
print(tuple_buah[-3:-1]) # Melon, Nanas

# Slicing Tanpa Batas
tuple_buah = ('Anggur', 'Melon', 'Nanas', 'Semangka')
print(tuple_buah[0:])    # Anggur, Melon, Nanas, Semangka
print(tuple_buah[1:])    # Melon, Nanas, Semangka
print(tuple_buah[2:])    # Nanas, Semangka
print(tuple_buah[3:])    # Semangka dan Tak-terbatas
print(tuple_buah[:0])    # []
print(tuple_buah[:1])    # Anggur
print(tuple_buah[:2])    # Anggur, Melon
print(tuple_buah[:3])    # Anggur, Melon, Nanas
print(tuple_buah[:4])    # Anggur, Melon, Nanas, Semangka

print('-------------')

# Squence Unpaking (Mengekstrak Isi Dari Tuple ke Dalam Variable-Variable Tunggal, Secara Berurutan)
siswi = (' Natasia Tobrut', 'Makassar', 22)

nama, asal, usia = siswi # Ekstrak Data atau Juga dinamakan Sequence Unpacking (Setiap Variable Akan Memiliki Nilai dari Variable siswi)- yang pertama, nama maka mempunyai indeks [0]
print('Nama :', nama)    # Natasia Tobrut --> siswi[0] -nama
print('Asal : ', asal)   # Makassar       --> siswi[1] -asal
print('Usia : ', usia)   # 22             --> siswi[2] -usia

print('-------------')

# Menggabungkan Dua Buat Tuple atau Lebih Menjadi Satu
a = (1,2,3)
b = (4,5,6)
c = a + b
print('Hasil = ', c)    # 1,2,3,4,5,6

# FUNGSI - FUNGSI BAWAAN TUPLE
# 1. len() ---> Menghitung jumlah item pada tuple
# 2. max() ---> Mencari nilai paling besar dari sebuah tuple
# 3. min() ---> Mencari nilai paling kecil dari sebuah tuple