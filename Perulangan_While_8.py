""" Perulangan While digunakan untuk menjalankan blok kode selama kondisi benar atau True """

# Note :
# Itersi --> Proses di mana kita menelusuri atau melintasi setiap elemen dari suatu koleksi data seperti (ist, tuple, set dan dict) satu persatu (secara singkat adalah aksi atau proses) / proses mengulang elemen-elemen dari sebuah itrable
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
    try:            # --> Menjalankan blok kode di dalamnya, jika ada kesalahan dalam blok try, program akan melajutkan ke blok except
        nilai = int(input("Masukan nilai 0-100 : "))    # --> Kita meminta pengguna untuk melakukan input dan input dari pengguna di konversi menjadi integer dan tersimpan di variabel nilai
        if 0 <= nilai <=100:                            # --> Meguakan kodisional, kita memeriksa pakah nilai yang dimasukan berada dalam renatang 0 hingga 100
            break                                       # --> Jika nilai berada dalam rentang tersebut, kita menggunakan pernyataan break untuk menghentikan loop
        else:
            print("Nilai wajib diantara 0 sampai 100!") # --> Jika nilai tidak berada dalam rentang tersebut, kita mencetak pesan ini
    
    except ValueError:                      # --> Jika terjadi kesalahan koncersi, misalnya pengguna memasukan teks bukan angka, dengan ini kita menangkap kesalahan dengan blok except
        print("Masukan angka yang benar!")  # --> Jika terjadi kesalahan makan akan mencetak ini
print(f"Nilai yang di input : {nilai}")     # --> Hasilnya adalah dinamis (jika loop selesai kita mencetak nilai yang dimasukan olehpengguna)

# 10. Mwnggunakan while di dalam fungsi
def tobrut(t):      # --> Mendfinisikan fungsi tibrut dengan parameter t
    faktor = 1      # --> Inisialisasi variabel faktor dengan nilai 1
    while t > 1:    # --> Selama nilai t lebih besar dari 1, loop akan terus berjalan
        faktor *= t # --> Selajutnya kita mengalikan nilai faktor dengan t
        t -= 1      # --> Setiap iterasi nilai t akan dikurangi 1 (decrement) --> Proses ini terus berlanjut hingga t mencapai 1
    return faktor   # --> Mengembalikan nilai faktor
print(tobrut(5))    # --> Hasilnya adalah 120 --> Dalam kasus ini kita menghitung faktorial dari 5 (5 !=5 x4 x3 x2 x1 = 120)

# 11. Menggunakan while untuk iterasi dengan struktur data lain atau di sini dengan list
list_tobrut = [1,2,3,4,5]           # --> Inisialisasi list_tobrut dengan beberapa nilai atau elemen
index = 0                           # --> Inisialisasi variabel index dengan nilai 0
while index < len(list_tobrut):     # --> Selama nilai index kurang dari panjang list_tobrut, maka looping akan berjalan
    print(list_tobrut[index])       # --> Setiap iterasi akan mencetak elemen dari list_tobrut berdasarkan nilai index dan hasilnya adlaah 1 2 3 4 5
    index += 1                      # --> Setiap itersi, nilai index akan ditambahkan 1 (increment)

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
def kalkulator_tobrut():            # --> Mendefinisikan taua deklarasi fungsi kalkulator_tobrut
    while True:                     # --> Loop utama, ini akan terus berjalan selama dalam kondisi True (infinite loop)
        print("Kalkulator Tobrut")  # --> Judul
        print("Pilih operasi : ")   # --> Pilihan
        print("1. Pejumlahan")      # --> Pilihan
        print("2. Pengurangan")     # --> Pilihan
        print("3. Perkalian")       # --> Pilihan
        print("4. Pembagian")       # --> Pilihan

        # Memilih Operasi
        while True:                                                 # --> Looping untuk validasi input operasi!
            try:                                                    # --> Menjalankan blok kode di dalamnya, jika ada kesalahan dalam blok try, program akan melajutkan ke blok except
                operasi = int(input("Masukan pilihan 1/2/3/4 : "))  # --> Meminta pengguna untuk meng-input dan tersimpan di variabel operasi (ini ddikonversi ke integer)
                if operasi in [1,2,3,4]:                            # --> Pengguna diminta untuk memiliah operasi dengan memasukan angka 1,2,3,4 (jika input valid)
                    break                                           # --> Menghentikan paksa loop dengan pernyataan break, jika input benar
                else:                                               
                    print("Pilihan tidak benar, pilih antara 1-4!") # --> Jika input tidak sesuai dengan angka 1,2,3,4 (jika input tidak valid) dan ini akan dicetak
            except ValueError:                                      # --> Untuk menangani kesalahan jika pengguna memasukan input bukan angka (karena sebelumnya sudah di konversi ke integer)
                print("Masukan angka yang benar")                   
        # Memasukan Angka
        while True:                                                 # --> Loping untuk validasi input angka!
            try:                                                    # --> Menjalankan blok kode di dalamnya, jika ada kesalahan dalam blok try, program akan melajutkan ke blok except
                nums_1 = float(input("Masukan angka pertama : "))   # --> Meminta pengguna untuk meng-input angka pertama (dna mengkonversinya ke float)
                nums_2 = float(input("Masukan angka kedua : "))     # --> Meminta pengguna untuk meng-input angka kedua (dan mengkonversinya ke float)
                break                                               # --> Menghentikan loop secara pakasa dengan pernyataan break, jika input benar
            except ValueError:                                      # --> Untuk menangani kesalahan jika pengguna meng-input bukan angka
                print("Masukan angka yang benar!")

        # Melakukan Operasi
        if operasi == 1:             # --> Jika operasi adalah penjumlahan --> Apakah operasi yang dimasukan pengguna adalah penjumlahan (dengan memerikasa apakah nilai operasi sama dengan 1)
            hasil = nums_1 + nums_2  # --> Melakukan penjumlahan dua angka
            operasi_str = "+"        # --> Menyimpan operasi dalam bentuk string (pemanis saja)

        elif operasi == 2:           # --> Jika operasi adalah pengurangan --> Apakah operasi yang dimasukan pengguna adalah pengurangan (dengan memerikasa apakah nilai operasi sama dengan 2)
            hasil = nums_1 - nums_2  # --> Melakukan pengurangan dua angka
            operasi_str = "-"        # --> Menyimpan operasi dalam bentuk string (pemanis saja)

        elif operasi == 3:           # --> Jika operasi adalah perkalian --> Apakah operasi yang dimasukan pengguna adalah perkalian (dengan memerikasa apakah nilai operasi sama dengan 3)
            hasil = nums_1 * nums_2  # --> Melakukan perkalian dua angka
            operasi_str = "*"        # --> Menyimpan operasi dalam bentuk string (pemanis saja)

        elif operasi == 4:           # --> Jika operasi adlah pembagaian --> Apakah operasi yang dimasukan pengguna adalah pembagian (dengan memerikasa apakah nilai operasi sama dengan 4)
            if nums_2 == 0:          # --> Menggunakan kondisional untuk memeriksa apakah kedua angka bukan 0(untuk menghindari pembagian dengan 0)
                print("Pembagian 0 tidak benar!")
                continue             # --> Melajutkan ke iterasi selanjutnya
            hasil = nums_1 / nums_2  # --> Melakukan pembagian dua angka
            operasi_str = "/"        # --> Menyimpan operasi dalam bentuk string (pemanis saja)
        # Menampilkan Haisl
        print(f"Hasil : {nums_1} {operasi_str} {nums_2} = {hasil}") # --> Mencetak hasil perhitungan dengan format (hasil operasi)
        # Lanjut atau mandeg
        lanjut = input("Apa kamu ingin melanjutkan? (y/n)")         # --> Pilihan pengguna untuk melajutkan atau tidak
        if lanjut.lower() != "y":                                   # --> jika pengguna memasukan y, program kembali ke menu utama
            print("Terima kasih!")                                  # --> Jika pengguna memasukan selain y maka ini yang akan di cetak
            break                                                   # --> Menghentikan loop secara paksa menggunakan pernyataan break

kalkulator_tobrut() # Pemanggilah hujan, eh! fungsi kalkulator_tobrut
 
# 14. Menghitung bilangan prima dengan rentang tertentu (menemukan bilangan prima dalam rentang tertentu)
def ukhti_prima(tobrut):                # --> Mendefinisikan funsi ukhti_prima dengan parameter tobrut (memerikasa apakah tobrut adalah bilangan prima?)
    if tobrut<= 1:                      # --> Memerikasa apakah tobrut kurang dari atau sama dengan 1
        return False                    # --> Jika iya, maka akan mengambalikan False, karena bilangan prima harus lebih nesar dari 1 (bukan bilangan prima)
    montok = 2                          # --> Inisialisasi variabel montok dengan nilai 2
    while montok * montok <= tobrut:    # --> Selama kuadrat dari montok kurang dari atau sama dengan tobrut, maka lanjut ke itersi selajutnya
        if tobrut % montok == 0:        # --> Jika tobrut habis dibagi dengan montok
            return False                # --> Kita mengembalikan False, karena tobrut bukan bilangan prima
        montok += 1                     # --> Jika tidak, setiap iterasi nilai montok ditambah 1
    return True                         # --> Jika kita melewati semua iterasi dan tidak ada pembagian yang menghasilkan sisa nol, kita mengembalikan True karena tobrut adalah bilangan prima

def bilangan_prima(rentang_awal, rentang_akhir):                            # --> fungsi bilangan_prima dengan dua paramater, yang bertujuan mencetak semua bilangan prima dlam rentang awal hingga akhir
    print(f"Bilangan prima antara {rentang_awal} dan {rentang_akhir} : ")   # --> Mencetak pesan bilangan prima  rentang awal dan akhir
    nums= rentang_awal              # --> Inisialisasi variabel nums dengan nilai rentang awal
    while nums <= rentang_akhir:    # --> Mengitrasi melalui semua angka dalam rentang (loop akan berjalan selama nums kurang dari atau sama dengan rentang akhir)
        if ukhti_prima(nums):       # --> Jika numas adalah bilangan prima (dengan memanggil fungsi ukhti_prima)
            print(nums, end=" ")    # --> lalu kita mencentak bilangan prima
        nums += 1                   # --> Setiap iterasi nilai nums ditambah 1
    print() # Hasilnya adalah dinamis, misal pengguna memasukan rentang awal 1 dna rentang akhir 20 maka outputnya 2 3 4 7 11 13 17 19 --> Mencetak baris baru

rentang_awal = int(input("Masukkan rentang awal: "))    # --> Memnitnta pengguna untuk menginput rentang awal
rentang_akhir = int(input("Masukkan rentang akhir: "))  # --> Memnitnta pengguna untuk menginput rentang akhit
bilangan_prima(rentang_awal, rentang_akhir)             # --> Memanggil fungsi bilangan_prima dengan input dari pengguna

# 15. Membaca isi dari file
def baca_file(nama_file):                   # --> Deklarasi fungsi dengan satu parameter
    try:                                    # --> Menjalankan blok kode di dalamnya, jika ada kesalahan dalam blok try, program akan melajutkan ke blok except
        with open(nama_file, 'r') as file:  # --> Membuka file dengan nama yang diberikan dan dalam mode read
            baris = file.readline()         # --> Membaca satu baris dari file dan menyimpan dalam variabel baris
            while baris:                    # --> loop akan berjalan selama variabel baris tidak kosong (berisi tesks)
                print(baris.strip())        # --> Hasilnya adalah membaca isi dari file yang dimasukan pengguna, seperti contoh.txt (Mencetak isi dari baris)
                baris = file.readline()     # --> Membaca baris berikutnya dari file dan menyimpan kembali dalam variabel baris
    except FileNotFoundError:
        print(f"File {nama_file} tidak ditemukan.")        # --> Pesan akan dicetak jika file tidak ditemukan

nama_file = input("Masukkan nama file yang akan dibaca: ") # --> Meminta pengguna untuk memasukan nama file
baca_file(nama_file)                                       # --> Memanggil fungsi


# Bonus untuk kamu
halal = 0                   # --> Inisialisasi variabel halal dengan nilai 0
while halal < 100:          # --> Loop yang akan berjalan selama nilai halal kurang dari 100 dan tentu selama loop kode di dalamnya akan di eksekusi berulang kali (makanya pake kondisi atau break)
    hati = "I Love You"     # --> Variabel hati dengan nilai string
    if halal < 2:           # --> Menggunakan kondisin (jika nilai halal kurang dari 2, maka kode dalam blok if akan dieksekusi - pada iterasi pertama, ketika halal masih 0 dan kondisi terpenuhi dan string akan dicetak) dan tanpa kondisi pun bisa
        print(hati)         # --> Hasilnya adalah I Love You 2x (mencetak isi dari variabel hati)
    halal += 1              # --> Increment manual (setiap iterasi nilai halal ditambah 1)