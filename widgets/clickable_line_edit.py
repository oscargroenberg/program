#clickable_line_edit.py
from PyQt6.QtWidgets import QLineEdit
from PyQt6.QtCore import pyqtSignal

class ClickableLineEdit(QLineEdit):
    clicked = pyqtSignal()

    def mouseReleaseEvent(self, event):
        super().mouseReleaseEvent(event)
        self.clicked.emit()
