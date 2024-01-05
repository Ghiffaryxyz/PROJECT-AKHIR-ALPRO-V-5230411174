import sqlite3
fauna=sqlite3.connect('database_fauna.db')
fauna.execute('''
                CREATE TABLE FAUNA(
                    id_fauna INTEGER PRIMARY KEY AUTOINCREMENT,
                    nama_fauna VARCHAR(50),
                    jenis VARCHAR(50),
                    asal VARCHAR(50),
                    jml_skrng INT(10),
                    thn_ditemukan INT(10)
                )
                ''')
fauna.close()