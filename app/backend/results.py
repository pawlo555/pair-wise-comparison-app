import numpy as np
from typing import List

from app.backend.expert import Expert
from app.backend.matrix import VotingMatrix


class Results:
    """
    Class responsible for creating and storing results, for each category we can get:
        - inconsistency index
        - results for movies
        - matrix ranking (for basic criteria this two are the same)
    """

    def __init__(self, experts: List[Expert], method: str = "EVM") -> None:
        self.criteria_hierarchy = experts[0].criteria_hierarchy
        self.rankings = {}
        self.inconsistencies = {}
        for criterion_name in self.criteria_hierarchy.criteria_list():
            aggregated_matrix = VotingMatrix.aggregate_matrices(
                [expert.get_voting_matrix(criterion_name) for expert in experts])
            self.rankings[criterion_name] = aggregated_matrix.calc_ranking(method)
            self.inconsistencies[criterion_name] = aggregated_matrix.calc_inconsistency()

        # results
        self.results = {}
        criterion_levels = self.criteria_hierarchy.get_criterion_levels()
        for level in sorted(criterion_levels.keys(), reverse=True):
            for criterion_name in criterion_levels[level]:
                if level == 0:
                    self.results[criterion_name] = self.rankings[criterion_name]
                else:
                    node = self.criteria_hierarchy.node_dict[criterion_name]
                    children_names = node.get_children().keys()
                    children_rankings = [self.rankings[name] for name in children_names]
                    matrix = np.concatenate(children_rankings, axis=-1).T
                    self.results[criterion_name] = matrix * self.rankings[criterion_name]

    def get_ranking(self, criterion_name: str) -> np.ndarray:
        """
        Get the ranking vector for criterion
        :param criterion_name: Name of criterion
        :return: Ranking vector for criterion
        """
        return self.rankings[criterion_name]

    def get_inconsistency(self, criterion_name: str) -> float:
        """
        Get matrix inconsistency for selected criterion
        :param criterion_name: Name of criterion
        :return: Inconsistency of matrix
        """
        return self.inconsistencies[criterion_name]

    def get_result(self, criterion_name: str) -> np.ndarray:
        """
        Get the result vector for criterion
        :param criterion_name: Name of criterion
        :return: Result vector for criterion
        """
        return self.results[criterion_name]
