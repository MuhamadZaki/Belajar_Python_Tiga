# Keyword break Dan continue Sering Dipergunakan Dalam Perulangan Untuk Alterasi Flow Secara pPksa, Seperti Memberhentikan Perulangan Atau Memaksa Perulangan Untuk Lanjut Ke Iterasi Berikutnya

# 1. Keyword break
# Pengaplikasian break Biasanya Dikombinasikan Dengan Seleksi Kondisi
# Berisi Perulangan Yang Sifatnya Berjalan Terus-Menerus Tanpa Henti (Karena Menggunakan Nilai True Sebagai Kontrol)
# Perulangan Hanya Berhenti Jika Nilai input_konversi (Yang Didapat Dari Inputan User) Adalah Tidak Bisa Dibagi Dengan Angka 3

#while True:                                                            # --> Inisialisasi perulangan yang akan terus berjalan, selama kondisi True
    #input_konversi = int(input("Masukan angka yang habis dibagi 3: ")) # --> Meminta pengguna memasukan nilai sebagai string, lalu mengonversinya menjadi tipe data integer dan tersimpan pada variabel input_konversi

    #if input_konversi % 3 != 0:                                        # --> Kondisi, memeriksa apakah nilai input_konversi tidak habis dibagi 3 (sisa bagi bukan 0), jika kondisi terpenuhi maka akan mengeksekusi kode di dalamnya dan jika kondisi tidak terpenuhi maka akan melanjutkan ke blok kode berikutnya
        #break                                                          # --> Jika Kondisi benar atau terpenuhi, maka perulangan akan dihentikan dengan break

    #print("%d Habis dibagi 3" % (input_konversi))                      # --> Jika kondisi salah atau tidak terpenuhi, maka mencetak pesan 24 Habis dibagi 3 (jika pengguna menginput angka 24)


print("------")

# 2. Keyword continue
# Keyword continue Digunakan Untuk Memaksa Perulangan Lanjut Ke Iterasi Berikutnya (Seperti Proses Skip)

for index in range(10):        # --> Perulangan atau loop, sebanyak 10 kali (variabel index akan mengambil nilai 0 hingga 9)
    if index < 3 or index > 7: # --> Kondisi, memeriksa apakah nilai index kurang dari 3 atau nilai index lebih besar dari 7, jika kondisi terpenuhi maka akan mengeksekusi kode di dalamnya
        continue               # --> Jika kondisi benar atau terpenuhi (jika nilai index yang memenuhi kondisi ini 0,1,2,8,9), maka akan dilewati
    print(index)               # --> Jika kondisi salah atau tidak terpenuhi, maka akan mencetak pesan 3 4 5 6 7