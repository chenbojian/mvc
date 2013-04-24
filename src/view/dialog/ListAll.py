from PyQt4 import QtGui

class ListAll(QtGui.QDialog):

    OUTLAWS_HEADER = ['Name', 'Surname', 'Reward ($)']

    def __init__(self, controller=None, parent=None):
        super(ListAll, self).__init__(parent)
        self.controller = controller
        
        self.resize(650,400)
        self.setWindowTitle('All outlaws')    
        self._create_table() 
        self._create_buttons()
        self._create_events()
        self._create_vbox()
        
    def show(self):
        self._update_table()
        super(ListAll, self).show()
    
    def _create_vbox(self):
        vbox = QtGui.QVBoxLayout()
        
        vbox.addWidget(self.table)
        vbox.addWidget(self.ok_button)
        self.setLayout(vbox)
        
    def _create_buttons(self):
        self.ok_button = QtGui.QPushButton('OK', self)
        self.ok_button.setToolTip('Back to main screen.')
        
    def _create_events(self):
        self.ok_button.clicked.connect(self.close)
        
    def _create_table(self):
        self.table = QtGui.QTableWidget(0, 3, self)
        self.table.setHorizontalHeaderLabels(ListAll.OUTLAWS_HEADER)
        self.table.move(10,50)
        self.table.resize(620,300)
        self.table.setColumnWidth(0,200)
        self.table.setColumnWidth(1,200)
        self.table.setColumnWidth(2,200)
    
    def _update_table(self):
        self._remove_all()
        self._add_all()
        
    def _remove_all(self):
        for i in range(self.table.rowCount()):
            self.table.removeRow(0)
    
    def _add_all(self):
        _all = self.controller.get_all()
        
        for i in range(len(_all)):
            self.table.insertRow(i)
            self.table.setItem(i, 0, QtGui.QTableWidgetItem(_all[i].name))
            self.table.setItem(i, 1, QtGui.QTableWidgetItem(_all[i].surname))
            self.table.setItem(i, 2, QtGui.QTableWidgetItem(str(_all[i].reward)))