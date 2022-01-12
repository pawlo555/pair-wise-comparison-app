from typing import List, Dict

import numpy as np
import pandas as pd
from app.backend.api_manager import APIManager, VALUES
from app.backend.criteria_hierarchy import CriteriaHierarchy
from app.backend.expert import Expert
from app.backend.results import Results


class DataManager:
    """
    Class to communicate with frontend
    """
    def __init__(self, api=True):
        self.criteria_hierarchy = CriteriaHierarchy()
        self.experts_names = []
        self.movies_dictionaries = {}

        self.experts: Dict[str: Expert] = {}
        self.results = None
        self.method_name = "EVM"
        self.api_manager = None
        if api:
            self.api_manager = APIManager()

    def add_movie(self, movie_name: str) -> str:
        """
        Returns dictionary containing data about movie --> APIManager.fetch_movie()
        Adds information about movie to self.movies_dictionaries if movie founded

        :param movie_name: Name of movie
        :return: Dictionary containing information about movie or one "error" key
        """
        if self.api_manager:
            dictionary = self.api_manager.fetch_movie(movie_name)
            if "error" in dictionary.keys():
                return dictionary
            else:
                self.movies_dictionaries[dictionary['title']] = dictionary
                return dictionary
        else:
            return "no_api"

    def remove_movie(self, movie_title: str) -> None:
        """
        Remove a movie from movie list

        :param movie_title: Title of movie
        """
        self.movies_dictionaries.pop(movie_title)

    def get_movies_list(self) -> List[str]:
        """
        :return: List of movies
        """
        return sorted(self.movies_dictionaries.keys())

    def add_criterion(self, criterion_name: str):
        """
        Adds a criterion

        :param criterion_name: Name of criterion
        """
        self.criteria_hierarchy.add_node(criterion_name, "Result", [])

    def remove_criterion(self, criterion_name: str):
        """
        Remove a criterion

        :param criterion_name: Name of criterion
        """
        self.criteria_hierarchy.remove_node(criterion_name)

    def get_all_criteria_list(self) -> List[str]:
        """
        :return: List of criteria
        """
        return VALUES

    def get_picked_criteria_list(self) -> List[str]:
        """
        :return: Gets all criteria to choose most suitable
        """
        criteria_list = self.criteria_hierarchy.criteria_list()
        return criteria_list

    def create_complex_criterion(self, name: str, subcriteria: List[str], parent_name: str = "Result") -> None:
        """
        :param name: Name of criterion
        :param subcriteria: List of subcriteria
        :param parent_name: Name of parent criterion for the new one
        """
        self.criteria_hierarchy.add_node(name, parent_name, subcriteria)

    def add_expert(self, expert_name: str) -> None:
        """
        :param expert_name: Name of expert
        """
        self.experts_names.append(expert_name)

    def delete_expert(self, expert_name: str) -> None:
        """
        :param expert_name: Name of expert
        """
        self.experts_names.remove(expert_name)

    def get_experts_list(self) -> List[str]:
        """
        :return: List of current experts
        """
        return self.experts_names

    def initialize_matrices(self) -> None:
        """
        Use after all movies, criteria and experts all selected - initialize all matrices
        """
        for expert_name in self.experts_names:
            self.experts[expert_name] = Expert(expert_name, self.criteria_hierarchy,
                                               sorted(self.movies_dictionaries.keys()))

    def get_criterion_matrix(self, criterion_name: str, expert_name: str) -> pd.DataFrame:
        """
        :param criterion_name: Name of criterion
        :param expert_name: Name of expert
        :return: VotingMatrix as pandas DataFrame
        """
        return self.experts[expert_name].get_comparisons(criterion_name)

    def pass_criterion_matrix(self, criterion_name: str, user_name: str, matrix: np.ndarray):
        self.experts[user_name].pass_matrix(criterion_name, matrix)

    def set_method(self, method_name: str = "EVM") -> None:
        """
        Sets method of calculating result matrix.

        :param method_name: Name of method choose between EVM and GMM.
        """
        self.method_name = method_name

    def calc_results(self):
        self.results = Results(list(self.experts.values()), method=self.method_name)

    def get_result_matrix(self, criterion_name: str, expert_name: str = None) -> np.ndarray:
        return self.results.get_result(criterion_name, expert_name)

    # add user inconsistency
    def get_inconsistency(self, criterion_name: str, expert_name) -> np.ndarray:
        assert expert_name in self.experts.keys(), "There is no such expert"
        return self.results.get_inconsistency(criterion_name, expert_name)

    def get_ranking(self, criterion_name: str, expert_name: str = None) -> np.ndarray:
        return self.results.get_ranking(criterion_name, expert_name)

    def get_movie_info(self, movie_name: str) -> Dict[str, str]:
        return self.movies_dictionaries[movie_name]

    def get_movie_criteria(self) -> List[str]:
        movie_criteria = []
        for criterion in self.criteria_hierarchy.criteria_list():
            if not self.criteria_hierarchy.node_dict[criterion].get_children():
                movie_criteria.append(criterion)
        return movie_criteria

    def get_complex_criteria(self) -> List[str]:
        complex_criteria = []
        for criterion in self.criteria_hierarchy.criteria_list():
            if self.criteria_hierarchy.node_dict[criterion].get_children():
                complex_criteria.append(criterion)
        return complex_criteria
