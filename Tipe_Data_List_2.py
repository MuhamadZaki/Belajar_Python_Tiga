# Tipe Data Canggih atau Koleksi

# 1. List
# 2. Tuple
# 3. Set
# 4. Dictionary

# 1. Tipe Data List - (Ordered-Terurut) - (Changable-Bisa diubah)

# 1.1 List Kosong
list_kosong = [] # Kosong


# 1.2 List yang Berisi Kumpulan String
list_string = ['Manusia', 'adalah', 'mahluk', 'Bumi!'] # Manusia, adalah, mahluk, Bumi


# 1.3 List yang Berisi Kumpulan Integer
list_integer = [1,2,3,4,5,6,7,8,9,0] # 1,2,3,4,5,6,7,8,9,0


# 1.4 List yang Berisi Campuran Tipe Data (int, float, string, boolean)
list_campuran = [100, 10.0, 'Tobrut', True] # 100, 10.0, Tobrut, True

print('List Kosong :', list_kosong)
print('List_String :', list_string)
print('List Integer :', list_integer)
print('list Campuran :', list_campuran)


# 1.5 Mengambil Indeks dari List (Indeks dimulai dari 0)
print('Indeks 0 dari List_String :',list_string[0])         # manusia
print('Indeks 1 dari List_Integer : ', list_integer[1])     # 2
print('Indeks 4 dari List_Campuran :', list_campuran[3])    # True


# 1.6 Mengambil Indeks negatif
print('Indeks -1 dari List_String :',list_string[-1])       # Bumi
print('Indeks -2 dari List_Integer : ', list_integer[-2])   # 9
print('Indeks -3 dari List_Integer : ', list_integer[-3])   # 8
print('Indeks -4 dari List_Campuran :', list_campuran[-4])  # 100


# 1.7 Slicing List atau Teknik Memotong Value Pada List
list_buah = ['Anggur', 'Melon', 'Jeruk', 'Durian', 'Nanas']
print('Hasil List_Buah Utama : ', list_buah)

print(list_buah[0:1])   # Anggur
print(list_buah[0:2])   # Anggur, Mellon
print(list_buah[1:3])   # Melon, Jesruk
print(list_buah[0:-1])  # Anggur, Melon, Jeruk, Durian
print(list_buah[-1:-1]) # Kosong
print(list_buah[-1:-2]) # Kosong
print(list_buah[-1:-3]) # Kosong
print(list_buah[-1:3])  # Kosong
print(list_buah[-3:-1]) # Jeruk, Durian


# 1.8 Slicing Tanpa Batas
list_buah = ['Anggur', 'Melon', 'Jeruk', 'Durian']
print('Hasil List_Buah Utama : ', list_buah)
print(list_buah[0:])  # Tanpa batas
print(list_buah[1:])  # Mulai Indeks 1 yaitu Melon dan seterusnya (tanpa batas)
print(list_buah[2:])  # mulai Indeks 2 yaitu Jeruk dan seterusnya (tanpa batas)
print(list_buah[:0])  # Kosong
print(list_buah[0:1]) # Anggur
print(list_buah[0:2]) # Anggur, Melon
print(list_buah[:3])  # Anggur, Melon, Jeruk
print(list_buah[:4])  # Anggur, Melon, Jeruk, Durian


# 1.9 Mengubah Data di dalam List (changable/bisa diubah)
list_buah = ['Anggur', 'Melon', 'Jeruk', 'Durian']
print('Hasil List_Buah Utama : ', list_buah)

list_buah[0] = 'Nanas'
print(list_buah) # Nanas, Melon, Jeruk, Durian

list_buah = ['Anggur', 'Melon', 'Jeruk', 'Durian']
print('Hasil List_Buah Utama : ', list_buah)

list_buah[-1] = 'Belimbing'
print(list_buah) # Anggur, Melon, Jeruk, Belimbing


# 1.10 Mengubah Data dalam Range
list_buah = ['Anggur', 'Melon', 'Jeruk', 'Durian']
print('Hasil List_Buah Utama : ', list_buah)

list_buah[1:3] = ['Nangka', 'Semangka'] # Anggur, Nangka, Semangka, Durian
print(list_buah)

list_buah = ['Anggur', 'Melon', 'Jeruk', 'Durian']
print('Hasil List_Buah Utama : ', list_buah)

list_buah[2:4] = ['Nangka', 'Semangka'] # Anggur, Melon, Nangka, Semangka
print(list_buah)


# 1.11 Menambah Item ke Dalam List

# Menambah Data di index Belakang (fungsi append())
list_buah = ['Anggur', 'Melon', 'Jeruk', 'Durian']
print('Hasil List_Buah Utama : ', list_buah)

list_buah.append('Sirsak')
print(list_buah) # Anggur, Melon, Jeruk, Durian, Sirsak

# Menambah Data di index Depan (fungsi insert())
list_buah = ['Anggur', 'Melon', 'Jeruk', 'Durian']
print('Hasil List_Buah Utama : ', list_buah)

list_buah.insert(0, 'Sirsak')
print(list_buah) # Sirsak, Anggur, Melon, Jeruk, Durian

# Menambahkan Data di index Manapun (sungsi insert())
list_buah = ['Anggur', 'Melon', 'Jeruk', 'Durian']
print('Hasil List_Buah Utama : ', list_buah)

list_buah.insert(2, 'Sirsak')
print(list_buah) # Anggur, Melon, Sirsak, Jeruk, Durian


# 1.12 Menghapus Item dari List
list_angka = [1, 2, 3, 4, 5]
print('Hasil List_Angka utama :', list_angka)

# Hapus Satu Angka di Indeks Belakang (fungsi pop())
angka_yang_dihapus = list_angka.pop()
print('Angka yang di Hapus : ',angka_yang_dihapus) # 5

# Hapus Data yang Memiliki Value yang Sama atau Tidak (fungsi remove())
list_angka = [1, 2, 2, 3, 4, 5]
print('Hasil List_Angka utama :', list_angka)

list_angka.remove(1)
print(list_angka) # 2, 2, 3, 4, 5

list_buah = ['Anggur', 'Anggur', 'Melon', 'Jeruk', 'Durian']
print('Hasil List_Buah Utama : ', list_buah)

list_buah.remove('Anggur')
print(list_buah) # Anggur, Melon, Jeruk, Durian

# Menghapus dengan (statement del)
list_buah = ['Anggur', 'Melon', 'Jeruk', 'Durian']
print('Hasil List_Buah Utama : ', list_buah)

del list_buah[-1]
print(list_buah) # Anggur, Melon, Jeruk

list_buah = ['Anggur', 'Melon', 'Jeruk', 'Durian']
print('Hasil List_Buah Utama : ', list_buah)

del list_buah[0]
print(list_buah) # Melon, Jeruk, Durian

list_buah = ['Anggur', 'Melon', 'Jeruk', 'Durian']
print('Hasil List_Buah Utama : ', list_buah)

del list_buah[0:2]
print(list_buah) # Jeruk, Durian


# 1.13 Menggabungkan Dua Buah List atau Lebih
a = [1, 2, 3]
b = ['a']
c = [True, 'b', False]

list_baru = a + b + c
print(list_baru) # 1, 2, 3, a, True, b, False


# 1.14 Mengurutkan Data

# Urutkan Secara Ascending
list_buah = ['Mangga', 'Jeruk', 'Zaitun', 'Apel', 'Durian']
print('Hasil List_Buah Utama : ', list_buah)

list_buah.sort()
print(list_buah) # Apel, Durian, Jeruk, Mangga, Zaitun

# Membalikan Posisi Item List (Tidak Harus Berurut)
list_buah = ['Mangga', 'Jeruk', 'Zaitun', 'Apel', 'Durian']
print('Hasil List_Buah Utama : ', list_buah)

list_buah.reverse()
print(list_buah) # Durian, Apel, Zaitun, Jeruk, Mangga


# FUNGSI - FUNGSI BAWAAN LIST
# 1. append()   --> Menambahkan elemen baru pada list
# 2. clear()    --> Menghapus semua item pada list
# 3. copy()     --> Mengembalikan hasil duplikat dari list
# 4. count()    --> Mengembalikan jumlah item pada list sesuai yang didefinisikan
# 5. index()    --> Mengembalikan indeks pertama dari item yang sudah didefinisikan
# 6. insert()   --> Menambahkan item baru pada list pada posisi tertentu
# 7. pop()      --> Menghapus item terakhir pada list, atau juga bisa menghapus item pada posisi yang didefinisikan
# 8. remove()   --> Hapus item pada list sesuai dengan nilai yang didefinisikan
# 9. reverse()  --> Membalikan posisi tiap item pada list
# 10. sort()    --> Mengurutkan list