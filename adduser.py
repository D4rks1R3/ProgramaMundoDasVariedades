from PyQt5 import QtCore, QtGui, QtWidgets
from bdconnect import dbloja
import sys
class Ui_AddMainWindow(object):
    def cli(self):
        db = dbloja()
        name = str(self.input_name.text())
        tel = str(self.input_tell.text())
        valor = str(self.input_valor.text())
        data = str(self.input_date1.text())
        date2 = str(self.input_date2.text())
        try:
            db.insert(name, tel, valor, data, date2)
        except Exception as e:
                print(e)
    def setupUi(self, AddMainWindow):
        font = QtGui.QFont()
        font.setPointSize(14)
        
        AddMainWindow.setObjectName("AddMainWindow")
        AddMainWindow.resize(466, 560)
        AddMainWindow.setWindowTitle("Adicionar Usúario")
        AddMainWindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(AddMainWindow)
        self.centralwidget.setObjectName("centralwidget")
#-----------------------------------------------------------------------------------------------------------------#      
        #Labels não mudar
        self.name1 = QtWidgets.QLabel(self.centralwidget)
        self.name1.setGeometry(QtCore.QRect(40, 30, 61, 29))
        font = QtGui.QFont()
        font.setFamily("Lucida Console")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.name1.setFont(font)
        self.name1.setText("Nome:")
        self.name1.setObjectName("name1")

        self.fone2 = QtWidgets.QLabel(self.centralwidget)
        self.fone2.setGeometry(QtCore.QRect(40, 110, 91, 37))
        self.fone2.setText("Telefone:")
        font = QtGui.QFont()
        font.setFamily("Lucida Console")
        font.setPointSize(12)
        self.fone2.setFont(font)
        self.fone2.setObjectName("fone2")

        self.valor3 = QtWidgets.QLabel(self.centralwidget)
        self.valor3.setGeometry(QtCore.QRect(40, 200, 71, 31))
        self.valor3.setText("Valor:")
        font = QtGui.QFont()
        font.setFamily("Lucida Console")
        font.setPointSize(12)
        self.valor3.setFont(font)
        self.valor3.setObjectName("valor3")

        self.data4 = QtWidgets.QLabel(self.centralwidget)
        self.data4.setGeometry(QtCore.QRect(40, 280, 61, 41))
        self.data4.setText("Data:")
        font = QtGui.QFont()
        font.setFamily("Lucida Console")
        font.setPointSize(12)
        self.data4.setFont(font)
        self.data4.setObjectName("data4")

        self.dataven5 = QtWidgets.QLabel(self.centralwidget)
        self.dataven5.setGeometry(QtCore.QRect(40, 380, 191, 31))
        self.dataven5.setText("Data de Vencimento:")
        font = QtGui.QFont()
        font.setFamily("Lucida Console")
        font.setPointSize(12)
        self.dataven5.setFont(font)
        self.dataven5.setObjectName("dataven5")
#----------------------------------------------------------------------------------------------------------------------------#     
        #Input Name
        self.input_name = QtWidgets.QLineEdit(self.centralwidget)
        self.input_name.setGeometry(QtCore.QRect(40, 60, 391, 41))
        self.input_name.setStyleSheet("background-color:rgb(248, 248, 248);\n"
        "border-bottom: 3px solid #CD0000 ;")
        self.input_name.setFont(font)
        self.input_name.setFrame(False)
        self.input_name.setObjectName("input_name")         
#-------------------ui----------------------------------------------------------------------------------------------#
        #input Telefone
        self.input_tell = QtWidgets.QLineEdit(self.centralwidget)
        self.input_tell.setGeometry(QtCore.QRect(40, 150, 391, 41))
        self.input_tell.setStyleSheet("background-color:rgb(248, 248, 248);\n"
        "border-bottom: 3px solid #CD0000 ;")
        self.input_tell.setFont(font)
        self.input_tell.setFrame(False)
        self.input_tell.setObjectName("inpu_tell")
#-----------------------------------------------------------------------------------------------------------------#
        #Input valor        
        self.input_valor = QtWidgets.QLineEdit(self.centralwidget)
        self.input_valor.setGeometry(QtCore.QRect(40, 240, 391, 41))
        self.input_valor.setFont(font)
        self.input_valor.setStyleSheet("background-color:rgb(248, 248, 248);\n"
        "border-bottom: 3px solid #CD0000 ;")
        self.input_valor.setFrame(False)
        self.input_valor.setObjectName("input_valor")
#-----------------------------------------------------------------------------------------------------------------#
        #inputa data1
        self.input_date1 = QtWidgets.QLineEdit(self.centralwidget)
        self.input_date1.setGeometry(QtCore.QRect(40, 330, 391, 41))
        self.input_date1.setStyleSheet("background-color:rgb(248, 248, 248);\n"
        "border-bottom: 3px solid #CD0000 ;")
        self.input_date1.setFont(font)
        self.input_date1.setFrame(False)
        self.input_date1.setObjectName("unput_date1")
#-----------------------------------------------------------------------------------------------------------------#
        #inputa date2
        self.input_date2 = QtWidgets.QLineEdit(self.centralwidget)
        self.input_date2.setGeometry(QtCore.QRect(40, 420, 391, 41))
        self.input_date2.setStyleSheet("background-color:rgb(248, 248, 248);\n"
        "border-bottom: 3px solid #CD0000 ;")
        self.input_date2.setFrame(False)
        self.input_date2.setObjectName("input_date2")
        self.input_date2.setFont(font)
#-----------------------------------------------------------------------------------------------------------------#

        #Botão OK
        self.btn_add = QtWidgets.QPushButton(self.centralwidget)
        self.btn_add.setGeometry(QtCore.QRect(160, 480, 141, 51))
        self.btn_add.setText("OK")
        self.btn_add.setSizeIncrement(QtCore.QSize(0, 0))
        self.btn_add.setBaseSize(QtCore.QSize(0, 0))
        self.btn_add.setFont(font)
        self.btn_add.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.btn_add.setStyleSheet("background-color: rgb(252, 252, 252);\n"
        "border-color: rgb(255, 0, 0);")        
        self.btn_add.setFlat(True)
        self.btn_add.clicked.connect(self.cli)
        
         
        AddMainWindow.setCentralWidget(self.centralwidget)
        QtCore.QMetaObject.connectSlotsByName(AddMainWindow)
        
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    AddMainWindow = QtWidgets.QMainWindow()
    ui = Ui_AddMainWindow()
    ui.setupUi(AddMainWindow)
    AddMainWindow.show()
    sys.exit(app.exec_())
