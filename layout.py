from PyQt6.QtWidgets import QMainWindow, QWidget, QPushButton, QLineEdit, QComboBox, QLabel, QApplication, QMessageBox
from PyQt6.QtCore import Qt, QRegularExpression, QSize, QEvent
from PyQt6.QtGui import QRegularExpressionValidator, QIcon
import json
from style import (Colors, Sizing, ComboBoxStyles, InputStyles, BoxStyles, RemoveInputButtonStyles, ButtonStyles, PlusButtonStyles, InputFieldStyles, DeleteButtonStyles)
from widgets.hover_button import HoverButton
from widgets.clickable_line_edit import ClickableLineEdit
from widgets.clickable_combo_box import ClickableComboBox
from functools import partial
import os

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.additional_inputs = []
        self.input_fields_count = 0 
        self.init_ui()
        self.input_fields = []  # List to store all input fields
        self.load_data_and_populate_fields()

    def init_ui(self):
        self.setup_window()
        self.setup_boxes()
        self.setup_title()
        self.setup_box2_title()
        self.setup_number_input()
        self.setup_add_cvr_button()
        self.setup_year_input()
        self.setup_combo_boxes()
        self.setup_submit_button()
        self.setup_add_item_button()
        self.delete_buttons = []

    # Window Setup
    def setup_window(self):
        self.setWindowTitle("Visma...")
        self.setGeometry(100, 100, Sizing.WINDOW_WIDTH, Sizing.WINDOW_HEIGHT)

    # Box Setups
    def setup_boxes(self):
        self.box = self.setup_box(25, 25, 300, 550)
        self.box2 = self.setup_box(350, 25, 300, 550)

    def setup_box(self, x, y, width, height):
        box = QWidget(self)
        box.setGeometry(x, y, width, height)
        box.setStyleSheet(BoxStyles.STYLESHEET)
        return box

    # Title Setups
    def setup_titles(self):
        self.setup_title(self.box, "Form")
        self.setup_title(self.box2, "CVR Numrer")

    def setup_title(self, parent_box=None, title_text="Form"):
        if parent_box is None:
            parent_box = self.box
        self.title_label = QLabel(title_text, parent_box)
        title_width = 200
        title_height = 40
        title_x = int((parent_box.width() - title_width) / 2)
        title_y = 10
        self.title_label.setGeometry(
            title_x, title_y, title_width, title_height)
        self.title_label.setStyleSheet(
            "font-size: 24px; font-weight: bold; color: " + Colors.DARK_TEXT_COLOR)
        self.title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.title_label.raise_()
        self.title_label.show()


    # Input Setups
    def setup_inputs(self):
        self.setup_number_input()
        self.setup_year_input()

    def setup_number_input(self):
        self.number_input = self.create_input(self.box, "CVR Nummer",
                                              int((self.box.width() - InputStyles.WIDTH) / 2),
                                              int(self.box.height() - 5 * Sizing.SUBMIT_BUTTON_HEIGHT))
        number_validator = QRegularExpressionValidator(QRegularExpression(r"^\d+$"))
        self.number_input.setValidator(number_validator)

    def setup_year_input(self):
        self.year_input = self.create_input(self.box, "År",
                                            int((self.box.width() - InputStyles.WIDTH) / 2),
                                            int(self.box.height() - 3 * Sizing.SUBMIT_BUTTON_HEIGHT - 40))
        year_validator = QRegularExpressionValidator(QRegularExpression(r"^\d{4}$"))
        self.year_input.setValidator(year_validator)

    # Button Setups
    def setup_buttons(self):
        self.setup_add_cvr_button()
        self.setup_submit_button()

    def setup_add_cvr_button(self):
        self.add_cvr_btn = QPushButton("+", self.box)
        self.add_cvr_btn.setGeometry(
            int((self.box.width() + InputStyles.WIDTH) / 2) + 5,
            int(self.number_input.y() + (InputStyles.HEIGHT - 30) / 2),
            30, 30
        )
        self.add_cvr_btn.setStyleSheet(PlusButtonStyles.STYLESHEET)
        self.add_cvr_btn.clicked.connect(self.addNumberInputField)

    def setup_submit_button(self):
        self.submit_btn = HoverButton("Start", self.box)
        self.submit_btn.setGeometry(
            int((self.box.width() - Sizing.SUBMIT_BUTTON_WIDTH) / 2),
            int(self.box.height() - Sizing.SUBMIT_BUTTON_HEIGHT - 20),
            Sizing.SUBMIT_BUTTON_WIDTH,
            Sizing.SUBMIT_BUTTON_HEIGHT
        )
        self.submit_btn.clicked.connect(self.printYearAndMonths)
        
    
    
    
    
    #Setup for Combo Boxes
    
    def setup_box2_title(self):
        self.setup_title(self.box2, "CVR Numrer")
    
    
        
    def setup_combo_boxes(self):
        start_x = int((self.box.width() - 2 * ComboBoxStyles.WIDTH - 15) / 2)
        
        # Setup for combo1
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

        # Setup for combo2
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

        # Load data into the comboboxes
        self.load_combo_box_data()
        self.combo2.setCurrentText("Dec")



    # Utility Functions
    def create_input(self, parent, placeholder, x, y):
        input_field = QLineEdit(parent)
        input_field.setPlaceholderText(placeholder)
        input_field.setAlignment(Qt.AlignmentFlag.AlignCenter)
        input_field.setGeometry(x, y, InputStyles.WIDTH, InputStyles.HEIGHT)
        input_field.setStyleSheet(InputStyles.STYLESHEET)
        return input_field

    def load_combo_box_data(self):
        with open(os.path.join('json_files', 'months.json'), 'r') as file:
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
        new_input = self.create_input(self.box, "2. CVR",
                                    int((self.box.width() - InputStyles.WIDTH) / 2), new_input_y)
        new_input.show()
        self.additional_inputs.append(new_input)

        # Delete the old remove_input_btn if it exists
        if hasattr(self, 'remove_input_btn') and self.remove_input_btn:
            self.remove_input_btn.deleteLater()

        # Create the new styled remove_input_btn to match the "x" button in box2
        self.remove_input_btn = QPushButton("", self.box)
        icon_path = os.path.join("images", "cross_good.png")
        self.remove_input_btn.setIcon(QIcon(icon_path))
        
        self.remove_input_btn.setIconSize(QSize(10, 10))  # Adjust the size as needed

        self.remove_input_btn.setGeometry(
            int((self.box.width() + InputStyles.WIDTH) / 2) + 5,
            new_input_y + 10,
            30, 30  # Adjusted width and height to make it square
        )
        self.remove_input_btn.setStyleSheet("background-color: red; color: white; border: none; font-size:18px; border-radius: 15px;")  # Styling to match the "x" button in box2
        self.remove_input_btn.clicked.connect(self.removeNumberInputField)
        self.remove_input_btn.show()

        self.add_cvr_btn.hide()


    def removeNumberInputField(self):
        if self.additional_inputs:  # Check if the list is not empty
            input_to_remove = self.additional_inputs.pop()
            input_to_remove.deleteLater()
            self.number_input.move(self.number_input.x(), self.original_input_y)
            self.add_cvr_btn.show()

            # Delete the remove_input_btn
            if hasattr(self, 'remove_input_btn') and self.remove_input_btn:
                self.remove_input_btn.deleteLater()
                del self.remove_input_btn  # Explicitly delete the reference

    def mousePressEvent(self, event):
        focused_widget = QApplication.instance().focusWidget()
        if isinstance(focused_widget, (QLineEdit, QComboBox)):
            focused_widget.clearFocus()
        super().mousePressEvent(event)
        
        
        
    def setup_add_item_button(self):
        self.add_item_btn = QPushButton("Tilføj CVR", self.box2)
        self.add_item_btn.setGeometry(
            int((self.box2.width() - Sizing.SUBMIT_BUTTON_WIDTH) / 2),
            int(self.box2.height() - Sizing.SUBMIT_BUTTON_HEIGHT - 20),
            Sizing.SUBMIT_BUTTON_WIDTH,
            Sizing.SUBMIT_BUTTON_HEIGHT
        )
        self.add_item_btn.setStyleSheet(ButtonStyles.STYLESHEET)
        self.add_item_btn.clicked.connect(self.add_new_input_field)



    def load_data_and_populate_fields(self):
        try:
            filepath = os.path.join('json_files', 'cvr.json')
            with open(filepath, 'r') as file:
                data = json.load(file)
            
            for item in data:
                self.add_new_input_field(item["data"])
        except FileNotFoundError:
            pass  # Handle the case where the file doesn't exist yet

    def add_new_input_field(self, text=None):
        if self.input_fields_count < 10:  # Limit to 10 input fields
            y_coordinate = 50 + self.input_fields_count * (Sizing.INPUT_HEIGHT - 10)
            new_input = QLineEdit(self.box2)
            new_input.setGeometry(
                int((self.box2.width() - Sizing.INPUT_WIDTH) / 2),
                y_coordinate,
                Sizing.INPUT_WIDTH,
                Sizing.INPUT_HEIGHT
            )
            new_input.setStyleSheet(InputFieldStyles.STYLESHEET)
            
            # Set the validator to ensure 8 digits
            eight_digit_validator = QRegularExpressionValidator(QRegularExpression(r"^\d{8}$"))
            new_input.setValidator(eight_digit_validator)
            
            new_input.editingFinished.connect(self.save_to_json)
            if text:  # If text is provided, set it
                new_input.setText(text)
            new_input.show()
            self.input_fields.append(new_input)  # Add the new input to the list

            # Create delete button
            delete_button = QPushButton("X", self.box2)
            delete_button.setGeometry(
                new_input.x() + new_input.width() + 5,
                y_coordinate,
                30,  # Width of the delete button
                Sizing.INPUT_HEIGHT
            )
            delete_button.setStyleSheet(DeleteButtonStyles.STYLESHEET)
            delete_button.clicked.connect(partial(self.delete_input_field, new_input, delete_button))
            delete_button.show()

            # Add the delete button to the list
            self.delete_buttons.append(delete_button)

            self.input_fields_count += 1

    def delete_input_field(self, input_field, delete_button):
        # Get the index of the input field before removing it
        index = self.input_fields.index(input_field)

        # Remove the input field and its delete button
        self.input_fields.remove(input_field)
        self.delete_buttons.remove(delete_button)  # Remove the delete button from the list
        input_field.deleteLater()
        delete_button.deleteLater()

        # Adjust positions of the remaining input fields and their delete buttons
        for i in range(index, len(self.input_fields)):
            current_input = self.input_fields[i]
            current_input.move(current_input.x(), current_input.y() - (Sizing.INPUT_HEIGHT - 10))
            # Adjust the position and set a fixed height for the delete button as well
            current_delete_button = self.delete_buttons[i]
            current_delete_button.setGeometry(
                current_input.x() + current_input.width() + 5,
                current_input.y(),
                30,  # Width of the delete button
                30   # Fixed height of 30px
            )

        self.input_fields_count -= 1

        # Save the data to the JSON file
        self.save_to_json()
        
        # Repaint the widget to ensure the changes are immediately visible
        self.repaint()






    def save_to_json(self):
        data = [{"data": input_field.text()} for input_field in self.input_fields]
        filepath = os.path.join('json_files', 'cvr.json')
        with open(filepath, 'w') as file:
            json.dump(data, file)