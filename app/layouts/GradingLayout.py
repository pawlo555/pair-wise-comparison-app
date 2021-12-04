from PyQt6.QtWidgets import QHBoxLayout, QLabel


class GradingLayout(QHBoxLayout):
    def __init__(self):
        super().__init__()
        label = QLabel("Tutaj dokonujemy porównań parami")
        self.addWidget(label)
