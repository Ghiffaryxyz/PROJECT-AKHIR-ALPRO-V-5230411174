import sqlite3

# Membuat koneksi ke database atau membuat database baru jika belum ada
conn = sqlite3.connect('database_fauna.db')
cursor = conn.cursor()

# Menjalankan query SUM
cursor.execute("SELECT SUM(jml_skrng) FROM FAUNA")
jml_skrng = cursor.fetchone()[0]

print(f"Total Populasi hewan langka saat ini: {jml_skrng}")

# Menutup koneksi
conn.close()
