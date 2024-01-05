import sqlite3
fauna=sqlite3.connect('database_fauna.db')
#SELECT ALL DATA PEGAWAI
kursor=fauna.cursor()
#mengambil semua data dalam tabel dan tampilkan
kursor.execute("SELECT*FROM FAUNA WHERE jml_skrng <=1000")
#tampilkan dalam bentuk baris
baris_tabel=kursor.fetchall()
#membuat format tabel dengan method format()
print("data fauna 2023")
print("="*105)
print("{:<10}{:<20}{:<20}{:<20}{:<20}{:<20}".format("id_fauna","nama_fauna","jenis","asal","jml_skrng","thn_ditemukan"))
print("-"*105)
#tampilkan data sesuai format dng perulangan
for fun in baris_tabel:
    print("{:<10}{:<20}{:<20}{:<20}{:<20}{:<20}".format(fun[0],fun[1],fun[2],fun[3],fun[4],fun[5]))
fauna.close()