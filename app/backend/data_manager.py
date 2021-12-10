from app.backend.specialist import Specialist


class DataManager:
    """
    Class to communicate with frontend
    """
    def __init__(self):
        pass

    def add_movie(self, movie_name: str):
        pass

    def remove_movie(self, movie_name: str):
        pass

    def add_criterion(self, criterion_name: str):
        pass

    def remove_criterion(self, criterion_name: str):
        pass

    def add_user(self, user: str):
        pass

    def delete_user(self, user_name: str):
        pass

    def get_criterion_matrix(self, criterion_name: str, user_name: str):
        pass

    def set_method(self):
        pass

    def calc_results(self):
        pass

    def get_result_matrix(self, criterion_name: str):
        pass

    def get_inconsistency_matrix(self, criterion_name: str):
        pass
