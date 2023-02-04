from PyQt5.QtWidgets import QMainWindow, QApplication, QInputDialog, QPushButton
from PyQt5.QtGui import QPalette, QBrush, QPixmap
import sys
import functions

with open('map.png', 'wb') as file:
    file.write(functions.get_img().content)


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.UI()

    def UI(self):
        self.setGeometry(0, 0, 600, 450)
        self.setWindowTitle('Яндекс Карты')

        self.palette = QPalette()

        self.palette.setBrush(QPalette.Background, QBrush(QPixmap('./map.png')))
        self.setPalette(self.palette)

        but_get_coords = QPushButton('Введите координаты', self)
        but_get_coords.resize(120, 30)
        but_get_coords.move(10, 10)
        but_get_coords.clicked.connect(self.change_coords)

    def change_coords(self):
        try:
            text = QInputDialog.getText(self, '', 'Введите координаты')[0]
            coords = list(map(float, text.split()))
            with open('map.png', 'wb') as file:
                file.write(functions.get_img(scale=[0.1, 0.1], coords=coords).content)
            self.palette.setBrush(QPalette.Background, QBrush(QPixmap('./map.png')))
            self.setPalette(self.palette)
        except:
            print('ошибка')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Example()
    window.show()
    sys.exit(app.exec())
