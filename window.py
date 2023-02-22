import sqlite3
from PyQt5.QtWidgets import (
    QMainWindow, QTableWidgetItem, QPushButton, QDialog
)

from window_ui import Ui_MainWindow
from windows.dob_cof import DobCof
from izm_film.izmn_cof import IzmCoffe


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)
        self._init_ui()

    def _init_ui(self):
        self.con = sqlite3.connect("coffee.sqlite")
        self.pushButton.clicked.connect(self.dobavit_film_func)
        self.pushButton_2.clicked.connect(self.izmenit_film_func)
        self.otrisovka()

    def otrisovka(self):
        self.cur = self.con.cursor()

        result = self.cur.execute(f"""
                        SELECT title,stepen_objarki, molotiy_v_zernah,vkusno,price,obiyom_upakovki FROM coffes                            """).fetchall()

        self.tableWidget.setRowCount(len(result))
        self.tableWidget.setColumnCount(len(result[0]))

        self.tableWidget.setHorizontalHeaderLabels(
            ['Название', 'степень обжарки', 'молотый/в зернах', 'описание вкуса', 'цена', ' объем упаковки'])

        for i, elem in enumerate(result):
            for j, value in enumerate(elem):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(value)))

    def dobavit_film_func(self):

        dialog = DobCof(self)

        try:
            self.naz, self.stepen_obj, self.molot, self.opis, self.price, self.obiom = dialog.get_image_size()
            self.cur.execute(f"""
                            INSERT INTO coffes (title,stepen_objarki,molotiy_v_zernah,vkusno,price,obiyom_upakovki) VALUES ('{self.naz}', '{self.stepen_obj}', '{self.molot}', '{self.opis}', '{self.price}', '{self.obiom}')
                                """)
            self.con.commit()
            self.otrisovka()
        except BaseException:
            pass

    def izmenit_film_func(self):

        liste = []
        for i in range(0, 6):
            liste.append(self.tableWidget.item(self.tableWidget.currentRow(), i).text())


        dialog = IzmCoffe(self, liste[0], liste[1], liste[2], liste[3], liste[4], liste[5])

        try:
            self.naz, self.stepen_obj, self.molot, self.opis, self.price, self.obiom = dialog.get_image_size()

            self.cur.execute(         f"""UPDATE coffes SET title='{self.naz}', stepen_objarki='{self.stepen_obj}', molotiy_v_zernah='{self.molot}', vkusno='{self.opis}', price='{self.price}', obiyom_upakovki='{self.obiom}'
                            WHERE title='{liste[0]}' AND stepen_objarki='{liste[1]}'  AND molotiy_v_zernah='{liste[2]}' AND vkusno='{liste[3]}'  AND price='{liste[4]}' AND obiyom_upakovki='{liste[5]}' """)

            self.con.commit()
            self.otrisovka()
        except BaseException:
            pass
