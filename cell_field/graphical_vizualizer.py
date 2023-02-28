import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLabel, QLineEdit
from PyQt5 import QtGui
from pyqtgraph import PlotWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(100, 100, 950, 600)
        self.setWindowTitle('Graphical Visualizer')

        self.label = QLabel(self)
        self.label.setText('Graphical Visualizer')
        font = QtGui.QFont()
        font.setFamily("Terminal")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.move(400, 75)
        self.label.resize(220, 25)
        self.label.setStyleSheet('background-color: #c9c9c5')

        self.function_input = QLineEdit(self)
        self.function_input.move(510, 275)
        self.function_input.resize(340, 25)
        self.function_input.setPlaceholderText('Введите функцию')

        self.range_input = QLineEdit(self)
        self.range_input.move(510, 400)
        self.range_input.resize(340, 25)
        self.range_input.setPlaceholderText('Диапозон (2 целых числа через пробел)')

        self.button = QPushButton(self)
        self.button.move(635, 490)
        self.button.resize(100, 50)
        self.button.setText('Сгенерировать')
        self.button.clicked.connect(self.generate_graph)
        self.button.setStyleSheet("QPushButton{\n"
                                      "    border-radius: 10px;\n"
                                      "    background-color: #c9c9c5;\n"
                                      "    border: 2px solid #8f8f8d;\n"
                                      "    color: #000000;\n"
                                      "}\n"
                                      "\n"                    
                                      "QPushButton::hover{\n"
                                      "    border-radius: 10px;\n"
                                      "    background-color: #8f8f8d;\n"
                                      "    border: 2px solid #c9c9c5;\n"
                                      "    color: #c9c9c5;\n"
                                      "}\n"
                                      "\n"
                                      "QPushButton::pressed{\n"
                                      "    border-radius: 10px;\n"
                                      "    background-color: #c9c9c5;\n"
                                      "    color: #000000;\n"
                                      "}\n"
                                      "")

        self.coordinate_axis = PlotWidget(self)
        self.coordinate_axis.move(100, 150)
        self.coordinate_axis.resize(400, 400)

    def generate_graph(self):
        function = self.function_input.text()
        range_values = self.range_input.text()
        n1, n2 = map(int, range_values.split())
        self.coordinate_axis.clear()
        self.coordinate_axis.plot(
            [i for i in range(n1, n2)],
            [eval(function) for x in range(n1, n2)],
            pen='r'
        )


app = QApplication(sys.argv)
ex = MainWindow()
ex.show()
sys.exit(app.exec_())
