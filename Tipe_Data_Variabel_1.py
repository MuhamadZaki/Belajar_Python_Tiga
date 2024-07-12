"""  Name Variable dan Value """
# Note :
# Variabel Merupakan wadah untuk menympan nilai atau data yang dapat diubah selama eksekusi program

# Praktekan dan Pahami!

nama = 'Muhamad Zaki' # --> String atau teks                    --> (Inisialisasi variabel yang menyimpan data string )
usia = 23             # --> Integer atau bilangan bulat         --> (Inisialisasi variabel yang menyimpan data integer)
akhir = 5.5           # --> float atau nilai pecahan (desimal)  --> (Inisialisasi variabel yang meynimpan data float)
sudah_menikah = False # --> Boolean atau True dan False         --> (Inisialisasi variabel yang menyimpan data boolean)

print('Nama :', nama)                       # --> Muhamad Zaki  --> (Mencetak nilai variabel) (String di dalam cuma untuk pemanis)
print('Usia :', usia)                       # --> 23            --> (Mencetak nilai variabel) (String di dalam cuma untuk pemanis)
print('Akhir :', akhir)                     # --> 5.5           --> (Mencetak nilai variabel) (String di dalam cuma untuk pemanis)
print('Sudah Menikah :', sudah_menikah)     # --> False         --> (Mencetak nilai variabel) (String di dalam cuma untuk pemanis)

print('-------------')

""" Aturan Assignment """

# 1. Multiple Assignment --> Memungkinkan kita untuk menetapkan beberapa variabel dan memberikan data atau nilai sekaligus dalam satu pernyataan

a, b, c = 10, 11, 'MZ'   # --> Inisialisasi beberapa variabel yang menyimpan data integer, integer dan string
print('Multiple')
print('A :', a)          # --> 10 --> (Mencetak nilai variabel) (String di dalam cuma untuk pemanis)
print('B :', b)          # --> 11 --> (Mencetak nilai variabel) (String di dalam cuma untuk pemanis)
print('C :', c)          # --> MZ --> (Mencetak nilai variabel) (String di dalam cuma untuk pemanis)

# 2. Single Assignment --> Memungkinkan untuk menetapkan nilai yang sama ke beberapa variabel dalam satu pernyataan
a = b = c = 10  # --> Inisialisasi beberapa variabel yang menyimpan data integer atau nilai yang sama
print('Single') 
print('A :', a) # --> 10 --> (Mencetak nilai variabel) (String di dalam cuma untuk pemanis)
print('B :', b) # --> 10 --> (Mencetak nilai variabel) (String di dalam cuma untuk pemanis)
print('C :', c) # --> 10 --> (Mencetak nilai variabel) (String di dalam cuma untuk pemanis)

print('-------------')

""" Memeriksa Tipe Data """

a = 'Manusia'  # --> Inisialisasi variabel yang meyimpan data string
b = 50         # --> Inisialisasi variabel yang menyimpan data integer
c = 5.5        # --> Inisialisasi variabel yang meyimpan data float
d = True       # --> Inisialisasi variabel yang menyimpan data boolean
print(type(a)) # --> String  --> Memeriksa tipe data menggunakan fungsi type()
print(type(b)) # --> Integer --> Memeriksa tipe data menggunakan fungsi type()
print(type(c)) # --> Foloat  --> Memeriksa tipe data menggunakan fungsi type()
print(type(d)) # --> Boolean --> Memeriksa tipe data menggunakan fungsi type()

print('-------------')

""" Mencoba Tipe Data Numrik """

# 1
panjang = 5                            # --> Inisialisasi variabel yang menyimpan data integer
lebar = 5.5                            # --> Inisialisasi variabel yang menyimpan data float
luas = panjang * lebar                 # --> Menghitung dengan mengalikan nilai dari variabel panjang dan lebar yang akan disimpan pada variabel luas

print(panjang, '*', lebar, '=', luas)  # --> 5 * 5.5 = 27.5  --> (Mencetak nilai variabel) (String di dalam cuma untuk pemanis)
print(type(panjang))                   # --> 5               --> (Mencetak nilai variabel)
print(type(lebar))                     # --> 5.5             --> (Mencetak nilai variabel)     
print(type(luas))                      # --> 27.5            --> (Mencetak nilai variabel)   
 
# 2
a = 5j                   # --> Inisialisasi variabel yang menyimpan data complex
b = 10j                  # --> Inisialisasi variabel yang menyimpan data complex
c = a + b                # --> Menghitung dengan menjumlahkan nilai variabel a dan b yang akan disimpan pada variabel c

print(a, '+', b, '=', c) # --> 5j + 10j = 15j --> (Mencetak nilai variabel) (String di dalam cuma untuk pemanis)
print(type(a))           # --> 5j             --> Memeriksa tipe data menggunakan fungsi type()
print(type(b))           # --> 10j            --> Memeriksa tipe data menggunakan fungsi type()
print(type(c))           # --> 15j            --> Memeriksa tipe data menggunakan fungsi type()

print('-------------')

""" Tipe Data String atau Teks """

nama_depan = 'Muhamad'                           # --> Inisialisasi variabel yang menyimpan data string
nama_belakang = 'Zaki'                           # --> Inisialisasi variabel yang menyimpan data string
nama_lengkap = nama_depan + ' ' + nama_belakang  # --> Menyatukan nilai variabel nama_depan dan nama_belakang menggunakan operator penjumlahan (menambahkan spasi dengan '')
usia = '12'                                      # --> Inisialisasi variabel yang menyimpan data string
alamat = 'Jakarta'                               # --> Inisialisasi variabel yang menyimpan data string

print('Nama Lengkap :', nama_lengkap)            # --> Muhamad Zaki --> (Mencetak nilai variabel) (String di dalam cuma untuk pemanis)
print('Usia :', usia)                            # --> 12           --> (Mencetak nilai variabel) (String di dalam cuma untuk pemanis)
print('Alamat :', alamat)                        # --> Jakarta      --> (Mencetak nilai variabel) (String di dalam cuma untuk pemanis)

print(type(nama_lengkap))                        # --> String       --> Memeriksa tipe data menggunakan fungsi type()
print(type(usia))                                # --> String       --> Memeriksa tipe data menggunakan fungsi type()
print(type(alamat))                              # --> String       --> Memeriksa tipe data menggunakan fungsi type()

print('-------------')

""" Perbedaan Tipe Data String dan Numrik """

# 1. Penjumlahan Dua data String
print('5'+ '5')     # --> 55  --> Menggabungkan dua data string dengan operator penjumlahan


# 2. Penjumlahan Dua data Numrik
print(5 + 5)        # --> 10  --> Menjumlahkan dua data integer dengan operator penjumlahan


# 3. Perkalian String dan Numrik
print('Meki ' * 5)  # --> Meki Meki Meki Meki Meki --> Menggandakan data setring dengan operator perkalian, yang dikalikan string dengan data integer

print('-------------')

"""  Tipe Data Boolean (True or False) """

manusia = True                      # --> Inisialisasi variabel dengan data boolean
robot = False                       # --> Inisialisasi variabel dengan data boolean
print('Apa kamu manusia?', manusia) # --> True  (String di dalam cuma untuk pemanis)
print('Apa kamu ronot?', robot)     # --> False (String di dalam cuma untuk pemanis)

# Tipe Data Canggih atau Koleksi

# 1. List
# 2. Tuple
# 3. Set
# 4. Dictionary