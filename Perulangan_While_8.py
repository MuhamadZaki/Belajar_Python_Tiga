""" Perulangan While digunakan untuk menjalankan blok kode selama kondisi benar atau True """

# Note :
# Itersi atau Iteration --> Proses di mana kita menelusuri atau melintasi setiap elemen dari suatu koleksi data seperti (ist, tuple, set dan dict) satu persatu (secara singkat adalah aksi atau proses)
numbers = [1, 2, 3, 4, 5]   # --> list yang di iterasi
index = 0                   # --> Melacak posisi elemen lit, ini adalah bagiandari persiapan untuk melakukan iterasi

while index < len(numbers): # --> Iterasi dumulai dari blok ini
    print(numbers[index])   # --> Aksi yang dilakukan selama iterasi
    index += 1              # --> iterasi


# 1. Perulangan dasar dengan while
hitung = 0          # --> Inisialisasi variabel hitung dengan nilai 0
while hitung < 5:   # --> Selama nilai hitung kurang dari 5, loop akan terus berjalan
    print(hitung)   # --> Hasilnya adalah 0 1 2 3 4 (pada setiap iterasi kita mencetak nilai hitung)
    hitung += 1     # --> Pada setiap iterasi, nilai hitung akan ditambahkan 1 (increment)

print("----------")

# 2. While dengan kondisi spesifik
angka = 5           # --> Inisialisasi variabel angka dengan nilai 5
while angka > 0:    # --> Selama nilai angka lebih besar dari 0, loop akan terus berjalan
    print(angka)    # --> Hasilnya adalah 5 4 3 2 1 (pada setiap iterasi kita mencetak nilai angka)
    angka -= 1      # --> Pada setiap iterasi, nilai angka akan dikurangi 1 (decrement)

print("----------")

# 3 While dengan break --> Untuk menghentikan loop
hitung = 0          # --> Inisialisasi variabel hitung dengan nilai 0
while True:         # --> Infinite loop atau looping akan berjalan terus menerus, selama kondisi True
    print(hitung)   # --> Hasilnya adalah 0 1 2 3 4 (pada setiap iterasi kita mencetak nilai hitung)
    hitung += 1     # --> Pada setiap iterasi, nilai hitung akan ditambahkan 1 (increment)
    if hitung == 5: # --> Jika nilai hitung mencapai 5
        break       # --> Kita menggunakan pernyataan break untuk menghentikan loop

print("----------")

# 4. While dengan continue --> Untuk melewati iterasi tertentu dan melajutkan ke iterasi berikutnya
hitung = 0              # --> Inisialisasi variabel hitung dengan nilai 0
while hitung < 10:      # --> Selama nilai hitung kurang dari 10, loop akan terus berjalan
    hitung += 1         # --> Pada setiap iterasi, nilai hitung akan ditambahkan 1 (increment)
    if hitung % 2 == 0: # --> Memeriksa menggunakan kondisi, apakah nilai hitung genap (hitung % 2==0, menghitung sisa pembagian hitung dengan 2 dan jika sisa pembagian adalah 0) maka nilai hitung adalah genap
        continue        # --> Jika nilai hitung genap, kita menggunakan pernyataan continue untuk melewati iterasi ini dan melajutkan ke iterasi berikutnya
    print(hitung)       # Hasilnya adalah 1 3 5 7 9 (mencetak angka ganjil 1-9), karena kita melewati iterasi ketika nilai hitung adalah genap

print("----------")

hitung = 0         # --> Inisialisasi variable hitung dengan nilai 0
while hitung < 10: # --> Selama nilai hitung kurang dari 10, loop akan terus berjalan
    hitung += 1    # --> Pada setiap iterasi, nilai hitng akan ditambahkan 1 (increment)
    if hitung % 2: # --> Jika nilai hitung ganjil, (karena % 2 akan menghasilkan 1)
        continue   # --> Jika nilai hitung ganjil, kita menggunakan pernyataan continue untuk melewati iterasi ini dan melanjutkan ke iterasi berikutnya
    print(hitung)  # Hasilnya adalah 2 4 6 8 10 (mencetak angka genap 2-10), karena kita melewati iterasi ketika nilai hitung adalah ganjil

print("----------")

# 5. While dengan else --> Akan dijalankan jika loop while tidak dihentikan dengan break
hitung = 0         # --> Inisialisasi variable hitung dengan nilai 0
while hitung < 5:  # --> Selama nilai hitung kurang dari 5, loop akan terus berjalan
    print(hitung)  # --> Hasilnya adalah 0 1 2 3 4 (pada setiap iterasi kita mencetak nilai hitung)
    hitung += 1    # --> Pada setiap iterasi, nilai hitng akan ditambahkan 1 (increment)
else:
    print("Loop selesai tanpa break!") # --> Akan dieksekusi setelah loop selesai, jika loop berakhir karena kondisi tidak terpenuhi (nilai hitung tidak kurnag dari 5) akan tetapi kita tidak menggunakan break makan blok ini tetap di eksekusi


# 6. Nested while atau perulangan baersarang --> Bisa menggunakan while di dalam while
i = 0               # --> Inisialisasi variabel i dengan nilai 0
while i < 2:        # --> Selama nilai i kurang dari 2, loop akan terus berjalan
    j = 0           # --> Inisialisasi variabel j dengan nilai 0
    while j < 2:    # --> Looping di dalam looping, akan berjalan selama nilai j kurang dari 2
        print(f"i: {i}, j: {j}") # --> Hasilnya adalah i: 0 j: 0, i:0 j:1, i:1 j:0, i:1 j:1 (pada setiap iterasi nested loop, kita mencetak nilai i dan j)
        j += 1      # --> Pada setiap itrasi, nilai j akan ditambahkan 1 (increment)
    i +=1           # --> pada setiap iterasi nilai i akan ditamahkan 1 (increment)

# 7. Program interaktif menggunakan while (sederhana)
while True:                                           # --> Infinite loop atau looping akan berjalan terus menerus, selama kondisi True
    user_input = input("Ketik exit, untuk keluar : ") # --> Kita meminta pengguna untuk memasukan input, lalu ditampilkan dan input pengguna akan disimpan dalam variabel user_input
    if user_input.lower() == "exit":                  # --> Kita menggunakan kodisional, apakah input pengguna adalah exit (setelah diubah menjadi huruf kecil)
        break                                         # --> Jika input adalah exit, kita menggunakan pernyataan break untuk menghentikan loop
    print(f"Kamu masukan: {user_input}")              # --> Hasilnya adalah dinamis, jika input bukan exit, kita mencetak pesan Kamu masukan: {user_input}

# 8. Infinite loop --> Perulangan berjalan terus menerus sampai dihentikan secara manual atau dengan break
while True:         # --> Infinite loop atau looping akan berjalan terus menerus, selama kondisi True
    print("Tobrut") # --> Hasilnya adalah Tobrut (karena sudah dihentikan dengan break)
    break           # --> Karena loop dihentikan secara paksa dengan pernyataan break, bahakan jika kondisi loop masih terpenuhi.

# 9. Validasi atau menangani input pengguna dengan while
while True:         # --> Infinite loop atau looping akan berjalan terus menerus, selama kondisi True
    try:            # --> Menjalankan blok kode di dalamnya
        nilai = int(input("Masukan nilai 0-100 : "))    # --> Kita meminta pengguna untuk melakukan input dan input dari pengguna di konversi menjadi integer dan tersimpan di variabel nilai
        if 0 <= nilai <=100:                            # --> Meguakan kodisional, kita memeriksa pakah nilai yang dimasukan berada dalam renatang 0 hingga 100
            break                                       # --> Jika nilai berada dalam rentang tersebut, kita menggunakan pernyataan break untuk menghentikan loop
        else:
            print("Nilai wajib diantara 0 sampai 100!") # --> Jika nilai tidak berada dalam rentang tersebut, kita mencetak pesan ini
    
    except ValueError:                      # --> Jika terjadi kesalahan koncersi, misalnya pengguna memasukan teks bukan angka, dengan ini kita menangkap kesalahan dengan blok except
        print("Masukan angka yang benar!")  # --> Jika terjadi kesalahan makan akan mencetak ini
print(f"Nilai yang di input : {nilai}")     # --> Hasilnya adalah dinamis (jika loop selesai kita mencetak nilai yang dimasukan olehpengguna)

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