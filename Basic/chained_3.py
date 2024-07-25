""" Chaining """

# Chaining (rantai) --> Memungkinkan kita untuk menulis kode yang lebih bersih dan lebih intuitif dengan merantai beberapa metode atau operasi bersama-sama. Ini sangat berguna dalam banyak kasus seperti operasi string, list, dictionary, dan bahkan dengan fungsi custom.

""" Contoh Chaining Metode String """

print("-------->")      # --> Abaikan ini

my_string = "Hello, World!"                                     # --> Inisialisasi variabel yang menyimpan data string
results = my_string.strip().upper().replace("HELLO", "TOBRUT")  # --> Melakukan beberapa operasi berantai pada variabel my_string dan akan tersimpan pada variabel results
print(results)                                                  # --> mencetak variabel

# 1. strip()                    --> Mengapus sepasi di awal dan akhir string
# 2. upper()                    --> Mengubah string menjadi huruf besar
# 3. replace("HELLO", "TOBRUT") --> Menggantikan HELLO dengan TOBRUT

""" Contoh Chaining Operasi Aritmatika"""

print("-------->")      # --> Abaikan ini

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

""" Contoh Chaining Operasi List """

#nums = [5, 3, 2, 8, 1]
#results = sorted(nums, reverse=True.append(10)) # --> Akan menyebabkan error karena append mengembalikan None
#print(nums)

nums = [5, 3, 2, 8, 1]                    # --> Inisialisasi variabel yang menyimpan data list, berisi 5 elemen data integer 
sorted_nums = sorted(nums, reverse=True)  # --> List yang diurutkan
sorted_nums.append(10)                    # --> Menambahkan 1 elemen data integer yang sudah diurutkan
print(sorted_nums)                        # --> Mencetak variabel

# 1. sorted(nums)   --> Mengurutkan elemen-elemen di dalam variabel nums dari nilai terbesar ke nilai terkecil
# 2. reverse = True --> Menunjukan bahwa pengurutan dilakukan secara descending(menurun)
# 3. append()       --> Akan menambahkan elemen data ke akhir list

""" Chaining Dengan Fungsi Custom """

print("-------->")      # --> Abaikan ini

class kalkulator:                   
    def __init__(self, value=0):  
        self.value = value
    
    def add(self, amount):
        self.value += amount
        return self
    
    def kurang(self, amount):
        self.value -= amount
        return self
    
    def kali(self, amount):
        self.value *= amount
        return self
    
    def bagi(self, amount):
        if  self != 0:
            self.value /= amount
        return self

alat = kalkulator()
results = alat.add(10).kurang(5).kali(2).bagi(2).value
print(results)

""" Contoh Chaining Pada Dictionary"""

print("-------->")      # --> Abaikan ini

data = {                         # --> Insiasialisasi variabel yang menyimpan data dict, data berisi key user
    "user":{                     # --> ini key user sebuah dict yang memiliki key nama dan detail
        "nama":"Zaki",           # --> Ini key nama yang memiliki pasangan value
        "detail":{               # --> Ini key detail yang memiliki 2 key-value 
            "umur": 26,          # --> Ini key umur yang memiliki pasangan value
            "lokasi": "Jakarta"  # --> Ini key kokasi yang memiliki pasangan value
        }
    }
}

names1 = data.get("user", {})       
names2 = data.get("user", {}).get("nama", "kosong")        
locations = data.get("user", {}).get("detail", {}).get("lokasi", "kosong") 
print(names1)                                                    # --> Mencetak variabel
print(names2)                                                    # --> Mencetak variabel
print(locations)                                                 # --> Mencetak variabel

# 1. data.get("user", {})    --> Mengembil isi dari key user dalam variabel data, jika key user tidak ada maka akan mengembalikan dict kosong {}
# 2. get("nama", "kosong")   --> Mengambil value dari key nama, jika key nama tidak ada maka akan mengembalikan string "kosong" dan ini berkaitan dengan data.get("user", {}) 
# 3. get("detail", {})       --> Mengembil isi dari key detail, jika key detail tidak ada maka akan mengembalikan dict kosong {} dan ini berkaitan dengan data.get("user", {}) 
# 4. get("lokasi", "kosong") --> Mengambil value dari key lokasi, jika key lokasi tidak ada maka akan mengembalikan string "kosong" dan ini berkaitan dengan data.get("user", {}).get("detail", {})


""" Note! """

# Set dan Tupel sebenernya bisa menggunakan chaining tapi terbatas, karena sifat immutable