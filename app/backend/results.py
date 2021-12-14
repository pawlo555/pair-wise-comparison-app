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
            matrices = [expert.get_voting_matrix(criterion_name) for expert in experts]
            if all([np.count_nonzero(matrix == 0) == 0 for matrix in matrices]):  # all data are filled
                aggregated_matrix = VotingMatrix.aggregate_matrices(matrices)
                self.rankings[criterion_name] = aggregated_matrix.calc_ranking(method)
                self.inconsistencies[criterion_name] = aggregated_matrix.calc_inconsistency()
            else:
                rankings = [matrix.calc_ranking() for matrix in matrices]
                self.rankings[criterion_name] = self.aggregate_rankings(rankings)
                inconsistencies = [matrix.calc_inconsistency for matrix in matrices]
                self.inconsistencies[criterion_name] = np.mean(np.array(inconsistencies))

        # results
        self.results = {}
        criterion_levels = self.criteria_hierarchy.get_criterion_levels()

        for level in sorted(criterion_levels.keys(), reverse=True):
            for criterion_name in criterion_levels[level]:
                print(criterion_name, list(self.criteria_hierarchy.node_dict[criterion_name].get_children()), "Janusz")
                if not list(self.criteria_hierarchy.node_dict[criterion_name].get_children()):
                    self.results[criterion_name] = self.rankings[criterion_name]
                else:
                    node = self.criteria_hierarchy.node_dict[criterion_name]
                    children_names = node.get_children().keys()
                    print(criterion_name)
                    print(children_names)
                    children_rankings = [self.rankings[name].T for name in children_names]
                    print("Children:", children_rankings)
                    matrix = np.concatenate(children_rankings, axis=-1).T
                    print("Matrix:", matrix)
                    self.results[criterion_name] = np.matmul(self.rankings[criterion_name], matrix)

    @staticmethod
    def aggregate_rankings(rankings: List[np.ndarray]):
        stacked = np.stack(rankings, axis=-1)
        return np.mean(stacked, axis=-1)

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
