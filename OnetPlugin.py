from PyQt5 import QtWidgets, QtCore
from OnetWebService import OnetWebService
import sys
import pandas as pd
from numpy import random
from xml.etree import cElementTree as ET
from main_window import Ui_MainWindow

def Search(self):
    ui.questionTable.clear()
    skillList = []
    career = ui.searchField.text()
    row = careerList[careerList["Title"]==career]
    code = row["Code"].to_string(header=False, index=False)
    searchResults = onet_ws.call('mnm/careers/'+code+"/skills")
    count = 0
    total = 0
    introQuestion = random.randint(0,11)
    ui.questionTable.setItem(0,0,QtWidgets.QTableWidgetItem(questionDoc[0][introQuestion].text))
    questionSelection = [random.randint(0,11) for i in range(0,5)]
    try:
        for item in searchResults['group']:
            while total<5:
                for skill in item['element']:
                    skillList.append(skill['id'])
                    if count < 5:
                        for skill in questionDoc.findall('skill'):
                            if skill.find('title').get('id') == skillList[count]:
                                questions = skill.findall('element')
                                ui.questionTable.setItem(count+1,0, QtWidgets.QTableWidgetItem(questions[questionSelection[count]].text))
                    count += 1
                    total += 1
    except:
        for i in range (0,10):
            ui.questionTable.setItem(i,0,QtWidgets.QTableWidgetItem(questionDoc[0][i+1].text))
    ui.questionTable.resizeColumnsToContents()



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

    global questionDoc
    #questionDoc = ET.parse('questions')
    #for info in questionDoc.findall('.//skill/title'):

    #questionDoc = pd.read_xml('questions')
    #print(questionDoc)

    tree = ET.parse('questions')
    questionDoc = tree.getroot()
    #for child in root:
    #    print(child.tag, child.attrib)
    #for skill in questionDoc.findall('skill'):
    #    print(skill.find('title').get('id'))
    


    careerList = GetCareerList()
    completer = QtWidgets.QCompleter(careerList["Title"])
    completer.setCaseSensitivity(QtCore.Qt.CaseInsensitive)
    ui.searchField.setCompleter(completer)

    ui.searchButton.clicked.connect(Search)

    sys.exit(app.exec_())