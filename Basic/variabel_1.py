""" Variabel """

# Variabel --> Merupakan wadah untuk menampung nilai

# Aturan Penamaan Variabel
# 1. Nama variabel harus dimulai dengan huruf (a-z, A-Z) dan karakter garis bawah juga termasuk
# 2. Nama variabel tidak boleh dimulai dengan angka
# 3. Nama variabel hanya boleh mengandung karakter alfanumrik dan garis bawah (A-Z, a-z, 0-9 dan _)
# 4. Nama variabel menggunakan huruf besar-kecil (case-sensitive)

""" Contoh Penamaan Yang Benar """

print("-------->")  # --> Abaikan ini

nama = "Zaki"                               # --> Inisialisasi variabel yang menyimpan data string
umur = 26                                   # --> Inisialisasi variabel yang menyimpan data integer
_alamat = "Kebumen"                         # --> Inisialisasi variabel yang menyimpan data string
nilai2 = 9.5                                # --> Inisialisasi variabel yang menyimpan data float
Srigala = True                              # --> Inisialisasi variabel yang menyimpan data boolean
print(nama, umur, _alamat, nilai2, Srigala) # --> Mencetak variabel --> Zaki 26 Kebumen, 9.5 True

""" Contoh Penamaan Yang Salah """

# 2nilai = 10
# alamat-domisili = "Jakarta"

""" Inisialisasi Varibel """

print("-------->")  # --> Abaikan ini

a = 1               # --> Inisialisasi variabel yang menyimpan data integer
b = "Hello World!"  # --> Inisialisasi variabel yang menyimpan data string
c = 1.5             # --> Inisialisasi variabel yang menyimpan data folat
d = True            # --> Inisialisasi variabel yang menyimpan data boolean
print(a, b, c, d)   # --> Mencetak variabel 1 Hello World! 1.5 True

""" Mengubah Value Variabel """

print("-------->")  # --> Abaikan ini

himaswork = 10      # --> Inisialisasi variabel yang menyimpan data integer
himaswork = 10      # --> Inisialisasi variabel yang menyimpan data integer
print(himaswork)    # --> Mencetak variabel --> 10

""" Mengubah Value Dua Variabel """

print("-------->")  # --> Abaikan ini

maswork = 10                             # --> Inisialisasi variabel yang menyimpan data integer
himaswork = 20                           # --> Inisialisasi variabel yang menyimpan data integer
maswork, himaswork = himaswork, maswork  # --> Mengubah nilai dua variabel
print(maswork)                           # --> Mencetak variabel --> 20
print(himaswork)                         # --> Mencetak variabel --> 10

""" Tipe Data Umum Dalam Python """

# 1. Integer    --> Bilangan bulat
# 2. Float      --> Bilangan desimal
# 3. String     --> Kumpulan karakter
# 4. Boolean    --> Nilai True atau False
# 5. List       --> Tipe data yang berisi kumpulan elemen-elemen dengan berbagai tipe data seperti string, integer, float dan boolean (kumpulan nilai yang terurut dan bisa diubah)
# 6. Tuple      --> Tipe data yang berisi kumpulan elemen-elemen dengan berbagai tipe data seperti string, integer, float dan boolean (kumpulan nilai yang terurut dan tidak bisa diubah)
# 7. Set        --> Tipe data yang berisi kumpulan elemen-elemen dengan berbagai tipe data seperti string, integer, float dan boolean (kumpulan nilai yang tidak terurut dan bisa diubah tapi terbatas(menambahkan dan menghapus elemen))
# 8. Dictionary --> Kumpulan pasangan key-value

""" Contoh Penggunaan Tipe Data """

print("-------->")  # --> Abaikan ini

my_integer = 10            # --> Inisialisasi variabel yang menyimpan data integer
print(my_integer)          # --> Mencetak variabel --> 10

my_float = 5.5             # --> Inisialisasi variabel yang menyimpan data float
print(my_float)            # --> Mencetak variabel --> 5.5

my_string = "Hello Dunia!" # --> Inisalisasi yang menyimpan data string
print(my_string)           # --> Mencetak variabel --> Hello Dunia!

my_boolean = True          # --> Inisialisasi variabel yang menyimpan data boolean
print(my_boolean)          # --> Mencetak variabel --> True

my_list = [1, 2, 3, 4, 5]  # --> Inisialisasi variabel yang menyimpan data list, berisi 5 elemen data integer
print(my_list)             # --> Mencetak variabel --> [1, 2, 3, 4, 5]

my_tupel = (1, 2, 3, 4, 5) # --> Inisialisasi variabel yang menyimpan data tupel, berisi 5 elemen data integer
print(my_tupel)            # --> Mencetak variabel --> (1, 2, 3, 4, 5)

my_tupel = (10,)           # --> Inisialisasi variabel yang menyimpan data tupel, berisi 1 elemen data integer
print(my_tupel)            # --> Mencetak variabel --> (10,)

not_tupel = (10)           # --> Inisialisasi variabel yang menyimpan data integer
print(not_tupel)           # --> Mencetak variabel --> 10

my_set = {1,2,3,4,5}       # --> Inisialisasi variabel yang menyimpan data set, berisi 5 elemen data integer
print(my_set)              # --> Mencetak variabel --> {1,2,3,4,5}

my_dictionary = {"key1":"value1", "key2":"value2", "key3":"value3"} # --> Inisialisasi variabel yang menyimpan data dict, berisi 3 key dan value data string
print(my_dictionary)                                                # --> Mencetak variabel --> {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}

""" Memeriksa Tipe Data """

print("-------->")  # --> Abaikan ini

my_integer = 15         # --> Inisialisasi variabel yang menyimpan data integer
print(type(my_integer)) # --> Mencetak variabel, menggunakan fungsi type untuk memeriksa data suatu variabel --> <class 'int'>


""" Note! """
# 1. Objek di python mencakup variabel, class dan fungsi 