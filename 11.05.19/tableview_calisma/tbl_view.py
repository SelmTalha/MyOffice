from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import uic
import sys
import sqlite3

sql=sqlite3.connect("tbviewdeneme.db")
cursor=sql.cursor()
tb_ui="table_view.ui"
class BenimEkranim(QMainWindow):
    def __init__(self):
        super(BenimEkranim,self).__init__()
        uic.loadUi(tb_ui,self)
        self.setWindowTitle("Tbl_view deneme")
        self.liste=[]
        self.veritabanindan_oku()
        self.table_olustur()
        self.model=self.get_model()
        self.tableView.setModel(self.model)      
        self.model.setHorizontalHeaderLabels(['Ad','Soyad','Numara'])
        self.secbutton.clicked.connect(self.secili_degerleri_getir)
        self.tablo_doldur()

    def secili_degerleri_getir(self, ad, soyad, telefon):
        
        self.txtAd.setText(ad)
        self.txtSoyad.setText(soyad)
        self.txtTelefon.setText(telefon)
        
    def get_model(self):
        temp = QStandardItemModel()
        sql=sqlite3.connect("tbviewdeneme.db")
        cursor=sql.cursor()

        for kayit in cursor.fetchall():
            ad = QStandardItem(kayit['ad'])
            soyad = QStandardItem(kayit['soyad'])
            telefon = QStandardItem(kayit['telefon'])
            temp.appendRow([ad, soyad, telefon])
        return temp

    def table_olustur(self):
        cursor.execute("""CREATE TABLE IF NOT EXISTS adres_defteri (ad VARCHAR(50),soyad VARCHAR(50),telefon VARCHAR(20))""")
        # cursor.execute("""INSERT INTO adres_defteri VALUES('Selim','Çağlar',25) """)
        sql.commit()

    def veritabanindan_oku(self):
        pass

    def tablo_doldur(self):
        for kisi in self.liste:
            print(kisi['Ad'])
            
app=QApplication(sys.argv)
selim=BenimEkranim()
selim.show()
sys.exit(app.exec_())