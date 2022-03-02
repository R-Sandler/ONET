from PyQt5 import QtCore, QtWidgets

class Ui_MainWindow(QtWidgets.QMainWindow):
    import sys
    def __init__(self, parent=None):
        super(Ui_MainWindow, self).__init__(parent=parent)
        self.setupUi(self)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowTitle("O*NET Search")
        self.centralWidget = QtWidgets.QWidget()

        self.grid = QtWidgets.QGridLayout()
        self.grid.setColumnMinimumWidth(0,400)

        self.searchField = QtWidgets.QLineEdit(self.centralWidget)
        self.searchField.setObjectName("searchField")
        self.grid.addWidget(self.searchField,0,0)

        self.searchButton = QtWidgets.QPushButton(self.centralWidget)
        self.searchButton.setDefault(False)
        self.searchButton.setFlat(False)
        self.searchButton.setObjectName("searchButton")
        self.searchButton.setText("Search")
        self.searchButton.setToolTip("This button searches the career list for the input career")
        self.grid.addWidget(self.searchButton,0,1)

        self.centralWidget.setLayout(self.grid)
        MainWindow.setCentralWidget(self.centralWidget)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)