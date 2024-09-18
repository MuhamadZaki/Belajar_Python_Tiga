# Set Merupakan Tipe Data Yang Digunakan Untuk Menampung Nilai Kolektif Unik, Jadi Tidak Ada Duplikasi Elemen Dan Elemen Yang Ada Pada set Disimpan Secara Tidak Terurut

# Urutan Elemen    : Tidak urut
# Akses Elemen     : Hanya Menggunakan Perulangan
# Mutability       : Elemen Bisa Diubah
# Duplikasi Elemen : Elemen Selalu Unik
# Tipe Data Eemen  : Bisa Sejenis, Maupun Berbeda Satu Sama Lain

# 1. Pengenalan set
# Implementasi Tipe Data set Dan set Bisa Menampung Tipe Datanya Bisa Sejenis Bisa Tidak, Sama Seperti tuple Dan list
# Fungsi len() Digunakan Untuk Menghitung Panjang Atau Lebar set

a_set = {5, "Laura", True, ("satu","dua")} # --> Inisialisasi variabel yang menyimpan data set, berisi elemen berbagai tipe data
print(a_set)                               # --> Mencetak variabel, maka akan mencetak pesan {('satu', 'dua'), 'Laura', 5, True}
print(len(a_set))                          # --> Mencetak variabel atau panjang jumlah elemen dari a_set, maka akan mencetak pesan 4

# Untuk Deklarasi Atau Inisialisasi set Kosong, Gunakan Fungsi set(), Bukan {} Karena Literal Tersebut Akan menciptakan Data Bertipe lainnya Yaitu Dict

a_set = set()       # --> Inisialisasi variabel yang menyimpan data set, berisi elemen kosong
print(a_set)        # --> Mencetak variabel, maka akan mecnetak pesan set()
print(type(a_set))  # --> Mencetak variabel dan mengecek tipe datanya, maka akan mencetak pesan <class 'set'>

a_dict = {}         # --> Inisialisasi variabel yang menyipan data dict, berisi elemen kosong
print(type(a_dict)) # --> Mencetak vairabel dan mengecek tipe datanya, maka akan mencetak pesan <class 'dict'>

