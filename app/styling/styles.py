from PyQt6.QtWidgets import QWidget


def setAppStylesheet(widget: QWidget):
    widget.setStyleSheet(
        "QMainWindow { background-color: #e3e3e3; border-radius: 20px; opacity: 100; border: 2px solid #00e0b7; "
        "margin: 7px } "
        
        "QWidget { font-family: Tahoma, sans-serif; }"
        
        "QPushButton { border: 5px; margin: 8px; padding: 8px; border-radius: 15px; background-color: #00e0b7; "
        "padding-left: 30px; padding-right: 30px;} "
        
        "QPushButton:hover { color: #59ffc5; background-color: #3d3d3d; } "
        
        "QLineEdit { border: 5px; margin: 8px; padding: 8px; border-radius: 15px; background-color: #bababa; }"
        
        "QListWidget { border: 5px; margin: 8px; padding: 8px; border-radius: 15px; background-color: #00e0b7}"
        "QListWidget > QWidget > QScrollBar { background: #00e0b7; border-radius: 10px; }"
        
        "QListWidgetItem {}"
        
        "QScrollArea { background: transparent; }"
        "QScrollArea > QWidget > QWidget { background: transparent; }"
        "QScrollArea > QWidget > QScrollBar { background: #00e0b7; border-radius: 10px; }"
        
        "QLabel { color: #292929;  font-family: Tahoma, sans-serif; }"
        
        "QLabel#titleLabel { color: #292929; font-size: 24px; padding-top: 20px; padding-bottom: 20px; }"
        
        "QMessageBox {  }"
        
        
        "QScrollArea {  border: 5px; margin: 8px; padding: 8px; border-radius: 15px; background: transparent; }"
        
        "QTableWidget { border: 5px; margin: 8px; padding: 8px; border-radius: 15px; }"
    )
