import numpy as np
import pandas as pd

from app.backend.matrix import VotingMatrix
from app.backend.criteria_hierarchy import CriteriaHierarchy


class Expert:
    """
    Saves information about expert preferences
    """
    def __init__(self, criteria_hierarchy: CriteriaHierarchy, movies_names):
        self.criteria_hierarchy = criteria_hierarchy
        self.matrix_dict = {}
        for criterion_name in criteria_hierarchy.criteria_list():
            subcriteria_names = criteria_hierarchy.node_dict.keys()
            if not subcriteria_names:
                self.matrix_dict[criterion_name] = VotingMatrix(movies_names)
            else:
                self.matrix_dict[criterion_name] = VotingMatrix(subcriteria_names)
        self.movies_names = movies_names

    def get_comparisons(self, criterion) -> pd.DataFrame:
        return self.matrix_dict[criterion].to_dataframe()

    def get_comparison_results(self, criterion_name, method: str = "EVM", need_all_values: bool = False) -> np.array:
        return self.matrix_dict[criterion_name].calc_ranking(method, need_all_values)

    def get_voting_matrix(self, criterion_name: str) -> VotingMatrix:
        return self.matrix_dict[criterion_name]
