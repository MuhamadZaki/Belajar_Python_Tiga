""" Percabangan if-else-elif  """
# Proses penentuan keputusan atau kita sebut dengan conditional statement

# Contoh Dalam Penentuan Nilai pada Siswa (Program)

while True: # --> I infinite loop terus berjalan sampai ada pernyataan break 
    try:    # --> Menjalankan blok kode di dalamnya, jika ada kesalahan dalam blok try, program akan melajutkan ke blok except

        nilai = int(input("Masukan nilai ujian : ")) # --> fungsi input(), mengambil input sebagai string dan mengkonversinya ke integer
    
        # Kondisional (tentukan hasil berdasarkan nilai)
        if nilai >= 90 and nilai <= 100:    # --> Menggunakan kondisional, mengevaluasi nilai yang dimasukan dan menentukan hasil berdasrakan rentang nilai (jika nilai antara 90 hingga 100, maka hasilnya lulus dengan niliai A)
            hasil = "Lulus dengan nilai A"

        elif nilai >= 80 and nilai < 90:    # --> Mengevaluasi nilai yang dimasukan dan menetukan hasil berdasarkan rentang nilai (jika nilai antara 80 hingga 89, maka hasilnya lulus dengan nilai B)
            hasil = "Lulus dengan nilai B"

        elif nilai >= 70 and nilai < 80:    # --> Mengevaluasi nilai yang dimasukan dan menentukan hasil berdasarkan rentang nilai (jika nilai antara 70 hingga 79, maka hasilnya lulus dengan niliai C)
            hasil = "Lulus dengan nilai C"

        elif nilai >= 60 and nilai < 70:    # --> Mengevaluasi nilai yang dimasukan dan menentukan hasil berdasarkan rentang nilai (jika nilai antara 60 hingga 69, maka hasilnya lulus dengan nilai D)
            hasil = "Lulus dengan nilai D"

        elif nilai >=0 and nilai < 60:      # --> Mengvaluasi nilai yang dimasukan dan menentukan hasil berdasarkan rentang nilai (jika nilai antara 0 hingga 59, maka hasilnya tidak lulus dengan nilai E)
            hasil = "Tidak Lulus dengan nilai E"
        else:
            print("Nilai diluar jangkauan! Masukan nilai antara 0 hingga 100!") # --> Jika nilai yang dimasukan di luar rentang 0 hingga 100, maka ini akan dicetak

        print(f"Hasil Nilai : {hasil}")                                         # --> Mencetak hasil pada, setiap iterasi (setiap pengguna memasukan nilai, program akan mengevaluasi nilai tersebut dan menampilkan hasilnya)

        lanjut = input("Ingin memasukan nilai lagi tidak tobrut? (y/n) :")      # --> Meminta input pengguna apakah ingin memasukan nilai lagi atau tidak

        if lanjut.lower() != 'y':           # --> Jika pengguna memasukan y, program kembali ke menu utama
            print("Terima kasih sayang!")   # --> Jika pengguna memasukan selain y maka ini yang akan di cetak         
            break                           # --> Menghentikan loop secara paksa menggunakan pernyataan break        
        
    except ValueError:                               # --> Jika terjadi kesalahan koncersi, misalnya pengguna memasukan teks bukan angka, dengan ini kita menangkap kesalahan dengan blok except
        print("Input tidak benar! Masukan angka!")   # --> Jika terjadi kesalahan makan akan mencetak ini

# Note if-elif-else :
# 1. if     --> Merupakan pernyataan kondisional yang memeriksa apakah suatu kondisi benar (True), jika kondisi benar blok code yang berada di bawah if akan dijalankan
# 2. elif   --> Merupakan singkatan dari else if, pernyataan ini digunakan untuk memeriksa kondisi tambahan jika kondisi if di atasnya salah (False) dan kita dapat memiliki beberpa elif dalam satu rangkaian pernyataan kondisional
# 3. else   --> Merupakan pernyataan yang digunakan untuk menangani semua kondisi lain yang tidak terpenuhi oleh if dan elif dan code di bawah else akan dijalankan ketika semua kondisi sebelumnya salah (False)

# Note while dan for:
# 1. while Looop --> Digunakan untuk menjalankan blok code selama kondisi yang ditentukan benar (True). Ini cocok untuk kasus di mana kita perlu terus menjalankan suatu proses berdasarkan input atau kondisi yang diuji
# 2. for Loop   --> digunakan untuk mengulangi item dalam suatu urutan seperti (list, tuple, string, dict, set) atau objek yang dapat diiterasi lainnya

"""  Note untuk kasus ini for --> Di python int tidak dapat diiterasi menggunakan Loop for dalam konteks ini. Kamu bisa menggunakan while! """