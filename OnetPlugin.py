from PyQt5 import QtWidgets, QtCore
from OnetWebService import OnetWebService
#import keyword_search
import sys, json
import pandas as pd
from main_window import Ui_MainWindow

def Search(self):
    career = ui.searchField.text()
    row = careerList[careerList["Title"]==career]
    code = row["Code"].to_string(header=False, index=False)
    searchResults = onet_ws.call('mnm/careers/'+code+"/skills")
    print(searchResults)

def GetCareerList():
    careerDoc = onet_ws.call('mnm/careers/?sort=name&start=1&end=923')
    careerNames = []
    careerCodes = []
    for item in careerDoc['career']:
        careerNames.append(item['title'])
        careerCodes.append(item['code'])

    zipList = list(zip(careerNames, careerCodes))
    global careerList
    careerList = pd.DataFrame(zipList, columns = ["Title", "Code"])
    return careerList


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)

if __name__ == "__main__":

    sys.excepthook = except_hook
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()

    onet_ws = OnetWebService("harqen_ai", "2298huc")

    careerList = GetCareerList()
    completer = QtWidgets.QCompleter(careerList["Title"])
    completer.setCaseSensitivity(QtCore.Qt.CaseInsensitive)
    ui.searchField.setCompleter(completer)
    
    ui.searchButton.clicked.connect(Search)

    sys.exit(app.exec_())