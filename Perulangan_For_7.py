""" Perulangan for Termasuk Penjelasan Dasar, Iterasi Melalui Berbagai Tipe Data """
""" Teknik Lebih Lanjut Juga Tersedia """

# Catatan sangat penting! :

# Itersi --> Proses di mana kita menelusuri atau melintasi setiap elemen dari suatu koleksi data seperti (ist, tuple, set dan dict) satu persatu (secara singkat adalah aksi atau proses) / proses mengulang elemen-elemen dari sebuah itrable
numbers = [1, 2, 3, 4, 5] # --> Ini adalah iterable yang diiterai
for number in numbers:    # --> Iterasi dimulai dari sini
    print(number)         # --> Aksi selama iterasi

    # 1. Iterasi eksplisit --> Kita secara jelas menulis kode untuk mengontrol loop atau perulangan elemen dalam koleksi data, ini biasanya dilakukan dengan menggunakan struktur kontrol loop seperti for dan while
numbers = [1, 2, 3, 4, 5] 
for number in numbers:    
    print(number)   

counts = 0
while counts < 5:
    print(counts)
    counts += 1

    # 2. Iterasi implisit --> Kita menggunakan fungsi built-in fuction python yang secara internal mengiterasi melalui elemen-elemen koleksi data tanpa kita harus menulis loop ekslisit, fugsi ini seperti map, filter dan list comprhension
numbers = [1, 2, 3, 4, 5]
squared = map(lambda x: x**2, numbers)
print(list(squared))

numbers = [1, 2, 3, 4, 5]
even = filter(lambda x: x % 2 == 0, numbers)
print(list(even))

numbers = [1, 2, 3, 4, 5]
squared = [x**2 for x in numbers]
print(squared)

print("Anjing")

# Iterable --> Merupakan objek yang dapat diulang (loop) satu persatu, seperti list, tuple, string, dict dan fitur ini memungkinkan kita untuk mengakses elemen-elemen dari objek tersebut secara berurutan
   # 1. Contoh itrabel
my_list = [1, 2, 3, 4, 5] # --> Ini adalah iterable yang diiterai
for lists in my_list:
    print(lists)

my_tuple = (1, 2, 3, 4, 5)
for tuples in my_tuple:
    print(tuples)
    
my_string = "Zaki"
for chars in my_string:
    print(chars)

my_dictionary = {'key1':'value1', 'key2':'value2'}
for dict in my_dictionary:
    print(dict)

    # 2. Untuk memeriksa apakah suatu objek adalah itrabel, kita dapat menggunakan fungsi iter() dan jika objek bisa diubah menjadi iterator, maka objek tersebut adalah iterabel
my_list = [1, 2, 3, 4, 5] # --> Ini adalah iterable yang diiterai
iter_obj = iter(my_list)  # --> Ini tidak akan menghasilkan error, sehingga my_list adalah iterator
print(iter_obj)           # --> Mencetak objek iterator

# Iterator --> Objek yang mengimplementasikan metode khusus __iter() / __next__() atau memungkinkan kita untuk menelusuri elemen-elemen dari suatu koleksi data seperti list, set, tuple, dict satu persatu dan ini membantu dalam mengakses item tersebut tanpa perlu mengakses seluruh kumpulan data secara langsung

    # 1. Iterator objek yang mewakili alur iterasi di atas iterabel, menggunakan metode iter(yang mengembalikan iterator dari itrabel) next(yang mengakses elemen untuk mengembalikan elemen selanjutnya, jika tidak ada elemen yang tersisa metode ini akan memunculkan pengecualian yaitu stopiteration)
list_buah = ["Apel", "Jeruk", "Mangga"]  # --> Ini adalah iterable yang diiterai
for buah in list_buah:                   # --> Proses iterasi menggunakan loop for
    print(buah)
iterator_buah = iter(list_buah)          # --> Mengembalikan iterator dari itrabel
print(next(iterator_buah))               # --> Menggunakan iterator untuk mengakses elemen dan mengambalikan elemen selanjutnya
print(next(iterator_buah))               # --> Menggunakan iterator untuk mengakses elemen dan mengambalikan elemen selanjutnya
print(next(iterator_buah))               # --> Menggunakan iterator untuk mengakses elemen dan mengambalikan elemen selanjutnya

# Iniisalisasi --> Mengatur nilai awal untuk variabel, objek atau fungsi sehingga siap digunakan dan ada berbagai cara kita bisa melakukan inisialisasi (tergantung pada konteksnya)
    # 1. Inisialisasi variabel (menugaskan nilai awal ke sebuah variabel)
nama = "Tobrut"
umur = 26
tinggi = 170.5
is_student = True
print(nama, umur, tinggi, is_student)

    # 2. Inisialisasi list, tuple, set dan dict --> Menyiapkan struktur data dengan nilai awal

buah = ["apel", "jeruk", "mangga"]
angka = [1, 2, 3, 4, 5]
campuran = [1, "dua", 3.0, True]
print(buah, angka, campuran)

warna = ("merah", "hijau", "biru")
angka_tuple = (1, 2, 3, 4, 5)
print(warna, angka_tuple)

hewan = {"anjing", "kucing", "burung"}
angka_set = {1, 2, 3, 4, 5}
print(hewan, angka_set)

mahasiswa = {"nama": "Tobrut", "umur": 26, "jurusan": "Teknik Informatika"}
angka_dict = {1: "satu", 2: "dua", 3: "tiga"}
print(mahasiswa, angka_dict)

    # 3. Inisialisasi objek dalam class, list, dict, nested data structure --> Menggunakan konstruktor __init__ untuk mengatur nilai-nilai awal atribut objek

# --> Mendefinisikan kelas
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# --> Inisialisasi objek dari kelas
person_satu = Person("Zaki", 26)
person_dua = Person("Ali", 30)

print(f"Nama: {person_satu.name}, Umur: {person_satu.age}")
print(f"Nama: {person_dua.name}, Umur: {person_dua.age}")


# --> Inisialisasi list berisi objek-objek dari class Person
people = [Person("Zaki", 26), Person("Ali", 30), Person("Tina", 22)] 
for person in people:
    print(f"Nama: {person.name}, Umur: {person.age}")

# --> Inisialisasi dict berisi on=bjek-objek dalam celass person
people_dict = {                             
    "Zaki": Person("Zaki", 26),
    "Ali": Person("Ali", 30),
    "Tina": Person("Tina", 22)
}
for key, person in people_dict.items():
    print(f"Kunci: {key}, Nama: {person.name}, Umur: {person.age}")

# --> Inisialisasi nested data structure atau struktur data bsersarang
data = {                                    
    "buah": ["apel", "jeruk", "mangga"],
    "angka": [1, 2, 3, 4, 5],
    "hewan": {"anjing", "kucing", "burung"},
    "mahasiswa": {"nama": "Tobrut", "umur": 26, "jurusan": "Teknik Informatika"}
}
print(data)

    # 4. Inisialisasi fungsi 

# --> Inisialisasi fungsi tanpa parameter
def halo_dunia():
    print("Halo, Dunia!")
halo_dunia()

# --> Inisialisasi fungsi dengan parameter
def halo_nama(nama):
    print(f"Halo, {nama}!")
halo_nama("Tobrut")

# --> Inisialisasi fungsi dengan nilai balik (return)
def tambah(a, b):
    return a + b
hasil = tambah(5, 3)
print(f"Hasil penjumlahan: {hasil}")

# --> Inisialisasi fungsi dengan parameter default
def sapa(nama="Dunia"):
    print(f"Halo, {nama}!")
sapa()
sapa("Tobrut")

# --> Inisialisasi fungsi dengan parameter variabel
def cetak_semua(*args):
    for arg in args:
        print(arg)
cetak_semua("apel", "jeruk", "mangga")

# --> Inisialisasi fungsi dengan keyword arguments
def cetak_detail(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
cetak_detail(nama="Tobrut", umur=26, pekerjaan="Programmer")

    # 5. inisialisasi menggunakan built-in functions

# --> Menggunakan built-in function untuk menginisialisasi list
list_angka = list(range(1, 6))
print(list_angka)

# --> Menggunakan built-in function untuk menginisialisasi string
str_angka = str(12345)
print(str_angka) 

# --> Menggunakan built-in function untuk menginisialisasi tuple
tuple_buah = tuple(["apel", "jeruk", "mangga"])
print(tuple_buah)  

# --> Menggunakan built-in function untuk menginisialisasi set
set_hewan = set(["anjing", "kucing", "burung"])
print(set_hewan) 

# --> Menggunakan built-in function untuk menginisialisasi dictionary
#dict_mahasiswa = dict(nama="Tobrut", umur=26, jurusan="Teknik Informatika")
#print(dict_mahasiswa)

# --> Menggunakan built-in function untuk memetakan (map) nilai
list_kuadrat = list(map(lambda x: x**2, list_angka))
print(list_kuadrat) 

# --> Menggunakan built-in function untuk menyaring (filter) nilai
list_genap = list(filter(lambda x: x % 2 == 0, list_angka))
print(list_genap)  

# --> Menggunakan built-in function untuk mendapatkan panjang elemen
panjang_list = len(list_angka)
print(f"Panjang list: {panjang_list}")  

# --> Menggunakan built-in function untuk mendapatkan nilai maksimum dan minimum
nilai_maks = max(list_angka)
nilai_min = min(list_angka)
print(f"Nilai maksimum: {nilai_maks}, Nilai minimum: {nilai_min}")  

# -->Menggunakan built-in function untuk mengurutkan elemen
list_terurut = sorted(list_angka, reverse=True)
print(list_terurut)  

# Catatan hanya sampai sini!

# Perulangan for digunakan untuk mengulangi item-item dalam urutan seperti (list, tuple, dict, set dan string)

# 1. Sintaks dasar perulangan for
#for item in itrable:
    #Lakukan sesuatu dengan item

# 2. Itersi melalui list
list_buah = ["Semangka", "Tobrut", "Jeruk", "Durian"] # --> Inisialisasi variabel yang menyimpan data list, berisi 4 elemen data string
for buah in list_buah:                                # --> loop for yang akan mengulang setiap elemen dalam list_buah dan pada setiap iterasi variabel buah akan berisi salah satu elemen dari list
    print(buah)                                       # --> Hasilnya adalah Semangka, Tobrut, Jeruk, Durian (mencetak nilai atau elemen dari variabel buah pada setiap iterasi)

# 3. Iterasi melalui string
toket_brutal = "Ukhti"      # --> Inisialisasi variabel yang menyimpan data string
for huruf in toket_brutal:  # --> Loop for yang akan mengulangi setiap karakter dalam toket_brutal dan pada setiap iterasi variabel huruf, akan berisi salah satu karakter dari string
    print(huruf)            # --> Hasilnya adalah mencetak setiap karakter dari ukhti secara terpisah (mencetak nilai dari variabel huruf pada setiap iterasi)

# 4. Iterasi melalui tuple
tuple_buah = ("Anggur", "Jeruk", "Nanas") # --> Inisialisasi variabel yang menyimpan data tuple, berisi 3 elemen data string (ingat tupel tuple bersifat immutabel atau tidak bisa diubah setelah dibuat)
for buah in  tuple_buah:                  # --> Loop for yang akan mengulang setiap elemen dalam tuple_buah dan pada setiap iterasi variabel buah, akan berisi salah satu elemen dari tuple
    print(buah)                           # --> Hasilnya adalah Amggur, Jeruk, Nanas (mencetak nilai dari variabel buah, pada setiap iterasi)


# 5. Iterasi melaui dictionary
dict_buah = {"Mangga": 1, "Apel": 2, "Jeruk": 3} # --> Inisialisasi variabel yang menyimpan data dict, berisi 3 key-value data stirng dan integer
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
set_buah = {'Apel', 'Mangga', 'Jeruk'} # --> Inisialisasi variabel yang menyimpan data set, berisi 3 elemen data string (perbedaan utama set dan list/dict adalah set tidak memiliki urutan dan tidak mengizinkan duplikasi)
for buah in set_buah:                  # --> Loop for yang akan mengulang setiap elemen dalam set_buah (pada setiap iterasi variabel buah akan berisi salah satu elemen dari set)
    print(buah)                        # --> Mencetak nilai dari variabel buah pada setiap iterasi dan hasilnya adalah Apel Mangga Jeruk

# 13. Menggunakan enumerate() --> Menambahkan penghitung ke itrable dan mengembalikannya dalam bentuk objek enum. Berguna ketika kita memerlukan indeks dalam perulangan
list_buah = ['Apel', 'Mangga', 'Jeruk']     # --> Inisialisasi variabel yang menyimpan data list, berisi 3 elemen data string
for index, buah in enumerate(list_buah):    # --> loop for yang akan mengulang setiap elemen dalam list_buah dan fungsi enumerate() digunakan untuk menghasilkan pasangan indeks dan nilai dari list (pada setiap iterasi, variabel index akan berisi indeks mulai dari 0 dan variabel buah akan berisi nilai dari lis)
    print(index, buah)                      # --> Mencetak nilai dari variabel index dan buah pada setiap iterasi dan hasilnya aalah 0 apel, 1 Mangga, 2 Jeruk (indeks dan nama buah yang ada dalam list)

# 14. Menggunakan zip() --> digunakan untuk menggabungkan dua atau lebih itrable, menghasilkan tuple pasangan elemen dari itrable
list_buah = ['Apel', 'Mangga', 'Jeruk']         # --> Inisialisasi variabel yang menyimpan data list, berisi 3 elemen data string
list_harga = [1000, 2000, 3000]                 # --> Inisialisasi variabel yang menyimpan data list, berisi 3 elemen data integer (nantinya masing-masing akan mewakili harga buah yang sesuai dengan urutan di list_buah)

for buah, harga in zip(list_buah, list_harga):  # --> Loop for yang akan mengulang setiap pasangan nilai dari list_buah dan list_harga dan fungsi zip menggabungkan elemen-elemen dari dua list menjadi pasang-pasangan (pada setiap iterasi variabel buah akan berisi nama buah dan variabel harga akan berisi harga buah yang sesuai)
    print(f"{buah}, {harga}")                   # --> Mencetak nilai dari variabel buah, harga pada setiap iterasi dan hasilnya adalah Apel 1000, Mangga 2000, Jeruk 3000


""" Teknik Lebih Lanjut Penggunaan list comprehensions, generator expressions, iterasi melalui file, serta manipulasi iterator. """

# 1. List Comprehension -->  Cara singkat dan elegan untuk membuat list baru dari itrable yang ada
# Membuat list dengan list comprehension
list_buah = ['Apel', 'Mangga', 'Jeruk']             # --> Inisialisasi variabel yang menyimpan data list, berisi 3 elemen data string
buah_baru = [buah.upper() for buah in list_buah]    # --> Membuat list baru yang berisi elemen dari list_buah, namun setiap elemen diubah menjadi huruf kapital menggunakan metode upper() atau (for untuk membuat list comprehension atau digunakan untuk mengitersi melalui setiap elemen dalam list_buah dan merubah elemen menjadi huruf kapital)
print(buah_baru)                                    # --> Mencetak dari list baru yaitu buah_baru dan hasilnya adalah APEL, MANGGA, JERUK

# list comprehension dengan kondisi
list_angka = [1,2,3,4,5,6,7,8,9,10]                              # --> Inisialisasi variabel yang meyimpan data list, berisi 10 elemen data integer
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
ukhti = 0                                       # --> Inisialisasi variabel yang menyimpan data integer
for tobrut in itertools.cycle(["A", "B", "C"]): # --> Loop for yang menggunakan generator iteratools, generator ini akan mengulang elemen dari list secara berulang tanpa henti dan setiap iterasi nilai akan disimpan dalam variabel tobrut
    print(tobrut)                               # --> Mencetak nilai tobrut pada setiap iterasi dan hasilnya aalah A B C. A B C, A B C
    ukhti += 1                                  # --> Pada setiap iterasi nilai ukhti akan ditambahkan 1 (increment)
    if ukhti == 9:                              # --> Menggunakan kondisional, memerikasa apakah nilai ukhti sama dengan 9
        break                                   # --> Jika kondisi terpenuhi, penyetaan break akan memekasa mehnetikan loop

# Itertools Chain --> Menggabungkan beberapa iterble menjadi satu iterator
list1 = [1,2,3]                             # --> Inisialisasi variabel yang menyimpan data list, berisi 3 elemen data integer (tanah air dan udara eh bukan avatar ding wkwkwk-abaikan)
list2 = ["a", "b", "c"]                     # --> Inisialisasi variabel yang menyimpan data list, berisi 3 elemen data string
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
ukhti = [[1,2,3], [4,5,6], [7,8,9]]             # --> Inisialisasi variabel yang menyimpan data list, berisi 3 list atau sublist lalu masing-masing dari sublist berisi 3 elemen data integer
tobrut = [num for row in ukhti for num in row]  # --> List comprehension yang menggabungkan semua elemen dari sublist menjadi satu list tunggal (1. for row mengulang memalui setiap sublist dalam ukhti | 2. for in row mengulang memaluli setiap elemen dalam sublist 3. num merupakan variabel yang menyimpan elemen)
print(tobrut)                                   # --> Mencetak isi dari list dan hasilnya adalah 1 2 3 4 5 6 7 8 9

# 7. Enumerete dengan start index --> Kita dapat menentukan dari mana index enumerate dimulai
list_buah = ['Apel', 'Mangga', 'Jeruk']             # --> Inisialisasi variabel yang menyimpan data list, berisi 3 elemen data string
for index, buah in enumerate(list_buah, start=1):   # --> loop for yang menggunakan fungsi enumrate (1. enumerate(list_buah, start=1) menghasilkan pasangan indeks dan nilai dari setiap elemen dalam list_buah | 2. index adalah variabel yang menyimpan indeks (dimulai dari 1 karena kita menggunakan start=1 | 3. buah adalah variabel yang menyimpan nilai dari setiap elemen dalam list_buah )
    print(index, buah)                              # --> Mencetak indeks dan nilai dari setiap elemen dalam list dan hasilnya adalah 1 Apel, 2 Mangga, 3 Jeruk

# 8. Menggunakan zip untuk menggabungkan list dengan panjang berbeda --> Dapat menggabungkan list dengan panjang yang berbeda
from itertools import zip_longest                               # --> Mengimpor fungsi zip_longest dari modul iteratools (digunakan untuk menggabungkan dua atau lebih itrable secara berurutan atau mengisi nilai default/None jika salah satu iterble lebih pendek dari yang lain)

list1 = [1, 2]                                                  # --> Inisialisasi variabel yang menyimpan data list, berisi 2 elemen data integer
list2 = ['a', 'b', 'c']                                         # --> Inisialisasi variabel yang menyimpan data list, berisi 3 elemen data string
for num, char in zip_longest(list1, list2, fillvalue='None'):   # --> Loop for yang menggunakan fungsi zip_longest (1. menggabungkan elemen kedua list secara berurutan, jika salah satu list lebih pendek nilai default/None akan digunakan sebagai pengganti - 2. num variabel yang menyimpan nilai dari list1 - 3. char adalah variabel yang menyimpan nilai dari list2)
    print(num, char)                                            # --> Mencetak nilai pada setiap iterasi dan hasilnya adalah 1 a, 2 b dan None c


# 9. Bonus untuk kamu
for heart in range(10): # --> Loop for yang akan berjalan dari 0 hingga 9 dan setiap iterasi variabel heart akan mengambil nilai dari rentang tersebut
    love = "I Love You" # --> Inisialisasi variabel yang menyimpan data string
    print(love)         # --> Mencetak nilai pada setiap iterasi dan hasilnya adalah I Love You 10x


hati = [1,2,3,4,5]      # --> Inisialisasi variabel yang menyimpan data list, berisi 5 elemen data integer
for sayang in hati:     # --> Loop for yang akan mengulang setiap elemen dalam list hati dan setiap iterasi nilai dari elemen akan disimpan dalam variabel sayang
    cinta = "I Love U"  # --> Inisialisasi variabel yang meyimpan data string
    if sayang < 3:      # --> Menggunakan kondisi, yang memeriksa apakah nilai sayang kurang dari 3 dan jika kondisi terpenuhi (yaitu sayang adalah 1 atau 2)
        print(cinta)    # --> Jika terpenuhi makan akan mencetan ini dan hasilnya adalah I Love U, I Love U

hati = ["Sayang"] * 2   # --> Inisialisasi variabel yang menyimpan data list, berisi 1 elemen data string yang diulangi 2 kali
for pesan in hati:      # --> Loop for yang mengulang melalui setiap elemen dalam list hati dan setiap iterasi, nilai dari elemen akan disimpan dalam variabel pesan
    print(pesan)        # --> Mencetak nilai dari variabel pesan pada setiap iterasi dan hasilnya adalah Sayang, Sayang
