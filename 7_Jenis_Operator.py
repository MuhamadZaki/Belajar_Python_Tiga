
# 1.1 Macam-Macam Operator 

# Sederhana Operator Aritmatika
a = 10 + 5  # 5 dan 10 disebut  Operan, lalu + disebut Operator
print(a)    # 15

# Tabel Operator Aritmatika
# 1. Penjumlahan     --> Menjumlahkan operan                    --> 5 + 5  = 10
# 2. Pengurangan     --> Mengurangi nilai operan                --> 5 - 4  = 1
# 3. Perkalian       --> Mengalikan nilai operan                --> 5 * 2  = 10
# 4. Pembagian       --> Membagi nilai operan                   --> 10 / 2 = 5
# 5. Modulus         --> Menghitung sisa hasil bagi dari operan --> 10 % 3 = 1
# 6. Perpangkatan    --> Menghitung pangkat dari operan         --> 2 ** 3 = 8
# 7. Pembagian Bulat --> Membagi operan lalu membulatkannya, dengan menghapus angka di belakang koma --> 10 // 3 = 3

a = 5 + 5
print ('Penjumlahan + :', a)    # 10

a = 5 - 4
print('Pengurangan - :', a)     # 1

a = 5 * 2
print('Perkalian * :', a)       # 10

a = 10 / 2
print('Pembagian / :', a)       # 5.0

a = 10 % 3
print('Modulus atau Sisa bagi % :', a) # 1

a = 2 ** 3
print('Pangkat ** :', a)         # 8

a = 10 // 3 
print('Pembagian Bulat // :', a) # 3

# Tabel Operator Komparasi atau Perbandingan 
# 1. Lebih dari                     --> 5 > 5       --> False
# 2. kurang dari                    --> 2 < 4       --> True
# 3. Sama dengan                    --> 10 == 10    --> True
# 4. Tidak sama dengan              --> 5 != 5      --> False
# 5. Lebih dari atau sama dengan    --> 10 >= 10    --> True
# 6. Kurang dari atau sama dengan   --> 9 <= 10     --> True

a = 5 > 5
print('Lebih dari > :', a)                  # False

a = 2 < 4
print('Kurang dari < :', a)                 # True

a = 10 == 10
print('Sama dengan == :', a)                # True

a = 5 != 5
print('Tidak sama dengan != :', a)          # False

a = 10 >= 10
print('Lebih dari atau sama dengan >= :', a) # True

a = 9 <= 10
print('Kurang dari atau sama dengan ')       # True

# Tabel Operator Penugasan
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
print('a = 10 -->', a)  # 10

a = 10
a += 5
print('a += 5 -->', a)  # 15

a = 10
a -= 5
print('a -= 5 -->', a)  # 5

a = 10
a *= 5
print('a *= 5 -->', a)  # 50

a = 10
a /=5
print('a /= 5 -->', a)  # 2.0

a = 10
a %= 3
print('a %= 5 -->', a)  # 1

a = 10
a //= 5
print('a //= 5 -->', a) # 2

a = 10
a **= 5
print('a **= 5 -->', a) # 100000

a = 10
a &= 5
print('a &=2 -->', a)   # 0

a = 10
a |= 5
print('a |= 5 -->', a)  # 15

a = 10
a ^= 5
print('a ^= 5 -->', a)  # 15

a = 10
a >>= 5
print('a >>= 5 -->', a) # 0

a = 10
a <<= 5
print('a <<= 5 -->', a) # 320

# Tabel Operator Logika

# 1. and --> Mengembalikan True jika dua statement sama-sama benar       --> True and True
# 2. or  --> Mengembalikan True jika salah satu statement bernilai benar --> 2 > 5 or 1 < 3
# 3. not --> Mengembalikan True menjadi False dan sebaliknya             --> not(1 > 5)

print(True and True)       # True
print(1 + 2 == 3 and True) # True
print(False and True)      # False
print(1 + 3 == 3 and True) # False

print('-------------')

print(True or False)       # True
print(5 > 1 or False)      # True
print(False or True)       # True
print(1 > 5 or True)       # True
print(False or False)      # False
print( 1 > 5 or False)     # False

print('-------------')

print(not(True))           # False
print(not(5 > 1))          # False
print(not(False))          # True
print(not(1 > 5))          # True

print('-------------')

# Tabel Operator Keanggotaan
# 1. in     --> Bernilai True jika suatu nilai ada di dalam sequence
# 2 not in  --> Bernilai False jika suatu nilai tidak ada di dalam sequence

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

# Tabel Operator Identitas
# 1. is     --> Bernilai True jika dua variabel bersifat identik baik dari segi nilai maupun penempatan lokasi di memory
# 2. is not --> Bernilai False jika dua variable tidak identik baik dari segi nilai mauoun penempatan lokasi di memory





# Jenis-Jenis Operator Pada Python
# 1. Operator Aritmatika
# 2. Operator Komperasi atau Perbandingan
# 3. Operator Penugasan
# 4. Operator Logika
# 5. Operator Keanggotaan
# 6. Operator Identitas
# 7. Operator Bitwise