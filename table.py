
from PyQt5 import QtCore, QtGui, QtWidgets
from adduser import Ui_AddMainWindow 
from bdconnect import dbloja

db = dbloja()
class Ui_Form(object):
	def ro(self):
		self.table.setColumnCount(db.nrow())
		self.table.setRowCount(db.ncolum())
		inte = QtWidgets.QTableWidgetItem(str("ID"))
		self.table.setHorizontalHeaderItem(0, inte)

		inte = QtWidgets.QTableWidgetItem(str("Nome"))
		self.table.setHorizontalHeaderItem(1, inte)

		inte = QtWidgets.QTableWidgetItem(str("Telefone"))
		self.table.setHorizontalHeaderItem(2, inte)

		inte = QtWidgets.QTableWidgetItem(str("Valor"))
		self.table.setHorizontalHeaderItem(3, inte)

		inte = QtWidgets.QTableWidgetItem(str("Data de compra"))
		self.table.setHorizontalHeaderItem(4, inte)

		inte = QtWidgets.QTableWidgetItem(str("Data de Vencimento"))
		self.table.setHorizontalHeaderItem(5, inte)

		inte = QtWidgets.QTableWidgetItem(str("Status"))
		self.table.setHorizontalHeaderItem(6, inte)



		for row, date_ in enumerate(db.dump()):
			for col, date in enumerate(date_):
				item = QtWidgets.QTableWidgetItem(str(date))
				item.setTextAlignment(QtCore.Qt.AlignCenter)
				self.table.setItem(row, col, item)             
	def search(self):
		sear = db.search(self.bar_search.text())
		self.table.setColumnCount(db.nrow())
		self.table.setRowCount(db.ncolum())
		for row, date_ in enumerate(sear):
				for col, date in enumerate(date_):
					item = QtWidgets.QTableWidgetItem(str(date))
					item.setTextAlignment(QtCore.Qt.AlignCenter)
					self.table.setItem(row, col, item)
	def AddUser(self):
		self.AddMainWindow = QtWidgets.QMainWindow()
		self.ui = Ui_AddMainWindow()
		self.ui.setupUi(self.AddMainWindow)
		self.AddMainWindow.show()
	def dell(self):
		if self.del_bar.text() == '':
			print('NONE')
		else:              
			db.delete(self.del_bar.text())
	def upd(self):
		db.update(self.input_datavenc.text(), self.input_new_value.text(), self.del_bar.text())
		#db.update("2")        
		#db.update()
		#db.update(self.input_new_value.text())
	def setupUi(self, Form):
		Form.setObjectName("Form")
		Form.setEnabled(True)
		Form.resize(1193, 689)

		font = QtGui.QFont()
		font.setPointSize(14)

		font2 = QtGui.QFont()
		font.setPointSize(12)
#---------------------------------------------------------------------------------------------------
		self.label = QtWidgets.QLabel(Form)
		self.label.setGeometry(QtCore.QRect(10, 330, 47, 31))
		self.label.setObjectName("label")
		self.label.setFont(font)
		self.label.setText("ID:")

		self.label = QtWidgets.QLabel(Form)
		self.label.setGeometry(QtCore.QRect(40, 400, 41, 21))
		self.label.setObjectName("Date_label")
		self.label.setFont(font2)
		self.label.setText("Data:")

		self.label = QtWidgets.QLabel(Form)
		self.label.setGeometry(QtCore.QRect(40, 470, 41, 21))
		self.label.setObjectName("value_label")
		self.label.setFont(font2)
		self.label.setText("Valor:")
#---------------------------------------------------------------------------------------------------
		self.table = QtWidgets.QTableWidget(Form)
		self.table.setGeometry(QtCore.QRect(290, 100, 851, 551))
		self.table.setObjectName("table")
		          
#---------------------------------------------------------------------------------------------------
		self.btn_search = QtWidgets.QPushButton(Form)
		self.btn_search.setGeometry(QtCore.QRect(330, 40, 101, 31))
		font = QtGui.QFont()
		font.setStrikeOut(False)
		self.btn_search.setFont(font)
		self.btn_search.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
		self.btn_search.setFocusPolicy(QtCore.Qt.StrongFocus)
		self.btn_search.setObjectName("btn_search")
		self.btn_search.clicked.connect(self.search)
#---------------------------------------------------------------------------------------------------
		self.btn_add = QtWidgets.QPushButton(Form)
		self.btn_add.setGeometry(QtCore.QRect(40, 120, 191, 32))
		self.btn_add.setMinimumSize(QtCore.QSize(171, 0))
		self.btn_add.setObjectName("btn_add")
		self.btn_add.clicked.connect(self.AddUser)
#---------------------------------------------------------------------------------------------------
		self.bar_search = QtWidgets.QLineEdit(Form)
		self.bar_search.setGeometry(QtCore.QRect(440, 40, 611, 31))
		self.bar_search.setDragEnabled(True)
		self.bar_search.setReadOnly(False)
		self.bar_search.setClearButtonEnabled(True)
		self.bar_search.setObjectName("bar_search")
#---------------------------------------------------------------------------------------------------
		self.del_bar = QtWidgets.QLineEdit(Form)
		self.del_bar.setGeometry(QtCore.QRect(40, 330, 191, 31))
		self.del_bar.setDragEnabled(True)
		self.del_bar.setReadOnly(False)
		self.del_bar.setClearButtonEnabled(True)
		self.del_bar.setObjectName("del_bar")
#---------------------------------------------------------------------------------------------------
		self.btn_update = QtWidgets.QPushButton(Form)
		self.btn_update.setGeometry(QtCore.QRect(40, 170, 191, 31))
		self.btn_update.setMinimumSize(QtCore.QSize(171, 0))
		self.btn_update.setObjectName("btn_update")
		self.btn_update.clicked.connect(self.ro)
#---------------------------------------------------------------------------------------------------
		self.btn_del = QtWidgets.QPushButton(Form)
		self.btn_del.setGeometry(QtCore.QRect(40, 281, 191, 31))
		self.btn_del.setMinimumSize(QtCore.QSize(171, 0))
		self.btn_del.setObjectName("btn_del")
		self.btn_del.clicked.connect(self.dell)
#---------------------------------------------------------------------------------------------------    
		self.input_datavenc= QtWidgets.QLineEdit(Form)
		self.input_datavenc.setGeometry(QtCore.QRect(40, 430, 191, 31))
		self.input_datavenc.setDragEnabled(True)
		self.input_datavenc.setReadOnly(False)
		self.input_datavenc.setClearButtonEnabled(True)
		self.input_datavenc.setObjectName("new_input_datavenc")
#---------------------------------------------------------------------------------------------------     
		self.input_new_value = QtWidgets.QLineEdit(Form)
		self.input_new_value.setGeometry(QtCore.QRect(40, 500, 191, 31))
		self.input_new_value.setDragEnabled(True)
		self.input_new_value.setReadOnly(False)
		self.input_new_value.setClearButtonEnabled(True)
		self.input_new_value.setObjectName("new_value")
#---------------------------------------------------------------------------------------------------
		self.btn_update2 = QtWidgets.QPushButton(Form)
		self.btn_update2.setGeometry(QtCore.QRect(40, 550, 191, 31))
		self.btn_update2.setMinimumSize(QtCore.QSize(171, 0))
		self.btn_update2.setObjectName("btn_update2")
		self.btn_update2.clicked.connect(self.upd)
#---------------------------------------------------------------------------------------------------
		self.retranslateUi(Form)
		QtCore.QMetaObject.connectSlotsByName(Form)
		#Form.setTabOrder(self.btn_search, self.table)

	def retranslateUi(self, Form):
		_translate = QtCore.QCoreApplication.translate
		Form.setWindowTitle(_translate("Form", "Form"))    

		self.btn_search.setText(_translate("Form", "Buscar"))
		self.btn_update.setText(_translate("Form", "Atualizar Tabela"))
		self.btn_add.setText(_translate("Form", "Adicionar  Cliente"))
		self.bar_search.setPlaceholderText(_translate("Form", "Search"))
		self.btn_del.setText(_translate("Form", "Deletar"))
		self.btn_update2.setText(_translate("Form", "Atualizar dados"))
if __name__ == "__main__":
	import sys
	app = QtWidgets.QApplication(sys.argv)
	Form = QtWidgets.QWidget()
	ui = Ui_Form()
	ui.setupUi(Form)
	Form.show()
	sys.exit(app.exec_())
