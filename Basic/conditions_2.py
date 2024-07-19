""" Conditions """

# Conditions --> Membuat keputusan dalam program

#if kondisi:
    # Blok kode yang dieksekusi jika kondisi True
#elif kondisi_lain:
    # Blok kode yang dieksekusi jika kondisi_lain True
#else:
    # Blok kode yang dieksekusi jika tidak ada kondisi yang benar

""" contoh Conditions dan Conditional """

print("-------->")      # -- Abaikan ini

# Condition (sebuah ekspresi)
mz = 10
condition = mz > 5

# Conditional statement
if condition:
    print(True)
else:
    print(False)

""" Contoh Penggunaan IF Statement"""

print("-------->")      # -- Abaikan ini

num = 10          # --> Inisialisasi variabel yang menyimpan data integer
if num > 5:       # --> Kondisi, jika nilai variabel num lebih beasr dari 5 dan jika kondisi terpenuhi maka akan mencetak blok kode di dalamnya
    print(True)   # --> Jika kondisi terpenuhi maka akan mencetak True

""" Contoh Penggunaan IF-Else Statement"""

print("-------->")      # -- Abaikan ini

num = 20          # --> Inisialisasi variabel yang menyimpan data integer
if num > 25:      # --> Kondisi, jika nilai variabel num lebih besar dari 25 dan jika kondisi terpenuhi maka akan mencetak blok kode di dalamnya, lalu jika tidak terpenuhi makan akan eksekusi blok kode selanjutnya
    print(True)   # --> jika kondisi terpenuhi maka akan mencetak True
else:             # --> Jika kondisi tidak terpenuhi atau tidak ada yang benar maka blok kode else akan dieksekusi
    print(False)  # --> jika kondisi tidak terpenuhi maka akan mencetak False

""" Contoh Penggunaan IF-Elif-Else Statement"""

print("-------->")      # -- Abaikan ini

num = 15           # --> Inisialisasi variabel yang menyimpan data integer
if num > 30:       # --> Kondisi, jika nilai variabel num lebih besar dari 30 dan jika kondisi terpenuhi maka akan mencetak blok kode di dalamnya, lalu jika tidak terpenuhi maka akan eksekusi blok kode selanjutnya
    print(True)    # --> Jika kondisi terpenuhi maka akan mencetak true

elif num > 10:     # --> Kondisi, jika nilai variabel num lebih besar dari 10 dan jika kondisi terpenuhi maka akan mencetak blok kode di dalamnya, lalu jika tidak terpenuhi maka akan eksekusi blok kode selanjutnya
    print(True)    # --> jika kondisi terpenuhi maka akan mencetak True

else:              # --> Jika semua kondisi tidak terpenuhi atau tidak ada yang benar maka blok kode else akan dieksekusi
    print(False)   # --> Jika semua kondisi tidak terpenuhi maka akan mencetak False

""" Contoh Kondisi Bersarang - Nested Conditions"""

print("-------->")      # -- Abaikan ini

""" Contoh Dalam Penentuan Nilai pada Siswa (Program) """

# Untuk kasus ini kita bisa menggunakan loop while

while True:  # --> Infinite loop
    try:     # --> Menjalankan blok kode di dalamnya, jika ada kesalahan dalam blok try, program akan melajutkan ke blok except

        nilai = int(input("Masukan nilai ujian : ")) # --> Inisialisasi variabel yang menyimpan data integer, menggunakan fungsi input() sebagai string dan mengkonversinya ke integer
    
        if nilai >= 90 and nilai <= 100:             # --> Kondisi, jika kita menginput nilai dalam rentang 90 hingga 100 dan kondisi terpenuhi maka akan mengeksekusi blok kode di dalamnya
            hasil = "Lulus dengan nilai A"           # --> Inisialisasi variabel yang menyimpan data string

        elif nilai >= 80 and nilai < 90:             # --> Kondisi, jika kita menginput nilai dalam rentang 80 hingga 90 dan kondisi terpenuhi maka akan mengeksekusi blok kode di dalamnya
            hasil = "Lulus dengan nilai B"           # --> Inisialisasi variabel yang menyimpan data string

        elif nilai >= 70 and nilai < 80:             # --> Kondisi, jika kita menginput nilai dalam rentang 70 hingga 80 dan kondisi terpenuhi maka akan mengeksekusi blok kode di dalamnya
            hasil = "Lulus dengan nilai C"           # --> Inisialisasi variabel yang menyimpan data string

        elif nilai >= 60 and nilai < 70:             # --> Kondisi, jika kita menginput nilai dalam rentang 60 hingga 70 dan kondisi terpenuhi maka akan mengeksekusi blok kode di dalamnya
            hasil = "Lulus dengan nilai D"           # --> Inisialisasi variabel yang menyimpan data string

        elif nilai >=0 and nilai < 60:               # --> Kondisi, jika kita menginput nilai dalam rentang 0 hingga 60 dan kondisi terpenuhi maka akan mengeksekusi blok kode di dalamnya
            hasil = "Tidak Lulus dengan nilai E"     # --> Inisialisasi variabel yang menyimpan data string
        else:                                                                   # --> Jika kita menginput nilai di luar kondisi rentang 0 hingga 100, maka blok kode ini akan dieksekusi
            print("Nilai diluar jangkauan! Masukan nilai antara 0 hingga 100!") # --> Jika semua kondisi tidak terpenuhi makan akan mencetak ini

        print(f"Hasil Nilai : {hasil}")                                         # --> Mencetak variabel hasil, pada setiap iterasi (setiap kita memasukan nilai, program akan mengevaluasi nilai tersebut dan menampilkan hasilnya)

        lanjut = input("Ingin memasukan nilai lagi tidak tobrut? (y/n) :")      # --> Inisialisasi variabel yang menyimpan data string, menggunakan fungsi input() meminta kita apakah ingin memasukan nilai lagi atau tidak

        if lanjut.lower() != 'y':                                               # --> Kondisi, jika pengguna memasukan y, program kembali ke menu utama
            print("Terima kasih sayang!")                                       # --> Jika pengguna memasukan selain y maka ini yang akan di cetak         
            break                                                               # --> Menghentikan loop secara paksa menggunakan pernyataan break        
        
    except ValueError:                                                          # --> Jika terjadi kesalahan koncersi, misalnya pengguna memasukan teks bukan angka, dengan ini kita menangkap kesalahan dengan blok except
        print("Input tidak benar! Masukan angka!")                              # --> Jika terjadi kesalahan makan akan mencetak ini

""" Note! """

# 1. Pelajari Operator!