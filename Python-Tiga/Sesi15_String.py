# String atau str, Merupakan Kumpulan Data char Atau Karakter Yang Tersimpan Secara Urut (text sequence). String Di Python Mengadopsi Standar Unicode Dengan default encoding UTF-8

# 1. Pengenalan string
# Python Mendesai Type Data string Dalam Bentuk Yang Sangat Sederhana Dan Mudah Digunakan
# Untuk membuat string Cukup Mudah, Ketik text dan apit menggunakan tanda petik satu atau dua

a_str = "Manusia Hawa" # --> Inisialisasi variabel yang menyimpan data string
print(a_str)           # --> Mencetak variabel, maka akan mencetak pesan Manusia Hawa
print(type(a_str))     # --> Mencetak variabel dan mengecek tipe datanya, maka akan mencetak pesan <class 'str'>

a_str = 'Manusia Adam' # --> Inisialisasi variabel yang menyimpan data string
print(a_str)           # --> Mencetak variabel, maka akan mecetak pesan Manusia Adam


# Multiline string
# Untuk string lebih dari satu baris 

# Menggunakan Karakter \n
a_str = "Manusia rasa\nbuaya" # --> Inisialisasi variabel yang menyimpan data string
print(a_str)                  # --> Mencetak variabel, maka akan mencetak pesan manusia rasa buaya

# Menggunakan """ Atau ''' Untuk Mengapit Text
a_str = """
Manusia
Rusa
"""          # --> Inisialisasi variabel yang menyimpan data string
print(a_str) # --> Mencetak variabel, maka akan mencetak pesan Manusia Rusa

a_str = '''
Manusia
Buaya
'''          # --> Inisialisasi variabel yang menyimpan data string

print(a_str) # --> Mencetak variabel, maka akan mencetak pesan Manusia Buaya

# Teknik Penulisan string Menggunakan Tanda """ atau ''' Selain Digunakan Untuk Membuat Multiline string, Juga Dapat Dimanfaatkan Untuk Hal Pembuatan docsting


# Escape character
# Python Mengenal escape character Umum Yang Ada Di Banyak Bahasa Pemrograman, Contoh Seperti \" Digunakan Untuk Menulis karakter " (Pada string Yangdibuat Menggunakan Literal "") Dan Penambahan karakter \ Adalah Penting Agar Karakter " Terdeteksi Sebagai Penanda string
# Sebagai Contoh Statement Berikut Adalah Ekuivalen

a_str = 'aku basah "dek"' # --> Inisialisasi variabel yang menyimpan data string
print(a_str)              # --> Mencetak variabel, maka akan mencetak pesan aku basah "dek"

a_str = "aku \"basah\" dek" # --> Inisialisasi variabel yang menyimpan data string
print(a_str)                # --> mencetak variabel, maka akan mencetak pesan aku "basah" dek



print("------")

# 2. String special characters
# Di Atas Telah Dicontohkan Bagaimana Cara Menulis Karakter Newline Atau Baris Baru Menggunakan \n, Dan Karakter Petik Dua Menggunakan \". Dua Karakter Tersebut Adalah Contoh Dari Special characters.

# Python Mengenal banyak Spesial karakter Yang Masing-masing Memiliki Kegunaan Yang Cukup Spesifik.

