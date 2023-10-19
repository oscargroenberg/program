from PyQt6.QtWidgets import QMainWindow, QWidget, QPushButton, QLineEdit, QComboBox, QLabel, QApplication
from PyQt6.QtCore import Qt, QRegularExpression, QSize
from PyQt6.QtGui import QRegularExpressionValidator, QIcon
import json
from style import (Colors, Sizing, ComboBoxStyles, InputStyles, BoxStyles, RemoveInputButtonStyles, ButtonStyles,
                   Box2AddCVRButtonStyles, PlusButtonStyles, DeleteButtonStyles, CopyButtonStyles, SecondPlusButtonStyles)
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
        self.setup_boxes()
        self.setup_title()
        self.setup_box2_title()
        self.setup_number_input()
        self.setup_add_cvr_button()
        self.setup_year_input()
        self.setup_combo_boxes()
        self.setup_submit_button()

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
        with open('json_files\months.json', 'r') as file:
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
        self.remove_input_btn.setIcon(QIcon("images\cross_good.png"))
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

    def add_cvr_to_json(self):
        """Add the CVR from the input field to cvr.json and refresh the display."""
        if hasattr(self, 'box2_number_input'):
            cvr_number = self.box2_number_input.text()
            if cvr_number:
                try:
                    with open('json_files\cvr.json', 'r+') as file:
                        try:
                            data = json.load(file)
                        except json.JSONDecodeError:
                            data = []
                        data.append({"CVR": cvr_number})
                        file.seek(0)
                        json.dump(data, file, indent=4)
                        file.truncate()
                    self.box2_show_number_input()  # Refresh the display
                except Exception as e:
                    print(f"Error while processing the JSON file: {e}")
        else:
            print("Error: CVR input field not found.")

    def remove_cvr_input(self):
        # Check if the object exists before trying to delete
        if hasattr(self, 'box2_number_input'):
            self.box2_number_input.deleteLater()
            del self.box2_number_input  # Explicitly delete the reference

        if hasattr(self, 'box2_checkmark_btn'):
            self.box2_checkmark_btn.deleteLater()
            del self.box2_checkmark_btn

        if hasattr(self, 'box2_x_btn'):
            self.box2_x_btn.deleteLater()
            del self.box2_x_btn

    def delete_cvr(self, cvr):
        """Delete the specified CVR from cvr.json and refresh the display."""
        try:
            with open('json_files\cvr.json', 'r+') as file:
                data = json.load(file)
                data = [entry for entry in data if entry["CVR"] != cvr]
                file.seek(0)
                json.dump(data, file, indent=4)
                file.truncate()
            self.box2_show_number_input()  # Refresh the display
        except Exception as e:
            print(f"Error while processing the JSON file: {e}")

    def copy_cvr_to_clipboard(self, cvr):
        """Copy the specified CVR to the clipboard."""
        clipboard = QApplication.clipboard()
        clipboard.setText(cvr)
