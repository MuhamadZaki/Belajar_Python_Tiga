""" Percabangan if-else-elif  """
# Proses penentuan keputusan atau kita sebut dengan conditional statement

# Contoh Dalam Penentuan Nilai pada Siswa (Program)

while True: # --> Loop ini akan terus berjalan sampai pernyataan break
    try:    # --> Menjalankan kode di dalam (sembari untuk menangani error)

        nilai = int(input("Masukan nilai ujian : ")) # Fungsi input String yang dikonversi ke Integer
    
        # Kondisional (tentukan hasil berdasarkan nilai)
        if nilai >= 90 and nilai <= 100: #  Jika menggunakan operator dengan rentang tertentu contoh rentang 90 hingga 100, dan tambahkan --> nilai >=90 and nilai <=100
            hasil = "Lulus dengan nilai A"

        elif nilai >= 80 and nilai < 90:
            hasil = "Lulus dengan nilai B"

        elif nilai >= 70 and nilai < 80:
            hasil = "Lulus dengan nilai C"

        elif nilai >= 60 and nilai < 70:
            hasil = "Lulus dengan nilai D"

        elif nilai >=0 and nilai < 60:
            hasil = "Tidak Lulus dengan nilai E"
        else:
            print("Nilai diluar jangkauan! Masukan nilai antara 0 hingga 100!")

        print(f"Hasil Nilai : {hasil}") # Dinamis, jika user memasukan nilai berupa angka (karena string sudah konversi menjadi integer)

        lanjut = input("Ingin memasukan nilai lagi tidak tobrut? (y/n) :")

        if lanjut.lower() != 'y':
            break
        
    except ValueError: # Pesan kesalahan
        print("Input tidak benar! Masukan angka!")

# Note if-elif-else :
# 1. if     --> Merupakan pernyataan kondisional yang memeriksa apakah suatu kondisi benar (True), jika kondisi benar blok code yang berada di bawah if akan dijalankan
# 2. elif   --> Merupakan singkatan dari else if, pernyataan ini digunakan untuk memeriksa kondisi tambahan jika kondisi if di atasnya salah (False) dan kita dapat memiliki beberpa elif dalam satu rangkaian pernyataan kondisional
# 3. else   --> Merupakan pernyataan yang digunakan untuk menangani semua kondisi lain yang tidak terpenuhi oleh if dan elif dan code di bawah else akan dijalankan ketika semua kondisi sebelumnya salah (False)

# Note while dan for:
# 1. while Looop --> Digunakan untuk menjalankan blok code selama kondisi yang ditentukan benar (True). Ini cocok untuk kasus di mana kita perlu terus menjalankan suatu proses berdasarkan input atau kondisi yang diuji
# 2. for Loop   --> digunakan untuk mengulangi item dalam suatu urutan seperti (list, tuple, string, dict, set) atau objek yang dapat diiterasi lainnya

"""  Note untuk kasus ini for --> Di python int tidak dapat diiterasi menggunakan Loop for dalam konteks ini. Kamu bisa menggunakan while! """