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
from visma_løn_login import visma_løn_login_func

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.additional_inputs = []
        self.input_fields_count = 0 
        self.init_ui()
        self.input_fields = []
        self.additional_inputs_box2 = []
        self.original_box_height = self.box.height()
        self.load_input_fields()


    def init_ui(self):
        self.setup_window()
        self.setup_boxes()
        self.setup_title()
        self.setup_box2_title()
        self.setup_new_text_input()
        self.setup_number_input()
        self.setup_visma_username()
        self.setup_visma_password()
        self.setup_year_input()
        self.setup_add_cvr_button()
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
        self.box = self.setup_box(25, 25, 300, 490)
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

        
    def setup_new_text_input(self):
        title_bottom = self.title_label.y() + self.title_label.height() + 10  # 10 is a margin
        self.new_text_input = self.create_input(self.box, "Mit-ID",
                                                int((self.box.width() - InputStyles.WIDTH) / 2),
                                                title_bottom)
   

    def setup_number_input(self):
        new_text_input_bottom = self.new_text_input.y() + self.new_text_input.height() + 10  # 10 is a margin
        self.number_input = self.create_input(self.box, "1. CVR",
                                            int((self.box.width() - InputStyles.WIDTH) / 2),
                                            new_text_input_bottom)
        number_validator = QRegularExpressionValidator(QRegularExpression(r"^\d+$"))
        self.number_input.setValidator(number_validator)
        return self.number_input.text()


    def setup_visma_username(self):
        new_text_input_bottom = self.new_text_input.y() + self.new_text_input.height() + 70  # 10 is a margin
        self.first_additional_input = self.create_input(self.box, "VismaLøn Brugernavn",
                                                        int((self.box.width() - InputStyles.WIDTH) / 2),
                                                        new_text_input_bottom)
        return self.first_additional_input.text()

    def setup_visma_password(self):
        first_additional_input_bottom = self.first_additional_input.y() + self.first_additional_input.height() + 10  # 10 is a margin
        self.second_additional_input = self.create_input(self.box, "VismaLøn Password",
                                                        int((self.box.width() - InputStyles.WIDTH) / 2),
                                                        first_additional_input_bottom)
        return self.second_additional_input.text()







    def setup_year_input(self):
        number_input_bottom = self.number_input.y() + self.number_input.height() + 130  # 10 is a margin
        self.year_input = self.create_input(self.box, "År",
                                            int((self.box.width() - InputStyles.WIDTH) / 2),
                                            number_input_bottom)
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
        start_y = self.combo2.y() + self.combo2.height() + 10  # Start below the combo2
        self.submit_btn = HoverButton("Start", self.box)
        self.submit_btn.setGeometry(
            int((self.box.width() - Sizing.SUBMIT_BUTTON_WIDTH) / 2),
            start_y,
            Sizing.SUBMIT_BUTTON_WIDTH,
            Sizing.SUBMIT_BUTTON_HEIGHT
        )
        self.submit_btn.clicked.connect(self.on_submit_button_clicked)

    def on_submit_button_clicked(self):    
        
        brugernavn_value = self.first_additional_input.text()
        password_value = self.second_additional_input.text()
        cvr_value = self.number_input.text()
        visma_løn_login_func(brugernavn_value, password_value, cvr_value)  # Connect the clicked signal to print_input_values
        
    
    
    
    
    #Setup for Combo Boxes
    
    def setup_box2_title(self):
        self.setup_title(self.box2, "CVR Numrer")
    
    
        
    def setup_combo_boxes(self):
        start_x = int((self.box.width() - 2 * ComboBoxStyles.WIDTH - 15) / 2)
        start_y = self.year_input.y() + self.year_input.height() + 10  # Start below the year_input
        
        # Setup for combo1
        self.combo1 = ClickableComboBox(self.box)
        self.combo1.setEditable(True)
        self.combo1.lineEdit().setReadOnly(True)
        self.combo1.lineEdit().setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.combo1.setGeometry(
            start_x,
            start_y,
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
            start_y,
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
        # Store the original y-coordinates if they haven't been stored yet
        if not hasattr(self, 'original_year_input_y'):
            self.original_year_input_y = self.year_input.y()
        if not hasattr(self, 'original_first_additional_input_y'):
            self.original_first_additional_input_y = self.first_additional_input.y()
        if not hasattr(self, 'original_second_additional_input_y'):
            self.original_second_additional_input_y = self.second_additional_input.y()

        # Calculate the new y-coordinate for the year_input
        year_input_new_y = self.original_year_input_y + InputStyles.HEIGHT + 10
        self.year_input.move(self.year_input.x(), year_input_new_y)

        # Create the new input field directly below the first CVR input
        new_input_y = self.number_input.y() + self.number_input.height() + 10  # Added a 10-pixel gap for spacing
        new_input = self.create_input(self.box, "2. CVR",
                                    int((self.box.width() - InputStyles.WIDTH) / 2), new_input_y)
        new_input.show()
        self.additional_inputs.append(new_input)

        # Move the additional inputs down
        self.first_additional_input.move(self.first_additional_input.x(), self.original_first_additional_input_y + InputStyles.HEIGHT + 10)
        self.second_additional_input.move(self.second_additional_input.x(), self.original_second_additional_input_y + InputStyles.HEIGHT + 10)

        # Increase the height of the box
        self.box.setFixedHeight(self.box.height() + InputStyles.HEIGHT + 10)

        # Move the comboboxes and submit button down
        self.combo1.move(self.combo1.x(), self.combo1.y() + InputStyles.HEIGHT + 10)
        self.combo2.move(self.combo2.x(), self.combo2.y() + InputStyles.HEIGHT + 10)
        self.submit_btn.move(self.submit_btn.x(), self.submit_btn.y() + InputStyles.HEIGHT + 10)

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
        self.mousePressEvent(None)  # Clear focus from any widget


    def removeNumberInputField(self):
        if self.additional_inputs:  # Check if the list is not empty
            input_to_remove = self.additional_inputs.pop()
            input_to_remove.deleteLater()

            # Move the year_input back to its original position
            if hasattr(self, 'original_year_input_y'):
                self.year_input.move(self.year_input.x(), self.original_year_input_y)

            # Move the comboboxes, submit button, and additional inputs up
            self.combo1.move(self.combo1.x(), self.combo1.y() - InputStyles.HEIGHT - 10)
            self.combo2.move(self.combo2.x(), self.combo2.y() - InputStyles.HEIGHT - 10)
            self.submit_btn.move(self.submit_btn.x(), self.submit_btn.y() - InputStyles.HEIGHT - 10)
            self.first_additional_input.move(self.first_additional_input.x(), self.first_additional_input.y() - InputStyles.HEIGHT - 10)
            self.second_additional_input.move(self.second_additional_input.x(), self.second_additional_input.y() - InputStyles.HEIGHT - 10)

            # Restore the original height of the box
            self.box.setFixedHeight(self.original_box_height)

            self.add_cvr_btn.show()

            # Delete the remove_input_btn
            if hasattr(self, 'remove_input_btn') and self.remove_input_btn:
                self.remove_input_btn.deleteLater()
                del self.remove_input_btn  # Explicitly delete the reference





    def mousePressEvent(self, event):
        focused_widget = QApplication.instance().focusWidget()
        if isinstance(focused_widget, (QLineEdit, QComboBox)):
            focused_widget.clearFocus()
        if event:  # Check if event is not None before calling the superclass method
            super().mousePressEvent(event)

        
        
        
    def setup_add_item_button(self):
        self.add_item_btn = HoverButton("Tilføj CVR", self.box2)
        self.add_item_btn.setGeometry(
            int((self.box2.width() - Sizing.SUBMIT_BUTTON_WIDTH) / 2),
            int(self.box2.height() - Sizing.SUBMIT_BUTTON_HEIGHT - 20),
            Sizing.SUBMIT_BUTTON_WIDTH,
            Sizing.SUBMIT_BUTTON_HEIGHT
        )
        self.add_item_btn.setStyleSheet(ButtonStyles.STYLESHEET)
        self.add_item_btn.clicked.connect(self.add_input_fields)

    
    
    
    def load_input_fields(self):
        json_file_path = os.path.join('json_files', 'cvr.json')
        if os.path.exists(json_file_path):
            with open(json_file_path, 'r') as f:
                data = json.load(f)
                for entry in data:
                    text = str(entry.get('text', ''))
                    number = str(entry.get('number', ''))
                    self.add_input_fields(text=text, number=number)

    def add_input_fields(self, *, text='', number=''):
        # Ensure text and number are strings
        text = str(text)
        number = str(number)
        # Check if the maximum number of input fields has been reached
        if hasattr(self, 'additional_inputs_box2') and len(self.additional_inputs_box2) >= 10:
            return  # Exit the function

        # Calculate the starting y-coordinate for the new input fields
        start_y = 50  # You can adjust this value as needed
        
        # If there are already input fields present, adjust the start_y value
        if hasattr(self, 'additional_inputs_box2') and self.additional_inputs_box2:
            last_input_field = self.additional_inputs_box2[-1]
            start_y = last_input_field[0].y() + last_input_field[0].height() + 22
        
        input_width = int((Sizing.INPUT_WIDTH - 5) / 2)  # Adjusted input width to include space
        input_height = 20  # Set a fixed height for the input fields
        
        # Define the stylesheet with adjusted padding for placeholder text
        adjusted_style = InputFieldStyles.STYLESHEET + "padding-top: -50px;"  # Adjust the padding as needed
        
        # Create the text input field
        text_input = QLineEdit(self.box2)
        text_input.setGeometry(30, start_y, input_width, input_height)
        text_input.setPlaceholderText("Firma")

        # Set a validator to allow only letters and spaces, and limit to 8 characters
        text_validator = QRegularExpressionValidator(QRegularExpression(r"^[a-zA-Z\s]{0,8}$"))
        text_input.setValidator(text_validator)

        text_input.setStyleSheet(adjusted_style)  # Apply adjusted styling
        text_input.textChanged.connect(lambda: self.update_json_file())  # Connect textChanged signal
        text_input.show()
        text_input.setText(text)  # Set the text of the input field

        # Create the number input field
        number_input = QLineEdit(self.box2)
        number_input.setGeometry(30 + input_width + 5, start_y, input_width, input_height)  # Adjusted x position
        number_input.setPlaceholderText("CVR")
        number_validator = QRegularExpressionValidator(QRegularExpression(r"^\d{0,8}$"))
        number_input.setValidator(number_validator)
        number_input.setStyleSheet(adjusted_style)  # Apply adjusted styling
        number_input.textChanged.connect(lambda: self.validate_number_input() and self.update_json_file())  # Connect textChanged signal
        number_input.show()
        number_input.setText(number)  # Set the text of the input field
        
        # Create the delete button
        delete_button = QPushButton('X', self.box2)
        delete_button.setGeometry(30 + input_width * 2 + 10, start_y - 10, 30, 30)  # Moved up by 10px
        delete_button.setStyleSheet(DeleteButtonStyles.STYLESHEET)
        delete_button.clicked.connect(lambda: self.delete_input_fields(text_input, number_input, delete_button))
        delete_button.show()
        
        # Store the input fields and delete button in a list for future reference
        if not hasattr(self, 'additional_inputs_box2'):
            self.additional_inputs_box2 = []
        self.additional_inputs_box2.append((text_input, number_input, delete_button))

        # Add the input fields to the JSON file
        self.update_json_file()


    def update_json_file(self):
        if not self.validate_number_input():
            return  # Skip updating if total digit count exceeds 8

        # Define the path to the JSON file
        json_file_path = os.path.join('json_files', 'cvr.json')

        # Prepare the data to be written to the JSON file
        data = []
        if hasattr(self, 'additional_inputs_box2'):
            for text_input, number_input, _ in self.additional_inputs_box2:
                text = text_input.text()
                number = number_input.text()
                data.append({'text': text, 'number': number})

        # Write the updated data back to the JSON file
        with open(json_file_path, 'w') as f:
            json.dump(data, f, indent=4)
            
    def validate_number_input(self):
        total_characters = sum(len(input_field.text()) for input_field, _, _ in self.additional_inputs_box2)
        total_digits = sum(len(number_input.text()) for _, number_input, _ in self.additional_inputs_box2)
        
        return total_characters <= 8 and total_digits <= 8





    def delete_input_fields(self, text_input, number_input, delete_button):
        # Find the index of the input fields to be deleted
        index = self.additional_inputs_box2.index((text_input, number_input, delete_button))
        
        # Delete the input fields and button
        text_input.deleteLater()
        number_input.deleteLater()
        delete_button.deleteLater()
        
        # Remove the input fields and button from the list
        del self.additional_inputs_box2[index]
        
        # Move up all input fields and buttons that come after the deleted one
        for i in range(index, len(self.additional_inputs_box2)):
            text, number, button = self.additional_inputs_box2[i]
            y = text.y() - text.height() - 22  # Calculate new y position
            text.setGeometry(text.x(), y, text.width(), text.height())
            number.setGeometry(number.x(), y, number.width(), number.height())
            button.setGeometry(button.x(), y - 10, button.width(), button.height())  # Adjust for delete button's offset

        # Delete the input fields from the JSON file
        self.delete_from_json_file(index)

    def delete_from_json_file(self, index):
        # Define the path to the JSON file
        json_file_path = os.path.join('json_files', 'cvr.json')

        # Check if the JSON file exists
        if not os.path.exists(json_file_path):
            return  # Exit the function if the file does not exist

        # Read the existing data from the JSON file
        with open(json_file_path, 'r') as f:
            data = json.load(f)

        # Check if the index is valid
        if index < 0 or index >= len(data):
            return  # Exit the function if the index is invalid

        # Remove the input fields at the specified index from the data
        del data[index]

        # Write the updated data back to the JSON file
        with open(json_file_path, 'w') as f:
            json.dump(data, f, indent=4)
            
            
            
            
            
        
        
        
    def print_input_values(self):
        mit_id = self.new_text_input.text()
        cvr1 = self.number_input.text()
        cvr2 = self.additional_inputs[0].text() if self.additional_inputs else ""
        vismalon_username = self.first_additional_input.text()
        vismalon_password = self.second_additional_input.text()
        year = self.year_input.text()
        month1 = self.combo1.currentText()
        month2 = self.combo2.currentText()

        print(f"Mit-ID: {mit_id}, 1. CVR: {cvr1}, 2. CVR: {cvr2}, VismaLøn Brugernavn: {vismalon_username}, "
              f"VismaLøn Password: {vismalon_password}, Year: {year}, Month 1: {month1}, Month 2: {month2}")
        # Clear all input fields
        self.new_text_input.clear()
        self.number_input.clear()
        if self.additional_inputs:
            self.additional_inputs[0].clear()
        self.first_additional_input.clear()
        self.second_additional_input.clear()
        self.year_input.clear()