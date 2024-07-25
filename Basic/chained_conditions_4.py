""" Chained Conditionals Atau Kondisi Berantai """

# Kondisi berantai --> Memungkinkan kita untuk memeriksa beberpa kondisi dalam satu baris code

""" Contoh Kondisi Berantai Dengan If-Elif-Else """

print("-------->")      # --> Abaikan ini

angka = 50                  # --> Inisialisasi variabel yang menyimpan data integer
if angka >= 90:             # --> Kondisi, jika nilai variabel angka lebih besar sama dengan 90 dan kondisi terpenuhi maka akan mengeksekusi blok kode di dalamnya, jika tidak terpenuhi maka akan melanjutkan ke kondisi berikutnya
    print("Nilai A")        # --> Jika kondisi terpenuhi maka akan mencetak data string

elif angka >= 80:           # --> Kondisi, jika nilai variabel angka lebih besar sama dengan 80 dan kondisi terpenuhi maka akan mengeksekusi blok kode di dalamnya, jika tidak terpenuhi maka akan melanjutkan ke kondisi berikutnya
    print("Nilai B")        # --> Jika kondisi terpenuhi maka akan mencetak data string

elif angka >= 70:           # --> Kondisi, jika nilai variabel angka lebih besar sama dengan 70 dan kondisi terpenuhi maka akan mengeksekusi blok kode di dalamnya, jika tidak terpenuhi maka akan melanjutkan ke kondisi berikutnya
    print("Nilai C")        # --> Jika kondisi terpenuhi maka akan mencetak data string

elif angka >= 60:           # --> Kondisi, jika nilai variabel angka lebih besar sama dengan 60 dan kondisi terpenuhi maka akan mengeksekusi blok kode di dalamnya, jika tidak terpenuhi maka akan melanjutkan ke kondisi berikutnya
    print("Nilai D")        # --> Jika kondisi terpenuhi maka akan mencetak data string

else:                       # --> Kondisi, jika semua kondisi sebelumnya tidak ada yang terpenuhi maka blok kode ini akan dieksekusi
    print("Tidak Lulus!")   # --> Jika semua kondisi tidak terpenuhi maka akan mencetak data string

""" Kondisi Berantai Dengan Operator Logika AND """

print("-------->")      # --> Abaikan ini

umur = 17                            # --> Inisialisasi variabel yang menyimpan data integer
pendapatan = 9000                    # --> Inisialisasi variabel yang menyimpan data integer
if umur >= 18 and pendapatan > 5000: # --> Kondisi, jika nilai variabel umur lebih besar sama dengan 18 lalu menggabungkan kondisi dengan operator and dan jika nilai variabel pendapatan lebih besar dari 5000, selajutnya jika kondisi terpenuhi maka akan mengeksekusi blok kode di dalamnya, jika tidak terpenuhi maka akan melajutkan ke kondisi berikutnya
    print("Pinjol diterima!")        # --> Jika kondisi terpenuhi maka akan mencetak data string

else:                                # --> Kondisi, jika semua kondisi sebelumnya tidak terpenuhi, maka blok kode ini akan dieksekusi
    print("Pinjol ditolak!")         # --> Jika semua kondisi sebelumnya tidak terpenuhi maka akan mencetak data string


#print(True and False)  --> Jika salah satu kondisi False, maka akan mencetak False  (Ibaratkan menggunakan kondisi)
#print(False and True)  --> Jika salah satu kondisi False, maka akan mencetak False  (Ibaratkan menggunakan kondisi)
#print(True and True)   --> Jika kedua kondisi True, maka akan mecetak True          (Ibaratkan menggunakan kondisi)
#print(False and False) --> Jika kedua kondisi False, maka akan mencetak False       (Ibaratkan menggunakan kondisi)

""" Kondisi Berantai Dengan Operator Logika OR """

print("-------->")      # --> Abaikan ini

umur = 15                            # --> Inisialisasi variabel yang menyimpan data integer
pendapatan = 9000                    # --> Inisialisasi variabel yang menyimpan data integer
if umur >= 16 or pendapatan > 10000: # --> Kondisi, jika nilai variabel umur lebih besar sama dengan 16 lalu menggabungkan kondisi menggunakan operator or dan jika nilai variabel pendapatan lebih besar dari 10000, selajutnya jika kondisi terpenuhi maka akan mengeksekusi blok kode di dalamnya, jika tidak terpenuhi maka akan melajutkan ke kondisi berikutnya
    print("Pinjol diterima!")

else:
    print("Pinjol ditolak!")

#print(True or False)  # --> Jika salah satu kondisi True, maka mencetak True    (Ibaratkan menggunakan kondisi)
#print(False or True)  # --> Jika salah satu Kondisi True, maka mencetak True    (Ibaratkan menggunakan kondisi)
#print(True or True)   # --> Jika kedua kondisi True, maka mencetak True         (Ibaratkan menggunakan kondisi)
#print(False or False) # --> Jika kedua kondisi False, maka mencetak False       (Ibaratkan menggunakan kondisi)

""" Contoh Kondisi Berantai Dengan Operator Ternary """

print("-------->")      # --> Abaikan ini

umur = 25                                        # --> Inisialisasi variabel yang menyimpan data integer
status = "Dewasa" if umur >= 40 else "Anak-anak" # --> Kondisi, jika nilai variabel umur lebih besar sama dengan 18 (jika kondisi terpenuhi maka akan mecetak string "Dewasa") dan Jika kondisi tidak terpenuhi maka akan mengeksekusi blok else (mencetak data string "Anak-anak") lalu menyimpannya pada variabel status
print(status)                                    # --> Mencetak variabel


""" Contoh Kondisi Berantai Lebih Kompleks """

print("-------->")      # --> Abaikan ini

x = 15                                    # --> Inisialisasi variabel yang menyimpan data integer
if x > 13 and (x % 2 == 0 or x % 3 == 0): # --> Kondisi, jika nilai variabel x lebih besar dari 13 lalu menggabungkan kondisi dengan operator and jika kondisi pertama terpenuhi maka akan melajutkan ke kondisi berikutnya dan selanjutnya (x % 2 == 0): Ini memeriksa apakah x adalah kelipatan dari 2 (menggabungkan kondisi dengan operator or), (x % 3 == 0): Ini memeriksa apakah x adalah kelipatan dari 3, jika kondisi terpenuhi maka akan mengeksekusi blok kode di dalamnya, jika tidak terpenuhi maka akan melajutkan ke kondisi berikutnya 
    print("x lebih besar dari 10 dan merupakan kelipatan dari 2 atau 3") # --> Jika kondisi terpenuhi, maka akan mencetak data string
else:                                                                    # --> Kondisi, jika semua kondisi sebelumnya tidak terpenuhi, maka blok else akan dieksekusi
    print("x tidak memenuhi kedua kondisi tersebut")                     # --> Jika semua kondisi sebelumnya tidak terpenuhi maka akan mencetak data string


angka = 60                               # --> Inisialisasi variabel yang menyimpan data integer
kehadiran = 85                           # --> Inisialisasi variabel yang menyimpan data integer

if angka >= 90 and kehadiran >= 75:      # --> Kondisi, jika nilai variabel angka lebih besar sama dengan 90 lalu menggabungkan kondisi dengan operator and jika nilai variabel kehadiran lebih besar sama dengan 75, selanjutnya jika kondisi terpenuhi maka akan mengeksekusi blok kode di dalamnya, jika tidak terpenuhi maka akan melanjutkan ke kondisi berikutnya
    grade = "Amat Baik"                  # --> Inisialisasi variabel yang menyimpan data string
elif angka >= 80 and kehadiran >= 75:    # --> Kondisi, jika nilai variabel angka lebih besar sama dengan 80 lalu menggabungkan kondisi dengan operator and jika nilai variabel kehadiran lebih besar sama dengan 75, selanjutnya jika kondisi terpenuhi maka akan mengeksekusi blok kode di dalamnya, jika tidak terpenuhi maka akan melanjutkan ke kondisi berikutnya 
    grade = "Baik"                       # --> Inisialisasi variabel yang menyimpan data string
elif angka >= 70 and kehadiran >= 75:    # --> Kondisi, jika nilai variabel angka lebih besar sama dengan 70 lalu menggabungkan kondisi dengan operator and jika nilai variabel kehadiran lebih besar sama dengan 75, selanjutnya jika kondisi terpenuhi maka akan mengeksekusi blok kode di dalamnya, jika tidak terpenuhi maka akan melanjutkan ke kondisi berikutnya
    grade = "Cukup"                      # --> Inisialisasi variabel yang menyimpan data string
else:                                       # --> Kondisi, jika semua kondisi sebelumnya tidak terpenuhi, maka blok kode else akan dieksekusi
    grade = "D" if kehadiran >= 75 else "F" # --> Jika semua kondisi sebelumnya tidak terpenuhi dan terdapat kondisi lagi, jika nilai variabel kehadiran lebih besar sama dengan 75, jika terpenuhi mengambalikan data string "Dongo"dan jika tidak terpenuhi mengembalikan data string "Folol" kemudian di simpan pada variabel grade (Baris code ini menggunakan operator ternary)
print(grade)                                # --> Mencetak variabel

#print(True and False)  --> Jika salah satu kondisi False, maka akan mencetak False  (Ibaratkan menggunakan kondisi)
#print(False and True)  --> Jika salah satu kondisi False, maka akan mencetak False  (Ibaratkan menggunakan kondisi)
#print(True and True)   --> Jika kedua kondisi True, maka akan mecetak True          (Ibaratkan menggunakan kondisi)
#print(False and False) --> Jika kedua kondisi False, maka akan mencetak False       (Ibaratkan menggunakan kondisi)

#print(True or False)  # --> Jika salah satu kondisi True, maka mencetak True    (Ibaratkan menggunakan kondisi)
#print(False or True)  # --> Jika salah satu Kondisi True, maka mencetak True    (Ibaratkan menggunakan kondisi)
#print(True or True)   # --> Jika kedua kondisi True, maka mencetak True         (Ibaratkan menggunakan kondisi)
#print(False or False) # --> Jika kedua kondisi False, maka mencetak False       (Ibaratkan menggunakan kondisi)


""" Contoh Kondisi Berantai Dengan Fungsi """

print("-------->")      # --> Abaikan ini

def evaluasi_nilai(angka, kehadiran):           # --> Membuat fungsi evaluasi_nailai dengan 2 parameter yaitu nilai dan kehadiran
    if angka >= 90 and kehadiran >= 75:         # --> Kondisi, jika nilai variabel angka lebih besar sama dengan 90 lalu menggabungkan kondisi dengan operator and jika nilai variabel kehadiran lebih besar sama dengan 75, selanjutnya jika kondisi terpenuhi maka akan mengeksekusi blok kode di dalamnya, jika tidak terpenuhi maka akan melanjutkan ke kondisi berikutnya
        return "A"                              # --> Mengembalikan data string
    elif angka >= 80 and kehadiran >= 75:       # --> Kondisi, jika nilai variabel angka lebih besar sama dengan 80 lalu menggabungkan kondisi dengan operator and jika nilai variabel kehadiran lebih besar sama dengan 75, selanjutnya jika kondisi terpenuhi maka akan mengeksekusi blok kode di dalamnya, jika tidak terpenuhi maka akan melanjutkan ke kondisi berikutnya
        return "B"                              # --> Mengembalikan data string
    elif angka >= 70 and kehadiran >= 75:       # --> Kondisi, jika nilai variabel angka lebih besar sama dengan 70 lalu menggabungkan kondisi dengan operator and jika nilai variabel kehadiran lebih besar sama dengan 75, selanjutnya jika kondisi terpenuhi maka akan mengeksekusi blok kode di dalamnya, jika tidak terpenuhi maka akan melanjutkan ke kondisi berikutnya
        return "C"                              # --> Mengembalikan data string
    else:                                       # --> Jika semua kondisi sebelumnya tidak terpenuhi, maka blok kode else akan dieksekusi
        return "D" if kehadiran >= 75 else "F"  # --> Jika semua kondisi sebelumnya tidak terpenuhi dan mengembalikan data string, namun terdapat kondisi lagi jika nilai variabel kehadiran lebih besar sama dengan 75, jika terpenuhi mengambalikan data string "Dongo"dan jika tidak terpenuhi mengembalikan data string "Folol" (Baris code ini menggunakan operator ternary)

nilai = 65                                      # --> Inisialisasi variabel yang menyimpan data integer
hadir = 80                                      # --> Inisialisasi variabel yang menyimpan data integer
grade = evaluasi_nilai(nilai, hadir)            # --> Memanggil fungsi dengan argumen nilai, hadir dan menyimpan pada variabel grade
print(grade)                                    # --> Mencetak variabel

""" Note! """

# 1. Pelajari operator!