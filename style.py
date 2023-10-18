# Colors
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
    HOVER_COLOR = "#e6e6e7"  # Background color when hovering

# Sizing
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
    DROPDOWN_WIDTH = COMBOBOX_WIDTH - 20  # Adjust as needed

# ComboBox Styles
class ComboBoxStyles:
    WIDTH = Sizing.COMBOBOX_WIDTH
    HEIGHT = Sizing.COMBOBOX_HEIGHT
    DROPDOWN_WIDTH = Sizing.COMBOBOX_WIDTH - 20  # Adjust as needed
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
            min-width: {Sizing.DROPDOWN_WIDTH}px;
            max-width: {Sizing.DROPDOWN_WIDTH}px;
        }}
        QComboBox QAbstractItemView::item {{
            background-color: transparent;
            padding: 0px 0px;
            margin: 0px;
            color: {Colors.DARK_TEXT_COLOR};
        }}
        QComboBox QAbstractItemView::item:selected {{
            background-color: {Colors.HOVER_COLOR};
            color: {Colors.DARK_TEXT_COLOR};
        }}
        QComboBox QAbstractItemView::item:hover {{
            background-color: {Colors.HOVER_COLOR};
            selection-background-color: {Colors.HOVER_COLOR};
            border: none;
        }}
    """

# Input Styles
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

# Button Styles
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

# Box Styles
class BoxStyles:
    STYLESHEET = f"""
        background-color: {Colors.SECONDARY_BACKGROUND_COLOR};
        border-radius: {Sizing.RADIUS}px;
    """

# Remove Input Button Styles
class RemoveInputButtonStyles:
    STYLESHEET = """
        background-color: transparent; 
        color: red; 
        font-size: 16px; 
        font-weight: bold; 
        border: none;
    """



class Box2AddCVRButtonStyles:
    STYLESHEET = """
        QPushButton {
            background-color: #4CAF50;  # Green background
            color: #FFFFFF;  # White text
            border-radius: 15px;  # Rounded corners
            font-size: 16px;  # Font size
        }
        QPushButton:hover {
            color: #E0E0E0;  # Lighter text color on hover
        }
    """


