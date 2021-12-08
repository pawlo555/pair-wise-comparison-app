import numpy as np
import pandas as pd

from app.backend.matrix import VotingMatrix


class Specialist:
    """
    Saves information about voter preferences
    """

    def __init__(self, criteria_names, movies_names):
        self.criteria_dict = {}
        for criterion_name in criteria_names:
            self.criteria_dict[criterion_name] = VotingMatrix(movies_names)
        self.movies_names = movies_names

    def add_criterion(self, criterion_name):
        if criterion_name not in self.criteria_dict.keys():
            self.criteria_dict[criterion_name] = VotingMatrix(self.movies_names)

    def add_movie(self, movie_name: str):
        for voting_matrix in self.criteria_dict.values():
            voting_matrix.add_movie(movie_name)

    def get_comparisons(self, criterion) -> pd.DataFrame:
        return self.criteria_dict[criterion].to_pandas_frame()

    def get_comparison_results(self, criterion_name, method: str = "EVM", need_all_values: bool = False) -> np.array:
        return self.criteria_dict[criterion_name].calc_ranking(method, need_all_values)