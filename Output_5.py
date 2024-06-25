""" Ini Adalah Beberapa Output """

# Praktekan dan Pahami!

# Menampilkan String
print("Hello World!") # Hasilnya adalah Hello World!

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
# 1. \n
print("Baris pertama\nBaris kedua") # Hasilnya adalah Baris pertama Baris Kedua

# 2. \t
print("Nama:\tTobrut\nUmur: 25")    # Hasilny adalah nama Tobrut Umur 25

# 3. \\
print("Folder path: C:\\User\Tobrut") # Hasilnya adalah Folder path: C:\User\Tobrut

# 4. '
print("kamu, \'Tobrut?\'")            # Hasilnya adalah kamu, 'Tobrut?'

# 5. "
print("Saya, \"Tobrut!\"")            # Hasilnya adalah Saya, "Tobrut!"

# 6. \r
print("Baris pertama\rBaris kedua")   # Hasilnya adalah Baris keduama

# 7. \b
print("Ukhtie\b Tobrut!")             # Hasilnya adalah Ukhti Tobrut!

# 8. \f
print("Halaman pertama\fHalaman kedua") # Hasilnya adalah Halaman pertama Halaman kedua

# 9. \v
print("Baris pertama\vBaris kedua")     # Hasilnya adalah Baris pertama Baris kedua

# 10. \0
print("Null\0character")                # Hasilnya adalah Nullcharacter

# 11. Sep (Separator)
print("Nama", "Umur", sep=" - ")    # Hasilnya adlaah Nama - Umur

# 12. End 
print("Ini adalah", end=" ")        # Hasilnya adalah Ini adalah satu baris
print("satu baris.")

# Noted karakter Khusus :
# 1. \n (Baris baru (newline)  --> Dalam string untuk memulai baris baru
# 2. \t (Tab horizontal)       --> Untuk menambahkan tab dalam string
# 3. \\ (Backslash)            --> Untuk menyertakan backslash dalam string
# 4. '  (Kutip tunggal)        --> Untuk menyertakan tanda kutip tunggal pada string
# 5. "  (Kutip ganda)          --> Untuk menyertakan tanda kutip ganda dalam string
# 6. \r (carriage return)      --> Untuk menembalikan krusor ke awal baris
# 7. \b (Backspace)            --> Untuk menghapus karakter sebelumnya
# 8. \f (Form feed)            --> Untuk membuat halaman baru
# 9. \v (Vertical tab)         --> Untuk vertical tab
# 10. \0 (Null character)      --> Untuk null character
# 11. sep (separator)          --> Mengubah Pemisah Default (sepasi) antara item yang dicetak
# 12. End                      --> Mengubah Karakter yang digunakan di akhir cetakan (Default Baris Baru)


# 4. File --> Menulis Output ke File dan Alih-Alih ke Konsol
with open("output.txt", "w") as file:
    print("Hello, World!", file=file)  # Hasilnya adalah output.txt yang beisi Hello, World!

with open("output.txt", "a") as file:
    file.write("Toket Brutal!\n")      # Hasilnya adalah menambahkan Toket Brutal! ke file output.txt
    
with open("output.txt", "r") as file:
    konten = file.read()
    print(konten) # Hasilnya adalah Membaca file output.txt

    # Note dalam open() :
    # 1. w (Write)  --> Jika file tidak ada , mode ini akan membuat file baru dan jika file ada maka kontennya akan dihapus
    # 2. r (Read)   --> Membuka file untuk dibaca dan akan menjadi error jika file tidak ada
    # 3. a (Append) --> Membuka file untuk menambahkan data di akhir file dan jika file tidak ada, maka akan dibuat
    # 4. x (Excusive Creation) --> Membuka file untuk penulisan, tetap jika file tidak ada dan akan terjadi error jika file sudah ada
    # 5. b (Binary) --> Membuka file dalam mode biner, digunakan bersamaan dengan mode lainnya (misal rb atau wb)
    # 6. t (Text)   --> Mode default, membuka file dalam mode teks dan biasanya tidak perlu ditentukan karena ini adalah default
    # 7. = (Update) --> Membuka file untuk pembacaan dan penulisan (misal r+ atau w+)

# 5. Flush --> Menyegarkan Aliran Output Secara Paksa
import time
for tobrut in range(10):
    print(tobrut, end=" ", flush=True) # Hasilnya adlaah 0 1 2 3 4 5 6 7 8 9
    time.sleep(1)
