""" Perulangan for Termasuk Penjelasan Dasar, Iterasi Melalui Berbagai Tipe Data """
""" Teknik Lebih Lanjut Juga Tersedia """

# Perulangan for digunakan untuk mengulangi item-item dalam urutan seperti (list, tuple, dict, set dan string)

# 1. Sintaks dasar perulangan for
#for item in itrable:
    #Lakukan sesuatu dengan item

# 2. Itersi melalui list
list_buah = ["Semangka", "Tobrut", "Jeruk", "Durian"]

for buah in list_buah:
    print(buah) # Hasilnya adalah Semangka, Tobrut, Jeruk, Durian

# 3. Iterasi melalui string
toket_brutal = "Ukhti"

for huruf in toket_brutal:
    print(huruf) # Hasilnya adalah ukhti

# 4. Iterasi melalui tuple
tuple_buah = ("Anggur", "Jeruk", "Nanas")

for buah in  tuple_buah:
    print(buah) # Hasilnya adalah Amggur, Jeruk, Nanas


# 5. Iterasi melaui dictionary
dict_buah = {"Mangga": 1, "Apel": 2, "Jeruk": 3}

for kunci in dict_buah:
    print(kunci, dict_buah[kunci]) # Hasilnya adalah Mangga 1, Apel 2, Jeruk 3

# 6. Menggunakan range() --> Untuk menghasilkan urutan bilangan
for tobrut in range(5):
    print(tobrut) # Hasilnya adalah 0 1 2 3 4

# 7. Menggunakan range() dengan strat dan stop
for tobrut in range(1, 5):
    print(tobrut) # Hasilnya adalah 1 2 3 4

# 8. Menggunakan range() dengan step
for tobrut in range(1, 8, 2):
    print(tobrut) # Hasilnya adalah 1 3 5 7

# 9. Menggunakan perulangan bersarang (nested loops)
for tobrut in range(3):
    for brutal in range(2):
        print(f"tobrut: {tobrut}, brutal: {brutal}") # Hasilnya adalah tobrut:0, brutal:0 - tobrut:0, brutal:1 - tobrut1, brutal0 - tobrut:1, brutal:1 - tobrut:2, nrutal:0 - tobrut:2, brutal:1

# 10. Perulangan dengan else
for tobrut in range(3):
    print(tobrut) # Hasilnya adalah 0 1 2
else:
    print("Selesai") # Hasilnya adalah Selesai

# 11. Menggunakan break dan continue
# break untuk menghentikan perulangan
for tobrut in range(5):
    if tobrut == 3:
        break
    print(tobrut) # Hasilnya adalah 0 1 2

# continue untuk melewati iterasi
for tobrut in range(5):
    if tobrut == 3:
        continue
    print(tobrut) # Hasilnya adalah 0 1 2 3 4

# 12. Iterasi melalui set
set_buah = {'Apel', 'Mangga', 'Jeruk'}
for buah in set_buah:
    print(buah) # Hasilnya adalah Apel Mangga Jeruk

# 13. Menggunakan enumerate() --> Menambahkan penghitung ke itrable dan mengembalikannya dalam bentuk objek enum. Berguna ketika kita memerlukan indeks dalam perulangan
list_buah = ['Apel', 'Mangga', 'Jeruk']
for index, buah in enumerate(list_buah):
    print(index, buah) # 0 apel, 1 Mangga, 2 Jeruk

# 14. Menggunakan zip() --> digunakan untuk menggabungkan dua atau lebih itrable, menghasilkan tuple pasangan elemen dari itrable
list_buah = ['Apel', 'Mangga', 'Jeruk']
list_harga = [1000, 2000, 3000]

for buah, harga in zip(list_buah, list_harga):
    print(f"{buah}, {harga}") # Hasilnya adalah Apel 1000, Mangga 2000, Jeruk 3000


""" Teknik Lebih Lanjut Penggunaan list comprehensions, generator expressions, iterasi melalui file, serta manipulasi iterator. """

# 1. List Comprehension -->  Cara singkat dan elegan untuk membuat list baru dari itrable yang ada
# Membuat list dengan list comprehension
list_buah = ['Apel', 'Mangga', 'Jeruk']
buah_baru = [buah.upper() for buah in list_buah]
print(buah_baru) # Hasilnya adalah APEL, MANGGA, JERUK

# list comprehension dengan kondisi
list_angka = [1,2,3,4,5,6,7,8,9,10]
angka_genap = [angka for angka in list_angka if angka % 2 == 0]
angka_ganjil = [nomor for nomor in list_angka if nomor % 2]
print(angka_genap) # Hasilnya adalah genap 2 4 8 10
print(angka_ganjil) # Hasilnya adalah ganil 1 3 5 7 9

# 2. Generator Expressions --> Mirip dengan list comprehension, tetapi ini menghasilkan item satu per satu menggunakan iterator, yang lebih effisien dalam penggunaan memori untuk data yang besar
generator_angka = (angka for angka in range(10))
for angka in generator_angka:
    print(angka) # Hasilnya adalah 0 1 2 3 4 5 6 7 8 9

# 3. Iterasi melalui file --> Kita dapat membaca file baris demi baris menggunakan perulangan for
with open("contoh.txt", "w") as file:  # Membuat file contoh.txt
    file.write("Toket brutal 2024!\n") # Isi dari file contoh.txt
    file. write("Terlalu unfaedah\n")  # Isi dari file contoh.txt

with open("contoh.txt", "r") as file:  # Membaca  isi file dari contoh.txt
    for line in file:
        hasil_line = line.strip() # strip() --> menghapus spasi putih di awal dan akhir
        print(hasil_line) # Hasilnya adlaah isi dari file contoh.txt

# 4. Manipulasi Iterator dengan itertools Count --> Menghasilkan iterator yang menghasilkan angka yang tidak pernah berakhir

import itertools
for tobrut in itertools.count(10):
    print(tobrut) # Hasilnya adalah 10 11 12 13 14 15
    if tobrut >= 15:
        break

# Itertools Cycle --> Mengulang elemen dari iterable tanpa henti
ukhti = 0
for tobrut in itertools.cycle(["A", "B", "C"]):
    print(tobrut) # Hasilnya aalah A B C. A B C, A B C
    ukhti += 1
    if ukhti == 9:
        break

# Itertools Chain --> Menggabungkan beberapa iterble menjadi satu iterator
list1 = [1,2,3]
list2 = ["a", "b", "c"]
for item in itertools.chain(list1, list2):
    print(item) # --> Hasilnya adalah 1 2 3 a b c

# 5. Menggunakan fungsi buatan sendiri dalam List Comprehension
def is_tobrut(t):
    if t <= 1:
        return False
    for tobrut in range(2, int(t ** 0.5) + 1):
        if t % tobrut == 0:
            return False
    return True

ukhti_tobrut = [x for x in range(20) if is_tobrut(x)]
print(ukhti_tobrut) # Hasilnya adalah 2 3 5 7 11 13 17 19

# 6. Nested List Comprehension --> ini juga bisa bersarang untuk mengulangi melalui nested struktur
ukhti = [[1,2,3], [4,5,6], [7,8,9]]
tobrut = [num for row in ukhti for num in row]
print(tobrut) # Hasilnya adalah 1 2 3 4 5 6 7 8 9

# 7. Enumerete dengan start index --> Kita dapat menentukan dari mana index enumerate dimulai
list_buah = ['Apel', 'Mangga', 'Jeruk']
for index, buah in enumerate(list_buah, start=1):
    print(index, buah) # Hasilnya adalah 1 Apel, 2 Mangga, 3 Jeruk

# 8. Menggunakan zip untuk menggabungkan list dengan panjang berbeda --> Dapat menggabungkan list dengan panjang yang berbeda
from itertools import zip_longest

list1 = [1, 2]
list2 = ['a', 'b', 'c']
for num, char in zip_longest(list1, list2, fillvalue='None'):
    print(num, char) # Hasilnya adalah 1 a, 2 b dan None c