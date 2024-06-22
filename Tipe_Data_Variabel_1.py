# Name Variable dan Value

nama = 'Muhamad Zaki' # --> String atau teks
usia = 23             # --> Integer atau bilangan bulat
akhir = 5.5           # --> float atau nilai pecahan (desimal)
sudah_menikah = False # --> Boolean atau True dan False

print('Nama :', nama)                       # Muhamad Zaki
print('Usia :', usia)                       # 23
print('Akhir :', akhir)                     # 5.5
print('Sudah Menikah :', sudah_menikah)     # False

# Aturan Assignment

# 1. Multiple

a, b, c = 10, 11, 'MZ'
print('Multiple')
print('A :', a) # 10
print('B :', b) # 11
print('C :', c) # MZ

# 2. Single
a = b = c = 10
print('Single')
print('A :', a) # 10
print('B :', b) # 10
print('C :', c) # 10

# Memeriksa Tipe Data
a = 'Manusia'
b = 50
c = 5.5
d = True
print(type(a)) # String
print(type(b)) # Integer
print(type(c)) # Foloat
print(type(d)) # True

# Mencoba Tipe Data Numrik

# 1
panjang = 5
lebar = 5.5
luas = panjang * lebar

print(panjang, '*', lebar, '=', luas)
print(type(panjang)) # 5
print(type(lebar))   # 5.5
print(type(luas))    # 27.5

# 2
a = 5j
b = 10j
c = a + b

print(a, '+', b, '=', c)
print(type(a)) # 5j
print(type(b)) # 10j
print(type(c)) # 15j

# Tipe Data String atau Teks

nama_depan = 'Muhamad'
nama_belakang = 'Zaki'
nama_lengkap = nama_depan + ' ' + nama_belakang
usia = '12'
alamat = 'Jakarta'

print('Nama Lengkap :', nama_lengkap) # Muhamad Zaki
print('Usia :', usia)                 # 12
print('Alamat :', alamat)             # Jakarta

print(type(nama_lengkap)) # String
print(type(usia))         # String
print(type(alamat))       # String

# Perbedaan Tipe Data String dan Numrik

# 1. Penjumlahan Dua data String
print('5'+ '5')     # 55


# 2. Penjumlahan Dua data Numrik
print(5 + 5)        # 10


# 3. Perkalian String dan Numrik
print('Meki ' * 5)  # Meki Meki Meki Meki Meki

# Tipe Data Boolean (True or False)
manusia = True
robot = False
print('Apa kamu manusia?', manusia) # True
print('Apa kamu ronot?', robot)     # False

# Tipe Data Canggih atau Koleksi

# 1. List
# 2. Tuple
# 3. Set
# 4. Dictionary