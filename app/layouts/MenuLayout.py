from PyQt6.QtWidgets import QVBoxLayout, QPushButton, QListWidget, QLabel, QTableWidget

from app import MainWindow


class MenuLayout(QVBoxLayout):
    def __init__(self, mainWindow: MainWindow):
        """
        :param mainWindow: MainWindow of application - use for changing layouts
        """

        super().__init__()
        self.mainWindow = mainWindow

        label = QLabel("Movies")
        self.addWidget(label)

        self.movies = QListWidget()
        self.movies.addItem("Diuna")
        self.movies.addItem("Start Wars The Last Jedi")
        self.addWidget(self.movies)

        self.addMovieButton = QPushButton("Add movie")
        self.addWidget(self.addMovieButton)
        self.addMovieButton.clicked.connect(self.addMovieClicked)
        self.removeMovieButton = QPushButton("Delete movie")
        self.addWidget(self.removeMovieButton)

        label = QLabel("Criteria")
        self.addWidget(label)

        self.criteria = QListWidget()
        self.criteria.addItem("Director")
        self.criteria.addItem("Production Year")
        self.addWidget(self.criteria)

        self.addCriteriaButton = QPushButton("Add criteria")
        self.addWidget(self.addCriteriaButton)
        self.addCriteriaButton.clicked.connect(self.criteriaClicked)
        self.removeCriteriaButton = QPushButton("Delete criteria")
        self.addWidget(self.removeCriteriaButton)
        self.editCriteriaButton = QPushButton("Edit criteria")
        self.addWidget(self.editCriteriaButton)

        self.gradingButton = QPushButton("Enter grading")
        self.gradingButton.clicked.connect(self.gradingClicked)
        self.addWidget(self.gradingButton)

        label = QLabel("Users")
        self.addWidget(label)

        self.users = QListWidget()
        self.users.addItem("Kuba")
        self.users.addItem("Piotr")
        self.addWidget(self.users)

        self.addUserButton = QPushButton("Add user")
        self.addWidget(self.addUserButton)
        self.removeUserButton = QPushButton("Delete user")
        self.addWidget(self.removeUserButton)

        self.results = QPushButton("Show results")
        self.results.clicked.connect(self.resultsClicked)
        self.addWidget(self.results)

        tableWidget = QTableWidget()
        tableWidget.setRowCount(10)
        tableWidget.setColumnCount(5)

        self.addWidget(tableWidget)

    def addMovieClicked(self):
        self.mainWindow.changeMainLayout(0)

    def criteriaClicked(self):
        self.mainWindow.changeMainLayout(1)

    def gradingClicked(self):
        self.mainWindow.changeMainLayout(2)

    def resultsClicked(self):
        self.mainWindow.changeMainLayout(3)
