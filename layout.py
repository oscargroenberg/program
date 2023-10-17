from PyQt6.QtWidgets import QMainWindow, QWidget, QPushButton, QLineEdit, QComboBox, QLabel
from PyQt6.QtCore import Qt, QRegularExpression
from PyQt6.QtGui import QRegularExpressionValidator
import json
from style import Colors, Sizing, ComboBoxStyles, InputStyles, BoxStyles, RemoveInputButtonStyles
from widgets.hover_button import HoverButton
from widgets.clickable_line_edit import ClickableLineEdit
from widgets.clickable_combo_box import ClickableComboBox

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.additional_inputs = []
        self.init_ui()

    def init_ui(self):
        self.setup_window()
        self.setup_box()
        self.setup_title()  # Ensure the title setup is after the box setup
        self.setup_number_input()
        self.setup_add_cvr_button()
        self.setup_year_input()
        self.setup_combo_boxes()
        self.setup_submit_button()

    def setup_window(self):
        self.setWindowTitle("Visma...")
        self.setGeometry(100, 100, Sizing.WINDOW_WIDTH, Sizing.WINDOW_HEIGHT)

    def setup_box(self):
        self.box = QWidget(self)
        self.box.setGeometry(25, 25, 300, 550)
        self.box.setStyleSheet(BoxStyles.STYLESHEET)

    def setup_title(self):
        self.title_label = QLabel("Form", self.box)  # Parented the label to the box
        title_width = 200
        title_height = 40
        title_x = int((self.box.width() - title_width) / 2)
        title_y = 10  # Top of the box
        self.title_label.setGeometry(title_x, title_y, title_width, title_height)
        self.title_label.setStyleSheet("font-size: 24px; font-weight: bold; color: " + Colors.DARK_TEXT_COLOR)
        self.title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)  # Center the text within the label
        self.title_label.raise_()  # Ensure the label is on top of other widgets
        self.title_label.show()  # Explicitly show the label

    def setup_number_input(self):
        self.number_input = self.create_input(self.box, "Tilføj CVR Nummer", 
                                              int((self.box.width() - InputStyles.WIDTH) / 2),
                                              int(self.box.height() - 5 * Sizing.SUBMIT_BUTTON_HEIGHT))
        number_validator = QRegularExpressionValidator(QRegularExpression(r"^\d+$"))
        self.number_input.setValidator(number_validator)

    def setup_add_cvr_button(self):
        self.add_cvr_btn = QPushButton("+", self.box)
        self.add_cvr_btn.setGeometry(
            int((self.box.width() + InputStyles.WIDTH) / 2) + 5,
            int(self.number_input.y() + (InputStyles.HEIGHT - 30) / 2),
            30, 30
        )
        self.add_cvr_btn.setStyleSheet("background-color: green; color: white; border: none; font-size:18px;")
        self.add_cvr_btn.clicked.connect(self.addNumberInputField)

    def setup_year_input(self):
        self.year_input = self.create_input(self.box, "Enter Year", 
                                            int((self.box.width() - InputStyles.WIDTH) / 2),
                                            int(self.box.height() - 3 * Sizing.SUBMIT_BUTTON_HEIGHT - 40))
        year_validator = QRegularExpressionValidator(QRegularExpression(r"^\d{4}$"))
        self.year_input.setValidator(year_validator)

    def setup_combo_boxes(self):
        start_x = int((self.box.width() - 2 * ComboBoxStyles.WIDTH - 15) / 2)
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

        self.combo2 = ClickableComboBox(self.box)
        self.combo2.setEditable(True)
        self.combo2.lineEdit().setReadOnly(True)
        self.combo2.lineEdit().setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.combo2.setGeometry(
            start_x + ComboBoxStyles.WIDTH + 15,
            int(self.box.height() - 2 * Sizing.SUBMIT_BUTTON_HEIGHT - 30),
            ComboBoxStyles.WIDTH,
            ComboBoxStyles.HEIGHT
        )
        self.combo2.setStyleSheet(ComboBoxStyles.STYLESHEET)
        self.combo2.setMaxVisibleItems(12)

        self.load_combo_box_data()
        self.combo2.setCurrentText("Dec")

    def setup_submit_button(self):
        self.submit_btn = HoverButton("Start", self.box)
        self.submit_btn.setGeometry(
            int((self.box.width() - Sizing.SUBMIT_BUTTON_WIDTH) / 2),
            int(self.box.height() - Sizing.SUBMIT_BUTTON_HEIGHT - 20),
            Sizing.SUBMIT_BUTTON_WIDTH,
            Sizing.SUBMIT_BUTTON_HEIGHT
        )
        self.submit_btn.clicked.connect(self.printYearAndMonths)

    def create_input(self, parent, placeholder, x, y):
        input_field = QLineEdit(parent)
        input_field.setPlaceholderText(placeholder)
        input_field.setAlignment(Qt.AlignmentFlag.AlignCenter)
        input_field.setGeometry(x, y, InputStyles.WIDTH, InputStyles.HEIGHT)
        input_field.setStyleSheet(InputStyles.STYLESHEET)
        return input_field

    def load_combo_box_data(self):
        with open('C:/Users/oscar/Desktop/visma/months.json', 'r') as file:
            months_data = json.load(file)
        for month in months_data:
            self.combo1.addItem(month["Month"], month["ID"])
            self.combo2.addItem(month["Month"], month["ID"])

    def printYearAndMonths(self):
        year = self.year_input.text()
        month1 = self.combo1.currentText()
        month2 = self.combo2.currentText()
        print(f"Year: {year}, Month 1: {month1}, Month 2: {month2}")

    def addNumberInputField(self):
        self.original_input_y = self.number_input.y()
        self.number_input.move(self.number_input.x(), 
                               self.original_input_y - InputStyles.HEIGHT - 10)
        new_input_y = self.number_input.y() + InputStyles.HEIGHT + 10
        new_input = self.create_input(self.box, "Tilføj 2. CVR Nummer", 
                                      int((self.box.width() - InputStyles.WIDTH) / 2), new_input_y)
        new_input.show()
        self.additional_inputs.append(new_input)

        self.remove_input_btn = QPushButton("x", self.box)
        self.remove_input_btn.setGeometry(
            int((self.box.width() + InputStyles.WIDTH) / 2) + 5,
            new_input_y + 5,
            20, 30
        )
        self.remove_input_btn.setStyleSheet(RemoveInputButtonStyles.STYLESHEET)
        self.remove_input_btn.clicked.connect(self.removeNumberInputField)
        self.remove_input_btn.show()

        self.add_cvr_btn.hide()

    def removeNumberInputField(self):
        input_to_remove = self.additional_inputs.pop()
        input_to_remove.deleteLater()
        self.remove_input_btn.deleteLater()
        self.number_input.move(self.number_input.x(), self.original_input_y)
        self.add_cvr_btn.show()
