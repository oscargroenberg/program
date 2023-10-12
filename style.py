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
            border: none;
        }}
        QComboBox::down-arrow {{
            image: none;
        }}
        
        QComboBox QAbstractItemView {{
            border: 2px solid darkgray;
            selection-background-color: #f01245;
            background-color: #ffffff;
            border-radius: 25px;
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
