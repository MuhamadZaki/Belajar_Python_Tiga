""" Control Flow If Else"""

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