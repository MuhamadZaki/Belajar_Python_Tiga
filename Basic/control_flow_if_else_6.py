""" Control Flow If Else 1 """

print("-------->")     

# 1. Struktru Dasar if

x = 10            # --> Inisialisasi variabel yang menyimpan data integer
if x > 5:         # --> Kondisi, jika nilai vairabel x lebih besar dari 5 dan jika kondisi terpenuhi maka akan mengeksekusi blok kode di dalamnya
    print(True)   # --> Jiksa kondisi terpenuhi makan akan mencetak True

print("-------->")     

# 2. Struktur if-else

x = 10             # --> Inisialisasi variabel yang menyimpan data integer
if x < 5:          # --> Kondisi, jika nilai variabel x lebih besar dari 5 dan jika kondisi terpenuhi makan akan mengeksekusi blok kode di dalamnya, jika tidak terpenuhi maka akan melanjutkan ke kondisi berikutnya
    print(True)    # --> Jika kondisi terpenuhi maka akan mencetak True

else:              # --> Kondisi, jika kondisi sebelumnya tidak ada yang terpenuhi maka blok kode ini akan diesekusi
    print(False)   # --> Jika semua kondisi tidak terpenuhi maka akan mencetak False

print("-------->")     

# 3. Struktur if-elif-else

x = 10              # --> Inisialisasi variabel yang menyimpan data integer
if x > 20:          # --> Kondisi, jika nilai vairbel x lebih besar dari 20 dan jika kondisi terpenuhi maka akan mengeksekusi blok kode di dalamnnya, jika tidak terpenuhi maka akan melajutkan ke kondisi berikutnya
    print("x > 20") # --> Jika kondisi terpenuhi maka akan mencetak x > 20

elif x > 5:         # --> Kondisi, jika nilai variabel x lebih besar dari 5 dan jika kondisi terpenuhi maka akan mengeksekusi blok kode di dalamnya, jika tidak terpenuhi maka akan melajutkan ke kondisi berikutnya
    print("x > 5")  # --> Jika kondisi terpenuhi makan akan mencetak x > 5

else:               # --> Kondisi, jika kondisi sebelumnya tidak ada yang terpenuhi maka blok kode ini akan dieksekusi
    print(False)    # --> Jiksa semua kondisi tidak terpenuhi makan akan mencetak False

print("-------->")  

# 4. Nested if atau if bersarang

x = 10                  # --> Inisialisasi variabel yang menyimpan data integer
if  x > 9:              # --> Kondisi, jika nilai variabel x lebih besar dari 9 dan jika kondisi terpenuhi maka akan mengeksekusi blok kode di dalamnya, jika tidak terpenuhi maka akan melanjutkan ke kondisi berikutnya
    print("x > 9")      # --> Jika kondisi terpenuhi maka akan mencetak x > 9

    if x > 11:          # --> Kondis (besarang), kalau kondisi pertama terpenuhi maka blok kode ini akan dieksekusi, jika x lebih besar dari 11 dan jika kondisi terpenuhi maka akan mengeksekusi blok kode di dalamnya, jika tidak terpenuhi maka akan melajutkan ke kondisi berikutnya
        print("x > 11") # --> Jiksa kondisi terpenuhi makan akan mencetak x > 11
    else:               # --> Kondisi, jika kondisi sebelumnya tidak ada yang terpenuhi maka blok kode ini akan dieksekusi
        print("Salah")  # --> Jika semua kondisi tidak terpenuhi maka akan mencetak Salah

else:                   # --> kondisi, jika kondisi peratama tidak terpenuhi maka blok kode ini dieksekusi
    print(False)        # --> Jika kondisi pertama tidak terpenuhi makan akan mencetak False


print("-------->")     

# 5. Ternary if atau kondisi dalam satu baris

x = 10                             # --> Inisialisasi variabel yang menyimpan data integer
results = True if x > 5 else False # --> Kondisi (ternary) jika x lebih besar dari 5, jika kondisi terpenuhi makan akan mencetak True, jika tidak terpenuhi maka akan mengeksekusi kondisi else mencetak False dan tersimpan pda variabel results
print(results)                     # --> Mencetak variabel

print("-------->")  

# 6. If tanpa blok else

x = 4                        # --> Inisialisasi variabel yang menyimpan data integer 
if x % 2 == 0:               # --> Kondisi, jika nilai variabel angka genap dan jika kondisi terpenuhi maka akan mengeksekusi blok kode di dalamnya
    print("Bilangan genap!") # --> Jika kondisi terpenuhi maka akan mencetak Bilangan genap!

x = 5                        # --> Inisialisasi variabel yang menyimpan data integer
if x % 2:                    # --> Kondisi, jika nilai variabel angka ganjil dan jika kondisi terpenuhi maka akan mengeksekusi blok kode di dalamnya
    print("Bilangan ganjil") # --> Jika kondisi terpenuhi maka akan mencetak Bilangan ganjil

# 7. Penggunaan pass dalam blok if

x = 10    # --> Inisialisasi variabel yang menyimpan data integer
if x > 5: # --> Kondisi, jika nilai variabel x lebih besar dari 5 dan jika kondisi terpenuhi maka akan mengeksekusi blok kode di dalamnya, jika tidak terpenuhi maka akan melajutkan ke kondisi berikutnya
    pass  # --> Lewati, tidak mealukan apa-apa

# 8. Menggabungkan kondisi dengan and or

x = 10              # --> Inisialisasi variabel yang menyimpan data integer
y = 5               # --> Inisialisasi variabel yang menyimpan data integer
if x > y and y < x: # --> Kondisi, Jika nilai vairbael x lebih besar dari nilai variabel y dan digabungkan dengan nilai variabel y lebih kecil dari nilai variabel x, jika keduanya True atau kondisi terpenuhi maka akan mengeksekusi blok kode di dalamnya, jika tidak terpenuhi maka akan melajutkan ke kondisi berikutnya
    print(True)     # --> Jika kondisi terpenuhi maka akan mencetak True
else:               # --> Kondisi, jika kondisi sebelumnya tidak ada yang terpenuhi maka blok kode ini akan dieksekusi
    print(False)    # --> Jika semua kondisi tidak terpenuhi makan akan mencetak False

x = 10              # --> Inisialisasi variabel yang menyimpan data integer
y = 5               # --> Inisialisasi variabel yang menyimpan data integer 
if x > y or y > x:  # --> Kondisi, jika nilai variabel x lebih besar dari nilai variabel y dan digabungkan dengan nilai variabel y lebih besar dari nilai variabel x, jika salah satu True atau kondisi terpenuhi maka akan mengeksekusi blok kode di dalamnya, jika tidak terpenuhi maka akan melanjutkan ke kondisi berikutnya
    print(True)     # --> Jika kondisi terpenuhi maka akan mencetak True
else:               # --> Kondisi, jika kondisi sebelumnya tidak ada yang terpenuhi maka blok kode ini akan dieksekusi
    print(False)    # --> Jika semua kondisi tidak terpenuhi maka akan mencetak False

# 9. Contoh program sangat sederhana

users = int(input("Coba masukan angka 1, -1 dan 0 : ")) # --> Inisialisasi variabel yang menyimpan data integer, menggunakan fungsi input() sebagai string dan mengkonversinya ke integer
if users > 0:       # --> Kondisi, jika nilai variabel users lebih besar dari 0 dan jika kondisi terpenuhi maka akan mengeksekusi blok kode di dalamnya, jika kondisi tidak terpenuhi maka akan melajutkan ke kondisi berikutnya
    print("Lebih")  # --> Jika kondisi terpenuhi maka akan mencetak Lebih
elif users < 0:     # --> Kondisi, jika nilai variabel users lebih kecil dari 0 dan jika kondisi terpenuhi maka akan mengeksekusi blok kode di dalamnya, jika kondisi tidak terpenuhi maka akan melajutkan ke kondisi berikutnya
    print("Kurang") # --> Jika kondisi terpenuhi maka akan mencetak Kurang
else:               # --> Kondisi, jika kondisi sebelumnya tidak ada yang terpenuhi maka blok kode ini akan dieksekusi
    print(False)    # --> Jika semua kondisi tidak terpenuhi maka akan mencetak False

""" Control Flow If Else 2 """

# --> Lanjut besok