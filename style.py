class Colors: 
    ACTION_COLOR = "#f01245"
    ACTION_HOVER_COLOR = "#003253"
    ACTION_HOVER_DURATION = 150

    BACKGROUND_COLOR = "#f2f2f3"
    SECONDARY_BACKGROUND_COLOR = "#ffffff"

    LIGHT_TEXT_COLOR = "#FFFFFF"
    DARK_TEXT_COLOR = "#191919"
    
    COMBOBOX_BACKGROUND_COLOR = "#f2f2f3"
    COMBOBOX_BORDER_COLOR = "#d1d1d1"


class Sizing:
    WINDOW_WIDTH = 1000
    WINDOW_HEIGHT = 600
    
    INPUT_WIDTH = 215
    INPUT_HEIGHT = 50
    
    SUBMIT_BUTTON_WIDTH = 215
    SUBMIT_BUTTON_HEIGHT = 50
    
    RADIUS = 25
    
    COMBOBOX_WIDTH = 100
    COMBOBOX_HEIGHT = 50
    

    
class ComboBoxStyles:
    WIDTH = Sizing.COMBOBOX_WIDTH
    HEIGHT = Sizing.COMBOBOX_HEIGHT
    DROPDOWN_WIDTH = Sizing.COMBOBOX_WIDTH - 20  # Adjust as needed
    HOVER_COLOR = "#e6e6e7"  # Background color when hovering

    STYLESHEET = f"""
        QComboBox {{
            background-color: {Colors.COMBOBOX_BACKGROUND_COLOR};
            border: 1px solid {Colors.COMBOBOX_BORDER_COLOR};
            border-radius: {Sizing.RADIUS}px;
            font-size: 16px;
            padding: 0px;
        }}
        QComboBox::drop-down {{
            width: 0px;
        }}
        QComboBox::down-arrow {{
            image: none;
        }}
        QComboBox::indicator {{
            width: 0px;
            height: 0px;
        }}
        QComboBox QAbstractItemView {{
            border: none;
            background-color: transparent;
            padding-left: 0px;
            padding-right: 0px;
            outline: 0px;
            margin: 0px;
            min-width: {DROPDOWN_WIDTH}px;
            max-width: {DROPDOWN_WIDTH}px;
        }}
        QComboBox QAbstractItemView::item {{
            background-color: transparent;
            padding: 0px 0px;
            margin: 0px;
            color: {Colors.DARK_TEXT_COLOR};  /* Set text color to black for normal items */
        }}
        QComboBox QAbstractItemView::item:selected {{
            background-color: {HOVER_COLOR};
            color: {Colors.DARK_TEXT_COLOR};  /* Text color for selected items */
            outline: none;  /* Remove the dotted border when selected */
        }}
        QComboBox QAbstractItemView::item:hover {{
            background-color: {HOVER_COLOR};
            selection-background-color: {HOVER_COLOR};
            border: none;
        }}
    """

class InputStyles:
    WIDTH = Sizing.INPUT_WIDTH
    HEIGHT = Sizing.INPUT_HEIGHT
    STYLESHEET = f"""
        QLineEdit {{
            background-color: {Colors.SECONDARY_BACKGROUND_COLOR};
            border: 1px solid {Colors.COMBOBOX_BORDER_COLOR};
            border-radius: {Sizing.RADIUS}px;
            font-size: 16px;
            padding: 5px;
        }}
    """






class ButtonStyles:
    FONT_SIZE = 18
    FONT_WEIGHT = "bold"
    STYLESHEET = f"""
        QPushButton {{
            background-color: {Colors.ACTION_COLOR};
            color: {Colors.LIGHT_TEXT_COLOR};
            border-radius: {Sizing.RADIUS}px;
            font-size: {FONT_SIZE}px;
            font-weight: {FONT_WEIGHT};
        }}
    """