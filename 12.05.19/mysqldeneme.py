from mysql.connector import MySQLConnection
from mysql.connector.errors import DatabaseError, ProgrammingError

config={
    'host':'localhost',
    'database':'siparis',
    'user':'root',
    'password':''
}
connection = MySQLConnection(**config)
cur = connection.cursor()

cur.execute("CREATE DATABASE IF NOT EXISTS siparis")
cur.execute("CREATE TABLE IF NOT EXISTS siparis (ad TEXT,soyad TEXT , iletisim_no INT , siparis TEXT ,guncelleme REAL) ")
cur.execute("INSERT INTO siparis(ad,soyad,iletisim_no,siparis) Values('selim','çağlar',26,'ayran')")
