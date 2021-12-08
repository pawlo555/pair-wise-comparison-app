from PyQt6.QtWidgets import QHBoxLayout, QLabel


class MovieAddLayout(QHBoxLayout):
    def __init__(self):
        super().__init__()
        label = QLabel("Tutaj wybieramy filmy")
        self.addWidget(label)
