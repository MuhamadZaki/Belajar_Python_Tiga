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


print("------")

# List Normal

results = []                                               # --> Inisialisasi variabel yang menyimpan data list, berisi elemen kosong
for index in range(10):                                    # --> Perulangan atau loop, mengiterasi sebanyak 10 kali (variabel index akan mengambil nilai 0 hingga 9)
    if index % 2 == 1:                                     # --> Kondisi, memerikasa apakah dalam rentang nilai variabel index terdapat biangan ganjil, jika kondisi terpenuhi maka akan mengeksekusi kode di dalamnya
        results.append(index)                              # --> Jika kondisi benar atau terpenuhi, setiap iterasi terdapat bilangan ganjil, maka akan ditambahkan ke dalam variabel results
print(results)                                             # --> Mencetak vairabel, maka akan mencetak pesan [1, 3, 5, 7, 9]

# List Comprehension

results = [index for index in range(10) if index % 2 == 1] # --> List comprehension, variabel index  menghasilkan rentang 0 hingga 9 dan memeriksa apakah dalam rentang nilai variabel index terdapat bilangan ganjil, jika kondisi terpenuhi atau terdpaat bilangna ganjil maka akan tersimpan pada variabel results
print(results)                                             # --> Mencetak vairabel, maka akan mencetak pesan [1, 3, 5, 7, 9]


print("------")

# List Normal

results =  []                    # --> Inisialisasi variabel yang menyimpan data list, berisi elemen kosong
for index in range(1,10):        # --> Perulangan atau loop, mnegiterasi sebanyak 10 kali, dimulai dari rentang 1 hingga 9
    if index % 2 == 0:           # --> Kondisi, memeriksa apakah dalam rentang nilai variabel index terdapat bilangan genap
        results.append(index*2)  # --> Jika kondisi terpenuhi (bilangan genap), maka akan mengalikannya dengan 2
    else:                        # --> Kondisi, jika kondisi sebelumnya tidak terpenuhi (bilangan ganjil) maka blok kode ini dieksekusi
        results.append(index*3)  # --> Jika kondisi salah atau tidak terpenuhi, lalu akan mengalikanya dengan 3
print(results)                   # --> Mencetak variabel, maka akan mencetak pesan [3, 4, 9, 8, 15, 12, 21, 16, 27]

# List Normal Dengan Ternary

results = []                                                 # --> Inisialisasi variabel yang menyimpan data list, berisi elemen kosong                            
for index in range(1, 10):                                   # --> Perulangan atau loop, mengiterasi sebanyak 10 kali, dimulai dari rentang 1 hingga 9
    results.append(index * (2 if index % 2 == 0 else 3))     # --> Kondisi, memeriksa apakah dalam rentang nilai variabel index terdapat bilangan genap, lalu jika terdapat bilangan genap maka mengalikannya dengan 2, jika (bilangan ganjil) menggantingan dengan 3 dan ditambahkan ke variabel results
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

results = [(index * (2 if index % 2 == 0 else 3)) for index in range(1,10)] # --> List comprehension, variabel index menghasilkan rentang 1 hingga 9, lalu memeriksa apakah setiap rentang index terdapat bilangan genap, jika terdapat bilangan genap maka dikalikan dengan 2, jika tidak menggantikannya dengan 3 dan tersimpan pada variabel results
print(results)                                                              # --> Menetak variabel, maka akan mencetak pesan [3, 4, 9, 8, 15, 12, 21, 16, 27]


print("------")

# List Normal

a_list = ["a", "b", "c"]            # --> Inisialisasi vairabel yang menyimpan data list, berisi 3 elemen data string
b_list = ["1", "2", "3"]            # --> Inisialisasi variabel yang menyimpan data list, berisi 3 elemen data string

results = []                        # --> Inisialisasi variabel yang menyimpan data list, berisi elemen kosong
for index in a_list:                # --> Perulangan atau loop, mengitersi melalui setiap elemen index dalam variabel a_list
    for i in b_list:                # --> perulangan bersarang, mengiterasi melalui setiap elemen i dalam variabel b_list
        results.append(index + i)   # --> Menggabungkan index, i menggunakan operator dan menambahkan ke dalam variabel results
print(results)                      # --> Mencetak variabel, maka akan mencetak pesan ['a1', 'a2', 'a3', 'b1', 'b2', 'b3', 'c1', 'c2', 'c3']

# List Comprehension

a_list = ["a", "b", "c"]            # --> Inisialisasi vairabel yang menyimpan data list, berisi 3 elemen data string
b_list = ["0", "1", "2"]            # --> Inisialisasi variabel yang menyimpan data list, berisi 3 elemen data string

results = [ index + i for index in a_list for i in b_list] # --> Mengiterasi melalui setiap elemen index dalam variabel a_list, mengiterasi melalui setiap elemen i dalam varibel b_list, lalu menggebungkan index, i menggunakan operator dan tersimpan pada variabel results
print(results)                                             # --> Mencetak variabel, maka akan mencetak pesan ['a0', 'a1', 'a2', 'b0', 'b1', 'b2', 'c0', 'c1', 'c2']


print("------")

# List Normal

nums = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12]
]                               # --> Inisialisasi variabel yang menyimpan data list, berisi 3 sub list

results = []                    # --> Inisialisasi variabel yang menyimpan data list, berisi list kosong
for index in range(4):          # --> Perulangan atau loop, mengiterasi variabel index dari rentang 0 hingga 3
    res = []                    # --> Inisialisasi vairbel yang menyimpan data list, berisi list kosong
    for row in nums:            # --> perulangan bersarang, mengiterasi setiap elemen row dalam nums 
        res.append(row[index])  # --> Menambahkan elemen ke-index dari row ke dalam res
    results.append(res)         # --> Menambahkan res ke dalam results
print(results)                  # --> Mencetak variabel, maka akan mencetak pesan [[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]

# List Ringkas

nums = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12]
]                                                # --> Inisialisasi variabel yang menyimpan data list, berisi 3 sub list

results = []                                     # --> Inisialisasi variabel yang menyimpan data list, berisi elemen kosong
for index in range(4):                           # --> Perulangan atau loop, mengiterasi variabel index dari rentang 0 hingga 3
    results.append([row[index] for row in nums]) # --> Menggunakan list comprehension untuk mengambil elemen ke-index dari setiap list dalam nums
print(results)                                   # --> Mencetak variabel, maka mencetak pesan [[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]

# List Lebih ringkas

nums = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12]
]                                                              # --> Inisialisasi variabel yang menyimpan data list, berisi 3 sub list

results = [[row[index] for row in nums] for index in range(4)] # --> Mengiterasi variabel index dari rentang 0 hingga 3, di dalam list comprehension, mengambil elemen ke-index dari setiap list dalam nums dan tersimpan pada varibel results
print(results)                                                 # --> Mencetak varabel, maka mencetak pesan [[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]

# Hasil dari list comprehension ini adalah list yang memutar (transpose) elemen-elemen dari list nums