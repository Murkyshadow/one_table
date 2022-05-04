from DataBase import DataBase
from PyQt5 import uic
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QApplication, QTableWidget, QTableWidgetItem
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.db = DataBase()
        self.ui = uic.loadUi("forms/shop_table.ui", self)
        self.window().setWindowTitle("Магазин")
        self.ui.btn_add_name.clicked.connect(self.add_shop)
        self.ui.btn_save_data.clicked.connect(self.save_shop_in_db)
        self.ui.btn_add_product.clicked.connect(self.add_product)
        self.ui.btn_save_data_product.clicked.connect(self.save_product_in_db)

        # print(self.db.get_shop())
        self.id_shop.addItems(self.db.get_shop())

        self.draw_shop()
        self.draw_product()

    def add_product(self):
        name = self.ui.name_2.text()
        cost = self.ui.cost.value()
        id = self.id_shop.currentText()
        id = id.split(' ')[0]
        if name != '':
            self.db.add_in_product(name, cost, id)
            self.update_draw_product()

    def update_combobox(self):
        self.id_shop.clear()
        self.id_shop.addItems(self.db.get_shop())

    def save_product_in_db(self):
        self.table = self.ui.table_product
        data = self.get_from_table()
        for string in data:
            if string[1]!='':
                self.db.update_product(string[0], string[1], string[2], string[3])
            else:
                self.db.delete_from_product(string[0])
        self.update_draw_product()

    def save_shop_in_db(self):
        self.table = self.ui.table_shop
        data = self.get_from_table()
        for string in data:
            if string[1]!='':
                self.db.update_shop(string[0], string[1], string[2])
            else:
                self.db.delete_from_shop(string[0])
        self.update_draw_shop()
        self.update_draw_product()
        self.update_combobox()


    def add_shop(self):
        name = self.ui.name.text()
        address = self.ui.address.text()
        if name!= '' and address != '':
            self.db.add_in_shop(name, address)
            self.update_draw_shop()
        self.update_combobox()

    def update_draw_shop(self):
        self.table = self.ui.table_shop
        self.table.clear()
        self.draw_shop()

    def update_draw_product(self):
        self.table = self.ui.table_product
        self.table.clear()
        self.draw_product()

    def draw_shop(self):
        self.table = self.ui.table_shop
        rec = self.db.get_from_shop()
        self.table.setColumnCount(3)
        i = 0
        for shop in rec:
            x = 0
            self.table.setRowCount(i+1)
            for field in shop:
                item = QTableWidgetItem()
                item.setText(str(field))
                if x==0: # для id делаем некликабельные ячейки
                    item.setFlags(Qt.ItemIsEnabled)
                self.table.setItem(i, x, item)
                x += 1
            i += 1

    def draw_product(self):
        self.table = self.ui.table_product
        rec = self.db.get_from_product()
        self.table.setColumnCount(4)
        i = 0
        for shop in rec:
            x = 0
            self.table.setRowCount(i+1)
            for field in shop:
                item = QTableWidgetItem()
                item.setText(str(field))
                if x==0: # для id делаем некликабельные (чтобы их нельзя было переписать) ячейки
                    item.setFlags(Qt.ItemIsEnabled)
                self.table.setItem(i, x, item)
                x += 1
            i += 1

    def get_from_table(self):
        rows = self.table.rowCount()
        cols = self.table.columnCount()
        data = []
        for row in range(rows):
            tmp = []
            for col in range(cols):
                try:
                    tmp.append(self.table.item(row, col).text())
                except:
                    tmp.append('No data')
            data.append(tmp)
        return data


if __name__ == '__main__':
    qapp = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    # window.draw_shop()

    qapp.exec()