import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle('Фокус со словами')
        self.btn = QPushButton('->', self)
        self.btn.resize(20, 20)
        self.btn.move(140, 140)
        self.word_input_1 = QLineEdit(self)
        self.word_input_1.move(5, 140)
        self.word_input_2 = QLineEdit(self)
        self.word_input_2.move(162, 140)
        self.btn.clicked.connect(self.redirection)

    def redirection(self):
        if self.btn.text() == '->':
            self.btn.setText('<-')
            word = self.word_input_1.text()
            self.word_input_2.setText(word)
            self.word_input_1.setText('')
        elif self.btn.text() == '<-':
            word = self.word_input_2.text()
            self.word_input_1.setText(word)
            self.word_input_2.setText('')
            self.btn.setText('->')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())