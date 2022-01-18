import numpy as np

from typing import List, Dict

from app.backend.utils import calc_results, calc_aggregate_rankings
from app.backend.expert import Expert


class AggregatedResults:
    """
    Class for storing aggregated results
    - movies results for selected criterion
    - matrix ranking for selected criterion (for basic criteria this two are the same)
    """

    def __init__(self, experts: List[Expert], method: str = "EVM") -> None:
        """
        Calculate all results for the give experts and method

        :param experts: List of Experts
        :param method: Method of calculating ranking EVM and GMM is available
        """
        self.__rankings: Dict[str, np.ndarray] = {}
        self.__results: Dict[str, np.ndarray] = {}

        criteria_hierarchy = experts[0].criteria_hierarchy
        for criterion_name in criteria_hierarchy.criteria_list():
            matrices = [expert.get_voting_matrix(criterion_name) for expert in experts]
            self.__rankings[criterion_name] = calc_aggregate_rankings(matrices, method)

        # results
        self.__results = calc_results(self.__rankings, criteria_hierarchy)

    def get_results(self, criterion_name: str) -> np.ndarray:
        """
        Get a movie results for selected criterion

        :param criterion_name: name of criterion
        :return: AHP results array for movies
        """
        return self.__results[criterion_name]

    def get_ranking(self, criterion_name: str) -> np.ndarray:
        """
        Get a ranking for selected criterion

        :param criterion_name: name of criterion
        :return: Ranking for matrix elements importance
        """
        return self.__rankings[criterion_name]
