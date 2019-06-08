#Buton yardımı ile veritabanına veri yollama ve bunları tableviewda görme
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import uic
import sys
from mysql.connector import MySQLConnection 

class SecomCalisma(QMainWindow):
    def __init__(self):
        super(SecomCalisma,self).__init__()
        uic.loadUi("arayuz.ui",self)
        self.config = {
            'user': 'root',
            'password': '',
            'database': 'secom',
            'host': '127.0.0.1'
        }
        self.setWindowTitle("Secom Calisma")
        self.database_olustur()
        self.tablo_olustur()
        self.model = self.get_model()
        self.tv.setModel(self.model)
        self.tv.clicked.connect(self.secildiginde)
        self.secili=None
        self.btnEkle.clicked.connect(self.veri_yolla)
        self.btnSil.clicked.connect(self.tablo_sil)

    def secildiginde(self, index: QModelIndex):
        row = index.row() #Satır
        column = index.column() #Sütun
        id = index.sibling(row, 0).data()
        self.secili = id
        ad = index.sibling(row, 1).data()
        soyad = index.sibling(row, 2).data()
        telefon = index.sibling(row, 3).data()
    
    def tablo_sil(self):
        if self.secili is not None:
            sql = 'DELETE FROM siparis WHERE id = {id}'.format(id=self.secili)
            connection = MySQLConnection(**self.config)
            cur = connection.cursor()
            cur.execute(sql)
            connection.commit()
            model = self.get_model()
            self.tv.setModel(model)
            self.secili = None

    def database_olustur(self):
        connection = MySQLConnection(**self.config)
        cur = connection.cursor()
        cur.execute('CREATE DATABASE IF NOT EXISTS secom_siparis;')

    def tablo_olustur(self):
        connection = MySQLConnection(**self.config)
        cur = connection.cursor()
        cur.execute("""CREATE TABLE IF NOT EXISTS siparis (id INT PRIMARY KEY AUTO_INCREMENT,
        ad VARCHAR(50),soyad VARCHAR(50),telefon VARCHAR(20));""")

    def veri_yolla(self):
        connection = MySQLConnection(**self.config)
        cur = connection.cursor()
        kayit = {
            'ad': self.txtAd.text(),
            'soyad': self.txtSoyad.text(),
            'telefon': self.txtTelefon.text(),
        }
        cur.execute("INSERT INTO siparis(ad,soyad,telefon) Values(%s,%s,%s)",
        (kayit['ad'],kayit['soyad'],kayit['telefon']))
        connection.commit()
        model = self.get_model()
        self.tv.setModel(model)
        
    def get_model(self):
        temp = QStandardItemModel()
        connection = MySQLConnection(**self.config)
        cur = connection.cursor(dictionary=True)
        cur.execute('SELECT id, ad, soyad, telefon FROM siparis;')

        for kayit in cur.fetchall():
            id = QStandardItem(str(kayit['id']))
            ad = QStandardItem(kayit['ad'])
            soyad = QStandardItem(kayit['soyad'])
            telefon = QStandardItem(kayit['telefon'])
            temp.appendRow([id,ad, soyad, telefon])

        return temp

app=QApplication(sys.argv)
selim=SecomCalisma()
selim.show()
sys.exit(app.exec_())