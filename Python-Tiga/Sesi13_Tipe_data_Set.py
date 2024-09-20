# Set Merupakan Tipe Data Yang Digunakan Untuk Menampung Nilai Kolektif Unik, Jadi Tidak Ada Duplikasi Elemen Dan Elemen Yang Ada Pada set Disimpan Secara Tidak Terurut

# Urutan Elemen    : Tidak urut
# Akses Elemen     : Hanya Menggunakan Perulangan
# Mutability       : Elemen Bisa Diubah
# Duplikasi Elemen : Elemen Selalu Unik
# Tipe Data Eemen  : Bisa Sejenis, Maupun Berbeda Satu Sama Lain

# 1. Pengenalan set
# Implementasi Tipe Data set Dan set Bisa Menampung Tipe Datanya Bisa Sejenis Bisa Tidak, Sama Seperti tuple Dan list
# Fungsi len() Digunakan Untuk Menghitung Panjang Atau Lebar elemen set

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
    print(boom)                    # --> Mencetak variabel setiap iterasi, maka akan mencetak pesan satu, tiga, dua (ingat posisi elemen akan berubah-ubah setiap code dijalankan)


# Eliminasi Elemen Duplikat
# Tipe Data set memang Didesain Menyimpan Data Unik, Duplikasi elemen Tidak Mungkin Terjadi Meskipun Dipaksa
# Variabel a_set Yang Di Isi Dengan Data set Dengan banyak Elemen Duplikasi, Sewaktu Di print Elemennya Adalah Unik

a_set = {1,2,3,3,2,1,2,3,1} # --> Inisialisasi variabel yang menyimpan data set, berisi 9 elemen data integer
print(a_set)                # --> Mencetak variabel, maka akan mencetak pesan {1, 2, 3}

# Menggunkaan set untuk Mengeleminasi elemen Duplikat Pada Suatu list

data = [1,2,3,2,1,4,3,4,5]  # --> Inisialisasi variabel yang menyimpan data list, berisi 9 elemen data integer
print(data)                 # --> Mencetak variabel, maka akan mencetak pesan [1, 2, 3, 2, 1, 4, 3, 4, 5]

data_unik_set = set(data)   # --> Mengonversi data list menjadi set, untuk menghilangkan duplikasi dan menghasilkan nilai set berisi elemen unik
print(data_unik_set)        # --> Mencetak variabel, maka akan mecetak pesan {1, 2, 3, 4, 5}

data_unik_list = list(data_unik_set) # --> Mengonversi set kembali menjadi list
print(data_unik_list)                # --> Mencetak variabel, maka akan mencetak pesan [1, 2, 3, 4, 5]

# Mengecek Apakah elemen Ada
# Selain Untuk Kasus Sebelumnnya, set Jua Bisa Digunakan Untuk Pengecekan membership Dengan Kombinasi Keyword if Dan in

data = {"satu", "dua", "tiga"} # --> Inisialisasi variabel yang menyimpan data set, berisi 3 elemen data string
temukan = "dua"                # --> Inisialisasi variabel yang menyimpan data string

if temukan in data:            # --> Kondisi, memeriksa apakah nilai yang ada dalam variabel temukan terdapat dalam variabel data, jika kondisi terpenuhi maka akan mengeksekusi kode di dalamnya dan jika kondisi tidak terpenuhi maka akan melajutkan ke kondisi berikutnya
    print(temukan)             # --> Jika kondisi benar atau terpenuhi, maka akan mencetak pesan dua
else:                          # --> Kondisi, jika kondisi sebelumnya tidak terpenuhi maka blok kode ini dieksekusi
    print(False)               # --> Jika kondisi salah atau tidak terpenuhi, maka mencetak pesan False


print("------")

# 3. Operasi Pada set
# Method add() Milik Tipe Data set Digunakan Untuk Menambahkan Element Baru Dan Perlu Diingat Tipe Data Ini Didesain Untuk Mengabaikan Urutan elemen, Jadi Urutan Tersimpannya Elemen Bisa Saja Acak

datas = set()      # --> Inisialisasi variabel yang menyimpan data set, berisi elemen kosong
datas.add("Satu")  # --> Menambahkan elemen data string ke dalam variabel datas
datas.add("Dua")   # --> Menambahkan elemen data string ke dalam variabel datas
print(datas)       # --> Mencetak variabel, maka akan mencetak pesan {'Satu', 'Dua'}

# Menghapus Elemen Secara Acak
# Kita Menggunakan Method pop() Untuk Menghapus Satu Elemen Secara Acak Atau Random

datas = {"satu", "dua", "tiga"} # --> Inisialisasi variabel yang menyimpan data set, berisi 3 elemen data string
datas.pop()                     # --> Menghapus satu elemen secara acak dari vairbel datas
datas.pop()                     # --> Menghapus satu elemen secara acak dari variabel datas
print(datas)                    # --> Mencatak variabel, maka akan mencetak pesan {'satu'} (ingat hasil akan berubah-ubah setiap code dijalankan)

# Menghapus Spesifik elemen
# Ada Dua Method Tersedia Untuk Kebutuhan Menghapus Elemen Tertentu dari Suatu set, Yaitu discard() Dan remove() Dan Penggunaan Keduanya Adalah Sama, Harus Disertai Dengan 1 Argumen Pemanggilan Method Yaitu Elemen Yang Ingin Dihapus
# Pada Method discard(), Jika Elemen Yang Dihapus Tidak Ada maka tidak error Dan Pada Method remove() Maka Akan Error

datas = {"satu", "dua", "tiga"} # --> Inisialisasi variabel yang menyimpan data set, berisi 3 elemen data string
datas.discard("dua")            # --> Menghapus elemen "dua" pada vairbel datas
print(datas)                    # --> Mencetak variabel, maka akan mencetak pesan {'tiga', 'satu'} (ingat posisi elemen akan berubah-ubah setiap code dijalankan)

datas = {"satu", "dua", "tiga"} # --> Inisialisasi variabel yang menyimpan data set, berisi 3 elemen data string
datas.remove("tiga")            # --> Menghapus elemen "tiga" pada variabel datas
print(datas)                    # --> Mencetak variabel, maka akan mencetak pesan {'satu', 'dua'} (ingat posisi akan berubah-ubah setiap code dijalankan)


# Mengosongkan isi Set
# Menggunakan Methode clear() Yang Digunakan Untuk Mengosongkan Isi Dari data set

datas = {"satu", "dua", "tiga"} # --> Inisialisasi variabel yang menyimpan data set, berisi 3 elemen data string
datas.clear()                   # --> Mengosongkan elemen dari variabel datas
print(datas)                    # --> Mencetak variabel, maka akan mencetak pesan set()

# Copy set
# Method copy() Digunakan Untuk Mengkopi set Dan Menghasilkan Data set Baru
# Opersi Kopi Ini Jenisnya Shallow Kopi

datas = {"satu", "dua", "tiga"} # --> Inisialisasi variabel yang menyimpan data set, berisi 3 elemen data string
results = datas.copy()          # --> Mengkopi nilai dari variabel datas dan tersimpan pada variabel results
print(results)                  # --> Mencetak variabel, maka akan mencetak pesan {'tiga', 'dua', 'satu'} (ingat posisi akan berubah-ubah setiap code dijalankan)

# Pengecekan difference Antar set
# Method difference() Digunakan Untuk Mencari Perbedaan Elemen Antara Data yang Dimana method Dipanggsil vs Data Pada Argumen Pemanggil Method Tersebut
# Selain method difference(), Adalagi yaitu Menthod diffrence_update() Yang Kegunaannya Adalah Mengubah Nilai Data (Dimana Method Dipanggil) Dengan Nilai Baru Yang Didapat Dari Perbedaan Elemen Antara Data Tersebut vs Data pada Argumen Pemanggil Method

datas = {"satu", "dua", "tiga"}   # --> Inisialisasi variabel yang menyimpan data set, berisi 3 elemen data string
hello = {"satu", "dua", "empat"}  # --> Inisialisasi variabel yang menyimpan data set, berisi 3 elemen data string

results = datas.difference(hello) # --> Menghitung perbedaan antara elemen dari variabel datas dan hello, lalu mengembalikan data set berisi elemen yang hanya ada di variabel datas dan tidak ada di variabel hello dan terimpan pada variabel results
print(results)                    # --> Mencetak variabel, maka akan mencetak pesan {'tiga'}

datas = {"satu", "dua", "tiga", "lima", "enam"}   # --> Inisialisasi variabel yang menyimpan data set, berisi 5 elemen data setring
hello = {"satu", "dua", "empat"}  # --> Inisialisasi variabel yang menyimpan data set, berisi 3 elemen data string

datas.difference_update(hello)    # --> Mengubah variabel datas dengan menghapus elemen-elemen yang juga terdapat dalam variabel hello
print(datas)                      # --> Mencetak variabel, maka akan mencetak pesan {'lima', 'tiga', 'enam'} (ingat posisi akan berubah-ubah setiap code dijalankan)

# Pengecekan intersection Antar set
# Method intersection() Digunakan Untuk Mencari Elemen yang Ada Di Data (Dimana Method Dipanggil) Vs Data Pada Argumen Pemanggil Method Tersebut
# Ada Juga Method intersection_update() Yang Berguna Untuk Mengubah Nilai Data (Dimana Method Dipanggil) Dengan Nilai baru yang Didapat Dari Kesamaan Elemen Antara Data Tersebut Vs Data Pada Arguman Pemanggil Method

datas = {"satu", "dua", "tiga"}     # --> Inisialisasi variabel yang menyimpan data set, berisi 3 elemen data string
hello = {"satu", "dua", "empat"}    # --> Inisialisasi variabel yang menyimpan data set, berisi 3 elemen data string

results = datas.intersection(hello) # --> Menghitung antara variabel  datas dan hello, lalu mengembalikan elemen-elemen yang ada di kedua variabel dan tersimpan pada variabel results
print(results)                      # --> Mencetak variabel, maka akan mencetak pesan {'dua', 'satu'}


datas = {"satu", "dua", "tiga"}     # --> Inisialisasi variabel yang menyimpan data set, berisi 3 elemen data string
hello = {"satu", "dua", "empat"}    # --> Inisialisasi variabel yang menyimpan data set, berisi 3 elemen data string

datas.intersection_update(hello)    # --> Menghitung antara variabel  datas dan hello, lalu mengubah set secara langsung atau in-place dan hanya mempertahankan elemen-elemen yang ada di kedua variabel 
print(datas)                        # --> Mencetak variabel, maka akan mencetak pesan {'satu', 'dua'}

# Pengecekan Keanggotaan atau mempership subset
# Sebelumnya Kita Sudah Menggunakan Pengecekan Membership Menggunakan Keyword if Dan in, Lalu Selain Metode Tersebut Ada Alternatif Lain Yang Bisa Digunakan Untuk Mengecek Apakah Suatu Data (Yang Pada Konteks Ini Adalah set) Merupakan Bagian Dari Elemen set Lain Dan Caranya Yaitu Menggunakan Method issubset()
# Method issubset() Menerima Argumen Berupa Data set
# Selain Method issubset() Ada Juga issuperset() Yang Berfungsi Kurang Lebih Sama Namun Kondisi Pengecekannya Dibalik

datas = {"satu", "dua", "tiga"}     # --> Inisialisasi variabel yang menyimpan data set, berisi 3 elemen data string
hello = {"satu", "dua", "empat"}    # --> Inisialisasi variabel yang menyimpan data set, berisi 3 elemen data string

results = hello.issubset(datas)     # --> Memeriksa apakah variabel hello adalah subset dari variabel datas atau jika semua elemen dalam variabel hello juga ada dalam variabel datas maka hello dianggap subset dari variabel datas dan tersimpan dalam variabel results
print(results)                      # --> Mencetak variabel, maka akan mencetak pesan False

datas = {"satu", "dua", "tiga"}     # --> Inisialisasi variabel yang menyimpan data set, berisi 3 elemen data string
hello = {"satu", "dua", "tiga"}     # --> Inisialisasi variabel yang menyimpan data set, berisi 3 elemen data string

results = hello.issubset(datas)     # --> Memeriksa apakah variabel hello adalah subset dari variabel data atau jika semua elemen dalam variabel hello juga ada dalam variabel datas maka hello dianggap subset dari variabel datas dan tersimpan dalam variabel results
print(results)                      # --> Mencetak variabel, maka akan mencetak pesan True


datas = {"satu", "dua", "tiga",}     # --> Inisialisasi variabel yang menyimpan data set, berisi 3 elemen data string
hello = {"satu", "dua", "empat"}    # --> Inisialisasi variabel yang menyimpan data set, berisi 3 elemen data string

results = datas.issuperset(hello)   # --> Memeriksa apakah variabel datas adalah superset dari variabel hello atau jika semua elemen dalam variabel hello ada dalam variabel datas maka datas dianggap superset dari variabel hello  dan tersimpan pada variabel results
print(results)                      # --> Mencetak variabel, maka akan mencetak pesan False

datas = {"satu", "dua", "tiga"}     # --> Inisialisasi variabel yang menyimpan data set, berisi 3 elemen data string
hello = {"satu", "dua", "tiga"}     # --> Inisialisasi variabel yang menyimpan data set, berisi 3 elemen data string

results = datas.issuperset(hello)   # --> Memeriksa apakah variabel datas adalah superset dari variabel hello atau jika semua elemen dalam variabel hello ada dalam variabel datas maka datas dianggap superset dari variabel hello  dan tersimpan pada variabel results
print(results)                      # --> Mencetak variabel, maka akan mencetak pesan True


# Pengecekan Keanggotaan Atau Membership disjoint
# Method isdisjoint() Mengembalikan Nilai True Jika set Pada Pemanggilan Fungsi Berisi Elemen Yang Semuanya Bukan Anggota Data Method Dipanggil