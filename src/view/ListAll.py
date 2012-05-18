from PyQt4 import QtGui

class ListAllView(QtGui.QDialog):

    OUTLAWS_HEADER = ['Name', 'Surname', 'Reward ($)']

    def __init__(self, controller=None, parent=None):
        super(ListAllView, self).__init__(parent)
        
        self._create_labels()  
        self._create_buttons()      
        self._center()
        
    def create_buttons(self):
        self.ok = QtGui.QPushButton('OK', self)
        self.ok.setToolTip('Back to main screen.')
        self.ok.resize(100, 35)
        self.ok.move(400, 530)
        
    def _create_labels(self):
        self.outlaw_label = QtGui.QLabel('Outlaws', self)
        self.outlaw_label.move(10,20)
        
        self.prison_label = QtGui.QLabel('Prisons', self)
        self.prison_label.move(10,270)
        
    def _create_table(self, data):
        table = QtGui.QTableWidget(len(data), 3, self)
        table.setFixedSize(680, 200)
        table.setHorizontalHeaderLabels(ListAllView.OUTLAWS_HEADER)
        table.move(10, 50)
        
        self.outlaws_table = self._create_table(data, 10, 50)
        
        self.outlaws_table.setColumnWidth(0, 225)
        self.outlaws_table.setColumnWidth(1, 225)
        self.outlaws_table.setColumnWidth(2, 225)
        
        for i in range(len(data)):
            self.outlaws_table.setItem(i, 0, QtGui.QTableWidgetItem(data[i].name))
            self.outlaws_table.setItem(i, 1, QtGui.QTableWidgetItem(data[i].surname))
            self.outlaws_table.setItem(i, 2, QtGui.QTableWidgetItem(str(data[i].reward)))
        
        self.outlaws_table.show()
        
        return table 