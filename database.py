import sqlite3
import os

class kayit():  
    def __init__(self):  
        dizin_yol = os.path.dirname(os.path.abspath(__file__))
        self.db_yol = os.path.join(dizin_yol, 'database.db')
          

    

    def ac(self):
        self.conn = sqlite3.connect(self.db_yol)
        self.cursor = self.conn.cursor()

    def kapat(self):
        self.conn.close()
    
    def KullaniciEkle(self, ad, soyad, telno, eposta, sifre):
        try:
            self.ac()
            sql = "INSERT INTO kayit (ad, soyad, telno, eposta, sifre) VALUES (?, ?, ?, ?, ?)"
            self.cursor.execute(sql, (ad, soyad, telno, eposta, sifre,))
            self.conn.commit()
            return True
        except sqlite3.Error as e:
            print(f"Bir hata oluştu: {e.args[0]}")
            return False
        finally:
            self.kapat()
            
    def KullaniciGetir(self):
        try:
            self.ac()
            sql = "SELECT * FROM kayit ORDER BY id"
            self.cursor.execute(sql)
            veri = self.cursor.fetchall()
            return veri
        except sqlite3.Error as e:
            print(f"Bir hata oluştu: {e.args[0]}")
            return False
        finally:
            self.kapat()
            
    def TelefonEkle(self, marka, model, hafiza, garanti, sikayet):
        try:
            self.ac()
            sql = "INSERT INTO telefon (marka, model, hafiza, garanti, sikayet) VALUES (?, ?, ?, ?, ?)"
            self.cursor.execute(sql, (marka, model, hafiza, garanti, sikayet,))
            self.conn.commit()
            return True
        except sqlite3.Error as e:
            print(f"Bir hata oluştu: {e.args[0]}")
            return False
        finally:
            self.kapat()
    
    def Telefon(self):
        try:
            self.ac()
            sql = "SELECT * FROM telefon ORDER by id"
            self.cursor.execute(sql)
            veriler = self.cursor.fetchall()
            return veriler
        except sqlite3.Error as e:
            print(f"Bir hata oluştu: {e.args[0]}")
            return False
        finally:
            self.kapat()
            
    def telefon_sil(self, id):
        self.ac()
        self.cursor.execute("DELETE FROM telefon WHERE id=?",(id,))
        self.conn.commit()
        self.kapat()
        
    
    def ParcaEkle(self, parcaadi, parcafiyat, parcaadet):
        try:
            self.ac()
            sql = "INSERT INTO parca (parcaadi, parcafiyat, parcaadet) VALUES (?, ?, ?)"
            self.cursor.execute(sql, (parcaadi, parcafiyat, parcaadet,))
            self.conn.commit()
            return True
        except sqlite3.Error as e:
            print(f"Bir hata oluştu: {e.args[0]}")
            return False
        finally:
            self.kapat()
            
    def Parca(self):
        try:
            self.ac()
            sql = "SELECT * FROM parca ORDER by id"
            self.cursor.execute(sql)
            veriler = self.cursor.fetchall()
            return veriler
        except sqlite3.Error as e:
            print(f"Bir hata oluştu: {e.args[0]}")
            return False
        finally:
            self.kapat()

    def parca_sil(self, id):
        self.ac()
        self.cursor.execute("DELETE FROM parca WHERE id=?",(id,))
        self.conn.commit()
        self.kapat()
        
        
        
        
        
        
        
        
        
        
        
