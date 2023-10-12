from PyQt6.QtWidgets import QMainWindow, QWidget, QPushButton, QGraphicsColorizeEffect
from PyQt6.QtCore import Qt, QPropertyAnimation, QEasingCurve
from PyQt6.QtGui import QColor
from PyQt6.QtCore import pyqtProperty
from PyQt6.QtGui import QPalette
from style import Colors, Sizing

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
        button_style = f"""
            QPushButton {{
                background-color: {color.name()};
                color: {Colors.LIGHT_TEXT_COLOR};
                border-radius: {Sizing.RADIUS}px;
                font-size: 18px;
                font-weight: bold;
            }}
        """
        self.setStyleSheet(button_style)


    @pyqtProperty(QColor)
    def color(self):
        return self._color

    @color.setter
    def color(self, color):
        self._color = color
        self.updateStyleSheet(color)




class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Visma...")
        self.setGeometry(100, 100, Sizing.WINDOW_WIDTH, Sizing.WINDOW_HEIGHT)

        # Box with specified dimensions, color, and radius
        self.box = QWidget(self)
        self.box.setGeometry(25, 25, 300, 550)  # Setting the position and size of the box
        self.box.setStyleSheet(f"""
            background-color: {Colors.SECONDARY_BACKGROUND_COLOR};
            border-radius: {Sizing.RADIUS}px;
        """)
        
        self.submit_btn = HoverButton("Start", self.box)  # Use the custom HoverButton
        self.submit_btn.setGeometry(
            int((self.box.width() - Sizing.SUBMIT_BUTTON_WIDTH) / 2),  # Centered horizontally
            int(self.box.height() - Sizing.SUBMIT_BUTTON_HEIGHT - 20),  # Positioned at the bottom with a 20px margin
            Sizing.SUBMIT_BUTTON_WIDTH,
            Sizing.SUBMIT_BUTTON_HEIGHT
        )
