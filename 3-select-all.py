import sqlite3
#koneksi database
fauna=sqlite3.connect('database_fauna.db')
#buat variabel cursos untuk menampung data
cur=fauna.cursor()
#select data from table
# bintang(*) artinya menyeleksi semua isian table
cur.execute("SELECT * FROM FAUNA")
data_fauna=cur.fetchall()

#menampilkan data dalam format table
if len(data_fauna)>0:
    print("{:<10}{:<20}{:<20}{:<20}{:<20}{:<20}".format("id_fauna","nama_fauna","jenis","asal","jml_skrng","thn_ditemukan"))
    print("="*105)
    for fun in data_fauna:
        print("{:<10}{:<20}{:<20}{:<20}{:<20}{:<20}".format(fun[0],fun[1],fun[2],fun[3],fun[4],fun[5]))
fauna.close()