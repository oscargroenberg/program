from PyQt6.QtWidgets import QMainWindow, QWidget, QPushButton, QGraphicsColorizeEffect, QComboBox, QLineEdit
from PyQt6.QtCore import Qt, QPropertyAnimation, QEasingCurve
from PyQt6.QtGui import QColor, QRegularExpressionValidator
from PyQt6.QtCore import QRegularExpression
from PyQt6.QtCore import pyqtProperty
from PyQt6.QtGui import QPalette
from PyQt6.QtWidgets import QListView
from PyQt6.QtCore import pyqtSignal
import json
from style import Colors, Sizing, ComboBoxStyles, InputStyles, ButtonStyles, BoxStyles, RemoveInputButtonStyles
from widgets.hover_button import HoverButton
from widgets.clickable_line_edit import ClickableLineEdit
from widgets.clickable_combo_box import ClickableComboBox



class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.additional_inputs = []  # Initialize the list here
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Visma...")
        self.setGeometry(100, 100, Sizing.WINDOW_WIDTH, Sizing.WINDOW_HEIGHT)

        # Box with specified dimensions, color, and radius
        self.box = QWidget(self)
        self.box.setGeometry(25, 25, 300, 550)  # Setting the position and size of the box
        self.box.setStyleSheet(BoxStyles.STYLESHEET)

        
        # Initial "Enter CVR Number" Input Field
        self.number_input = QLineEdit(self.box)
        self.number_input.setPlaceholderText("Tilføj CVR Nummer")
        self.number_input.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.number_input.setGeometry(
            int((self.box.width() - InputStyles.WIDTH) / 2),  # Centered horizontally
            int(self.box.height() - 5 * Sizing.SUBMIT_BUTTON_HEIGHT),  # Adjusted position to be higher up
            InputStyles.WIDTH,
            InputStyles.HEIGHT
        )
        self.number_input.setStyleSheet(InputStyles.STYLESHEET)

        # Number Input Field Validator (to ensure only numbers are entered)
        number_validator = QRegularExpressionValidator(QRegularExpression(r"^\d+$"))
        self.number_input.setValidator(number_validator)

        # "Tilføj CVR" Button
        self.add_cvr_btn = QPushButton("+", self.box)  # Using a plus sign emoji
        self.add_cvr_btn.setGeometry(
            int((self.box.width() + InputStyles.WIDTH) / 2) + 5,  # Positioned to the right of the input field
            int(self.number_input.y() + (InputStyles.HEIGHT - 30) / 2),  # Centered vertically relative to the input field
            30,  # Width of the button
            30   # Height of the button
        )
        self.add_cvr_btn.setStyleSheet("background-color: green; color: white; border: none; font-size:18px;")  # Green background with white text, no border
        self.add_cvr_btn.clicked.connect(self.addNumberInputField)
     
        
        
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
        start_x = int((self.box.width() - 2 * ComboBoxStyles.WIDTH - 15) / 2)  # Adjusted spacing from 10 to 12

        # First ComboBox
        self.combo1 = ClickableComboBox(self.box)
        self.combo1.setEditable(True)
        self.combo1.lineEdit().setReadOnly(True)
        self.combo1.lineEdit().setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.combo1.setGeometry(
            start_x,
            int(self.box.height() - 2 * Sizing.SUBMIT_BUTTON_HEIGHT - 30),
            ComboBoxStyles.WIDTH,
            ComboBoxStyles.HEIGHT
        )
        self.combo1.setStyleSheet(ComboBoxStyles.STYLESHEET)
        self.combo1.setMaxVisibleItems(12)

        # Second ComboBox
        self.combo2 = ClickableComboBox(self.box)
        self.combo2.setEditable(True)
        self.combo2.lineEdit().setReadOnly(True)
        self.combo2.lineEdit().setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.combo2.setGeometry(
            start_x + ComboBoxStyles.WIDTH + 15,  # Adjusted spacing from 10 to 12
            int(self.box.height() - 2 * Sizing.SUBMIT_BUTTON_HEIGHT - 30),
            ComboBoxStyles.WIDTH,
            ComboBoxStyles.HEIGHT
        )
        self.combo2.setStyleSheet(ComboBoxStyles.STYLESHEET)
        self.combo2.setMaxVisibleItems(12)

        
        # Load data from the JSON file
        with open('C:/Users/oscar/Desktop/visma/months.json', 'r') as file:
            months_data = json.load(file)

        for month in months_data:
            self.combo1.addItem(month["Month"], month["ID"])
            self.combo2.addItem(month["Month"], month["ID"])
        
        self.combo2.setCurrentText("Dec")
        
        self.submit_btn = HoverButton("Start", self.box)  # Use the custom HoverButton
        self.submit_btn.setGeometry(
            int((self.box.width() - Sizing.SUBMIT_BUTTON_WIDTH) / 2),  # Centered horizontally
            int(self.box.height() - Sizing.SUBMIT_BUTTON_HEIGHT - 20),  # Positioned at the bottom with a 20px margin
            Sizing.SUBMIT_BUTTON_WIDTH,
            Sizing.SUBMIT_BUTTON_HEIGHT
        )
        
        # Connect the submit button's clicked signal to the printYearAndMonths method
        self.submit_btn.clicked.connect(self.printYearAndMonths)
        
    def printYearAndMonths(self):
        year = self.year_input.text()
        month1 = self.combo1.currentText()
        month2 = self.combo2.currentText()
        print(f"Year: {year}, Month 1: {month1}, Month 2: {month2}")
        
    def showComboPopup(self, event):
        sender = self.sender()
        if sender:
            sender.showPopup()



    def addNumberInputField(self):
        # Store the original position of the "Enter CVR Number" Input Field if not already stored
        if not hasattr(self, 'original_input_y'):
            self.original_input_y = self.number_input.y()

        # Shift the original "Enter CVR Number" Input Field upwards
        self.number_input.move(
            self.number_input.x(),
            self.original_input_y - InputStyles.HEIGHT - 10  # Shift upwards by the height of the input field + 10px spacing
        )

        # Calculate the position for the new input field based on the shifted position of the original input field
        new_input_y = self.number_input.y() + InputStyles.HEIGHT + 10  # 10px spacing between the two input fields
        new_input = QLineEdit(self.box)
        new_input.setPlaceholderText("Tilføj 2. CVR Nummer")
        new_input.setAlignment(Qt.AlignmentFlag.AlignCenter)
        new_input.setGeometry(
            int((self.box.width() - InputStyles.WIDTH) / 2),  # Centered horizontally
            new_input_y,
            InputStyles.WIDTH,
            InputStyles.HEIGHT
        )
        new_input.setStyleSheet(InputStyles.STYLESHEET)
        new_input.show()

        # Add the new input to the list of additional inputs
        self.additional_inputs.append(new_input)

        # Create the red "X" icon next to the new input field
        self.remove_input_btn = QPushButton("x", self.box)
        self.remove_input_btn.setGeometry(
            int((self.box.width() + InputStyles.WIDTH) / 2) + 5,  # Just to the right of the input field
            new_input_y + 5,  # Adjusted for the reduced height
            20,  # Width of the "X" icon
            30   # Reduced height of the "X" icon
        )
        self.remove_input_btn.setStyleSheet(RemoveInputButtonStyles.STYLESHEET)
        self.remove_input_btn.clicked.connect(self.removeNumberInputField)
        self.remove_input_btn.show()

        # Hide the green plus sign button
        self.add_cvr_btn.hide()

    def removeNumberInputField(self):
        # Remove the additional input field
        input_to_remove = self.additional_inputs.pop()
        input_to_remove.deleteLater()

        # Remove the red "X" button
        self.remove_input_btn.deleteLater()

        # Reset the original "Enter CVR Number" Input Field to its original position
        self.number_input.move(
            self.number_input.x(),
            self.original_input_y
        )

        # Show the green plus sign button again
        self.add_cvr_btn.show()
