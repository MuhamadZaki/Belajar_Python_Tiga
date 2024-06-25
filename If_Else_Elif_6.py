""" Percabangan if-else-elif  """
# Proses penentuan keputusan atau kita sebut dengan conditional statement

# Contoh Dalam Penentuan Nilai pada Siswa (Program)

while True: # Loop ini akan terus berjalan sampai pernyataan break
    try:    # Menjalankan kode di dalam

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
            continue

        #break # Menghentikan looping jika input valid

        print(f"Hasil Nilai : {hasil}") # Dinamis, jika user memasukan nilai berupa angka (karena string di konversi menjadi integer)
        
    except ValueError: # Pesan kesalahan
        print("Input tidak benar! Masukan angka!")