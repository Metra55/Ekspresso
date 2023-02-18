import sqlite3

from PyQt5.QtWidgets import (
    QDialog,
    QWidget,
)

from .image_size_dialog_ui import Ui_dob_film_dialog


class DobFilm(Ui_dob_film_dialog, QDialog):
    def __init__(self, parent: QWidget) -> None:
        super().__init__(parent)
        self.setupUi(self)
        self._init_ui()
        self.setWindowTitle("Добавить фильм")
        self._size: tuple[int, int] | None = None

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
