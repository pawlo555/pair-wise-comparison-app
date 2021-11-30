from PyQt6.QtWidgets import QHBoxLayout, QPushButton


class DecisionCreator(QHBoxLayout):
    def __init__(self):
        super().__init__()
        button = QPushButton("Something")
        self.addWidget(button)
        button2 = QPushButton("XD")
        self.addWidget(button2)


if __name__ == '__main__':
    creator = DecisionCreator()
