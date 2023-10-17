from PyQt6.QtWidgets import QPushButton
from PyQt6.QtCore import Qt, QPropertyAnimation
from PyQt6.QtGui import QColor
from PyQt6.QtCore import pyqtProperty
from style import Colors, ButtonStyles

class HoverButton(QPushButton):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Set up the color animation
        self._color = QColor(Colors.ACTION_COLOR)
        self.animation = QPropertyAnimation(self, b"color")
        self.animation.setDuration(Colors.ACTION_HOVER_DURATION)  # Duration of the transition in milliseconds
        self.animation.setStartValue(QColor(Colors.ACTION_COLOR))
        self.animation.setEndValue(QColor(Colors.ACTION_HOVER_COLOR))
        
        # Initial stylesheet
        self.updateStyleSheet(self._color)

    def enterEvent(self, event):
        self.animation.setDirection(QPropertyAnimation.Direction.Forward)
        self.animation.start()
        super().enterEvent(event)

    def leaveEvent(self, event):
        self.animation.setDirection(QPropertyAnimation.Direction.Backward)
        self.animation.start()
        super().leaveEvent(event)

    def updateStyleSheet(self, color):
        button_style = ButtonStyles.STYLESHEET.replace(Colors.ACTION_COLOR, color.name())
        self.setStyleSheet(button_style)

    @pyqtProperty(QColor)
    def color(self):
        return self._color

    @color.setter
    def color(self, color):
        self._color = color
        self.updateStyleSheet(color)
