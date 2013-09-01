# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'python_editor.ui'
#
# Created: Sat Aug 31 18:44:27 2013
#      by: pyside-uic 0.2.14 running on PySide 1.2.0
#
# WARNING! All changes made in this file will be lost!

from pyqode.qt import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1078, 831)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setSpacing(1)
        self.gridLayout.setContentsMargins(1, 1, 1, 1)
        self.gridLayout.setObjectName("gridLayout")
        self.editor = QPythonCodeEdit(self.centralwidget)
        self.editor.setObjectName("editor")
        self.gridLayout.addWidget(self.editor, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1078, 20))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuSettings = QtGui.QMenu(self.menubar)
        self.menuSettings.setObjectName("menuSettings")
        self.menuPanels = QtGui.QMenu(self.menuSettings)
        self.menuPanels.setObjectName("menuPanels")
        self.menuModes = QtGui.QMenu(self.menuSettings)
        self.menuModes.setObjectName("menuModes")
        self.menuStyle = QtGui.QMenu(self.menuSettings)
        self.menuStyle.setObjectName("menuStyle")
        MainWindow.setMenuBar(self.menubar)
        self.toolBar = QtGui.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionOpen = QtGui.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/example_icons/rc/folder.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionOpen.setIcon(icon)
        self.actionOpen.setIconVisibleInMenu(True)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave = QtGui.QAction(MainWindow)
        self.actionSave.setEnabled(False)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/example_icons/rc/document-save.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSave.setIcon(icon1)
        self.actionSave.setIconVisibleInMenu(True)
        self.actionSave.setObjectName("actionSave")
        self.actionPanel = QtGui.QAction(MainWindow)
        self.actionPanel.setObjectName("actionPanel")
        self.actionModes = QtGui.QAction(MainWindow)
        self.actionModes.setObjectName("actionModes")
        self.actionAbout = QtGui.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionLight = QtGui.QAction(MainWindow)
        self.actionLight.setCheckable(True)
        self.actionLight.setObjectName("actionLight")
        self.actionDark = QtGui.QAction(MainWindow)
        self.actionDark.setCheckable(True)
        self.actionDark.setObjectName("actionDark")
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionSave)
        self.menuStyle.addAction(self.actionLight)
        self.menuStyle.addAction(self.actionDark)
        self.menuSettings.addAction(self.menuPanels.menuAction())
        self.menuSettings.addAction(self.menuModes.menuAction())
        self.menuSettings.addAction(self.menuStyle.menuAction())
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuSettings.menuAction())
        self.toolBar.addAction(self.actionOpen)
        self.toolBar.addAction(self.actionSave)

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.editor, QtCore.SIGNAL("dirtyChanged(bool)"), self.actionSave.setEnabled)
        QtCore.QObject.connect(self.actionSave, QtCore.SIGNAL("triggered()"), self.editor.saveToFile)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "pyQode - Python Editor", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFile.setTitle(QtGui.QApplication.translate("MainWindow", "File", None, QtGui.QApplication.UnicodeUTF8))
        self.menuSettings.setTitle(QtGui.QApplication.translate("MainWindow", "Settings", None, QtGui.QApplication.UnicodeUTF8))
        self.menuPanels.setTitle(QtGui.QApplication.translate("MainWindow", "Panels", None, QtGui.QApplication.UnicodeUTF8))
        self.menuModes.setTitle(QtGui.QApplication.translate("MainWindow", "Modes", None, QtGui.QApplication.UnicodeUTF8))
        self.menuStyle.setTitle(QtGui.QApplication.translate("MainWindow", "Style", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBar.setWindowTitle(QtGui.QApplication.translate("MainWindow", "toolBar", None, QtGui.QApplication.UnicodeUTF8))
        self.actionOpen.setText(QtGui.QApplication.translate("MainWindow", "Open", None, QtGui.QApplication.UnicodeUTF8))
        self.actionOpen.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+O", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave.setText(QtGui.QApplication.translate("MainWindow", "Save", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+S", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPanel.setText(QtGui.QApplication.translate("MainWindow", "Panel", None, QtGui.QApplication.UnicodeUTF8))
        self.actionModes.setText(QtGui.QApplication.translate("MainWindow", "Modes", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAbout.setText(QtGui.QApplication.translate("MainWindow", "About", None, QtGui.QApplication.UnicodeUTF8))
        self.actionLight.setText(QtGui.QApplication.translate("MainWindow", "Light", None, QtGui.QApplication.UnicodeUTF8))
        self.actionDark.setText(QtGui.QApplication.translate("MainWindow", "Dark", None, QtGui.QApplication.UnicodeUTF8))

from pyqode.python import QPythonCodeEdit
from . import editor_rc