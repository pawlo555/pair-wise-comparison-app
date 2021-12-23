from PyQt6.QtWidgets import QWidget


def setAppStylesheet(widget: QWidget):
    widget.setStyleSheet(
        "QMainWindow { background-color: #2b2a28; border-radius: 20px; opacity: 100; border: 2px solid #ff8f26; "
        "margin: 7px } "
        
        "QWidget { font-family: Tahoma, sans-serif; }"
        
        "QPushButton { border: 5px; margin: 8px; padding: 8px; border-radius: 15px; background-color: #ff8f26; "
        "padding-left: 30px; padding-right: 30px;} "
        
        "QPushButton:hover { color: #2b2a28; background-color: #e0dedc; } "
        
        "QLineEdit { border: 5px; margin: 8px; padding: 8px; border-radius: 15px; background-color: #c2b7ac}"
        
        "QListWidget { border: 5px; margin: 8px; padding: 8px; border-radius: 15px; background-color: #ff8f26}"
        "QListWidget > QWidget > QScrollBar { background: #ff8f26; border-radius: 10px; }"
        
        "QListWidgetItem {}"
        
        "QScrollArea { background: transparent; }"
        "QScrollArea > QWidget > QWidget { background: transparent; }"
        "QScrollArea > QWidget > QScrollBar { background: #ff8f26; border-radius: 10px; }"
        
        "QLabel { color: #e0dedc;  font-family: Tahoma, sans-serif; }"
        
        "QLabel#titleLabel { color: #e0dedc; font-size: 24px; padding-top: 20px; padding-bottom: 20px; }"
        
        "QMessageBox {  }"
        
        
        "QScrollArea {  border: 5px; margin: 8px; padding: 8px; border-radius: 15px; background: transparent; }"
        
        "QTableWidget { border: 5px; margin: 8px; padding: 8px; border-radius: 15px; }"
    )
