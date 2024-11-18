import sqlite3
con = sqlite3.connect("DB1.db")
cur = con.cursor()
a=input('Masukan Nomor: ')
b=input('Masukan Nama: ')
cur.execute("""
         INSERT INTO TBL1 VALUES
            ({},'{}')
""".format(a,b))
con.commit()