
import sys
from PyQt5 import QtWidgets
from PyQt5.QtGui import QPixmap
import design
from yolo3image import yolo3


class MainApp(QtWidgets.QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pushButton.clicked.connect(self.update_label_object)

    def update_label_object(self):
        self.label.setText('Processing ...')
        image_path = \
            QtWidgets.QFileDialog.getOpenFileName(self, 'Choose Image to Open',
                                                  '.',
                                                  '*.png *.jpg *.bmp')
        print(type(image_path))  # <class 'tuple'>
        print(image_path[0])  # /home/my_name/Downloads/example.png
        print(image_path[1])  # *.png *.jpg *.bmp
        image_path = image_path[0]  # /home/my_name/Downloads/example.png

        yolo3(image_path)
        pixmap_image = QPixmap('result.jpg')
        self.label.setPixmap(pixmap_image)
        self.label.resize(pixmap_image.width(), pixmap_image.height())

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MainApp()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
