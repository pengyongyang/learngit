#! /usr/bin/env python3
# -*- coding:utf-8 -*-

import sys
from PyQt5.QtWidgets import QMainWindow,QAction,QMenu,qApp,\
        QApplication,QWidget,QMessageBox,QDesktopWidget
from PyQt5.QtGui import QIcon

class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        exitAct = QAction(QIcon('exit.png'),'&Exit',self)
        exitAct.setShortcut('Ctrl+Q')
        exitAct.setStatusTip('Exit application')
        exitAct.triggered.connect(qApp.quit)
        
        newAct = QAction('New',self)
        newAct.setStatusTip('New File')

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        settingMenu = menubar.addMenu('&Setting')

        fileMenu.addAction(newAct)
        fileMenu.addAction(exitAct)

        self.statusBar()
        self.statusBar().showMessage('Ready')
        self.resize(1000,600)
        self.center()
        self.setWindowTitle('Simple TSP Window')
        self.show()
    
    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

