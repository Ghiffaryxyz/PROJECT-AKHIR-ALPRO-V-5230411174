import sqlite3

# Membuat koneksi ke database atau membuat database baru jika belum ada
fauna = sqlite3.connect('database_fauna.db')
kursor = fauna.cursor()

# Menjalankan query SELECT dengan ORDER BY
kursor.execute("SELECT * FROM FAUNA ORDER BY thn_ditemukan ASC") #ASC|DESC
baris_tabel = kursor.fetchall()

print("Data Pegawai:")
print("-"*105)
print("{:<10}{:<20}{:<20}{:<20}{:<20}{:<20}".format("id_fauna","nama_fauna","jenis","asal","jml_skrng","thn_ditemukan"))
print("-"*105)
#tampilkan data sesuai format dng perulangan
for fun in baris_tabel:
    print("{:<10}{:<20}{:<20}{:<20}{:<20}{:<20}".format(fun[0],fun[1],fun[2],fun[3],fun[4],fun[5]))
fauna.close()