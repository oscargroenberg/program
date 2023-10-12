from PyQt6.QtWidgets import QMainWindow, QWidget, QPushButton, QGraphicsColorizeEffect, QComboBox, QLineEdit
from PyQt6.QtCore import Qt, QPropertyAnimation, QEasingCurve
from PyQt6.QtGui import QColor, QRegularExpressionValidator
from PyQt6.QtCore import QRegularExpression
from PyQt6.QtCore import pyqtProperty
from PyQt6.QtGui import QPalette
import json
from style import Colors, Sizing, ComboBoxStyles, InputStyles

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
        
        
        
        # Year Input Field
        self.year_input = QLineEdit(self.box)
        self.year_input.setPlaceholderText("Enter Year")
        self.year_input.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.year_input.setGeometry(
            int((self.box.width() - InputStyles.WIDTH) / 2),  # Centered horizontally
            int(self.box.height() - 3 * Sizing.SUBMIT_BUTTON_HEIGHT - 40),  # Positioned above the ComboBoxes with a 10px margin
            InputStyles.WIDTH,
            InputStyles.HEIGHT
        )
        self.year_input.setStyleSheet(InputStyles.STYLESHEET)

        # Year Input Field Validator
        year_pattern = QRegularExpression(r"^\d{4}$")  # Regular expression for exactly 4 digits
        year_validator = QRegularExpressionValidator(year_pattern)
        self.year_input.setValidator(year_validator)

        
        
        
        # Calculate the starting x-coordinate for the ComboBoxes
        start_x = int((self.box.width() - 2 * ComboBoxStyles.WIDTH - 10) / 2)  # Centered horizontally with a 10px gap between ComboBoxes

        # First ComboBox
        self.combo1 = QComboBox(self.box)
        self.combo1.setEditable(True)
        self.combo1.lineEdit().setReadOnly(True)
        self.combo1.lineEdit().setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.combo1.setGeometry(
            start_x,
            int(self.box.height() - 2 * Sizing.SUBMIT_BUTTON_HEIGHT - 30),  # Positioned above the button with a 10px margin
            ComboBoxStyles.WIDTH,
            ComboBoxStyles.HEIGHT
        )
        self.combo1.setStyleSheet(ComboBoxStyles.STYLESHEET)

        # Second ComboBox (to the right of the first one with a 10px gap)
        self.combo2 = QComboBox(self.box)
        self.combo2.setEditable(True)
        self.combo2.lineEdit().setReadOnly(True)
        self.combo2.lineEdit().setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.combo2.setGeometry(
            start_x + ComboBoxStyles.WIDTH + 10,  # Add the width of the first ComboBox and the 10px gap
            int(self.box.height() - 2 * Sizing.SUBMIT_BUTTON_HEIGHT - 30),  # Positioned above the button with a 10px margin
            ComboBoxStyles.WIDTH,
            ComboBoxStyles.HEIGHT
        )
        self.combo2.setStyleSheet(ComboBoxStyles.STYLESHEET)
        
        # Load data from the JSON file
        with open('months.json', 'r') as file:
            months_data = json.load(file)

        for month in months_data:
            self.combo1.addItem(month["Month"], month["ID"])
            self.combo2.addItem(month["Month"], month["ID"])
        
        
        
        self.submit_btn = HoverButton("Start", self.box)  # Use the custom HoverButton
        self.submit_btn.setGeometry(
            int((self.box.width() - Sizing.SUBMIT_BUTTON_WIDTH) / 2),  # Centered horizontally
            int(self.box.height() - Sizing.SUBMIT_BUTTON_HEIGHT - 20),  # Positioned at the bottom with a 20px margin
            Sizing.SUBMIT_BUTTON_WIDTH,
            Sizing.SUBMIT_BUTTON_HEIGHT
        )
