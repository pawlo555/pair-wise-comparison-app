from PyQt5.QtCore import Qt
from PyQt6 import QtCore, QtGui
from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox, QSizePolicy, \
    QListWidget, QListWidgetItem


class MovieAddWidget(QWidget):
    """
        Widget to add new movies to movies list
    """
    def __init__(self, parent, dataManager, nextLayoutTrigger):
        super().__init__(parent)

        self.dataManager = dataManager
        self.mainLayout = QVBoxLayout()
        self.inputLayout = QHBoxLayout()
        self.mainLayout.addStretch(1)
        self.inputLayout.addStretch()

        # Title
        titleLabel = QLabel(self)
        titleLabel.setFont(QFont("SansSerif", 20))
        titleLabel.setText("Type movie title:")
        titleLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.mainLayout.addWidget(titleLabel)

        # List of picked movies
        self.pickedMovies = QListWidget(self)
        self.mainLayout.addWidget(self.pickedMovies)

        # Input field
        self.input = QLineEdit(self)
        self.inputLayout.addWidget(self.input)

        # Input confirmation button
        self.confirmButton = QPushButton("Add", self)
        self.confirmButton.clicked.connect(self.addMovie)
        self.inputLayout.addWidget(self.confirmButton)
        self.inputLayout.addStretch()
        self.mainLayout.addLayout(self.inputLayout)

        # Next stage button
        self.nextButton = QPushButton("Next stage", self)
        self.nextButton.clicked.connect(lambda: nextLayoutTrigger(1))
        self.mainLayout.addWidget(self.nextButton)
        self.mainLayout.addStretch(2)

        self.setLayout(self.mainLayout)

    def addMovie(self):
        newMovie = self.input.text()
        result = self.dataManager.add_movie(newMovie)

        if result:
            moviesList = self.dataManager.get_movies_list()
            for movie in moviesList:
                item = QListWidgetItem(movie)
                self.pickedMovies.addItem(item)
        else:
            self._showUnknownMovieError()

    def changeStage(self):
        pass

    def _showUnknownMovieError(self):
        movieErrorDialog = QMessageBox(self)
        movieErrorDialog.setText("Sorry, we don\'t know this movie :c")
        movieErrorDialog.setWindowTitle("Error")
        movieErrorDialog.show()

