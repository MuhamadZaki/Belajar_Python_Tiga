""" Chained Conditionals Atau Kondisi Berantai """

# Kondisi berantai --> Memungkinkan kita untuk memeriksa beberpa kondisi dalam satu baris code

""" Contoh Kondisi Berantai Dengan If-Elif-Else """

print("-------->")      # -- Abaikan ini

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

print("-------->")      # -- Abaikan ini

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

print("-------->")      # -- Abaikan ini

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

print("-------->")      # -- Abaikan ini

umur = 25                                        # --> Inisialisasi variabel yang menyimpan data integer
status = "Dewasa" if umur >= 18 else "Anak-anak" # --> Kondisi, jika nilai variabel umur lebih besar sama dengan 18 (jika kondisi terpenuhi maka akan mecetak string "Dewasa") dan Jika kondisi tidak terpenuhi maka akan mengeksekusi blok else (mencetak data string "Anak-anak") lalu menyimpannya pada variabel status
print(status)                                    # --> Mencetak variabel


""" Contoh Kondisi Berantai Lebih Kompleks """

print("-------->")      # -- Abaikan ini

x = 15                                    # --> Inisialisasi variabel yang menyimpan data integer
if x > 13 and (x % 2 == 0 or x % 3 == 0): # --> Kondisi, jika nilai variabel x lebih besar dari 13 lalu menggabungkan kondisi dengan operator and jika kondisi pertama terpenuhi maka akan melajutkan ke kondisi berikutnya dan selanjutnya (x % 2 == 0): Ini memeriksa apakah x adalah kelipatan dari 2 (menggabungkan kondisi dengan operator or), (x % 3 == 0): Ini memeriksa apakah x adalah kelipatan dari 3, jika kondisi terpenuhi maka akan mengeksekusi blok kode di dalamnya, jika tidak terpenuhi maka akan melajutkan ke kondisi berikutnya 
    print("x lebih besar dari 10 dan merupakan kelipatan dari 2 atau 3") # --> Jika kondisi terpenuhi, maka akan mencetak data string
else:                                                                    # --> Kondisi, jika semua kondisi sebelumnya tidak terpenuhi, maka blok else akan dieksekusi
    print("x tidak memenuhi kedua kondisi tersebut")                     # --> Jika semua kondisi sebelumnya tidak terpenuhi maka akan mencetak data string


nilai = 75
kehadiran = 85

if nilai >= 90 and kehadiran >= 75:
    grade = "A"
elif nilai >= 80 and kehadiran >= 75:
    grade = "B"
elif nilai >= 70 and kehadiran >= 75:
    grade = "C"
else:
    grade = "D" if kehadiran >= 75 else "F"

print(grade) # --> Cape negejelasinya, nanti lagi yah


""" Contoh Kondisi Berantai Dengan Fungsi """

print("-------->")      # -- Abaikan ini

def evaluasi_nilai(nilai, kehadiran):
    if nilai >= 90 and kehadiran >= 75:
        return "A"
    elif nilai >= 80 and kehadiran >= 75:
        return "B"
    elif nilai >= 70 and kehadiran >= 75:
        return "C"
    else:
        return "D" if kehadiran >= 75 else "F"

nilai = 65
kehadiran = 80
grade = evaluasi_nilai(nilai, kehadiran)
print(grade) # --> Cape negejelasinya, nanti lagi yah

""" Note! """

# 1. Pelajari operator!