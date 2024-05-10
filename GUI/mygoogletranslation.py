from PyQt5 import QtCore, QtGui, QtWidgets
import googletrans

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet("color: rgb(0, 0, 0);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 180, 801, 311))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.textEdit_ori = QtWidgets.QTextEdit(self.horizontalLayoutWidget)
        self.textEdit_ori.setObjectName("textEdit_ori")
        self.horizontalLayout.addWidget(self.textEdit_ori)
        self.transButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Leelawadee")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.transButton.setFont(font)
        self.transButton.setStyleSheet("color: rgb(166, 41, 255);")
        self.transButton.setObjectName("transButton")
        self.horizontalLayout.addWidget(self.transButton)
        self.textEdit_new = QtWidgets.QTextEdit(self.horizontalLayoutWidget)
        self.textEdit_new.setObjectName("textEdit_new")
        self.horizontalLayout.addWidget(self.textEdit_new)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(100, 20, 631, 101))
        font = QtGui.QFont()
        font.setFamily("Leelawadee")
        font.setPointSize(50)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(54, 28, 159);")
        self.label.setObjectName("label")
        self.clearButton = QtWidgets.QPushButton(self.centralwidget)
        self.clearButton.setGeometry(QtCore.QRect(340, 490, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Leelawadee")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.clearButton.setFont(font)
        self.clearButton.setStyleSheet("color: rgb(44, 75, 255);")
        self.clearButton.setObjectName("clearButton")
        self.comboBox_ori = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_ori.setGeometry(QtCore.QRect(0, 150, 331, 22))
        self.comboBox_ori.setObjectName("comboBox_ori")
        self.comboBox_new = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_new.setGeometry(QtCore.QRect(470, 150, 331, 22))
        self.comboBox_new.setObjectName("comboBox_new")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        #Add language to ComboBox
        for x in googletrans.LANGUAGES.values():
            self.comboBox_ori.addItem(x)
            self.comboBox_new.addItem(x)
        self.comboBox_ori.setCurrentText("english")
        self.comboBox_new.setCurrentText("thai")

        self.transButton.clicked.connect(self.tranlation)
        self.clearButton.clicked.connect(self.clear)


    def tranlation(self):
        google = googletrans.Translator()

        ori = self.textEdit_ori.toPlainText()
        langA = self.comboBox_ori.currentText()
        langB = self.comboBox_new.currentText()
        sum = google.translate(ori,src = langA ,dest= langB )
        self.textEdit_new.setText(sum.text)

    def clear(self):
        self.textEdit_ori.setText("")
        self.textEdit_new.setText("")

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.transButton.setText(_translate("MainWindow", "Translate"))
        self.label.setText(_translate("MainWindow", "Google Translation"))
        self.clearButton.setText(_translate("MainWindow", "Clear"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())

