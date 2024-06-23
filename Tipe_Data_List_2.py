# Tipe Data Canggih atau Koleksi

# 1. List
# 2. Tuple
# 3. Set
# 4. Dictionary

""" H1 Tipe Data List - (Ordered-Terurut) - (Changable-Bisa diubah) H1"""

# List Kosong
list_kosong = [] 


# List yang Berisi Kumpulan String
list_string = ['Manusia', 'adalah', 'mahluk', 'Bumi!'] 


# List yang Berisi Kumpulan Integer
list_integer = [1,2,3,4,5,6,7,8,9,0] 


# List yang Berisi Campuran Tipe Data (int, float, string, boolean)
list_campuran = [100, 10.0, 'Tobrut', True]

print('List Kosong :', list_kosong)     # []
print('List_String :', list_string)     # Manusia, adalah, mahluk, Bumi
print('List Integer :', list_integer)   # 1,2,3,4,5,6,7,8,9,0
print('list Campuran :', list_campuran) # 100, 10.0, Tobrut, True


""" Mengambil Indeks Dari List (Indeks dimulai dari 0) """

# Contoh 1 : Mengembalikan elemen pertama dari list_string
print('Indeks 0 dari List_String :',list_string[0])         # manusia

# Contoh 2 : Mengembalikan elemen kedua  dari list_integer
print('Indeks 1 dari List_Integer : ', list_integer[1])     # 2

# Contoh 3 : Mengembalikan elemen ke empat dari list_campuran
print('Indeks 4 dari List_Campuran :', list_campuran[3])    # True


""" Mengambil Indeks negatif """

# Contoh 1 : Mengembalikan elemen terakhir dari list_string
print('Indeks -1 dari List_String :',list_string[-1])       # Bumi

# Contoh 2 : Mengembalikan elemen kedua dari terakhir dari list_integer
print('Indeks -2 dari List_Integer : ', list_integer[-2])   # 9

# Contoh 3 : Mengembalikan elemen ketiga dari terakhir dari list_integer
print('Indeks -3 dari List_Integer : ', list_integer[-3])   # 8

# Contoh 4 : Mengembalikan elemen keempat dari terakhir dari list_campuran
print('Indeks -4 dari List_Campuran :', list_campuran[-4])  # 100

print('-------------')

"""Slicing List atau Teknik Memotong Value Pada List"""

list_buah = ['Anggur', 'Melon', 'Jeruk', 'Durian', 'Nanas']
print('Hasil List_Buah Utama : ', list_buah)

# Contoh 1 : Mengambil elemen dari indeks 0 hingga sebelum indeks 1
print(list_buah[0:1])   # Anggur

# COntoh 2 : Mengambil elemen dari indeks 0 hingga sebelum indeks 2
print(list_buah[0:2])   # Anggur, Mellon

# Contoh 3 : Mengambil elemen dari indeks 1 hingga sebelum indeks 3
print(list_buah[1:3])   # Melon, Jesruk

# Contoh 4 : Mengambil elemen dari indeks 0 hingga sebelum indeks -1 (elemen terakhir)
print(list_buah[0:-1])  # Anggur, Melon, Jeruk, Durian

# Contoh 5 : Mengambil elemen dari indeks -1 hingga sebelum indeks -1 --> Karena indeks mulai dan indeks akhir sama, hasilnya kosong
print(list_buah[-1:-1]) # []

# Contoh 6 : Mengambil elemen dari indeks -1 hingga sebelum indeks -2 --> Karena indeks mulai lebih besar dari indeks akhir, hasilnya kosong
print(list_buah[-1:-2]) # []

# Contoh 7 : Mengambil elemen dari indeks -3 hingga sebelum indeks -1
print(list_buah[-3:-1]) # Jeruk, Durian

print('-------------')

"""Slicing Tanpa Batas"""

list_buah = ['Anggur', 'Melon', 'Jeruk', 'Durian']
print('Hasil List_Buah Utama : ', list_buah)

# Contoh 1 : Mengambil semua elemen dari indeks 0 sampai akhir
print(list_buah[0:])  # Anggur, Melon, Jeruk, Durian

# Contoh 2 : Mengambil semua elemen dari indeks 1 sampai akhir
print(list_buah[1:])  # Melon, Jeruk, Durian

# Contoh 3 : Mengambil semua elemen dari indeks 2 sampai akhir
print(list_buah[2:])  # Jeruk, Durian

# Contoh 4 : Mengambil semua elemen dari awal sampai sebelum indeks 0
print(list_buah[:0])  # Kosong

# Contoh 5 : Mengambil elemen dari indeks 0 sampai sebelum indeks 1
print(list_buah[0:1]) # Anggur

# Contoh 6 : Mengambil elemen dari indeks 0 sampai sebelum indeks 2
print(list_buah[0:2]) # Anggur, Melon

# Contoh 7 : Mengambil semua elemen dari awal sampai sebelum indeks 3
print(list_buah[:3])  # Anggur, Melon, Jeruk

# Contoh 8 : Mengambil semua elemen dari awal sampai sebelum indeks 4
print(list_buah[:4])  # Anggur, Melon, Jeruk, Durian

print('-------------')

"""Mengubah Data di Dalam List (changable/bisa diubah)"""

# Contoh 1 : Mengubah elemen pertama (indeks 0)
list_buah = ['Anggur', 'Melon', 'Jeruk', 'Durian']
print('Hasil List_Buah Utama : ', list_buah)

list_buah[0] = 'Nanas'
print(list_buah) # Nanas, Melon, Jeruk, Durian

# Contoh 2 : Mengubah elemen terakhir (indeks -1)
list_buah = ['Anggur', 'Melon', 'Jeruk', 'Durian']
print('Hasil List_Buah Utama : ', list_buah)

list_buah[-1] = 'Belimbing'
print(list_buah) # Anggur, Melon, Jeruk, Belimbing

print('-------------')

""" Mengubah Data dalam Range Pada List """

# Contoh 1: Mengubah elemen pada indeks 1 sampai 2 (termasuk)
list_buah = ['Anggur', 'Melon', 'Jeruk', 'Durian']
print('Hasil List_Buah Utama : ', list_buah)

list_buah[1:3] = ['Nangka', 'Semangka'] # Anggur, Nangka, Semangka, Durian
print(list_buah)

# Contoh 2: Mengubah elemen pada indeks 2 sampai 3 (termasuk)
list_buah = ['Anggur', 'Melon', 'Jeruk', 'Durian']
print('Hasil List_Buah Utama : ', list_buah)

list_buah[2:4] = ['Nangka', 'Semangka'] # Anggur, Melon, Nangka, Semangka
print(list_buah)

print('-------------')

# Contoh : Menambahkan elemen baru di indeks akhir
list_buah = ['Anggur', 'Melon', 'Jeruk', 'Durian']
print('Hasil List_Buah Utama : ', list_buah)

list_buah.append('Sirsak')
print(list_buah) # Anggur, Melon, Jeruk, Durian, Sirsak

# Contoh : Menghapus semua elemen pada list
list_buah = ['Anggur', 'Melon', 'Jeruk', 'Durian']
print('Hasil List_Buah Utama : ', list_buah)

list_buah.clear()
print(list_buah) # []

# Contoh : Membuat salinan baru dari list
list_buah = ['Anggur', 'Melon', 'Jeruk', 'Durian']
print('Hasil List_Buat Utama : ')

list_buah_copy = list_buah.copy()
print('Salinan List_Buah : ', list_buah_copy)  # Anggur, Melon, Jeruk, Durian

# Contoh : Menambahkan elemen baru Sirsak di posisi indeks 0
list_buah = ['Anggur', 'Melon', 'Jeruk', 'Durian']
print('Hasil List_Buah Utama : ', list_buah)

list_buah.insert(0, 'Sirsak')
print(list_buah) # Sirsak, Anggur, Melon, Jeruk, Durian

# Contoh : Menambahkan elemen baru sirsak di posisi indeks 2
list_buah = ['Anggur', 'Melon', 'Jeruk', 'Durian']
print('Hasil List_Buah Utama : ', list_buah)

list_buah.insert(2, 'Sirsak')
print(list_buah) # Anggur, Melon, Sirsak, Jeruk, Durian

# Contoh : Mengembalikan posisi indeks pertama dari elemen Jeruk
list_buah = ['Anggur', 'Melon', 'Jeruk', 'Durian']
print('Hasil List_Buah Utama : ', list_buah)

index_jeruk = list_buah.index('Jeruk')
print('Indeks dari Jeruk : ', index_jeruk) # 2

print('-------------')

# Contoh : Menghapus dan mengembalikan elemen akhir dari list
list_angka = [1, 2, 3, 4, 5]
print('Hasil List_Angka utama :', list_angka)

angka_yang_dihapus = list_angka.pop()
print('Angka yang di Hapus : ',angka_yang_dihapus) # 5

# Contoh : Menghitung berapa kali nilai 2 muncul di dalam list
list_angka = [1, 2, 2, 3, 4, 5]
print('Hasil List_Angka utama :', list_angka)

jumlah_dua = list_angka.count(2)
print('Jumlah angka 2 : ', jumlah_dua) # 2

# Contoh : Menghapus elemen pertama yang memiliki nilai 1 dari list
list_angka = [1, 2, 2, 3, 4, 5]
print('Hasil List_Angka utama :', list_angka)

list_angka.remove(1)
print(list_angka) # 2, 2, 3, 4, 5

print('-------------')

# Contoh : Menghapus elemen pertama yang memiliki nilai Anggur dari list
list_buah = ['Anggur', 'Anggur', 'Melon', 'Jeruk', 'Durian']
print('Hasil List_Buah Utama : ', list_buah)

list_buah.remove('Anggur')
print(list_buah) # Anggur, Melon, Jeruk, Durian

# Contoh : Menghapus elemen terakhir dari list
list_buah = ['Anggur', 'Melon', 'Jeruk', 'Durian']
print('Hasil List_Buah Utama : ', list_buah)

del list_buah[-1]
print(list_buah) # Anggur, Melon, Jeruk

# Contoh : Menghapus elemen pertama dari list
list_buah = ['Anggur', 'Melon', 'Jeruk', 'Durian']
print('Hasil List_Buah Utama : ', list_buah)

del list_buah[0]
print(list_buah) # Melon, Jeruk, Durian

# Contoh : Menghapus elemen dari indeks 0 hingga 1 (indeks 0 dan 1) dari list
list_buah = ['Anggur', 'Melon', 'Jeruk', 'Durian']
print('Hasil List_Buah Utama : ', list_buah)

del list_buah[0:2]
print(list_buah) # Jeruk, Durian

print('-------------')

"""Menggabungkan Dua Buah List atau Lebih"""
a = [1, 2, 3]
b = ['a']
c = [True, 'b', False]

list_baru = a + b + c
print(list_baru) # 1, 2, 3, a, True, b, False

print('-------------')

# Contoh : Mengurutkan list secara asceding atau menaik, yaitu elemen yang diurutkan dari yang terkecil ke yang terbesar berdasarkan urutan alfabet untuk string
list_buah = ['Mangga', 'Jeruk', 'Zaitun', 'Apel', 'Durian']
print('Hasil List_Buah Utama : ', list_buah)

list_buah.sort()
print(list_buah) # Apel, Durian, Jeruk, Mangga, Zaitun

# Contoh : Membalik urutan elemen dalam list, yaitu elemen akan diputar ke arah yang berlawanan dari urutan sebelumnya
list_buah = ['Mangga', 'Jeruk', 'Zaitun', 'Apel', 'Durian']
print('Hasil List_Buah Utama : ', list_buah)

list_buah.reverse()
print(list_buah) # Durian, Apel, Zaitun, Jeruk, Mangga

# Contoh : Menambahkan semua elemen dari list, yaitu di ikuti dari semua elemen dari variabel baru list
list_buah = ['Mangga', 'Jeruk', 'Zaitun']
buah_tambahan = ['Apel', 'Durian']

list_buah.extend(buah_tambahan)
print(list_buah) # Mangga, Jeruk, Zaitun, Apel, Durian


# FUNGSI - FUNGSI BAWAAN LIST
# 1. append()   --> Menambahkan elemen baru pada akhir list
# 2. clear()    --> Menghapus semua elemen dari list atau membuat list menjadi kosong
# 3. copy()     --> Mengembalikan hasil salinan (duplikat) dari list
# 4. count()    --> Mengembalikan jumlah kemunculan suatu elemen dari list
# 5. index()    --> Mengembalikan indks pertama dari elemen yang cocok dengan nilai yang diberikan 
# 6. insert()   --> Menambahkan item baru pada list pada posisi tertentu
# 7. pop()      --> Menghapus dan mengembalikan elemen terakhir dari list, atau menghapus elemen pada indeks yang diberikan
# 8. remove()   --> Menghapus elemen pertama dari list yang nilainya sama dengan nilai yang diberikan
# 9. reverse()  --> Membalikan urutan elemen-elemen dalam list
# 10. sort()    --> Mengurutkan  elemen-elemen dalam list secara ascending (default) atau sesuai dengan kriteria yang diberikan