""" Ini Adalah Beberapa Output """

# Menampilkan String
print("Hello World") # Hasilnya adalah Hello World

# Menampilkan Angka
print(1997) # Hasilnya adalah Integer 1997
print(3.14) # Hasilnya adalah float 3.14

# Menampilkan Variabel
nama = "Tobrut"
umur = 26
print("Nama : ", nama) # Menggunakan variabel dengan nilai dan hasilnya adalah String Tobrut
print("Umur : ", umur) # Menggunakan variabel dengan nilai dan hasilnya adalah Integer 26

# Penggabaungan String dan Variabel
# 1. Menggunakan Operator
nama = "Tobrut"
umur = 27
print("Nama saya " + nama + " dan saya berumur " + str(umur) + " tahun") # Setelah menggabungkan dan mengkonversi dari int to string dan hasilnya  Nama saya Tobrut dan saya berumur 27 tahun

# 2. Menggunakan F-String atau Format String
nama = "Tobrut"
umur = 28
print(f"Nama saya {nama} dan saya berumur {umur} tahun") # Hasilnya adalah Nama saya Tobrut dan saya berumur 28 tahun

# 3. Menggunakan format() Method
nama = "Tobrut"
umur = 29
print("Nama saya adalah {} dan saya berumur {} tahun".format(nama, umur)) # Haislnya adalah Nama saya adalah Tobrut dan saya berumur 29 tahun

# Menampilkan Beberapa Item Sekaligus
# 1. Menggunakan Koma
nama = "Tobrut"
umur = 30
print("Nama", nama, 'dan', "Umur", umur) # Nama Tobrut dan Umur 30

# Menampilkan Struktur Data
# 1. List
list_buah = ["Mangga", "Apel", "Tobrut"]
print(list_buah) # Hasilnya adlaah Mangga, Apel, tobrut

# 2 Dictionary
data_dict = {"nama": "Tobrut", "umur": 31}
print(data_dict) # Hasilnya adalah Nama Tobrut Umur 31

# Karakter Khusus
# 1. Baris Baru dan Tab
print("Baris pertama\nBaris kedua") # Hasilnya adalah Baris pertama Baris Kedua
print("Nama:\tTobrut\nUmur: 25")    # Hasilny adalah nama Tobrut Umur 25

# 2. Sep (Separator) --> Mengubah Pemisah Default (sepasi) antara item yang dicetak
print("Nama", "Umur", sep=" - ")    # Hasilnya adlaah Nama - Umur

# 3. End --> Mengubah Karakter yang digunakan di akhir cetakan (Default Baris Baru)
print("Ini adalah", end=" ")        # Hasilnya adalah Ini adalah satu baris
print("satu baris.")

# 4. File --> Menulis Output ke File dan Alih-Alih ke Konsol
with open("output.txt", "w") as file:
    print("Hello, world!", file=file)  # Hasilnya adalah output.txt

# 5. Flush --> Menyegarkan Aliran Output Secara Paksa
import time
for tobrut in range(10):
    print(tobrut, end=" ", flush=True) # Hasilnya adlaah 0 1 2 3 4 5 6 7 8 9
    time.sleep(1)
