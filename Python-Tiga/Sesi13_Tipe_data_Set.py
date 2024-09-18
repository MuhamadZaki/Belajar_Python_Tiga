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


print("------")

# 2. Mengakses elemen set
# Nilai set By Default Hanya Bisa Diakses Menggunakan Perulangan

duar_mew = {"satu", "dua", "tiga"} # --> Inisialisasi variabel yang menyimpan data set, berisi 3 elemen data string
for boom in duar_mew:              # --> Perulangan atau loop melalui setiap elemen dalam duar_mew dan vriabel boom akan mengambil nilai dari setiap elemen saat perulangan berlangsung
    print(boom)                    # --> Mencetak variabel setiap iterasi, maka akan mencetak pesan satu, tiga, dua (ingat hasil akan berubah-ubah setiap code dijalankan)


# Eliminasi Elemen Duplikat
# Tipe Data set memang Didesain Menyimpan Data Unik, Duplikasi elemen Tidak Mungkin Terjadi Meskipun Dipaksa
# Variabel a_set Yang Di Isi Dengan Data set Dengan banyak Elemen Duplikasi, Sewaktu Di print Elemennya Adalah Unik

a_set = {1,2,3,3,2,1,2,3,1} # --> Inisialisasi variabel yang menyimpan data set, berisi 9 elemen data integer
print(a_set)                # --> Mencetak variabel, maka akan mencetak pesan {1, 2, 3}

# Menggunkaan set untuk Mengeleminasi elemen Duplikat Pada Suatu list
