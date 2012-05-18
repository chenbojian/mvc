from Form import Form
from ListAll import ListAll
from About import About
from PyQt4 import QtGui

class MainView(QtGui.QWidget):

    def __init__(self, controller):
        super(MainView, self).__init__()
        self.controller = controller
        self.init_ui()
                
    def init_ui(self):
        self.resize(350, 504)
        self.setWindowTitle('The Outlaws')
        
        self.label = QtGui.QLabel(self)
        self.label.setPixmap(QtGui.QPixmap('../media/bang.jpg'))
        
        self._center()
        self._create_buttons()
        self._create_events()
        
    def _create_buttons(self):
        self.insert_outlaw_button = QtGui.QPushButton('Insert Outlaw', self)
        self.insert_outlaw_button.setToolTip('Insert a new outlaw.')
        self.insert_outlaw_button.resize(100, 35)
        self.insert_outlaw_button.move(230,200)
        
        self.list_all_button = QtGui.QPushButton('List all', self)
        self.list_all_button.setToolTip('List all the outlaws.')
        self.list_all_button.resize(100, 35)
        self.list_all_button.move(230, 240)
        
        self.about_button = QtGui.QPushButton('About', self)
        self.about_button.setToolTip('About this software.')
        self.about_button.resize(100, 35)
        self.about_button.move(230, 280)
        
    def _create_events(self):
        self.insert_outlaw_button.clicked.connect(self._show_form)
        self.list_all_button.clicked.connect(self._show_all)
        self.about_button.clicked.connect(self._show_about)
        
    def _show_form(self):
        form = Form(self.controller, self)
        form.exec_()
        form.destroy(True, True)
        
    def _show_all(self):
        list_all = ListAll(self.controller)
        list_all.exec_()
        list_all.destroy(True, True)
        
    def _show_about(self):
        about = About(self)
        about.exec_()
        about.destroy(True, True)
        
    def _center(self):
        qr = self.frameGeometry()
        cp = QtGui.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())