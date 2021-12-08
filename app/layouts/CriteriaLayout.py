from PyQt6.QtWidgets import QHBoxLayout, QLabel


class CriteriaLayout(QHBoxLayout):
    def __init__(self):
        super().__init__()
        label = QLabel("Tutaj wybieramy kryteria")
        self.addWidget(label)
