from PyQt5.QtWidgets import (QWidget, QSlider, QApplication,
    QHBoxLayout, QVBoxLayout, QMessageBox, QDialog,QGridLayout,QLabel)
from PyQt5.QtCore import QObject, Qt, pyqtSignal
from PyQt5.QtGui import QPainter, QFont, QColor, QPen
from PyQt5 import QtGui, QtCore

class MDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle(u'Add new category')
        lay = QGridLayout(self)
        lay.addWidget(QLabel(u'Name'), 0, 0, 1, 1)
        self.setGeometry(100,100,100,100)
