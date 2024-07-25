""" Catatan Sangat Penting! Pahami Secukupnya, Karena Kita Harus Mempelajari Pondasinya Terlebih Dahulu Dan Maka Dari Itu Setiap Baris Code Di Bagian Ini Tidak Saya Jelaskan Secara Detail """

# Itersi --> Proses di mana kita menelusuri atau melintasi setiap elemen dari suatu koleksi data seperti (list, tuple, set dan dict) satu persatu (secara singkat adalah aksi atau proses) / proses mengulang elemen-elemen dari sebuah itrable
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
my_list = [1, 2, 3, 4, 5]
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
my_list = [1, 2, 3, 4, 5] # --> Ini adalah iterable yang diiterasi
iter_obj = iter(my_list)  # --> Ini tidak akan menghasilkan error, sehingga my_list adalah iterator
print(iter_obj)           # --> Mencetak objek iterator

# Iterator --> Objek yang mengimplementasikan metode khusus __iter() / __next__() atau memungkinkan kita untuk menelusuri elemen-elemen dari suatu koleksi data seperti list, set, tuple, dict satu persatu dan ini membantu dalam mengakses item tersebut tanpa perlu mengakses seluruh kumpulan data secara langsung

    # 1. Iterator objek yang mewakili alur iterasi di atas iterabel, menggunakan metode iter(yang mengembalikan iterator dari itrabel) next(yang mengakses elemen untuk mengembalikan elemen selanjutnya, jika tidak ada elemen yang tersisa metode ini akan memunculkan pengecualian yaitu stopiteration)
list_buah = ["Apel", "Jeruk", "Mangga"]  # --> Ini adalah iterable yang diiterasi
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
