from typing import Dict

import numpy as np

from app.backend.expert import Expert
from app.backend.utils import calc_results


class ExpertResults:
    """
    Class for storing results for the specified expert.
    Implements getters to get such results:
        - matrix inconsistency for selected criterion
        - movies results for selected criterion
        - matrix ranking for selected criterion (for basic criteria this two are the same)
    """

    def __init__(self, expert: Expert, ranking_method: str = "EVM"):
        """
        Initialize results for selected Expert

        :param expert: Expert used to calculated results
        :param ranking_method: method of calculating a ranking - EVM and GMM is possible
        """
        self.__rankings: Dict[str, np.ndarray] = {}
        self.__results: Dict[str, np.ndarray] = {}
        self.__inconsistency: Dict[str, float] = {}
        criteria_hierarchy = expert.criteria_hierarchy

        for criterion_name in criteria_hierarchy.criteria_list():
            self.__rankings[criterion_name] = expert.get_voting_matrix(criterion_name).calc_ranking(ranking_method)
            self.__inconsistency[criterion_name] = expert.get_voting_matrix(criterion_name).calc_inconsistency(
                ranking_method)

        self.__results = calc_results(self.__rankings, criteria_hierarchy)

    def get_inconsistency(self, criterion_name: str, ) -> float:
        """
        Get an inconsistency value for selected criterion matrix

        :param criterion_name: name of criterion
        :return: Value of inconsistency for selected criterion and method of calculation
        """
        return self.__inconsistency[criterion_name]

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
