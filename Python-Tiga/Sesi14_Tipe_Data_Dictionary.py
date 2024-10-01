# Salah Satu Tipe Data mapping di Python, Yaitu dictionary

# 1. Pengenalan dictionary
# Dictionary atau dict Merupakan Tipe Data Kolektif berbentuk key-value

bio = {
    "id":2,
    "name":"Laura",
    "awas":["Setan"],
    "perempuan":True
}                    # --> Inisialisasi variabel yang menyimpan data dict, berisi 4 key-value

# Literal dict Tertulis Dengan Menggunakan {}, Mirip Seperti Tipe Data Set, Hanya Saja bedanya Pada Tipe dictionary Isinya Berbentuk keu-value

print(bio)           # --> Mencetak variabel, mak aakan mencetak pesan {'id': 2, 'name': 'Laura', 'awas': ['Setan'], 'perempuan': True}
print(len(bio))      # -- Mencetak variabel atau panjang jumlah elemen dari variabel bio, maka akan mencetak pesan 4

# Peringatan! Pengaksesan Item Menggunakan key yang Tidak Dikenali Akan Menghasilkan Error

""" bio = {
    "id":2,
    "name":"Laura",
    "perempuan":True
}                    

print(bio["umur"]) """


# Urutam Item dictionary
# Mulai Dari Python Versi 3.7, Item dictionary Tersimpan Secara Urut Dan Artinya Urutan Item dict Akan Selalu Sesuai Dengan bagaimana Inisialisasi Awalnya.


# Pretty print dictionary
# Ada Tips Agar Data dict yang Di-Print Console Muncul Dengan Tampilan Yang Lebih Mudah Dibaca (lebih kompleks)

# Menggunakan pprint.pprint()
import pprint        # --> Memanggil pprint

bio = {
    "id":2,
    "name":"Laura",
    "awas":["Setan"],
    "perempuan":True
}                    # --> Inisialisasi variabel yang menyimpan data dict, berisi 4 key-value

pprint.pprint(bio)   # --> Mencetak variabel menggunakan pprint, maka akan mencetak pesan {'awas': ['Setan'], 'id': 2, 'name': 'Laura', 'perempuan': True}

# Menggunakan json.dumps()
import json                      # --> Memanggil json
bio = {
    "id":2,
    "name":"Laura",
    "awas":["Setan"],
    "perempuan":True
}                                # --> Inisialisasi variabel yang menyimpan data dict, berisi 4 key-value

print(json.dumps(bio, indent=4)) # --> Mencetak variabel dengan mengkonversi variabel bio menjadi format JSON (JavaScript Object Notation) dengan identasi 4 spasi



print("------")

# 2. Inisialisasi dictionary
# Pembuatan Data dict Bisa Dilakukan Menggunakan beberapa Cara

# Menggunakan {}
bio = {
    "id":2,
    "name":"Laura",
    "awas":["Setan"],
    "perempuan":True
}                                # --> Inisialisasi variabel yang menyimpan data dict, berisi 4 key-value

print(json.dumps(bio, indent=4)) # --> Mencetak variabel dengan mengkonversi variabel bio menjadi format JSON (JavaScript Object Notation) dengan identasi 4 spasi

# Menggunakan Fungsi dict() Dengan Isi Argumen key-value
bio = dict(
    set="id",
    nama="Laura",
    awas="Setan",
    perempuan=True
)                                # --> Inisialisasi variabel yang menyimpan data dict, berisi 4 key-value

print(json.dumps(bio, indent=4)) # --> Mencetak variabel dengan mengkonversi variabel bio menjadi format JSON (JavaScript Object Notation) dengan identasi 4 spasi

# Menggunakan Fungsi dict() Dengan Isi list tuple
bio = dict([
    ("set", "id"),
    ("name", "Laura"),
    ("awas", ["Setan"]),
    ("perempuan", True)
])

print(json.dumps(bio, indent=4)) # --> Mencetak variabel dengan mengkonversi variabel bio menjadi format JSON (JavaScript Object Notation) dengan identasi 4 spasi


# Sedangkan Untuk Membuat dict Tanpa Item Atau Kosong, Bisa Hanya Menggunakan {} atau dict()

bio = {}      # --> Inisialisasi variabel yang menyimpan data dict kosong
print(bio)    # --> Mencetak variabel, maka akan mencetak pesan {}

bio = dict()  # --> Inisialisasi variabel yang menyimpan data dict kosong
print(bio)    # --> Mencetak variabel, maka akan mencetaj pesan {}



print("------")

# 3. Perulangan item dictionary
# Gunakan Keyword for dan in Untuk mengiterasi Data Tiap key Milik dict Dan Dari key Tersebut Kemudian Akses valuenya

bio = {
    "id":2,
    "name":("Laura", "Natasia"),
    "awas":"Setan",
    "perempuan":True
}                                # --> Inisialisasi variabel yang menyimpan data dict, berisi 4 key-value

for key in bio:                  # --> Melakukan perulangan atau loop, yang mengiterasi melalui setiap keys vriabel bio (vairbel key, digunakan untuk menyimpan keys selama iterasi)
    print(key, bio[key])         # --> Mencetak variebl selama iterasi, akan mencetak keys dan values pada setiap pasangan dalam variabel bio 



print("------")

# 4. Nestes dictionary
# Dictionary becabang atau bersarang Bisa Dimanfaatkan Untuk menyimpan data Dengan Struktur yang Kopleks, Misalnya dict yang Salah Satu value itemnya Adalah list
# Penerapannya Tidak Berbeda Seperti Inisialisasi dict Pada Umumnya, Langsung Tulis Saja dict Sebagai Child dictionary

