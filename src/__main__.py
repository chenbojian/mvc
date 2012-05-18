if __name__ == '__main__':
    import sys
    from PyQt4 import QtGui
    from view.MainView import MainView
    from controller.OutlawController import OutlawController
    
    app = QtGui.QApplication(sys.argv)
    main = MainView(OutlawController())
    main.show()
    sys.exit(app.exec_())