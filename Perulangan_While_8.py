""" Perulangan While digunakan untuk menjalankan blok kode selama kondisi benar atau True """

# 1. Perulangan dasar dengan while
hitung = 0
while hitung < 5:
    print(hitung) # Hasilnya adalah 0 1 2 3 4
    hitung += 1

print("----------")

# 2. While dengan kondisi spesifik
angka = 5
while angka > 0:
    print(angka)  # Hasilnya adalah 5 4 3 2 1
    angka -= 1

print("----------")

# 3 While dengan break --> Untuk menghentikan loop
hitung = 0
while True:
    print(hitung)  # Hasilnya adalah 0 1 2 3 4
    hitung += 1
    if hitung == 5:
        break

print("----------")

# 4. While dengan continue --> Untuk melewati iterasi tertentu dan melajutkan ke iterasi berikutnya
hitung = 0
while hitung < 10:
    hitung += 1
    if hitung % 2 == 0:
        continue
    print(hitung) # Hasilnya adalah 1 3 5 7 9 (mencetak angka ganjil)

print("----------")

hitung = 0
while hitung < 10:
    hitung += 1
    if hitung % 2:
        continue
    print(hitung) # Hasilnya adalah 2 4 6 8 10 (mencetak angka genap)

print("----------")

# 5. While dengan else --> Akan dijalankan jika loop while tidak dihentikan dengan break
hitung = 0
while hitung <5:
    print(hitung)
    hitung += 1
else:
    print("Loop selesai tanpa break!") # Hasilnya adalah 0 1 2 3 4 dan Loop selesai tanpa break!


# 6. Nested while atau perulangan baersarang --> Bisa menggunakan while di dalam while
i = 0
while i < 2:
    j = 0
    while j < 2:
        print(f"i: {i}, j: {j}") # Hasilnya adalah i: 0 j: 0, i:0 j:1, i:1 j:0, i:1 j:1
        j += 1
    i +=1

# 7. Program interaktif menggunakan while (sederhana)
while True:
    user_input = input("Ketik exit, untuk keluar : ")
    if user_input.lower() == "exit":
        break
    print(f"Kamu masukan: {user_input}") # hasilnya adalah dinamis, ketika user input exit maka akan keluar dari program, jika input Tobrut maka akan dicetak Tobrut

# 8. Infinite loop --> Perulangan berjalan terus menerus sampai dihentikan secara manual atau dengan break
while True:
    print("Tobrut") # Hasilnya adalah Tobrut (karena sudah dihentikan dengan break)
    break

# 9. Validasi atau menangani input pengguna dengan while
while True:
    try:
        nilai = int(input("Masukan nilai 0-100 : ")) # String konversi ke integer
        if 0 <= nilai <=100:
            break
        else:
            print("Nilai wajib diantara 0 sampai 100!")
    
    except ValueError:
        print("Masukan angka yang benar!")
print(f"Nilai yang di input : {nilai}") # Hasilnya adalah dinamis, tergantung inputan user dan dengan rentang nilai 0 sampai 100

# 10. Mwnggunakan while di dalam fungsi
def tobrut(t):
    faktor = 1
    while t > 1:
        faktor *= t
        t -= 1
    return faktor
print(tobrut(5)) # Hasilnya adalah 120

# 11. Menggunakan while untuk iterasi dengan struktur data lain atau di sini dengan list
list_tobrut = [1,2,3,4,5]
index = 0
while index < len(list_tobrut):
    print(list_tobrut[index]) # Hasilnya adlaah 1 2 3 4 5
    index += 1

# 12. Game sederhana tebak angka menggunakan while
""" import random

angka_rahasia = random.randint(1,100)
tobrut_tebak = None
while tobrut_tebak != angka_rahasia:
    try:

        tobrut_tebak = int(input("Masukan angka 1-100 : "))
        if tobrut_tebak < angka_rahasia:
            print("Sanagat rendah!")
        elif tobrut_tebak > angka_rahasia:
            print("Terlalu tinggi!")

    except ValueError:
        print("Masukan angka yang benar!")

print("Tobrut tertebak!") """ # Hasilnya adalah dinamis, masukan angka di mulai dari 1 hingga 100

# 13. kalkulator sederhana --> Melakukan operasi dasar
def kalkulator_tobrut():
    while True:
        print("Kalkulator Tobrut")
        print("Pilih operasi : ")
        print("1. Pejumlahan")
        print("2. Pengurangan")
        print("3. Perkalian")
        print("4. Pembagian")

        while True:
            try:
                operasi = int(input("Masukan pilihan 1/2/3/4 : "))
                if operasi in [1,2,3,4]:
                    break
                else:
                    print("Pilihan tidak benar, pilih antara 1-4!")
            except ValueError:
                print("Masukan angka yang benar")
    
        while True:
            try:
                nums_1 = float(input("Masukan angka pertama : "))
                nums_2 = float(input("Masukan angka kedua : "))
                break
            except ValueError:
                print("Masukan angka yang benar!")
    
        if operasi == 1:
            hasil = nums_1 + nums_2
            operasi_str = "+"

        elif operasi == 2:
            hasil = nums_1 - nums_2
            operasi_str = "-"

        elif operasi == 3:
            hasil = nums_1 * nums_2
            operasi_str = "*"

        elif operasi == 4:
            if nums_2 == 0:
                print("Pembagian 0 tidak benar!")
                continue
            hasil = nums_1 / nums_2
            operasi_str = "/"

        print(f"Hasil : {nums_1} {operasi_str} {nums_2} = {hasil}")
        
        lanjut = input("Apa kamu ingin melanjutkan? (y/n)")
        if lanjut.lower() != "y":
            print("Terima kasih!")
            break

kalkulator_tobrut()

# 14. Menghitung bilangan prima dengan rentang tertentu (menemukan bilangan prima dalam rentang tertentu)
def ukhti_prima(tobrut):
    if tobrut<= 1:
        return False
    montok = 2
    while montok * montok <= tobrut:
        if tobrut % montok == 0:
            return False
        montok += 1
    return True

def bilangan_prima(rentang_awal, rentang_akhir):
    print(f"Bilangan prima antara {rentang_awal} dan {rentang_akhir} : ")
    nums= rentang_awal
    while nums <= rentang_akhir:
        if ukhti_prima(nums):
            print(nums, end=" ")
        nums += 1
    print() # Hasilnya adalah dinamis, misal pengguna memasukan rentang awal 1 dna rentang akhir 20 maka outputnya 2 3 4 7 11 13 17 19

rentang_awal = int(input("Masukkan rentang awal: "))
rentang_akhir = int(input("Masukkan rentang akhir: "))
bilangan_prima(rentang_awal, rentang_akhir)

# 15. Membaca file dan memproses isi tobrut
def baca_file(nama_file):
    try:
        with open(nama_file, 'r') as file:
            baris = file.readline()
            while baris:
                print(baris.strip()) # Hasilnya adalah isi dari file yang di baca, contoh saat tobrut meng input file contoh.txt
                baris = file.readline()
    except FileNotFoundError:
        print(f"File {nama_file} tidak ditemukan.")

nama_file = input("Masukkan nama file yang akan dibaca: ")
baca_file(nama_file)


# Bonus untuk kamu
halal = 0
while halal < 100:
    hati = "I Love You"
    if halal < 2:   # Menggunakan kondisi dan tanpa kondisi pun bisa
        print(hati) # Hasilnya adalah I Love You 2x
    halal += 1      # Increment manual