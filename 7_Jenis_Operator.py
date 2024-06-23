""" Macam-Macam Operator  """

# Sederhana Operator Aritmatika
a = 10 + 5  # 5 dan 10 disebut  Operan, lalu + disebut Operator
print(a)    # 15

# Tabel Operator Aritmatika untuk melakukan operasi matematika
# 1. Penjumlahan     --> Menjumlahkan operan                    --> 5 + 5  = 10
# 2. Pengurangan     --> Mengurangi nilai operan                --> 5 - 4  = 1
# 3. Perkalian       --> Mengalikan nilai operan                --> 5 * 2  = 10
# 4. Pembagian       --> Membagi nilai operan                   --> 10 / 2 = 5
# 5. Modulus         --> Menghitung sisa hasil bagi dari operan --> 10 % 3 = 1
# 6. Perpangkatan    --> Menghitung pangkat dari operan         --> 2 ** 3 = 8
# 7. Pembagian Bulat --> Membagi operan lalu membulatkannya, dengan menghapus angka di belakang koma --> 10 // 3 = 3

a = 5 + 5
print ('Penjumlahan + :', a)    # karena 5 ditambah 5 dan hasilnya adalah 10

a = 5 - 4
print('Pengurangan - :', a)     # karena 5 dikurangi 4 dan hasilnya adalah 1

a = 5 * 2
print('Perkalian * :', a)       # Karena 5 dikali 2 dan hasilnya adalah 10

a = 10 / 2
print('Pembagian / :', a)       # karena 10 dibagi 2 dan hasilnya adalah 5.0 (hasil pembagian adalah float)

a = 10 % 3
print('Modulus atau Sisa bagi % :', a) # Karena 10 modulus 3 dan hasilnya adalah 1 (sis pembagian 10 dibagi 3)

a = 2 ** 3
print('Pangkat ** :', a)         # Karena 2 dipangkatkan 3 dan hasilnya adalah 8

a = 10 // 3 
print('Pembagian Bulat // :', a) # Karena 10 dibagi secara floor dengan 3 dan hasilnya adalah 3 (hasil pembagian dibulatkan)

# Tabel Operator Komparasi atau Perbandingan untuk membandingkan dua nilai (True dan False)
# 1. Lebih dari                     --> 5 > 5       --> False
# 2. kurang dari                    --> 2 < 4       --> True
# 3. Sama dengan                    --> 10 == 10    --> True
# 4. Tidak sama dengan              --> 5 != 5      --> False
# 5. Lebih dari atau sama dengan    --> 10 >= 10    --> True
# 6. Kurang dari atau sama dengan   --> 9 <= 10     --> True

a = 5 > 5
print('Lebih dari > :', a)                  # Karena 5 tidak lebih besar dari 5 dan hasilnya adalah False

a = 2 < 4
print('Kurang dari < :', a)                 # Karena 2 lebih kecil dari 4 dan hasilnya adalah True

a = 10 == 10
print('Sama dengan == :', a)                # Karena 10 sama dengan 10 dan hasilnya adalah True

a = 5 != 5
print('Tidak sama dengan != :', a)          # Karena 5 sama dengan 5 dan hasilnya adalah False

a = 10 >= 10
print('Lebih dari atau sama dengan >= :', a) # Karena 10 lebih besar atau samadengan 10 dan hasilnya adalah True

a = 9 <= 10
print('Kurang dari atau sama dengan ')       # Karena 9 kurang dari atau sama dengan 10 dan hasilnya adalah True

# Tabel Operator Penugasan untuk menetapkan nilai ke variabel 
# 1. =      --> a = 10     --> a = 10
# 2. +=     --> a += 5     --> a = a + 5
# 3. -=     --> a -= 5     --> a = a - 5
# 4. *=     --> a *= 5     --> a = a * 5
# 5. /=     --> a /= 5     --> a = a / 5
# 6. %=     --> a %= 5     --> a = a % 5
# 7. //=    --> a //= 5    --> a = a // 5
# 8. **=    --> a **= 5    --> a = a ** 5
# 9. &=     --> a &= 5     --> a = a & 5
# 10. |=    --> a |= 5     --> a = a | 5
# 11. ^=    --> a ^= 5     --> a = a ^ 5
# 12. >>=   --> a >>= 5    --> a = a >> 5
# 13. <<=   --> a <<= 5    --> a = a << 5

a = 10
print('a = 10 -->', a)  # Karena nilai dari variable a adalah 10 dan hasilnya adalah 10

a = 10
a += 5
print('a += 5 -->', a)  # karena 10 ditambah 5 dan hasilnya adalah 15

a = 10
a -= 5
print('a -= 5 -->', a)  # Karena 10 dikurangi 5 dan hasilnya adalah 5

a = 10
a *= 5
print('a *= 5 -->', a)  # Karena 10 dikalikan 5 dan hasilnya adalah 50

a = 10
a /=5
print('a /= 5 -->', a)  # Karena 10 dibagi 5 dan hasilnya adalah 2.0 (hasil pembagian adalah float)

a = 10
a %= 3
print('a %= 5 -->', a)  # Karena 10 modulus 3 dan hasilnya adalah 1 (sisa pembagian dari 10 dibagi 3)

a = 10
a //= 5
print('a //= 5 -->', a) # Karena 10 dibagi secara floor dengan 5 dan hasilnya adalah 2 (hasil pembagian dibulatkan)

a = 10
a **= 5
print('a **= 5 -->', a) # Karena 10 dipangkatkan 5 dan hasilnya adalah 100000

a = 10
a &= 5
print('a &=2 -->', a)   # Karena 10 bitwise AND dengan 5 (1010 & 0101 --> 0000) dan hasilnya adalah 0 

a = 10
a |= 5
print('a |= 5 -->', a)  # Karena 10 bitwise OR dengan 5 (1010 | 0101 --> 1111) dan hasilnya adalah 15

a = 10
a ^= 5
print('a ^= 5 -->', a)  # Karena 10 bitwise XOR dengan 5 (1010 ^ 0101 --> 1111) dan hasilnya adalah 15

a = 10
a >>= 5
print('a >>= 5 -->', a) # Karena 10 di-shift right 5 bit (1010 >> 5 --> 0) dan hasilnya adalah 0

a = 10
a <<= 5
print('a <<= 5 -->', a) # Karena 10 di-shift left 5 bit (1010 << 5 --> 101000000) dan hasilnya adalah 320

# Tabel Operator Logika untuk menggabungkan kondisi atau ekspresi logika dalam pemrograman

# 1. and --> Mengembalikan True jika kedua statement atau operan adalah True
#        --> Mengembalikan false jika salah satu atau kedua operan adalah False

# 2. or  --> Mengembalikan True jika salah satu atau kedua statement atau operan adalah True
#        --> Mengembalikan False hanya jika kedua operan adalah false

# 3. not --> Mengembalikan True menjadi False dan sebaliknya atau membalikan nilai operan
#        --> not True itu menjadi False
#        --> not False itu menjadi True

print(True and True)       # Karena kdua operan adalah True dan hasilnya adalah True
print(1 + 2 == 3 and True) # Karena 1 + 2 == 3 itu (True) dan and True dan hasilnya adlalah True
print(False and True)      # Karena salah satu operan itu False dan hasilnya adalah False
print(1 + 3 == 3 and True) # Karena 1 + 3 == 3 itu (False) dan and True dan hasilnya adalah False

print('-------------')

print(True or False)       # Karena salah satu operan adalah True dan hasilnya adalah True
print(5 > 1 or False)      # Karena 5 > 1 itu (True) dan or False  dan hasilnya adalah True
print(False or True)       # Karena salah satu operan adalah True dan hasilnya adalah True
print(1 > 5 or True)       # Karena 1 > 5 itu (False) dan or True dan  hasilnya adalah True
print(False or False)      # Karena kedua operan adalah False dan hasilnya adalah False
print( 1 > 5 or False)     # Karena 1 > 5 itu (False) dan or False dan hasinya adalah False

print('-------------')

print(not(True))           # Karena not True adalah false dan hasilnya adalah False
print(not(5 > 1))          # karena 5 > 1 itu (True) dan hasilnya adalah False
print(not(False))          # Karena not False adalah True dan hasilnya adalah True
print(not(1 > 5))          # karena 1 > 5 itu (False) dan not False dan hasilnya adalah True

print('-------------')

# Tabel Operator Keanggotaan untuk menguji apakah nilai atau variabel ada di dalam suatu urutan (list, tuple, string, dict)

# 1. in     --> Bernilai True jika nila tersebut ada di dalam sequence (seperti string, list, tuple dan dict)
#           --> Bernilai False jika nilai tersebut tidak ada di dalam sequence
#           --> Noted : Operator in digunakan untuk memeriksa keanggotaan suatu nilai di dalam sebuah sequence

# 2 not in  --> Bernilai True jika nilai tidak ada di dalam sequence (seperti stringm list, tuple dan dict)
#           --> Bernilai False jika nilai ada di dalam sequence
#           --> Noted : Operator ini digunakan untuk mengecek kebalikan dari keanggotaan suatu nilai di dalam sequence (yaitu apakah nilai tersebut tidak ada di dalam sequence)

kampus = 'Universitas Tamia'
lokasi = ['Jawa', 'Sumatra', 'Sulawesi']

mahasiswa = {
    'nama' : 'Muhamad Zaki',
    'asal' : 'Jakarta'
}
print("Apakah 'i' berada di variabel kampus?", 'i' in kampus) # Karena i berada di variabel kampus dan True
print("Apakah 'k' berada di variabel kampus?", 'k' in kampus) # Karena k tidak ada di variabel kampus dan False

print("Apakah 'k' berada di variabel kampus?", 'k' not in kampus ) # Karena k tidak ada di variabel kampus dan True
print("Apakah 'i' berada di variabel kampus?", 'i' not in kampus)  # Karena i berada di variable kampus dan False

print("Apakah 'Kebumen' berada di variabel lokasi?", 'Kebumen' in lokasi)   # Karena kebumen tidak ada di variabel lokasi dan False
print("Apakah 'Sulawesi' berada di variable lokasi?", 'Sulawesi' in lokasi) # Karena Sulawesi berada di variable lokasi dan True

print("Apakah 'Kebumen' berada di variable lokasi?", 'Kebumen' not in lokasi)   # Karena Kebumen tidak ada di variable lokasi dan True
print("Apakah 'Sulawesi' berada di variabel lokasi?", 'Sulawesi' not in lokasi) #  karena Sulawesi berada di variabel loakasi dan False

print("Apakah 'nama' berada di variabel mahasiswa?", 'nama' in mahasiswa)     # Karena nama berada di variabel mahasiswa dan True
print("Apakah 'tobrut' berada di variabel mahasiswa?", 'tobrut' in mahasiswa) # Karena tobrut tidak ada di variabel mahasiswa False

print("Apakah 'asal' berada di variabel mahasiswa?", 'asal' not in mahasiswa) # Karena asal berada di variable mahasiswa dan False
print("Apakah 'tobrut' berada di variable mahasiswa?", 'tobrut' not in mahasiswa) # Karena tobrut tidak ada di bvariable mahasiswa dan True

print('-------------')

# Tabel Operator Identitas untuk membandingkan objek, melihat apakah mereka sebenarnya adalah objek yang sama dan bukan hanya memiliki nilai yang sama

# 1. is     --> Bernilai True jika dua variabel menunjuk ke objek yang sama di memory
#           --> Bernilai False jika dua variable menunjuk ke objek yang berbeda di memory

# 2. is not --> Bernilai True jika dua variable menunjuk ke objek yang berbeda di memory
#           --> Bernilai False jika dua variable menunjuk ke objek yang sama di memory

a = 5
b = 5

list_a = [1,2,3]
list_b = [1,2,3]

str_a = 'Tobrut'
str_b = 'Tobrut'

tuple_a = (10,)
tuple_b = (10,)



print(a is b)           # Karena nilai a dan b identik(sama) dan True
print(a is not b)       # Karena nilai a dan b identik(sama) dan False

print(list_a is list_b)     # Karena a dan b menunjuk lokasi yang berbeda di memory dan False
print(list_a is not list_b) # Karena a dan b menunjuk lokasi yang berbeda di memory dan True

print(str_a is str_b)     # Karena nilai a dan b identik(sama) dan True
print(str_a is not str_b) # Karena nilai a dan b identik(sama) dan False

print(tuple_a is tuple_b)       # Karena nilai a dan b identik(sama) dan True
print(tuple_a is not tuple_b)   # Karena nilai a dan b identik(sama) dan False

print('-------------')

# Cara Kerja id Mendapatkan alamat memori dari suatu objek

a = 10
print(id(a)) # Alamat memori dari objek yang diacu oleh a dan hasilnya adalah 140725277346520

b = 'kuning'
print(id(b)) # Alamat memori dari objek yang diacu oleh b dan hasilnya adalah 2836436821472

a = 10
b = a
print(id(b)) # Alamat memori yang sama dengan a dan hasilnya adalah 140725277346520

# Noted : Untuk medapatkan alamat memori unik dari sebuah objek.
# Refrensi objek
# --> Memastikan apakah dua variabel merujuk pada objek yang sama atau tidak.
# --> Memahami prilaku mutable dan immutable, misalnya ketika mengubah list (mutable) dan perubahan tersebut dapat tercermin di semua variable yang merujuk pada list yang sama

# Debuging Optimalisasi
# --> Untuk memastikan bahwa refrensi objek sedang dikelola sebagaimana mestinya
# --> Membantu dalam memahami optimisasi memori, seperti interning string dan integer

print('-------------')

# Tabel Operator Bitwise digunakan untuk melakukan operasi pada level bit pada operan

# 1. AND (&) --> Menghaislkan 1 hanya jika kedua bit operan adalah 1

a = 5 # 0101 dalam biner
b = 3 # 0011 dalam biner
hasil = a & b # 0001 dalam biner atau 1 dalam desimal
print(hasil)  # Hasilnya adalah 1

izin = 0b1010           # Ijin dalam biner
membaca_topeng = 0b1000 # Topeng untuk pengecekan membaca izin
membaca = izin & membaca_topeng # Hanya bit membaca yang di cek
print(membaca != 0)             # Hasilanya adalah True

# 2. OR (|) --> Menghasilkan 1 jika salah satu atau kedua bit operan adalah 1

a = 5 # 0101 dalam biner
b = 3 # 0011 dalam biner
hasil = a | b # 0111 dalam biner, atau 7 dalam desimal
print(hasil)  # Hasilnya adalah 7

izin = 0b1000         # Ijin awal
menulis_izin = 0b0010 # Topeng untuk menulis izin
izin = izin | menulis_izin # Tambahkan menulis izin
print(bin(izin))           # Haislnya adalah 0b1010

# 3. XOR (^) --> Menghasilkan 1 jika satu bit adalah 1 dan bit lainnya adalah 0

a = 5 # 0101 dalam biner
b = 3 # 0011 dalam biner
hasil = a ^ b # 0110 dalam biner, atau 6 dalam desimal
print(hasil)  # Hasilnya adalah 6

bendera = 0b1010        # Nilai awal
beralih_topeng = 0b0011 # Topeng untuk membalikan bit tertentu
bendera = bendera ^ beralih_topeng # Balikan bit sesuai topeng
print(bin(bendera))                # Hasinya adalah 0b1001

# 4. NOT (~) --> Membalikan semua bit dari operan 1 menjadi 0 dan 0 menjadi 1

a = 5        # 0101 dalam biner
hasil = ~ a  # 1010 dalam biner (untuk representasi 8-bit, ~5 = -6)
print(hasil) # Hasilnya adalah -6

# 5. Left Shift (<<) --> Menggeser bit operan pertama ke kiri sebanyak jumlah bit yang ditentukan oleh operan kedua (menambahakan 0 di tempat yang kosong)

a = 5           # 0101 dalam biner
hasil = a << 1  # 1010 dalam biner, atau 10 dalam desimal
print(hasil)   # Hasilnya adalah 10

# 6. Right Shift(>>) --> Menggeser bit operan pertama ke kanan sebanyak jumlah bit yang ditentukan oleh operan kedua

a = 5           # 0101 dalam biner
hasil = a>> 1   # 0010 dalam biner, atau 2 dalam desimal
print(hasil)    # Hasilnya adalah 2

print('-------------')


# Jenis-Jenis Operator Pada Python
# 1. Operator Aritmatika
# 2. Operator Komperasi atau Perbandingan
# 3. Operator Penugasan
# 4. Operator Logika
# 5. Operator Keanggotaan
# 6. Operator Identitas
# 7. Operator Bitwise