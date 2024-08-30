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


#for index in range(10):        # --> Perulangan atau loop, mengiterasi sebanyak 10 kali (variabel index akan mengambil nilai 0 hingga 9)
    #if index < 3 or index > 7: # --> Kondisi, memeriksa apakah nilai index kurang dari 3 atau nilai index lebih besar dari 7, jika salah satu kondisi terpenuhi maka akan mengeksekusi kode di dalamnya
        #continue               # --> Jika kondisi benar atau terpenuhi (jika nilai index yang memenuhi kondisi ini 0,1,2,8,9), maka akan dilewati
    #print(index)               # --> Jika kondisi salah atau tidak terpenuhi, maka akan mencetak pesan 3 4 5 6 7


print("------")

# 3. Label Perulangan
# Python Tidak Mengenal Konsep Perulangan Yang Memiliki Label
# Teknik Menamai Perulangan Dengan Label Umumnya Digunakan Untuk Mengontrol Flow Pada Perulangan Bercabang / Nested, Misalnya Untuk Menghentikan Perulangan Terluar Secara Paksa Ketika Suatu Kondisi Terpenuhi
# Di Python, Algoritma Seperti Ini Bisa Diterapkan Namun Menggunakan Tambahan Kode

input_konversi = int(input("Masukan nilai: ")) # --> Meminta pengguna memasukan nilai sebagai string, lalu mengonversinya menjadi tipe data integer dan tersimpan pada variabel input_konversi
lingkaranLuar = True                           # --> Inisialisasi variabel yang menyimpan data boolean, dengan nilai True

for index in range(input_konversi):            # --> Perulangan atau loop, mengiterasi sebanyak nilai yang dimasukan oleh pengguna (input_konvarsi) dan (variabel index akan mengambil nilai dari 0 hingga input_konveri -1)
    if not lingkaranLuar:                      # --> Kondisi, memeriksa apakah nilai lingkarLuar adalah False, Jika kondisi terpenuhi maka akan mengeksekusi kode di dalamnya dan jika kondisi tidak terpenuhi maka akan melanjutkan ke blok kode berikutnya
        break                                  # --> Jika kondisi benar atau terpenuhi, maka perulangan utama akan dihentikan dengan break

    for jidex in range(index + 1):             # --> Perulangan atau loop bersarang, mengitrasi sebanyak nilai index + 1
        print("*", end=" ")                    # --> Mencetak pesan karakter bintang dengan spasi sebagai pemisah (tanpa newline)

        if jidex >= 7:                         # --> Kondisi, memeriksa apakah nilai jidex lebih besar dari atau sama dengan 7, jika kondisi terpenuhi maka akan mengeksekusi kode di dalamnya
            lingkaranLuar = False              # --> Untuk mengakhiri perulangan atau loop, jika kondisi sebelumnya terpenuhi atau variabel lingkaranLuar diubah menjadi False
            break                              # --> Jika kondisi benar atau terpenuhi, maka perulangan atau loop terdalam dihentikan paksa
    print()                                    # --> Mencetak pesan newline (baris baru) setelah mencetak bintang sejumlah yang sesuai