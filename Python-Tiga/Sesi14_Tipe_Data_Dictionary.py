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

bio = {
    "id":2,
    "name":("Laura", "Natasia"),
    "awas":"Setan",
    "perempuan":True,

    "afiliasi":[
        {
            "ruko":"Zaki",
            "gerai":"Toko"
        },
        {
            "pedia":"Buah",
            "shope":"Hewan"
        },
    ]
}                                # --> Inisialisasi variabel yang menyimpan data dict, berisi key-value

print(bio["name"])               # --> Mencetak variabel, value dari keys "name" dan mencetak pesan ('Laura', 'Natasia')

for item in bio["afiliasi"]:                             # --> Melakukan perulangan atau loop, mengiterasi melalui list "afiliasi" 
    if "ruko" in item and "gerai" in item:               # --> Kondisi, memeriksa apakah keys "ruko", "gerai" ada dalam dict item, jika kedua kondisi benar atau terpenuhi maka akan mengeksekusi kode di dalamnya
        print("%s (%s)" % (item["ruko"], item["gerai"])) # --> Jika kondisi terpenuhi makan akan mengiterasi melalui setiap dict dalam list afiliasi dan mencetak value "ruko" dan "gerai", maka akan mencetak pesan Zaki (Toko)
    
# Pada Code Di Atas keys afiliasi Berisi List Object Dictionary

# Cara Mengakses value nested item dictionary
bio = {
    "id":2,
    "name":("Laura", "Natasia"),
    "awas":"Setan",
    "perempuan":True,

    "afiliasi":[
        {
            "ruko":"Zaki",
            "gerai":"Toko"
        },
        {
            "pedia":"Buah",
            "shope":"Hewan"
        },
    ]
}                                # --> Inisialisasi variabel yang menyimpan data dict, berisi key-value

values = bio["afiliasi"][0]["ruko"], bio["afiliasi"][0]["gerai"] # --> Mengambil value "name", "gerai" dari dict index pertama dalam list afiliasi dan tersimpam dalam variabel values
print("%s (%s)" % (values))                                      # --> Mencetak variabel, atau value dengan format string dan akan mencetak pesan Zaki (Toko)

values = bio["afiliasi"][1]["pedia"], bio["afiliasi"][1]["shope"] # --> Mengambil value "pedia", "shope" dari dict index kedua dalam list afiliasi dan tersimpan dalam variabel values
print("%s (%s)" % (values))                                       # --> Mencetak variabel, atau value dengan format string dan akan mencetak pesan Buah (Hewan)



print("------")

# 5. Dictionary mutability
# Item dict Adalah mutable, Perubahan value Item Bisa Dilakukan Langsung Menggunakan Operator assigment =

bio = {
    "id" : 2,
    "name" : "Laura",
    "perempuan" : True,
    "afiliasi": [
        {
            "satu": "Cantik",
            "dua": "Jelek"
        },
        {
            "tiga": "Aduhai",
            "empat": "Mempesona"
        }
    ]
}                                     # --> Inisialisasi variabel yang menyimpan data dict, berisi key-value

print(bio["afiliasi"][0]["dua"])      # --> Mencetak dan Mengambil value "dua" dari dict index pertama, dalam list afiliasi, maka akan mencetak pesan Jelek

bio["afiliasi"][0]["satu"] = "Aduhai" # --> Mengubah value "satu" dari dict index pertama, dalam list afiliasi

print(bio["afiliasi"][0]["satu"])     # --> Mencetak dan mengambil value baru "satu" setelah diubah, maka akan mencetak pesan Aduhai



print("------")

# Operasi Data dictionary

# Pengaksesan Item
# Pengaksesan Item dilakukan Lewat Notasi dict["keys"], Atau Bisa Digunakan Dengan Menggunakan Method get()

bio = {
    "id" : 2,
    "name" : "Laura",
    "perempuan" : True,
    "afiliasi":[
        {
            "satu" : "Lele",
            "dua"  : "Nila"
        },
        {
            "tiga" : "Gajah",
            "empat" : "Singa"
        }
    ]
}                               # --> Inisialisasi variabel yang menyimpan data dict, berisi key-value

print(bio["id"])                # --> Mencetak value dari keys "id", maka akan mencetak pesan 2
print(bio.get("name"))          # --> Mencetak value dari keys "name", maka akan mencetak pesan laura

# Mengubah Isi dictionary
# Mengubah value item dict Adalah Dengan Mengaksesnya Terlebih Dahulu, Kemudian Diikuti Operasi assignment

bio = {
    "id" : 4,
}                    # --> Inisialisasi variabel yang menyimpan data dict, berisi key-value

bio["plus"] = "Satu" # --> Menambahkan key-value baru ke dalam dict atau variabel bio

print(bio)           # --> Mencetak variabel, maka akan mencetak pesan {'id': 4, 'plus': 'Satu'}

# Selain Cara Di Atas Juga Bisa menggunakan Method update(), Tulis keys Dan value Baru yang Ingin Ditambahkan Sebagai Argument Method update() Dalam Bentuk dictionary

bio = {
    "id" : 4,
}                             # --> Inisialisasi variabel yang menyimpan data dict, berisi key-value

bio.update({"motor":"Vario"}) # --> Menambahkan key-value baru ke dalam dict variabel bio
print(bio)                    # --> Mencetak variabel, maka akan mencetak pesan {'id': 4, 'motor': 'Vario'}

# Menghapus Item dictionary
# Method pop() Digunakan Untuk Menghapus Item dictionary Berdasarkan keys

bio = {
    "id" : 3,
    "perempuan" : True
}                      # --> Inisialisasi variabel yang menyimpan data dict, berisi key-value

bio.pop("id")          # --> Menghapus keys "id" dari dict atau variabel bio
print(bio)             # --> Mencetak variabel, maka akan mencetak pesan {'perempuan': True}

# Keyword del Juga Bisa Difungsikan Untuk Operasi Yang Sama

bio = {
    "id": 2,
    "perempuan" : True
}                      # --> Inisialisasi variabel yang menyimpan data dict, berisi key-value

del bio["perempuan"]   # --> Menghapus keys "perempuan" dari dict atau variabel bio
print(bio)             # --> Mencetak variabe, maka akan mencetak pesan {'id': 2}


# Pengaksesan dictionary keys
# Method keys() Digunakan Untuk Mengakses Semua keys dictionary, Hasilnya Adalah Tipe Data view objects dict_keys Dan Dari Nilai Tersebut, Bungkus Menggunakan list() Untuk Mendapatkan Nilainya Dalam Bentuk list

bio = {
    "id": 2,
    "name": ("zaki", "Jeki"),
    "perempuan": True

}                               # --> Inisialisasi variabel yang menyimpan data dict, berisi key-value

print(list(bio.keys()))         # --> Mencetak semua keys yang ada dalam dict atau variabel bio, maka akan mencetak pesan dict_keys(['id', 'name', 'perempuan'])


# Pengaksesan dictionary values
# Method values() Digunakan Untuk Mengakses Semua value dict, Hasilnya Adalah Tipe Data view objects dict_values Dan Gunakan Fungsi list() Untuk Mengonversinya Ke Bentuk list

bi0 = {
    "id": 4,
    "name": "Zaki",
    "perempuan": False
}                               # --> Inisialisasi variabel yang menyimpan data dict, berisi key-value

print(list(bio.values()))       # --> Mencetak semua values yang ada dalam dict atau variabel bio, maka akan mencetak pesan [2, ('zaki', 'Jeki'), True]


# Method items() dictionary
# Digunakan Untuk Mengakses Semua item dict, Nilai Baliknya bertipe view objects dict_items Yang Strukturnya Cukup Mirip Seperti list Berisi tuple Dan Untuk Mengonversinya Ke Bentuk list, Gunakan Fungsi list()

bio = {
    "id": 3,
    "name": ("Ichigo", "Naruto"),
    "perempuan": False
}                               # --> Inisialisasi variabel yang menyimpan data dict, berisi key-value

print(list(bio.items()))        # --> Mencetak semua key-value yang ada dalam dict atau variabel bio, maka akan mencetak pesan [('id', 3), ('name', ('Ichigo', 'Naruto')), ('perempuan', False)]


# copy dictionary
# Method copy() Digunakan Untuk Meng-copy dictionary Dan Hasilnya Data dict Baru

bio = {
    "id": 3,
    "name": "Zaki",
    "perempuan": False
}                        # --> Inisialisasi variabel yang menyimpan data dict, berisi key-value

profil = bio.copy()      # --> Membuat salinan dari dict atau variabel bio dan tersimpan pada variabel profil
print(profil)            # --> Mencetak variabel, maka akan mencetak pesan {'id': 3, 'name': 'Zaki', 'perempuan': False}

# Operasi copy Disini Jenisnya Adalah shallow copy


# Mengosongkan Isi dictionary
# Method clear() Berguna Untuk Menghapus isi dictionary

bio = {
    "id": 3,
    "name": "Zaki",
    "perempuan": False
}                        # --> Inisialisasi variabel yang menyimpan data dict, berisi key-value

bio.clear()              # --> Mengosongkan atau menghapus isi dari dict atau variabel bio
print(bio)               # --> mencetak variabel, maka akan mencetak pesan {}