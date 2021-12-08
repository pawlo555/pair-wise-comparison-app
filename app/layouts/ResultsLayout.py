from PyQt6.QtWidgets import QHBoxLayout, QLabel


class ResultsLayout(QHBoxLayout):
    def __init__(self):
        super().__init__()
        label = QLabel("Tutaj pokazujemy wyniki")
        self.addWidget(label)
