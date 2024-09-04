# List Comprehension Merupakan Metode Ringkas Pembuatan list (Selain Menggunakan Literal []) Atau Menggunakan Fungsi list() Dan Tentu Cara Ini Banyak Diterapkan Untuk Operasi list Yang Menghasilkan Struktur Baru
# Membuat Kode Menjadi Sangat Ringkas, Dengan Konsekuensi Agak Sedikit membingungkan Untuk Yang Baru Nyemplung Dan Gunakan Sesuai kebutuhan


# Urutan Elemen    : Terurut Sesuai Indeks
# Akses Elemen     : Menggunakan Indeks Dan Perulangan 
# Mutability       : Elemen Bisa Diubah
# Duplikasi Elemen : Elemen Bisa Diduplikat
# Tipe Data Eemen  : Bisa Sejenis, Maupun Berbeda Satu Sama Lain

# List Normal

results = []                                # --> Inisialisasi variabel yang menyimpan data list, berisi elemen kosong
for index in range(6):                      # --> Perulangan atau loop, mengiterasi sebanyak 6 kali (variabel index akan mengambil nilia 0 hingga 5)
    results.append(index * 2)               # --> Setiap iterasi, mengalikian variabel index dengan 2 dan menambahkan ke dalam variabel results
print(results)                              # --> Mencetak variabel, maka akan mencetak pesan [0, 2, 4, 6, 8, 10]


# List Comprehension

results = [index * 2 for index in range(5)] # --> List comprehension, mengalikan variabel index dengan 2 (variabel index akan mengambil nilai 0 hingga 4) dan tersimpan dalam variabel results
print(results)                              # --> Mencetak variabel, maka akan mencetak pesan [0, 2, 4, 6, 8]

# List Normal

results = []                                        # --> Inisialisasi variabel yang menyimpan data list, berisi elemen kosong
for index in range(10):                             # --> Perulangan atau loop, mengiterasi sebanyak 10 kali (variabel index akan mengambil nilai 0 hingga 9)
    if index % 2 == 1:                              # --> Kondisi, memerikasa apakah dalam rentang nilai variabel index terdapat biangan ganjil, jika kondisi terpenuhi maka akan mengeksekusi kode di dalamnya
        results.append(index)                       # --> Jika kondisi benar atau terpenuhi, setiap iterasi terdapat bilangan ganjil, maka akan ditambahkan ke dalam variabel results
print(results)                                      # --> Mencetak vairabel, maka akan mencetak pesan [1, 3, 5, 7, 9]

# List Comprehension

results = [index for index in range(10) if index % 2 == 1] # --> List comprehension, variabel index  menghasilkan rentang 0 hingga 9 dan memeriksa apakah dalam rentang nilai variabel index terdapat bilangan ganjil, jika kondisi terpenuhi atau terdpaat bilangna ganjil maka akan tersimpan pada variabel results
print(results)                                             # --> Mencetak vairabel, maka akan mencetak pesan [1, 3, 5, 7, 9]

