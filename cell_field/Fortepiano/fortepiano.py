import sys
import keyboard
from PyQt5 import QtCore, QtMultimedia
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton
from PyQt5 import QtGui

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(100, 100, 600, 600)
        self.setWindowTitle('Фортепиано')
        self.banjo('data/banjo_E4_very-long_forte_normal.mp3')
        self.guitar('data/guitar_A2_very-long_forte_normal.mp3')
        self.mandolin('data/mandolin_D4_very-long_piano_tremolo.mp3')
        self.saxophone('data/saxophone_Gs4_15_fortissimo_normal.mp3')
        self.violin('data/violin_Cs4_1_forte_con-sord.mp3')

        self.label = QLabel(self)
        self.label.setText('Fortepiano')
        font = QtGui.QFont()
        font.setFamily("Terminal")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.move(240, 50)
        self.label.resize(110, 25)
        self.label.setStyleSheet('background-color: #c9c9c5')

        self.label_2 = QLabel(self)
        self.label_2.move(200, 125)
        self.label_2.resize(180, 20)
        self.label_2.setText('Выберите инструмент:')
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet('background-color: #c9c9c5')

        self.label_3 = QLabel(self)
        self.label_3.move(190, 200)
        self.label_3.resize(100, 20)
        self.label_3.setText('Банжо (F1)')
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet('background-color: #c9c9c5')

        self.label_4 = QLabel(self)
        self.label_4.move(180, 250)
        self.label_4.resize(110, 20)
        self.label_4.setText('Гитара (F2)')
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet('background-color: #c9c9c5')

        self.label_5 = QLabel(self)
        self.label_5.move(150, 300)
        self.label_5.resize(140, 20)
        self.label_5.setText('Мандолина (F3)')
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet('background-color: #c9c9c5')

        self.label_6 = QLabel(self)
        self.label_6.move(160, 350)
        self.label_6.resize(130, 20)
        self.label_6.setText('Саксофон (F4)')
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet('background-color: #c9c9c5')

        self.label_6 = QLabel(self)
        self.label_6.move(170, 400)
        self.label_6.resize(120, 20)
        self.label_6.setText('Скрипка (F5)')
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet('background-color: #c9c9c5')

        self.button = QPushButton(self)
        self.button.move(300, 200)
        self.button.resize(100, 20)
        self.button.setText('Играть')
        self.button.clicked.connect(self.player.play)
        keyboard.add_hotkey("f1", self.player.play)

        self.button_2 = QPushButton(self)
        self.button_2.move(300, 250)
        self.button_2.resize(100, 20)
        self.button_2.setText('Играть')
        self.button_2.clicked.connect(self.player_2.play)
        keyboard.add_hotkey("f2", self.player_2.play)

        self.button_3 = QPushButton(self)
        self.button_3.move(300, 300)
        self.button_3.resize(100, 20)
        self.button_3.setText('Играть')
        self.button_3.clicked.connect(self.player_3.play)
        keyboard.add_hotkey("f3", self.player_3.play)

        self.button_4 = QPushButton(self)
        self.button_4.move(300, 350)
        self.button_4.resize(100, 20)
        self.button_4.setText('Играть')
        self.button_4.clicked.connect(self.player_4.play)
        keyboard.add_hotkey("f4", self.player_4.play)

        self.button_5 = QPushButton(self)
        self.button_5.move(300, 400)
        self.button_5.resize(100, 20)
        self.button_5.setText('Играть')
        self.button_5.clicked.connect(self.player_5.play)
        keyboard.add_hotkey("f5", self.player_5.play)

    def banjo(self, filename):
        media = QtCore.QUrl.fromLocalFile(filename)
        content = QtMultimedia.QMediaContent(media)
        self.player = QtMultimedia.QMediaPlayer()
        self.player.setMedia(content)

    def guitar(self, filename):
        media = QtCore.QUrl.fromLocalFile(filename)
        content = QtMultimedia.QMediaContent(media)
        self.player_2 = QtMultimedia.QMediaPlayer()
        self.player_2.setMedia(content)

    def mandolin(self, filename):
        media = QtCore.QUrl.fromLocalFile(filename)
        content = QtMultimedia.QMediaContent(media)
        self.player_3 = QtMultimedia.QMediaPlayer()
        self.player_3.setMedia(content)

    def saxophone(self, filename):
        media = QtCore.QUrl.fromLocalFile(filename)
        content = QtMultimedia.QMediaContent(media)
        self.player_4 = QtMultimedia.QMediaPlayer()
        self.player_4.setMedia(content)

    def violin(self, filename):
        media = QtCore.QUrl.fromLocalFile(filename)
        content = QtMultimedia.QMediaContent(media)
        self.player_5 = QtMultimedia.QMediaPlayer()
        self.player_5.setMedia(content)

app = QApplication(sys.argv)
ex = MainWindow()
ex.show()
sys.exit(app.exec_())