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

results = []                                               # --> Inisialisasi variabel yang menyimpan data list, berisi elemen kosong
for index in range(10):                                    # --> Perulangan atau loop, mengiterasi sebanyak 10 kali (variabel index akan mengambil nilai 0 hingga 9)
    if index % 2 == 1:                                     # --> Kondisi, memerikasa apakah dalam rentang nilai variabel index terdapat biangan ganjil, jika kondisi terpenuhi maka akan mengeksekusi kode di dalamnya
        results.append(index)                              # --> Jika kondisi benar atau terpenuhi, setiap iterasi terdapat bilangan ganjil, maka akan ditambahkan ke dalam variabel results
print(results)                                             # --> Mencetak vairabel, maka akan mencetak pesan [1, 3, 5, 7, 9]

# List Comprehension

results = [index for index in range(10) if index % 2 == 1] # --> List comprehension, variabel index  menghasilkan rentang 0 hingga 9 dan memeriksa apakah dalam rentang nilai variabel index terdapat bilangan ganjil, jika kondisi terpenuhi atau terdpaat bilangna ganjil maka akan tersimpan pada variabel results
print(results)                                             # --> Mencetak vairabel, maka akan mencetak pesan [1, 3, 5, 7, 9]



# List Normal

results =  []                    # --> Inisialisasi variabel yang menyimpan data list, berisi elemen kosong
for index in range(1,10):        # --> Perulangan atau loop, mnegiterasi sebanyak 10 kali, dimulai dari rentang 1 hingga 9
    if index % 2 == 0:           # --> Kondisi, memeriksa apakah dalam rentang nilai variabel index terdapat bilangan genap, Jika kondisi terpenuhi maka akan mengeksekusi kode di dalamya dan jika kondisi tidak terpenuhi juga akan mengeksekusi blok kode berikutnya
        results.append(index*2)  # --> Jika kondisi benar atau terpenuhi, lalu jika terdapat bilangan genap maka akan mengalikannya dengan 2
    else:                        # --> Kondisi, jika kondisi sebelumnya tidak terpenuhi maka blok kode ini dieksekusi
        results.append(index*3)  # --> Jika kondisi salah atau tidak terpenuhi, lalu akan mengalikanya dengan 3
print(results)                   # --> Mencetak variabel, maka akan mencetak pesan [3, 4, 9, 8, 15, 12, 21, 16, 27]

# List Normal Dengan Ternary

results = []                                                 # --> Inisialisasi variabel yang menyimpan data list, nerisi elemen kosong                            
for index in range(1, 10):                                   # --> Perulangan atau loop, mengiterasi sebanyak 10 kali, dimulai dari rentang 1 hingga 9
    results.append(index * (2 if index % 2 == 0 else 3))     # --> Kondisi, memeriksa apakah dalam rentang nilai variabel index terdapat bilangan genap, lalu jika terdapat bilangan genap maka mengalikannya dengan 2, jika tidak menggantingan dengan 3 dan ditambahkan ke variabel results
print(results)                                               # --> Mencetak variabel, maka akan mencetak pesan [3, 4, 9, 8, 15, 12, 21, 16, 27]

# Angka 3 berasal dari 1 × 3
# Angka 4 berasal dari 2 × 2
# Angka 9 berasal dari 3 × 3
# Angka 8 berasal dari 4 × 2
# Angka 15 berasal dari 5 × 3
# Angka 12 berasal dari 6 × 2
# Angka 21 berasal dari 7 × 3
# Angka 16 berasal dari 8 × 2
# Angka 27 berasal dari 9 × 3

# List Comprehension

