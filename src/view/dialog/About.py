from PyQt4 import QtGui

class About(QtGui.QDialog):
    
    TEXT = '''
        Mid-West State University of Parana (UNICENTRO)
        Computer Science Department
        Object-Oriented Programming III
        
        Teacher: Andres Jesse Porfirio
        
        Model-View-Controller (MVC) Pattern example in Python,
        with SQLite3 and Qt4.
        
        Version: 1.1
        
        Authors:
            Alexandre Antoniu Neto      <alexandreantoniu@gmail.com>
            Victor Alexandre Padilha           <padilha@linuxmail.org>
            Willian Eiji Yassue                      <eiji.yassue@gmail.com>
            '''

    def __init__(self, parent=None):
        super(About, self).__init__(parent)
        
        self._create_buttons()
        self._create_vbox()
        
        self.ok_button.clicked.connect(self.close)   
        
    def _create_buttons(self):
        self.ok_button = QtGui.QPushButton('OK', self)
        self.ok_button.setToolTip('Back to main screen.')
        
    def _create_vbox(self):
        vbox = QtGui.QVBoxLayout()
        vbox.addWidget(QtGui.QLabel(About.TEXT))       
        vbox.addWidget(self.ok_button)      
        self.setLayout(vbox)
