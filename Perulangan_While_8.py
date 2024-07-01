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
    print(angka) # Hasilnya adalah 5 4 3 2 1
    angka -= 1

print("----------")

# 3 While dengan break --> Untuk menghentikan loop
hitung = 0
while True:
    print(hitung) # Hasilnya adalah 0 1 2 3 4
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

# Masih ada ngaso dulu, capek tau! Tapi enak!


# Bonus untuk kamu
halal = 0
while halal < 100:
    hati = "I Love You"
    if halal < 2:  # Menggunakan kondisi dan tanpa kondisi pun bisa
        print(hati) # Hasilnya adalah I Love You 2x
    halal += 1 # Increment manual