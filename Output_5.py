""" Ini Adalah Beberapa Output """

# Praktekan dan Pahami!

# Menampilkan String
print("Hello World!") # Hasilnya adalah Hello World!

# Menampilkan Angka
print(1997) # --> Hasilnya adalah Integer 1997
print(3.14) # --> Hasilnya adalah float 3.14

# Menampilkan Variabel
nama = "Tobrut"        # --> Inisialisasi variabel yang menyimpan data string
umur = 26              # --> Inisialisasi variabel yang menyimpan data integer
print("Nama : ", nama) # Tobrut --> Mencetak variabel (String di dalam cuma untuk pemanis)
print("Umur : ", umur) # 26     --> Mencetak variabel (String di dalam cuma untuk pemanis)

# Penggabaungan String dan Variabel
# 1. Menggunakan Operator
nama = "Tobrut"                                                          # --> Inisialisasi variabel yang menyimpan data string
umur = 27                                                                # --> Inisialisasi variabel yang menyimpan data integer
print("Nama saya " + nama + " dan saya berumur " + str(umur) + " tahun") # Tobrut, 27 --> Menggabungkan data variabel nama dan umur(integer dikonversi ke string) dengan operator penjumlahan (String di dalam cuma untuk pemanis)

# 2. Menggunakan F-String atau Format String
nama = "Tobrut"                                          # --> Inisialisasi variabel yang menyimpan data string
umur = 28                                                # --> Inisialisasi variabel yang menyimpan data integer
print(f"Nama saya {nama} dan saya berumur {umur} tahun") # Tobrut, 28 --> Menggabungkan data variabel nama dan umur menggunakan f-string (String di dalam cuma untuk pemanis)

# 3. Menggunakan format() Method
nama = "Tobrut"                                                           # --> Inisialisasi variabel yang menyimpan data string
umur = 29                                                                 # --> Inisialisasi variabel yang meyimpan data integer
print("Nama saya adalah {} dan saya berumur {} tahun".format(nama, umur)) # Tobrut, 29 --> Menggabungkan data variabel dengan method format() dan {}(sebagai tempat penampung, yang akan terisi dengan data dari variabel yang ada di dalam format)

# Menampilkan Beberapa Item Sekaligus
# 1. Menggunakan Koma
nama = "Tobrut"                          # --> Inisialisasi variabell yang menyimpan data string
umur = 30                                # --> inisialisasi variabel yang menyimpan data integer
print("Nama", nama, 'dan', "Umur", umur) # Tobrut, 30 --> Menggabungkan string menjadi satu dengan string concatenation 

# Menampilkan Struktur Data
# 1. List
list_buah = ["Mangga", "Apel", "Tobrut"] # --> Inisialisasi variabel yang menyimpan data list, berisi 3 elemen data string
print(list_buah)                         # Mangga, Apel, tobrut --> Mencetak variabel
 
# 2 Dictionary
data_dict = {"nama": "Tobrut", "umur": 31} # --> Inisialisasi variabel yang menyimpan data dict, berisi 2 key dan 2 value data string dan integer
print(data_dict)                           # Nama Tobrut Umur 31 --> Mencetak variabel

# Karakter Khusus
# 1. \n  --> Dalam string untuk memulai baris baru
print("Baris pertama\nBaris kedua")     # --> Hasilnya adalah Baris pertama Baris Kedua

# 2. \t  --> Untuk menambahkan tab dalam string
print("Nama:\tTobrut\nUmur: 25")        # --> Hasilny adalah nama Tobrut Umur 25

# 3. \\  --> Untuk menyertakan backslash dalam string
print("Folder path: C:\\User\Tobrut")   # --> Hasilnya adalah Folder path: C:\User\Tobrut

# 4. '   --> Untuk menyertakan tanda kutip tunggal pada string
print("kamu, \'Tobrut?\'")              # --> Hasilnya adalah kamu, 'Tobrut?'

# 5. "   --> Untuk menyertakan tanda kutip ganda dalam string
print("Saya, \"Tobrut!\"")              # --> Hasilnya adalah Saya, "Tobrut!"

# 6. \r  --> Untuk menembalikan krusor ke awal baris
print("Baris pertama\rBaris kedua")     # --> Hasilnya adalah Baris keduama

# 7. \b  --> Untuk menghapus karakter sebelumnya
print("Ukhtie\b Tobrut!")               # --> Hasilnya adalah Ukhti Tobrut!

# 8. \f  --> Untuk membuat halaman baru
print("Halaman pertama\fHalaman kedua") # --> Hasilnya adalah Halaman pertama Halaman kedua

# 9. \v  --> Untuk vertical tab
print("Baris pertama\vBaris kedua")     # --> Hasilnya adalah Baris pertama Baris kedua

# 10. \0 --> Untuk null character
print("Null\0character")                # --> Hasilnya adalah Nullcharacter

# 11. Sep (Separator) --> Mengubah Pemisah Default (sepasi) antara item yang dicetak
print("Nama", "Umur", sep=" - ")        # --> Hasilnya adlaah Nama - Umur

# 12. End             --> Mengubah Karakter yang digunakan di akhir cetakan (Default Baris Baru)
print("Ini adalah", end=" ")            # --> Hasilnya adalah Ini adalah satu baris
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


# 4. File --> Menulis Output ke File dan Alih-Alih ke Konsol ( konteks manajemen)
with open("output.txt", "w") as file:  # --> Membuka file dalam mode tulis, jika file tidak ada maka akan dibuat, jika ada maka akan dihapus kontennya
    print("Hello, World!", file=file)  # --> Mencetak Hello, World! ke dalam file

with open("output.txt", "a") as file:  # --> Membuka file dalam mode append, konten akan ditambahkan ke akhir di dalam file tanpa menghapus konten yang sudah ada
    file.write("Toket Brutal!\n")      # --> Menulis teks ke dalam file dan \n untuk membuat baris baru setelah teks
    
with open("output.txt", "r") as file:  # --> membuka file dalam mode baca
    konten = file.read()               # --> Membaca seluruh konten dalam file dan menyimpan dalam variabel konten
    print(konten)                      # --> Mencetak variabel

    # Note dalam open() :
    # 1. w (Write)  --> Jika file tidak ada , mode ini akan membuat file baru dan jika file ada maka kontennya akan dihapus
    # 2. r (Read)   --> Membuka file untuk dibaca dan akan menjadi error jika file tidak ada
    # 3. a (Append) --> Membuka file untuk menambahkan data di akhir file dan jika file tidak ada, maka akan dibuat
    # 4. x (Excusive Creation) --> Membuka file untuk penulisan, tetap jika file tidak ada dan akan terjadi error jika file sudah ada
    # 5. b (Binary) --> Membuka file dalam mode biner, digunakan bersamaan dengan mode lainnya (misal rb atau wb)
    # 6. t (Text)   --> Mode default, membuka file dalam mode teks dan biasanya tidak perlu ditentukan karena ini adalah default
    # 7. = (Update) --> Membuka file untuk pembacaan dan penulisan (misal r+ atau w+)
    # 8. with       --> Digunakan untuk membuka dan mengelola sumber daya (seperti file) secara otomatis
    # 9. open()     --> Membuka file yang berisi nama file dan mode 
    # 10. as file   --> Menggantikan objek yang mewakili file yang dibuka dengan nama variabel file

# 5. Flush --> Menyegarkan Aliran Output Secara Paksa
import time                            # --> Mengimpor modul time yang menyediakan berbagai fungsi terkait waktu
for tobrut in range(10):               # --> Melakukan iterasi menggunakan loop for menghasilkan urutan angka 0 hingga 9, pada setiap iterasi variabel tobrut akan mengambil nilai berikutnya dalam urutan tersebut
    print(tobrut, end=" ", flush=True) # --> Mencetak variabel diikuti oleh sepasi, alih-alih newline atau mencegah pindah ke baris baru setelah setiap cetakan dan memastikan bahwa output dicetak segera tanpa menunggu buffer penuh Hasilnya adlaah 0 1 2 3 4 5 6 7 8 9
    time.sleep(1)                      # --> Menunda eksekusi program selama 1 detik, jadi setiap angka yang dicetak akan berhenti selama 1 detik
