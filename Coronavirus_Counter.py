from PyQt5 import QtCore, QtGui, QtWidgets
import urllib.request
from bs4 import BeautifulSoup
from urllib.request import Request

url = Request("https://www.worldometers.info/coronavirus/#countries", headers={'User-Agent': 'Mozilla/5.0'})
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'lxml')
count_list = soup.find_all(class_='maincounter-number')
count_list_items = []
for i in count_list:
    count_list_items.append(i.get_text())

Total_cases = count_list_items[0]  # No of Total Cases
Total_deaths = count_list_items[1]  # No of Total Deaths
Total_Recovered = count_list_items[2]  # No of Recovered


class Ui_MainWindow(object):
    def Update(self):
        self.Cases.setText(Total_cases)
        self.Deaths.setText(Total_deaths)
        self.Recovered.setText(Total_Recovered)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(496, 600)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(-10, -200, 611, 631))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("background_1.jpg"))
        self.label.setScaledContents(False)
        self.label.setObjectName("label")

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(-10, 230, 511, 361))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)

        self.label_2.setFont(font)
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("background_2.jpg"))
        self.label_2.setObjectName("label_2")

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(50, 270, 121, 31))
        self.label_3.setObjectName("label_3")

        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(40, 330, 121, 31))
        self.label_4.setObjectName("label_4")

        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(60, 390, 161, 31))
        self.label_5.setObjectName("label_5")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(180, 480, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setDefault(False)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.Update)

        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(170, 230, 55, 16))
        self.label_6.setObjectName("label_6")

        self.Cases = QtWidgets.QLabel(self.centralwidget)
        self.Cases.setGeometry(QtCore.QRect(170, 270, 251, 37))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(80)
        self.Cases.setFont(font)
        self.Cases.setAutoFillBackground(True)
        self.Cases.setObjectName("Cases")
        self.Cases.setAlignment(QtCore.Qt.AlignCenter)

        self.Deaths = QtWidgets.QLabel(self.centralwidget)
        self.Deaths.setGeometry(QtCore.QRect(170, 330, 251, 37))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.Deaths.setFont(font)
        self.Deaths.setAutoFillBackground(True)
        self.Deaths.setObjectName("Deaths")
        self.Deaths.setAlignment(QtCore.Qt.AlignCenter)

        self.Recovered = QtWidgets.QLabel(self.centralwidget)
        self.Recovered.setGeometry(QtCore.QRect(170, 390, 251, 37))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(80)
        self.Recovered.setFont(font)
        self.Recovered.setAutoFillBackground(True)
        self.Recovered.setObjectName("Recovered")
        self.Recovered.setAlignment(QtCore.Qt.AlignCenter)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Coronavirus Counter"))
        self.label_3.setText(_translate("MainWindow",
                                        "<html><head/><body><p><span style=\" font-size:11pt; font-weight:600; color:#ffffff;\">Total Cases:</span></p></body></html>"))
        self.label_4.setText(_translate("MainWindow",
                                        "<html><head/><body><p><span style=\" font-size:11pt; font-weight:600; color:#ffffff;\">Total Deaths:</span></p></body></html>"))
        self.label_5.setText(_translate("MainWindow",
                                        "<html><head/><body><p><span style=\" font-size:11pt; font-weight:600; color:#ffffff;\">Recovered:</span></p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "UPDATE"))
        self.label_6.setText(_translate("MainWindow", "TextLabel"))
        self.Cases.setText(_translate("MainWindow",
                                      "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">Click Update</span></p></body></html>"))
        self.Deaths.setText(_translate("MainWindow",
                                       "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">Click Update</span></p></body></html>"))
        self.Recovered.setText(_translate("MainWindow",
                                          "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">Click Update</span></p></body></html>"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
