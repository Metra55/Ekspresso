import sqlite3

from PyQt5.QtWidgets import (
    QDialog,
    QWidget,
)

from .red_cofei import Redact


class IzmCoffe(Redact, QDialog):
    def __init__(self, parent: QWidget,naz, stepen, molot, vkus,price,obiom) -> None:

        super().__init__(parent)
        self.setupUi(self)
        self._init_ui()
        self.setWindowTitle("Редактирование записи")
        self._size: tuple[int, int] | None = None
        self.nazvanie_edit.setText(naz)
        self.stepen_obj_edit.setText(stepen)
        self.molot_edit.setText(molot)
        self.opisanie_edit.setText(vkus)
        self.price_edit.setText(price)
        self.obiom_edit.setText(obiom)


    def _init_ui(self) -> None:

        self.pushButton.clicked.connect(self._on_accepted)

    def _on_accepted(self) -> None:
        self.naz = self.nazvanie_edit.text()
        self.stepen_obj = self.stepen_obj_edit.text()
        self.molot = self.molot_edit.text()
        self.opis = self.opisanie_edit.text()
        self.price = self.price_edit.text()
        self.obiom = self.obiom_edit.text()

        if not self.naz or not self.stepen_obj or not self.molot or not self.opis or not self.price or not self.obiom:
            self.label_5.setText("Неверно Заполненная форма")
        else:
            self.close()


    def get_image_size(self) -> tuple[int, int] | None:
        self.exec()
        return (self.naz, self.stepen_obj, self.molot, self.opis, self.price, self.obiom)
