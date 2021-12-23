from PyQt6 import QtCore
from PyQt6.QtWidgets import QVBoxLayout, QLabel, QScrollArea, QWidget


class ScrollableLabel(QScrollArea):
    def __init__(self, *args, **kwargs):
        QScrollArea.__init__(self, *args, **kwargs)

        self.setWidgetResizable(True)

        content = QWidget(self)
        self.setWidget(content)

        layout = QVBoxLayout(content)
        self.label = QLabel(content)
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeft | QtCore.Qt.AlignmentFlag.AlignTop)
        self.label.setWordWrap(True)

        layout.addWidget(self.label)

    def setText(self, text):
        self.label.setText(text)
