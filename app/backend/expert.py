import numpy as np
import pandas as pd
from typing import List
from app.backend.criteria_hierarchy import CriteriaHierarchy
from app.backend.matrix import VotingMatrix


class Expert:
    """
    Saves information about expert preferences
    """
    def __init__(self, name: str, criteria_hierarchy: CriteriaHierarchy, movies_names: List[str]):
        """
        Initialize experts with VotingMatrices for criteria from criteria_hierarchy and specified movies

        :param name: Name of expert
        :param criteria_hierarchy: CriteriaHierarchy used to generated matrices
        :param movies_names: List with names of movies
        """
        self.name = name
        self.criteria_hierarchy = criteria_hierarchy
        self.matrix_dict = {}
        for criterion_name in criteria_hierarchy.criteria_list():
            subcriteria_names = criteria_hierarchy.node_dict[criterion_name].get_children_names()
            if not subcriteria_names:
                self.matrix_dict[criterion_name] = VotingMatrix(movies_names)
            else:
                self.matrix_dict[criterion_name] = VotingMatrix(subcriteria_names)
        self.movies_names = movies_names

    def get_comparisons(self, criterion: str) -> pd.DataFrame:
        """
        :param criterion: Name of criterion
        :return: VotingMatrix as pandas DataFrame
        """
        return self.matrix_dict[criterion].to_dataframe()

    def get_comparison_results(self, criterion_name: str, method: str = "EVM") -> np.array:
        """
        :param criterion_name: Name of criterion
        :param method: Method of calculating rankings EVM or GMM
        :return: Ranking calculated for selected criterion
        """
        return self.matrix_dict[criterion_name].calc_ranking(method)

    def get_voting_matrix(self, criterion_name: str) -> VotingMatrix:
        """
        :param criterion_name: Name of criterion
        :return: VotingMatrix for selected criterion
        """
        return self.matrix_dict[criterion_name]

    def pass_matrix(self, criterion_name: str, matrix: np.ndarray):
        """
        Fill VotingMatrix for selected criterion with selected matrix

        :param criterion_name: Name of criterion
        :param matrix: Matrix we want to pass
        """
        self.matrix_dict[criterion_name].matrix = matrix
