import configparser
import sys

from PyQt5.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget

CONFIG = configparser.ConfigParser()
CONFIG.read("config.ini")


class App(QWidget):
    def __init__(self):
        super().__init__()
        self.title = "PyQt5 textbox - pythonspot.com"
        self.left = 10
        self.top = 10
        self.width = 400
        self.height = 140
        self.labels = []
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.layout = QVBoxLayout(self)

        for section in CONFIG.sections():
            label = QLabel()
            label.setText(section)
            self.layout.addWidget(label)
            self.labels.append(label)

        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
