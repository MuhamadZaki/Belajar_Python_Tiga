# Tuple Merupakan Tipe Data Sequence Yang Ideal Digunakan Untuk Menampung Nilai Kolektif yang isinya Tidak Akan Berubah (Immutable), Berbeda Dengan list yang cocok Untuk Data Yang Bisa Berubah Nilai atau Elemennya (Mutable)

# Urutan Elemen    : Terurut Sesuai Indeks
# Akses Elemen     : Menggunakan Indeks Dan Perulangan 
# Mutability       : Elemen Tidak Bisa Diubah
# Duplikasi Elemen : Elemen Bisa Diduplikat
# Tipe Data Eemen  : Bisa Sejenis, Maupun Berbeda Satu Sama Lain

# 1 . Pengenalan tuple
# Deklarasi Atau Inisialisasi tuple Menggunakan Literal () Dengan Delimiter Tanda Koma ,
# Tuple bisa menampung element yang tipe datanya bisa sejenis atau tidak, sama seperti list

a_tuple = (1,2,3, "Zaki", True) # --> Inisialisasi variabel yang menyimpan data tuple, berisi 5 elemen data integer, string dan boolean
print(a_tuple)                  # --> Mencetak variabel, maka akan mencetak pesan (1, 2, 3, 'Zaki', True)
print(len(a_tuple))             # --> Mencetak variabel dan menghirung panjang atau jumlah elemen dari a_tuple, maka akan mencetak pesan 5
print(type(a_tuple))            # --> Mencetak variabel dan mengecek tipe data, maka akan mencetak pesan <class 'tuple'>



print("------")

# 2. Mengakses Element tuple Menggunakan index
# Element tuple Bisa Diakses Menggunakan Notasi tuple[index]
# Pengaksesan Elemen Menggunakan index Di Luar Kapasitas Data Akan Menyebabkan Error

a_tuple = (1,2,3,4,5)           # --> Inisialisasi variabel yang menyimpan data tuple, berisi 5 elemen data integer
results = a_tuple[4]            # --> Mengakses elemen menggunakan index dan tersimpan pada variabel results
print(results)                  # --> Mencetak variabel, maka akan mencetak pesan 5


print("------")

# 3. Perulangan tuple
# Tuple Merupakan Salah Satu Tipe Data Yang Bisa Digunakan Secara langsung Pada Perulangan Menggunakan Keyword for

a_tuple = (1,2,3,4,5)   # --> Inisialisasi variabel yang menyimpan data tuple, berisi 5 elemen data integer
for e in a_tuple:       # --> Perulangan atau loop, mengiterasi melalui setiap element e dalam variabel a_list 
    print(e)            # --> Mencetak variabel setiap iterasi, maka akan mencetak pesan 1,2,3,4,5


# Perulangan Di Ekuvalen

a_tuple = (1,2,3,4,5)            # --> Inisialisasi variabel yang menyimpan data tuple, berisi 5 elemen data integer
for i in range(0, len(a_tuple)): # --> Perulangan atau loop, mengiterasi nilai i mulai rentang 0 hingga panjang a_tuple 
    print(i, a_tuple[i])         # --> Mencetak variabel dan mencetak index juga elemen dari a_tuple, maka akan mencetak pesan  01 12 23 34 45


# Fungsi enumerate()
# Fungsi Ini Digunakan Untuk Membuat Data Sequence Menjadi Data enumrasi, Yang Jika Dimasukan Ke Perulangan Di Setiap Iterasinya Bisa Kisa Akses Index Berserta Elemennya

a_tuple = (1,2,3,4,5)            # --> Inisialisasi variabel yang menyimpan data tuple, berisi 5 elemen data integer

for i, n in enumerate(a_tuple):  # --> Perulangan atau loop, mengiterasi setiap index dan elemen dari a_tuple
    print(i, n)                  # --> Mencetak variabel dan mencetak index juga elemen dari a_tuple, maka akan mencetak pesan 01 12 23 34 45


print("------")

#  4. Mencek Apakah Elemen Ada Pada tuple
# Kombinasi keyword if Dan in Bisa Digunakan Untuk Mengidentifikasi Apakah Suatu Element Merupakan bagian Dari tuple Atau Tidak

a_tuple = (1,2,3,4,5)  # --> Inisialisasi variabel yang menyimpan data tuple, berisi 5 elemen data integer
e = 1                  # --> Inisialisasi variabel yang menyimpan data integer

if e in a_tuple:       # --> Kondisi, memerikasa apakah nilai e, terdapat pada variabel a_tuple, jika kondisi terpenuhi maka akan mengeksekusi kode di dalamnya dan jika kondisi tidak terpenuhi maka akan melanjutkan ke kondisi berikutnya
    print(True)        # --> Jika kondisi benar atau terpenuhi, maka akan mencetak pesan True
else:                  # --> Kondisi, jika kondisi sebelumnya tidak terpenuhi maka blok kode ini dieksekusi
    print(False)       # --> Jika kondisi salah atau tidak terpenuhi, maka akan mencetak pesan False


print("------")

# Nested tuple
# Dibuat Dengan Menuliskan Data tuple Sebagai ELemen tuple
