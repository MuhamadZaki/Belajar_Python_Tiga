""" Variabel """

# Variabel --> Merupakan wadah untuk menampung nilai

# Aturan Penamaan Variabel
# 1. Nama variabel harus dimulai dengan huruf (a-z, A-Z) dan karakter garis bawah juga termasuk
# 2. Nama variabel tidak boleh dimulai dengan angka
# 3. Nama variabel hanya boleh mengandung karakter alfanumrik dan garis bawah (A-Z, a-z, 0-9 dan _)
# 4. Nama variabel menggunakan huruf besar-kecil (case-sensitive)

""" Contoh Penamaan Yang Benar """

print("-------->")                          # -- Abaikan ini

nama = "Zaki"                               # --> Inisialisasi variabel yang menyimpan data string
umur = 26                                   # --> Inisialisasi variabel yang menyimpan data integer
_alamat = "Kebumen"                         # --> Inisialisasi variabel yang menyimpan data string
nilai2 = 9.5                                # --> Inisialisasi variabel yang menyimpan data float
Srigala = True                              # --> Inisialisasi variabel yang menyimpan data boolean
print(nama, umur, _alamat, nilai2, Srigala) # --> Mencetak variabel

""" Contoh Penamaan Yang Salah """

# 2nilai = 10
# alamat-domisili = "Jakarta"

""" Inisialisasi Varibel """

print("-------->")  # -- Abaikan ini

a = 1               # --> Inisialisasi variabel yang menyimpan data integer
b = "Hello World!"  # --> Inisialisasi variabel yang menyimpan data string
c = 1.5             # --> Inisialisasi variabel yang menyimpan data folat
d = True            # --> Inisialisasi variabel yang menyimpan data boolean
print(a, b, c, d)   # --> Mencetak variabel

""" Mengubah Value Variabel """

print("-------->")  # -- Abaikan ini

himaswork = 10      # --> Inisialisasi variabel yang menyimpan data integer
himaswork = 10      # --> Inisialisasi variabel yang menyimpan data integer
print(himaswork)    # --> Mencetak variabel

""" Mengubah Value Dua Variabel """

print("-------->")  # -- Abaikan ini

maswork = 10                             # --> Inisialisasi variabel yang menyimpan data integer
himaswork = 20                           # --> Inisialisasi variabel yang menyimpan data integer
maswork, himaswork = himaswork, maswork  # --> Mengubah nilai dua variabel
print(maswork)                           # --> Mencetak variabel
print(himaswork)                         # --> Mencetak variabel

""" Tipe Data Umum Dalam Python """

# 1. Integer    --> Bilangan bulat
# 2. Float      --> Bilangan desimal
# 3. String     --> Kumpulan karakter
# 4. Boolean    --> Nilai True atau False
# 5. List       --> Tipe data yang berisi kumpulan elemen-elemen dengan berbagai tipe data seperti string, integer, float dan boolean (kumpulan nilai yang terurut dan bisa diubah)
# 6. Tuple      --> Tipe data yang berisi kumpulan elemen-elemen dengan berbagai tipe data seperti string, integer, float dan boolean (kumpulan nilai yang terurut dan tidak bisa diubah)
# 7. Dictionary --> Kumpulan pasangan key-value

""" Contoh Penggunaan Tipe Data """

print("-------->")  # -- Abaikan ini

my_integer = 10                # --> Inisialisasi variabel yang menyimpan data integer
print(my_integer)              # --> Mencetak variabel

my_float = 5.5             # --> Inisialisasi variabel yang menyimpan data float
print(my_float)            # --> Mencetak variabel

my_string = "Hello Dunia!" # --> Inisalisasi yang menyimpan data ftring
print(my_string)           # --> Mencetak variabel

my_boolean = True          # --> Inisialisasi variabel yang menyimpan data boolean
print(my_boolean)          # --> Mencetak variabel

my_list = [1, 2, 3, 4, 5]  # --> Inisialisasi variabel yang menyimpan data list, berisi 5 elemen data integer
print(my_list)             # --> Mencetak variabel

my_tupel = (1, 2, 3, 4, 5) # --> Inisialisasi variabel yang menyimpan data tupel, berisi 5 elemen data integer
print(my_tupel)            # --> Mencetak variabel

my_tupel = (10,)           # --> Inisialisasi variabel yang menyimpan data tupel, berisi 1 elemen data integer
print(my_tupel)            # --> Mencetak variabel

not_tupel = (10)           # --> Inisialisasi variabel yang menyimpan data integer
print(not_tupel)           # --> Mencetak variabel

my_dictionary = {"key1":"value1", "key2":"value2", "key3":"value3"} # --> Inisialisasi variabel yang menyimpan data dict, berisi 3 key dan value data string
print(my_dictionary)                                                # --> Mencetak variabel

""" Memeriksa Tipe Data """

print("-------->")  # -- Abaikan ini

my_integer = 15         # --> Inisialisasi variabel yang menyimpan data integer
print(type(my_integer)) # --> Mencetak variabel, menggunakan fungsi type untuk memeriksa data suatu variabel


""" Note!"""

print("-------->")  # -- Abaikan ini

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