from PyQt4 import QtGui
from model.Outlaw import Outlaw

class Form(QtGui.QDialog):

    def __init__(self, controller=None, parent=None):
        super(Form, self).__init__(parent)
        
        self.controller = controller
        self._create_buttons()
        self._create_lines()
        self._create_grid()
        self._create_validator()
        self._create_events()
        
    def _create_buttons(self):
        self.insert_button = QtGui.QPushButton('Insert')
        self.cancel_button = QtGui.QPushButton('Cancel')
        
    def _create_lines(self):
        self.name_edit = QtGui.QLineEdit()
        self.surname_edit = QtGui.QLineEdit()
        self.reward_edit = QtGui.QLineEdit()
        self.reward_edit.setValidator(QtGui.QDoubleValidator(0.0, 100000.00, 2, self))
        
    def _create_grid(self):
        grid = QtGui.QGridLayout()
        
        grid.addWidget(QtGui.QLabel('Name:'), 0, 0)
        grid.addWidget(self.name_edit, 0, 1)
        
        grid.addWidget(QtGui.QLabel('Surname:'), 1, 0)
        grid.addWidget(self.surname_edit, 1, 1)
        
        grid.addWidget(QtGui.QLabel('Reward:'), 2, 0)
        grid.addWidget(self.reward_edit, 2, 1)
        
        grid.addWidget(self.insert_button, 3, 0)
        grid.addWidget(self.cancel_button, 3, 1)
        
        self.setLayout(grid)
        
    def _create_events(self):
        self.insert_button.clicked.connect(self._insert)
        self.cancel_button.clicked.connect(self._cancel)
        
    def _create_validator(self):
        self.validator = QtGui.QDoubleValidator(0.0, 100000.00, 2, self)
        
    def _insert(self):
        outlaw = Outlaw(str(self.name_edit.text()), str(self.surname_edit.text()), float(str(self.reward_edit.text())))
        self.controller.save(outlaw)
        self._clear()
    
    def _cancel(self):
        self.close()
        
    def _clear(self):
        self.name_edit.clear()
        self.surname_edit.clear()
        self.reward_edit.clear()