""" Chaining """

# Chaining (rantai) --> Untuk menulis code yang lebih singkat dan mudah dibaca

""" Contoh Chaining Metode String """

my_string = "Hello, World!"                                     # --> Inisialisasi variabel yang menyimpan data string
results = my_string.strip().upper().replace("HELLO", "TOBRUT")  # --> Melakukan beberapa operasi berantai pada variabel my_string dan akan tersimpan pada variabel results
print(results)                                                  # --> mencetak variabel

# 1. strip()                    --> Mengapus sepasi di awal dan akhir string
# 2. upper()                    --> Mengubah string menjadi huruf besar
# 3. replace("Hello", "TOBRUT") --> Menggantikan HELLO dengan TOBRUT

""" Contoh Chaining Operasi Aritmatika"""

print("-------->")      # -- Abaikan ini

integer_a = 5                                          # --> Inisialisasi variabel yang menyimpan data integer
integer_b = 3                                          # --> Inisialisasi variabel yang menyimpan data integer
integer_c = 2                                          # --> Inisialisasi variabel yang menyimpan data integer
results = (integer_a + integer_b - integer_c) * 2 / 3  # --> Melakukan beberapa operasi berantai pada variabel integer_a,integer_b, integer_c dan akan tersimpan pada variabel results
print(results)                                         # --> Mencetak variabel

# 1. () --> Mengutamakan (diutamakan)
# 2. +  --> Menjumlahkan 
# 3. -  --> Mengurangi
# 4. *  --> Mengalikan
# 5. /  --> Membagi (hasil float)

"""Contoh Chaining Operasi List"""