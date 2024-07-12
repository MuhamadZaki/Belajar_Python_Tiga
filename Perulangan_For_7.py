""" Perulangan for Termasuk Penjelasan Dasar, Iterasi Melalui Berbagai Tipe Data """
""" Teknik Lebih Lanjut Juga Tersedia """

# Note :
# Itersi --> Proses di mana kita menelusuri atau melintasi setiap elemen dari suatu koleksi data seperti (ist, tuple, set dan dict) satu persatu (secara singkat adalah aksi atau proses) / proses mengulang elemen-elemen dari sebuah itrable
numbers = [1, 2, 3, 4, 5] # --> List (iterabel) yang diitersi
for number in numbers:    # --> Iterasi dimulai dari sini
    print(number)         # --> Aksi selama iterasi

# Iterable --> Merupakan sebuah objek yang bisa diiterasi (diulang) atau dilintasi (secara singkat adalah objek yang mendukung aksi atau proses) dan Iterable memiliki metode khusus seperti __iter__() / __getitem__() lalu contoh umum untuk itrable adalah list, tuple, dict dan set.
my_list = [1, 2, 3, 4, 5] # --> myl_list Ini adalah contoh dari iterable (karena kita bisa mengulanginya menggunakan loop for)
iter_obj = iter(my_list)  # --> Ini tidak akan menghasilkan error, sehingga my_list adalah iterable
print(iter_obj)           # --> Mencetak objek iterator

# Iterator --> Objek yang mengimplementasikan metode khusus __iter() / __next__() atau objek yang melacak posisi saat ini dalam iterble dan mengembalikan elemen berikutnya saat diminta contoh dengan metode __next__()
list_buah = ["Apel", "Jeruk", "Mangga"] # --> Iterable
iterator_buah = iter(list_buah)  # --> Membuat iterator dari iterable
print(next(iterator_buah))       # --> Menggunakan iterator atau mendapatkan elemen berikutnya dari iterator

# Contoh lengkap
list_buah = ["Apel", "Jeruk", "Mangga"]  # --> Ini adalah iterable
for buah in list_buah:                   # --> Proses iterasi menggunakan loop for
    print(buah)
iterator_buah = iter(list_buah)          # --> Membuat iterator secara eksplisit

print(next(iterator_buah))               # --> Menggunakan iterator untuk iterasi atau mendapatkan elemen berikutnya dari iterator
print(next(iterator_buah))  
print(next(iterator_buah))  

# Note :
"""
- Deklarasi --> Pada saat deklarasi kita hanya menyatakan nama variabel tanpa memberikan nilai awal

- Deklarasi variabel dalam Python --> Memperkenalkan suatu variabel, fungsi, atau kelas ke dalam program. Dalam Python, deklarasi variabel terjadi secara implisit saat pertama kali variabel diberi nilai. Jadi, Python tidak memiliki konsep deklarasi variabel secara terpisah. 
tob = 10  # Deklarasi dan inisialisasi variabel tob dengan nilai 10

- Definisi di Python --> Memberikan bentuk atau nilai spesifik kepada variabel, fungsi, atau kelas. Dalam Python, mendefinisikan berarti memberikan nilai atau kode yang menentukan apa yang dilakukan atau diwakili oleh (entitas / variabel, fungsi, atau kelas) tersebut.
tob = 10  # Mendefinisikan variabel tob dengan nilai 10

Deklarasi variabel, fungsi, dan kelas terjadi secara bersamaan dengan definisinya. 

- Inisialisasi di Python --> Merupakan proses menetapkan nilai awal ke variabel pada saat didefinisikan. Dalam Python, setiap kali kamu menetapkan nilai ke variabel, itu disebut inisialisasi.
tob = 10  # Deklarasi dan inisialisasi variabel tob dengan nilai 10

Dalam Python, karena deklarasi dan inisialisasi terjadi secara bersamaan ketika kamu pertama kali menetapkan nilai pada variabel, tidak ada perbedaan yang jelas seperti dalam beberapa bahasa lain. Setiap kali kamu membuat variabel dan memberikan nilai kepadanya, kamu secara bersamaan mendeklarasikan dan menginisialisasi variabel tersebut.

"""

# Perulangan for digunakan untuk mengulangi item-item dalam urutan seperti (list, tuple, dict, set dan string)

# 1. Sintaks dasar perulangan for
#for item in itrable:
    #Lakukan sesuatu dengan item

# 2. Itersi melalui list
list_buah = ["Semangka", "Tobrut", "Jeruk", "Durian"] # --> Inisialisasi variabel list_buah dan berisi 4 elemen
for buah in list_buah:                                # --> loop for yang akan mengulang setiap elemen dalam list_buah dan pada setiap iterasi variabel buah akan berisi salah satu elemen dari list
    print(buah)                                       # --> Hasilnya adalah Semangka, Tobrut, Jeruk, Durian (mencetak nilai atau elemen dari variabel buah pada setiap iterasi)

# 3. Iterasi melalui string
toket_brutal = "Ukhti"      # --> Inisialisasi variabel toket_brutal dengan nilai atau elemen
for huruf in toket_brutal:  # --> Loop for yang akan mengulangi setiap karakter dalam toket_brutal dan pada setiap iterasi variabel huruf, akan berisi salah satu karakter dari string
    print(huruf)            # --> Hasilnya adalah mencetak setiap karakter dari ukhti secara terpisah (mencetak nilai dari variabel huruf pada setiap iterasi)

# 4. Iterasi melalui tuple
tuple_buah = ("Anggur", "Jeruk", "Nanas") # --> Inisialisasi variabel tuple_buah dan berisi tiga elemen string (ingat tupel tuple bersifat immutabel atau tidak bisa diubah setelah dibuat)
for buah in  tuple_buah:                  # --> Loop for yang akan mengulang setiap elemen dalam tuple_buah dan pada setiap iterasi variabel buah, akan berisi salah satu elemen dari tuple
    print(buah)                           # --> Hasilnya adalah Amggur, Jeruk, Nanas (mencetak nilai dari variabel buah, pada setiap iterasi)


# 5. Iterasi melaui dictionary
dict_buah = {"Mangga": 1, "Apel": 2, "Jeruk": 3} # --> Inisialisasi variabel dict_buah yang berisi tiga pasangan key-value
for kunci in dict_buah:                          # --> Loop for yang mengulang setiap key dalam dict_buah (pada setiap iterasi variabel kunci akan berisi salah satu key dari dict)
    print(kunci, dict_buah[kunci])               # --> Hasilnya adalah Mangga 1, Apel 2, Jeruk 3 (mencetak nilai dari variabel kunci (key dan value yang sesuai dari dict))

# 6. Menggunakan range() --> Untuk menghasilkan urutan bilangan
for tobrut in range(5): # --> Loop for yang akan mengulang setiap nilai dalam rentang 0 hingga 4 atau (pada setiap iterasi variabel tobrut akan mengambil nilai dari 0 hingga 4)
    print(tobrut)       # --> Mencetak nilai dari variabel tobrut pada setiap iterasi dan hasilnya adalah 0 1 2 3 4

# 7. Menggunakan range() dengan strat dan stop
for tobrut in range(1, 5): # --> loop for yang akan mengulang setiap nilai dalam rentang 1 hingga 4 (inklusif) atau (pada setiap iterasi variabel tobrut akan mengambil nilai dari 1 hingga 4)
    print(tobrut)          # --> Mencetak nilai dari variabel tobrut pada setiap iterasi dan hasilnya adalah 1 2 3 4

# 8. Menggunakan range() dengan step
for tobrut in range(1, 8, 2): # --> Loop for yang akan mengulang setiap nilai dalam rentang 1 hingga 7 (inklusif) dengan langkah sebesar 2 atau (pada setiap iterasi variabel tobrut akan mengambil nilai dari 1,3,5,7)
    print(tobrut)             # --> Mencetak nilai dari variabel tobrut pada setiap iterasi dan hasilnya adalah 1 3 5 7

# 9. Menggunakan perulangan bersarang (nested loops)
for tobrut in range(3):                              # --> Loop for terluar yang akan mengulang setiap nilai dalam rentang 0 hingga 2 (inklusif) atau (pada setiap iterasi variabel tobrut akan mengambil nilai dari 0 hingga 2)
    for brutal in range(2):                          # --> Loop bersarang yang berada di dalam loop terluar dan loop ini akan mengulang setiap nilai dalam rentang 0 hingga 1 (inklusif) atau (pada setiap iterasi variabel brutal akan mengambil nilai dari 0 hingga 1)
        print(f"tobrut: {tobrut}, brutal: {brutal}") # --> Mencetak nilai dari variabel tobrut dan brutal pada setiapp iterasi dan hasilnya adalah mencetak kombinasi pasangan nilai dari kedua loop tobrut:0, brutal:0 - tobrut:0, brutal:1 - tobrut1, brutal0 - tobrut:1, brutal:1 - tobrut:2, nrutal:0 - tobrut:2, brutal:1

# 10. Perulangan dengan else
for tobrut in range(3): # --> Loop for yang akan mengulang setiap nilai dalam rentang 0 hingga 2 (inklusif) atau (pada setiap iterasi variabel tobrut akan mengambil nilai 0 hingga 2)
    print(tobrut)       # --> Mencetak nilai dari variabel tobrut pada setiap iterasi dan hasilnya adalah 0 1 2
else:
    print("Selesai")    # --> Blok else dalam loop for akan dieksekusi setelah semua iterasi selesai dan hasilnya adalah Selesai

# 11. Menggunakan break dan continue
# break untuk menghentikan perulangan
for tobrut in range(5): # --> Loop for yang akan mengulang setiap nilai dalam rentang 0 hingga 4 (inklusif) atau (pada setiap iterasi variabel tobrut akan mengambil nilai 0 hingga 4)
    if tobrut == 3:     # --> Kita menggunakan kondisi, jika nilai tobrut sama dengan 3, maka pernyataan di dalam blok if akan dieksekusi atau (pada iterasi ketiga, ketika tobrut bernilai 3 kondisi terpenuhi)
        break           # --> Lalu loop akan dihentikan dengan pernyataan break
    print(tobrut)       # --> Mencetak nilai dari variabel tobrut pada setiap iterasi sebelum kondisi terpenuhi dan asilnya adalah 0 1 2

# continue untuk melewati iterasi
for tobrut in range(5):           # --> Loop for akan mengulang setiap nilai dalam rentang 0 hingga 4 (inklusif) atau (pada setiap iterasi variabel tobrut akan mengambil nilai 0 hingga 4)
    if tobrut == 3:               # --> Kita menggunakan kondisi, jika nilai tobrut sama dengan 3, maka pernyataan di dalam blok if akan dieksekusi atau (pada iterasi ketiga, ketika tobrut bernilai 3 kondisi terpenuhi)
        continue                  # --> Lalu loop akan melanjutkan ke iterasi berikutnya menggunakan pernyataan continue
    print(f"coba {tobrut}")       # --> Mencetak setiap nilai dari variabel tobrut pada setiap iterasi sebelum kondisi terpenuho dan hasilnya adalah 0 1 2 4 (kenapa 0 1 2 4 bukan 0 1 2 karena kita menggunakan pernyataan continue)

# 12. Iterasi melalui set
set_buah = {'Apel', 'Mangga', 'Jeruk'} # --> Inisialisasi variabel set_buah yang berisi 3 elemen (perbedaan utama set dan list/dict adalah set tidak memiliki urutan dan tidak mengizinkan duplikasi)
for buah in set_buah:                  # --> Loop for yang akan mengulang setiap elemen dalam set_buah (pada setiap iterasi variabel buah akan berisi salah satu elemen dari set)
    print(buah)                        # --> Mencetak nilai dari variabel buah pada setiap iterasi dan hasilnya adalah Apel Mangga Jeruk

# 13. Menggunakan enumerate() --> Menambahkan penghitung ke itrable dan mengembalikannya dalam bentuk objek enum. Berguna ketika kita memerlukan indeks dalam perulangan
list_buah = ['Apel', 'Mangga', 'Jeruk']     # --> Inisialisasi variabel list_buah yang berisi 3 elemen
for index, buah in enumerate(list_buah):    # --> loop for yang akan mengulang setiap elemen dalam list_buah dan fungsi enumerate() digunakan untuk menghasilkan pasangan indeks dan nilai dari list (pada setiap iterasi, variabel index akan berisi indeks mulai dari 0 dan variabel buah akan berisi nilai dari lis)
    print(index, buah)                      # --> Mencetak nilai dari variabel index dan buah pada setiap iterasi dan hasilnya aalah 0 apel, 1 Mangga, 2 Jeruk (indeks dan nama buah yang ada dalam list)

# 14. Menggunakan zip() --> digunakan untuk menggabungkan dua atau lebih itrable, menghasilkan tuple pasangan elemen dari itrable
list_buah = ['Apel', 'Mangga', 'Jeruk']         # --> Inisialisasi variabel list_buah yang berisi 3 elemen
list_harga = [1000, 2000, 3000]                 # --> Inisialisasi variabel list_harga yang berisi 3 elemen (nantinya masing-masing akan mewakili harga buah yang sesuai dengan urutan di list_buah)

for buah, harga in zip(list_buah, list_harga):  # --> Loop for yang akan mengulang setiap pasangan nilai dari list_buah dan list_harga dan fungsi zip menggabungkan elemen-elemen dari dua list menjadi pasang-pasangan (pada setiap iterasi variabel buah akan berisi nama buah dan variabel harga akan berisi harga buah yang sesuai)
    print(f"{buah}, {harga}")                   # --> Mencetak nilai dari variabel buah, harga pada setiap iterasi dan hasilnya adalah Apel 1000, Mangga 2000, Jeruk 3000


""" Teknik Lebih Lanjut Penggunaan list comprehensions, generator expressions, iterasi melalui file, serta manipulasi iterator. """

# 1. List Comprehension -->  Cara singkat dan elegan untuk membuat list baru dari itrable yang ada
# Membuat list dengan list comprehension
list_buah = ['Apel', 'Mangga', 'Jeruk']             # --> Inisialisasi variabel list_buah yang berisi 3 elemen
buah_baru = [buah.upper() for buah in list_buah]    # --> Membuat list baru yang berisi elemen dari list_buah, namun setiap elemen diubah menjadi huruf kapital menggunakan metode upper() atau (for untuk membuat list comprehension atau digunakan untuk mengitersi melalui setiap elemen dalam list_buah dan merubah elemen menjadi huruf kapital)
print(buah_baru)                                    # --> Mencetak dari list baru yaitu buah_baru dan hasilnya adalah APEL, MANGGA, JERUK

# list comprehension dengan kondisi
list_angka = [1,2,3,4,5,6,7,8,9,10]                              # --> Inisialisasi variabel list_angka yang berisi elemen atau nilai 1-10
angka_genap = [angka for angka in list_angka if angka % 2 == 0]  # --> Membuat list baru (list comprehension mengambil setiap elemen dari list_angka dan menyimpan dalam variabel angka, lalu memeriksa apakah elemen tersebut adalah angka genap) (jika kondisi terpenuhi, yaitu elemen yang berada di varieable angka adalah genap maka lemen tersebut disimpan ke dalam list baru yaitu angka_genap)
angka_ganjil = [nomor for nomor in list_angka if nomor % 2]      # --> Membuat list baru (list comprehension mengambil setiap elemen dari list_angka dan menyipan dalam variabel nomor, lalu memeriksa apakah elemen tesebut merupakan angka ganjil) (jika kondisi terpenuhi, yaitu elemen yang berada di variabel nomor adalah ganjil maka elemen tersebut disimpan ke dalam list baru yaitu angka_ganjil)
print(f"japan : {angka_genap}")                                  # --> Mencetak dari list angka_genap dan hasilnya adalah 2,4,6,8,10
print(f"Japan : {angka_ganjil}")                                 # --> Mencetak dari list angka ganjil dan hasilnya adalah 1,3,5,7,9

# 2. Generator Expressions --> Mirip dengan list comprehension, tetapi ini menghasilkan item satu per satu menggunakan iterator, yang lebih effisien dalam penggunaan memori untuk data yang besar
generator_angka = (angka for angka in range(10)) # --> Deklarasi generator dengan nama variabel generator_angka (list comprehension, memanfaatkan for di dalam variabel dengan mengmabil setiap angka dari mulai dari 0-9 dan menyimpan dalam list generator-angka)
for angka in generator_angka:                    # --> Loop for untuk mengitarasi melalui generator (setiap angka yang dihailkan oleh generator akan disimpan dalam variabel angka)
    print(angka)                                 # --> Laulu mencetak nilai dari variabel angka, pada setiap iterasi dan hasilnya adalah 0 1 2 3 4 5 6 7 8 9

# 3. Iterasi melalui file --> Kita dapat membaca file baris demi baris menggunakan perulangan for
with open("contoh.txt", "w") as file:  # --> Membuka file dalam mode tulis dan jika file tidak ada, maka akan dibuat
    file.write("Toket brutal 2024!\n") # --> Menulis teks ke dalam file dan \n untuk membuat baris baru setelah teks
    file. write("Terlalu unfaedah\n")  # --> Menulis teks ke dalam file dan \n untuk membuat baris baru setelah teks

with open("contoh.txt", "r") as file:  # --> Membuka file dalam mode baca dan dapat membaca isi file
    for line in file:                  # --> Membaca setiap baris dari isi file dan meyimpan dalam variabel line
        hasil_line = line.strip()      # --> strip() --> menghapus spasi putih di awal dan akhir setiap baris lalu menyimpan ke variabel hasil_line
        print(hasil_line)              # --> Mencetak isi setiap baris file dan hasilnya adlaah isi dari file contoh.txt

# 4. Manipulasi Iterator dengan itertools Count --> Menghasilkan iterator yang menghasilkan angka yang tidak pernah berakhir

import itertools                   # --> Mengimpor modul yang berisi fungsi dan generator untuk menghasilkan iterasi berbagai bentuk data
for tobrut in itertools.count(10): # --> Loop for (menggunakan generator iteratools) untuk mengitrasi generator ini yang akan menghasilkan angka secara beruntun dimulai dari angka 10 dan setiap iterasi, nilai akan disipan di variabel tobrut
    print(tobrut)                  # --> Mencetak nilai pada setiap iterasi dan hasilnya adalah 10 11 12 13 14 15
    if tobrut >= 15:               # --> Menggunakan kondisional, yang memerikas apakah nilai tobrut lebih besar sama dengan 15
        break                      # --> Jika kondisi terpenuhi yaitu 15, maka pernyataan break akan memekasa menghentikan loop

# Itertools Cycle --> Mengulang elemen dari iterable tanpa henti
ukhti = 0                                       # --> Inisialisasi variabel ukhti dengan nilai 0
for tobrut in itertools.cycle(["A", "B", "C"]): # --> Loop for yang menggunakan generator iteratools, generator ini akan mengulang elemen dari list secara berulang tanpa henti dan setiap iterasi nilai akan disimpan dalam variabel tobrut
    print(tobrut)                               # --> Mencetak nilai tobrut pada setiap iterasi dan hasilnya aalah A B C. A B C, A B C
    ukhti += 1                                  # --> Pada setiap iterasi nilai ukhti akan ditambahkan 1 (increment)
    if ukhti == 9:                              # --> Menggunakan kondisional, memerikasa apakah nilai ukhti sama dengan 9
        break                                   # --> Jika kondisi terpenuhi, penyetaan break akan memekasa mehnetikan loop

# Itertools Chain --> Menggabungkan beberapa iterble menjadi satu iterator
list1 = [1,2,3]                             # --> Inisialisasi variabel list1 dengan 3 elemen (tanah air dan udara eh bukan avatar ding wkwkwk-abaikan)
list2 = ["a", "b", "c"]                     # --> Inisialisasi variabel list2 dengan 3 elemen
for item in itertools.chain(list1, list2):  # --> Loop for yang menggunakan generator itertools, generator ini menggabungkan elemen dari kedua list dan menjadikan satu urutan, lalu setiap elemen akan di smpan dalam variabel item
    print(item)                             # --> Mencetak nilai item dalam setiap iterasi dan hasilnya adalah 1 2 3 a b c

# 5. Menggunakan fungsi buatan sendiri dalam List Comprehension
def is_tobrut(t):                               # --> Deklarasi fungsi is_tobrut dengan satu parameter
    if t <= 1:                                  # --> Menggunakan kondisi, jika nilai t kurang dari sama dengan 1
        return False                            # --> lalu jika terpenuhi maka akan mengembalikan false
    for tobrut in range(2, int(t ** 0.5) + 1):  # --> Loop for yang akan berjalan dari 2 hingga akhir kuadrat dari t (dibulatkan ke atas) dan dalam setiap iterasi nilai tobrut akan mengembil nilai dari rentang tersebut
        if t % tobrut == 0:                     # --> Menggunakan kondisi, jika nilai t dapat dibagi habis oleh tobrut
            return False                        # --> lalu jika terpenuhi makan akan mengembalikan False
    return True                                 # --> Jika kondisi di atas tidak terpenuhi, fungsi akan mengembalikan True (menandakan bahwa t adalah bilangan prima)

ukhti_tobrut = [x for x in range(20) if is_tobrut(x)] # --> List comprehension, ukhti_tobrut yang berisi bilangan prima dari 0 hingga 19 (1. mengulang dari 0 hingga 19 | 2. kondisi yang memeriksa apakah x adalah bilangan prima dan menggunakan fungsi is_tobrut | 3. jika kondisi terpenuhi, x akan dimasukan ke dalam list ukhti_tobrut)
print(ukhti_tobrut)                                   # --> Mencetak isi list yang berisi bilangan prima 0 hingga 19 dan hasilnya adalah 2 3 5 7 11 13 17 19

# 6. Nested List Comprehension --> ini juga bisa bersarang untuk mengulangi melalui nested struktur
ukhti = [[1,2,3], [4,5,6], [7,8,9]]             # --> Inisialisasi variabel ukhti yang berisi 3 list atau sublist lalu masing-masing dari sublist berisi 3 elemen
tobrut = [num for row in ukhti for num in row]  # --> List comprehension yang menggabungkan semua elemen dari sublist menjadi satu list tunggal (1. for row mengulang memalui setiap sublist dalam ukhti | 2. for in row mengulang memaluli setiap elemen dalam sublist 3. num merupakan variabel yang menyimpan elemen)
print(tobrut)                                   # --> Mencetak isi dari list dan hasilnya adalah 1 2 3 4 5 6 7 8 9

# 7. Enumerete dengan start index --> Kita dapat menentukan dari mana index enumerate dimulai
list_buah = ['Apel', 'Mangga', 'Jeruk']             # --> Inisialisasi variabel list_buah yang berisi 3 elemen
for index, buah in enumerate(list_buah, start=1):   # --> loop for yang menggunakan fungsi enumrate (1. enumerate(list_buah, start=1) menghasilkan pasangan indeks dan nilai dari setiap elemen dalam list_buah | 2. index adalah variabel yang menyimpan indeks (dimulai dari 1 karena kita menggunakan start=1 | 3. buah adalah variabel yang menyimpan nilai dari setiap elemen dalam list_buah )
    print(index, buah)                              # --> Mencetak indeks dan nilai dari setiap elemen dalam list dan hasilnya adalah 1 Apel, 2 Mangga, 3 Jeruk

# 8. Menggunakan zip untuk menggabungkan list dengan panjang berbeda --> Dapat menggabungkan list dengan panjang yang berbeda
from itertools import zip_longest                               # --> Mengimpor fungsi zip_longest dari modul iteratools (digunakan untuk menggabungkan dua atau lebih itrable secara berurutan atau mengisi nilai default/None jika salah satu iterble lebih pendek dari yang lain)

list1 = [1, 2]                                                  # --> Inisialisasi variabel list1 yang berisi 2 element
list2 = ['a', 'b', 'c']                                         # --> Inisialisasi variabel list2 yang berisi 3 elemen
for num, char in zip_longest(list1, list2, fillvalue='None'):   # --> Loop for yang menggunakan fungsi zip_longest (1. menggabungkan elemen kedua list secara berurutan, jika salah satu list lebih pendek nilai default/None akan digunakan sebagai pengganti - 2. num variabel yang menyimpan nilai dari list1 - 3. char adalah variabel yang menyimpan nilai dari list2)
    print(num, char)                                            # --> Mencetak nilai pada setiap iterasi dan hasilnya adalah 1 a, 2 b dan None c


# 9. Bonus untuk kamu
for heart in range(10): # --> Loop for yang akan berjalan dari 0 hingga 9 dan setiap iterasi variabel heart akan mengambil nilai dari rentang tersebut
    love = "I Love You" # --> Inisialisasi variabel Love dengan nilai string
    print(love)         # --> Mencetak nilai pada setiap iterasi dan hasilnya adalah I Love You 10x


hati = [1,2,3,4,5]      # --> Inisialisasi variabel hati dengan 5 elemen
for sayang in hati:     # --> Loop for yang akan mengulang setiap elemen dalam list hati dan setiap iterasi nilai dari elemen akan disimpan dalam variabel sayang
    cinta = "I Love U"  # --> Inisialisasi variabel cinta dengan nilai string
    if sayang < 3:      # --> Menggunakan kondisi, yang memeriksa apakah nilai sayang kurang dari 3 dan jika kondisi terpenuhi (yaitu sayang adalah 1 atau 2)
        print(cinta)    # --> Jika terpenuhi makan akan mencetan ini dan hasilnya adalah I Love U, I Love U

hati = ["Sayang"] * 2   # --> Inisialisasi variabel hati dengan elemen tunggal yang diulangi 2 kali
for pesan in hati:      # --> Loop for yang mengulang melalui setiap elemen dalam list hati dan setiap iterasi, nilai dari elemen akan disimpan dalam variabel pesan
    print(pesan)        # --> Mencetak nilai dari variabel pesan pada setiap iterasi dan hasilnya adalah Sayang, Sayang
