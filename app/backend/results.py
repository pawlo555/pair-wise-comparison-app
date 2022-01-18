from typing import List, Dict

import numpy as np
from app.backend.expert import Expert
from app.backend.expert_results import ExpertResults
from app.backend.aggregated_results import AggregatedResults


class Results:
    """
    Class responsible for creating and storing personal and aggregated results, for each category we can get:
        - inconsistency index - for specified expert and criterion
        - results for movies - for specified expert and criterion or for criterion aggregated for all experts
        - matrix ranking (for basic criteria this two are the same) - for specified experts and criterion or aggregated
            for all experts
    """

    def __init__(self, experts: List[Expert], method: str = "EVM") -> None:
        """
        Calculate all results for the give experts and method

        :param experts: List of Experts
        :param method: Method of calculating ranking EVM and GMM is available
        """
        self.__aggregated_results = AggregatedResults(experts, method)
        self.__individual_results: Dict[str: ExpertResults] = {}
        for expert in experts:
            self.__individual_results[expert.name] = ExpertResults(expert, method)

    def get_ranking(self, criterion_name: str, expert_name: str = None) -> np.ndarray:
        """
        Get the ranking vector for criterion

        :param criterion_name: Name of criterion
        :param expert_name: Name of expert if None method will return aggregated results
        :return: Ranking vector for criterion
        """
        if expert_name:
            return self.__individual_results[expert_name].get_ranking(criterion_name)
        else:
            return self.__aggregated_results.get_ranking(criterion_name)

    def get_inconsistency(self, criterion_name: str, expert_name: str) -> float:
        """
        Get matrix inconsistency for selected criterion

        :param expert_name: Name of the expert to take matrices for
        :param criterion_name: Name of criterion
        :return: Inconsistency of matrix
        """
        return self.__individual_results[expert_name].get_inconsistency(criterion_name)

    def get_result(self, criterion_name: str, expert_name: str = None) -> np.ndarray:
        """
        Get the result vector for criterion

        :param criterion_name: Name of criterion
        :param expert_name: Name of expert if None method will return aggregated results
        :return: Result vector for criterion
        """
        if expert_name:
            return self.__individual_results[expert_name].get_results(criterion_name)
        else:
            return self.__aggregated_results.get_results(criterion_name)
