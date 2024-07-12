# Praktekan dan Pahami!

# Note:
# List adalah tipe data yang berisi kumpulan elemen-elemen dengan berbagai tipe data seperti string, integer, float dan boolean

# Tipe Data Canggih atau Koleksi

# 1. List
# 2. Tuple
# 3. Set
# 4. Dictionary

""" Tipe Data List - (Ordered-Terurut) - (Changable-Bisa diubah) """

# List Kosong
list_kosong = [] # --> Inisialisasi variabel dengan data list yang berisi elemen kosong


# List yang Berisi Kumpulan String
list_string = ['Manusia', 'adalah', 'mahluk', 'Bumi!'] # --> Inisialisasi variabel yang menyimpan data list, berisi 4 elemen data string


# List yang Berisi Kumpulan Integer
list_integer = [1,2,3,4,5,6,7,8,9,0] # --> Inisialisasi variabel yang menyimpan data list, berisi 10 elemen data integer


# List yang Berisi Campuran Tipe Data (int, float, string, boolean)
list_campuran = [100, 10.0, 'Tobrut', True] # --> Inisialisasi list dengan 4 elemen

print('List Kosong :', list_kosong)         # --> []
print('List_String :', list_string)         # --> Manusia, adalah, mahluk, Bumi
print('List Integer :', list_integer)       # --> 1,2,3,4,5,6,7,8,9,0
print('list Campuran :', list_campuran)     # --> 100, 10.0, Tobrut, True


""" Mengambil Indeks Dari List (Indeks dimulai dari 0) """

print('Indeks 0 dari List_String :',list_string[0])         # --> Mengembalikan elemen pertama dari list_string dan hasilnya adalah manusia

print('Indeks 1 dari List_Integer : ', list_integer[1])     # --> Mengembalikan elemen kedua  dari list_integer dan hasilnya adalah 2

print('Indeks 4 dari List_Campuran :', list_campuran[3])    # --> Mengembalikan elemen ke empat dari list_campuran dan hasilnya adalah True


""" Mengambil Indeks negatif """

print('Indeks -1 dari List_String :',list_string[-1])       # --> Mengembalikan elemen terakhir dari list_string dan hasilnya adalah Bumi

print('Indeks -2 dari List_Integer : ', list_integer[-2])   # --> Mengembalikan elemen kedua dari terakhir dari list_integer dan hasilnya adalah 9

print('Indeks -3 dari List_Integer : ', list_integer[-3])   # --> Mengembalikan elemen ketiga dari terakhir dari list_integer dan hasilnya adalah 8

print('Indeks -4 dari List_Campuran :', list_campuran[-4])  # --> Mengembalikan elemen keempat dari terakhir dari list_campuran dan hasilnya adalah 100

print('-------------')

""" Slicing List atau Teknik Memotong Value Pada List """

list_buah = ['Anggur', 'Melon', 'Jeruk', 'Durian', 'Nanas'] # --> Inisialisasi list dengan 5 elemen
print('Hasil List_Buah Utama : ', list_buah)

print(list_buah[0:1])   # --> Mengambil elemen dari indeks 0 hingga sebelum indeks 1 dan hasilnya adalah Anggur

print(list_buah[0:2])   # --> Mengambil elemen dari indeks 0 hingga sebelum indeks 2 Anggur, dan hasilnya aalah Mellon

print(list_buah[1:3])   # --> Mengambil elemen dari indeks 1 hingga sebelum indeks 3 dan hasilnya adalah Melon, Jeruk

print(list_buah[0:-1])  # --> Mengambil elemen dari indeks 0 hingga sebelum indeks -1 (elemen terakhir) dan hasilnya adalah Anggur, Melon, Jeruk, Durian

print(list_buah[-1:-1]) # --> Mengambil elemen dari indeks -1 hingga sebelum indeks -1 --> Karena indeks mulai dan indeks akhir sama, dan hasilnya kosong []

print(list_buah[-1:-2]) # --> Mengambil elemen dari indeks -1 hingga sebelum indeks -2 --> Karena indeks mulai lebih besar dari indeks akhir, dan hasilnya kosong []

print(list_buah[-3:-1]) # --> Mengambil elemen dari indeks -3 hingga sebelum indeks -1 dan hasilnya adalah Jeruk, Durian

print('-------------')

""" Slicing Tanpa Batas """

list_buah = ['Anggur', 'Melon', 'Jeruk', 'Durian'] # --> Inisialisasi list dengan 4 elemen
print('Hasil List_Buah Utama : ', list_buah)

print(list_buah[0:])  # --> Mengambil semua elemen dari indeks 0 sampai akhir dan hasilnya adalah Anggur, Melon, Jeruk, Durian

print(list_buah[1:])  # --> Mengambil semua elemen dari indeks 1 sampai akhir dan hasilnya adalah Melon, Jeruk, Durian

print(list_buah[2:])  # --> Mengambil semua elemen dari indeks 2 sampai akhir dan hasilnya adalah Jeruk, Durian

print(list_buah[:0])  # --> Mengambil semua elemen dari awal sampai sebelum indeks 0 dan hasinya adalah Kosong

print(list_buah[0:1]) # --> Mengambil elemen dari indeks 0 sampai sebelum indeks 1 dan hasilnya adalah Anggur

print(list_buah[0:2]) # --> Mengambil elemen dari indeks 0 sampai sebelum indeks 2 dan hasilnya adalah Anggur, Melon

print(list_buah[:3])  # --> Mengambil semua elemen dari awal sampai sebelum indeks 3 dan hasilnya adalah Anggur, Melon, Jeruk

print(list_buah[:4])  # --> Mengambil semua elemen dari awal sampai sebelum indeks 4 dan hasilnya adalah Anggur, Melon, Jeruk, Durian

print('-------------')

""" Mengubah Data di Dalam List (changable/bisa diubah) """

list_buah = ['Anggur', 'Melon', 'Jeruk', 'Durian'] # --> Inisialisasi list dengan 4 elemen
print('Hasil List_Buah Utama : ', list_buah)

list_buah[0] = 'Nanas'                             # --> Mengubah elemen pertama (indeks 0)
print(list_buah)                                   # --> Mencetak variabel list_buah dan hasilnya adalah Nanas, Melon, Jeruk, Durian

list_buah = ['Anggur', 'Melon', 'Jeruk', 'Durian'] # --> Inisialisasi list dengan 4 elemen
print('Hasil List_Buah Utama : ', list_buah)

list_buah[-1] = 'Belimbing'                        # --> Mengubah elemen terakhir (indeks -1) 
print(list_buah)                                   # --> Mencetak varibel list_buah dan hasilnya adalah Anggur, Melon, Jeruk, Belimbing

print('-------------')

""" Mengubah Data dalam Range Pada List """

list_buah = ['Anggur', 'Melon', 'Jeruk', 'Durian'] # --> Inisialisasi list dengan 4 elemen
print('Hasil List_Buah Utama : ', list_buah)

list_buah[1:3] = ['Nangka', 'Semangka']            # --> Mengubah elemen pada indeks 1 sampai 2 (termasuk) 
print(list_buah)                                   # --> Mencetak variabel list_buah dan hasilnya adalah Anggur, Nangka, Semangka, Durian

list_buah = ['Anggur', 'Melon', 'Jeruk', 'Durian'] # --> Inisialisasi list dengan 4 elemen
print('Hasil List_Buah Utama : ', list_buah)

list_buah[2:4] = ['Nangka', 'Semangka']            # --> Mengubah elemen pada indeks 2 sampai 3 (termasuk) 
print(list_buah)                                   # --> Mencetak variabel list_buah dan hasilnya adalah Anggur, Melon, Nangka, Semangka

print('-------------')

list_buah = ['Anggur', 'Melon', 'Jeruk', 'Durian'] # --> Inisialisasi list dengan 4 elemen
print('Hasil List_Buah Utama : ', list_buah)

list_buah.append('Sirsak')                         # --> Menambahkan elemen baru di indeks akhir 
print(list_buah)                                   # --> Mencetak variabel list_buah dan hasilnya adalah Anggur, Melon, Jeruk, Durian, Sirsak

list_buah = ['Anggur', 'Melon', 'Jeruk', 'Durian'] # --> Inisialisasi list dengan 4 elemen
print('Hasil List_Buah Utama : ', list_buah)

list_buah.clear()                                  # --> Menghapus semua elemen pada list 
print(list_buah)                                   # --> Mencetak list_buah dan hasilnya adalah kosong []

list_buah = ['Anggur', 'Melon', 'Jeruk', 'Durian'] # --> Inisialisasi list dengan 4 elemen
print('Hasil List_Buat Utama : ')

list_buah_copy = list_buah.copy()                  # --> Membuat salinan baru dari list 
print('Salinan List_Buah : ', list_buah_copy)      # --> Mencetak variabel list_buah_copy dan hasilnya adalah Anggur, Melon, Jeruk, Durian

list_buah = ['Anggur', 'Melon', 'Jeruk', 'Durian'] # --> Inisialisasi list dengan 4 elemen
print('Hasil List_Buah Utama : ', list_buah)

list_buah.insert(0, 'Sirsak')                      # --> Menambahkan elemen baru Sirsak di posisi indeks 0 
print(list_buah)                                   # --> Mencetak variabel list_buah dan hasilnya adalah Sirsak, Anggur, Melon, Jeruk, Durian

list_buah = ['Anggur', 'Melon', 'Jeruk', 'Durian'] # --> Inisialisasi list dengan 4 elemen
print('Hasil List_Buah Utama : ', list_buah)

list_buah.insert(2, 'Sirsak')                      # --> Menambahkan elemen baru sirsak di posisi indeks 2 
print(list_buah)                                   # --> Mencetak variabel list_buah dan hasilnya adalah Anggur, Melon, Sirsak, Jeruk, Durian

list_buah = ['Anggur', 'Melon', 'Jeruk', 'Durian'] # --> Inisialisasi list dengan 4 elemen
print('Hasil List_Buah Utama : ', list_buah)

index_jeruk = list_buah.index('Jeruk')             # --> Mengembalikan posisi indeks pertama dari elemen Jeruk 
print('Indeks dari Jeruk : ', index_jeruk)         # --> Mencetak variabel index_jeruk dan hasilnya adalah 2

print('-------------')

list_angka = [1, 2, 3, 4, 5]                       # --> Inisialisasi list dengan 5 elemen
print('Hasil List_Angka utama :', list_angka)

angka_yang_dihapus = list_angka.pop()              # --> Menghapus dan mengembalikan elemen akhir dari list 
print('Angka yang di Hapus : ',angka_yang_dihapus) # --> Mencetak variabel dan hasilnya adalah 5

list_angka = [1, 2, 2, 3, 4, 5]                    # --> Inisialisasi list dengan 5 elemen
print('Hasil List_Angka utama :', list_angka)

jumlah_dua = list_angka.count(2)                   # --> Menghitung berapa kali nilai 2 muncul di dalam list 
print('Jumlah angka 2 : ', jumlah_dua)             # --> Mencetak variabel jumlah_angka dan hasilnya adalah 2

list_angka = [1, 2, 2, 3, 4, 5]                    # --> Inisialisasi list dengan 5 elemen
print('Hasil List_Angka utama :', list_angka)

list_angka.remove(1)                               # --> Menghapus elemen pertama yang memiliki nilai 1 dari list 
print(list_angka)                                  # --> Mencetak variabel list_angka dan hasilnya adalah 2, 2, 3, 4, 5 

print('-------------')

list_buah = ['Anggur', 'Anggur', 'Melon', 'Jeruk', 'Durian'] # --> Inisialisasi list dengan 5 elemen
print('Hasil List_Buah Utama : ', list_buah)

list_buah.remove('Anggur')                                   # --> Menghapus elemen pertama yang memiliki nilai Anggur dari list 
print(list_buah)                                             # --> Mencetak variabel list_buah dan hasilnya adalah Anggur, Melon, Jeruk, Durian

list_buah = ['Anggur', 'Melon', 'Jeruk', 'Durian']           # --> Inisialisasi list dengan 4 elemen
print('Hasil List_Buah Utama : ', list_buah)

del list_buah[-1]                                            # --> Menghapus elemen terakhir dari list 
print(list_buah)                                             # --> Mencetak variabel list_buah dan hasilnya adalah Anggur, Melon, Jeruk

list_buah = ['Anggur', 'Melon', 'Jeruk', 'Durian'] # --> Inisialisasi list dengan 4 elemen
print('Hasil List_Buah Utama : ', list_buah)

del list_buah[0]                                   # --> Menghapus elemen pertama dari list 
print(list_buah)                                   # --> Mencetak variabel list_buah dan hasilnya adalah Melon, Jeruk, Durian


list_buah = ['Anggur', 'Melon', 'Jeruk', 'Durian'] # --> Inisialisasi list dengan 4 elemen
print('Hasil List_Buah Utama : ', list_buah)

del list_buah[0:2]                                 # --> Menghapus elemen dari indeks 0 hingga 1 (indeks 0 dan 1) dari list 
print(list_buah)                                   # --> Mencetak variabel list_buah dan hasilnya adalah Jeruk, Durian

print('-------------')

""" Menggabungkan Dua Buah List atau Lebih """
a = [1, 2, 3]           # --> Inisialisasi list dengan 3 elemen
b = ['a']               # --> Inisialisasi list dengan 1 elemen
c = [True, 'b', False]  # --> Inisialisasi list dengan 3 elemen

list_baru = a + b + c   # --> Menggebungkan ketiga list menjadi list tunggal dengan urutan elemen yang sesuai dengan urutan penjumlahan
print(list_baru)        # --> Mencetak variabel list_baru dan hasilnya adalah 1, 2, 3, a, True, b, False

print('-------------')

list_buah = ['Mangga', 'Jeruk', 'Zaitun', 'Apel', 'Durian'] # --> Inisialisasi list dengan 5 elemen
print('Hasil List_Buah Utama : ', list_buah)

list_buah.sort() # --> Mengurutkan list secara asceding atau menaik, yaitu elemen yang diurutkan dari yang terkecil ke yang terbesar berdasarkan urutan alfabet untuk string 
print(list_buah) # --> Mencetan variabel list_buah dan hasilnya adalah Apel, Durian, Jeruk, Mangga, Zaitun


list_buah = ['Mangga', 'Jeruk', 'Zaitun', 'Apel', 'Durian'] # --> Inisialisasi list dengan 5 elemen
print('Hasil List_Buah Utama : ', list_buah)

list_buah.reverse() # --> Membalik urutan elemen dalam list, yaitu elemen akan diputar ke arah yang berlawanan dari urutan sebelumnya 
print(list_buah)    # --> Mencetak variable list_buah dan hasilnya adalah Durian, Apel, Zaitun, Jeruk, Mangga


list_buah = ['Mangga', 'Jeruk', 'Zaitun'] # --> Inisialisasi list dengan 3 elemen
buah_tambahan = ['Apel', 'Durian']        # --> Inisialisasi list dengan 2 elemen

list_buah.extend(buah_tambahan)           # --> Menambahkan semua elemen dari list, yaitu di ikuti dari semua elemen dari variabel baru list 
print(list_buah)                          # --> Mencetak variabel list_buah dan hasilnya adalah Mangga, Jeruk, Zaitun, Apel, Durian


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