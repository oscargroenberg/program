#clickable_combo_box.py
from PyQt6.QtWidgets import QComboBox, QLineEdit
from PyQt6.QtCore import Qt
from style import ComboBoxStyles
from widgets.clickable_line_edit import ClickableLineEdit


class ClickableComboBox(QComboBox):
    DROPDOWN_WIDTH = ComboBoxStyles.DROPDOWN_WIDTH  # Define the DROPDOWN_WIDTH here

    def __init__(self, parent=None):
        super(ClickableComboBox, self).__init__(parent)
        self.setEditable(True)
        self.setLineEdit(ClickableLineEdit(self))
        self.lineEdit().clicked.connect(self.showPopup)
        
        # Adjust the viewport margins to remove the space around the list items
        listView = self.view()
        listView.setStyleSheet("QListView { padding: 0px; margin: 0px; }")

    def showPopup(self):
        popup = self.view().parentWidget()  # This gets the viewport's parent, which is the actual dropdown popup
        popup.setFixedWidth(self.DROPDOWN_WIDTH)
        super().showPopup()

        # Calculate the offset needed to center the dropdown
        offset = int((self.width() - self.DROPDOWN_WIDTH) / 2)
        popup.move(popup.x() + offset, popup.y())
