from PyQt6 import QtCore
from PyQt6.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox, \
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
        titleLabel.setObjectName("titleLabel")
        titleLabel.setText("type movies here 🎬")
        titleLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.mainLayout.addWidget(titleLabel)

        # List of picked movies
        self.pickedMovies = QListWidget(self)
        self.mainLayout.addWidget(self.pickedMovies)

        # Input field
        self.input = QLineEdit(self)
        self.inputLayout.addWidget(self.input)

        # Input confirmation button
        self.confirmButton = QPushButton("add", self)
        self.confirmButton.clicked.connect(self.addMovie)
        self.inputLayout.addWidget(self.confirmButton)
        self.inputLayout.addStretch()
        self.mainLayout.addLayout(self.inputLayout)

        # Next stage button
        self.nextButton = QPushButton("next stage", self)
        self.nextButton.clicked.connect(lambda: nextLayoutTrigger(1))
        nextButtonLayout = QHBoxLayout()
        nextButtonLayout.addStretch(1)
        nextButtonLayout.addWidget(self.nextButton)
        nextButtonLayout.addStretch(1)
        self.mainLayout.addLayout(nextButtonLayout)
        self.mainLayout.addStretch(2)

        self.setLayout(self.mainLayout)

    def addMovie(self):
        newMovie = self.input.text()
        result = self.dataManager.add_movie(newMovie)

        if result:
            moviesList = self.dataManager.get_movies_list()
            self.pickedMovies.clear()
            for movie in moviesList:
                item = QListWidgetItem(movie)
                self.pickedMovies.addItem(item)
        else:
            self.showUnknownMovieError()

    def showUnknownMovieError(self):
        movieErrorDialog = QMessageBox(self)
        movieErrorDialog.setText("Sorry, we don\'t know this movie :c")
        movieErrorDialog.setWindowTitle("Error")
        movieErrorDialog.show()
