txt = 'Hello World'

jumlah_karakter = len(txt)
print(jumlah_karakter)  # Output: 11

karakter_terakhir = txt[-1]
print(karakter_terakhir)  # Output: 'd'

potongan = txt[2:5]
print(potongan)  # Output: 'llo'

tanpa_spasi = txt.replace(" ", "")
print(tanpa_spasi)  # Output: 'HelloWorld'

huruf_besar = txt.upper()
print(huruf_besar)  # Output: 'HELLO WORLD'

huruf_kecil = txt.lower()
print(huruf_kecil)  # Output: 'hello world'

ganti_h_j = txt.replace("H", "J")
print(ganti_h_j)  # Output: 'Jello World'

