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