from typing import List

from app.backend.expert import Expert
from app.backend.api_manager import APIManager, VALUES
from app.backend.criteria_hierarchy import CriteriaHierarchy


class DataManager:
    """
    Class to communicate with frontend
    """
    def __init__(self):
        self.criteria_hierarchy = CriteriaHierarchy()
        self.experts_names = []
        self.movies_dictionaries = {}

        self.experts = {}
        self.method_name = "EVM"
        self.api_manager = APIManager()

    def add_movie(self, movie_name: str) -> str:
        """
            Returns dictionary containing data about movie --> APIManager.fetch_movie()
        """
        dictionary = self.api_manager.fetch_movie(movie_name)
        if "error" in dictionary.keys():
            return dictionary
        else:
            self.movies_dictionaries[dictionary['title']] = dictionary
            return dictionary

    def remove_movie(self, movie_title: str) -> None:
        self.movies_dictionaries.pop(movie_title)

    def get_movies_list(self) -> List[str]:
        return sorted(self.movies_dictionaries.keys())

    def add_criterion(self, criterion_name: str):
        self.criteria_hierarchy.add_node(criterion_name, "Result", [])

    def remove_criterion(self, criterion_name: str):
        self.criteria_hierarchy.remove_node(criterion_name)

    def get_all_criteria_list(self) -> List[str]:
        return VALUES

    def get_picked_criteria_list(self, selected_criteria: List[str]) -> List[str]:
        all_criteria = set(self.criteria_hierarchy.criteria_list())
        selected_set = set(selected_criteria)
        return sorted(list(all_criteria.intersection(selected_set)))

    def create_complex_criterion(self, name: str, subcriteria: List[str], parent_name: str = "Result"):
        self.criteria_hierarchy.add_node(name, parent_name, subcriteria)

    def add_expert(self, expert_name: str) -> None:
        self.experts_names.append(expert_name)

    def delete_expert(self, expert_name: str) -> None:
        self.experts_names.remove(expert_name)

    def get_experts_list(self) -> List[str]:
        return self.experts_names

    def initialize_matrices(self) -> None:
        """
        Use after all movies, criteria and experts all selected - initialize all matrices
        """
        for expert_name in self.experts_names:
            self.experts[expert_name] = Expert(self.criteria_hierarchy, sorted(self.movies_dictionaries.keys()))

    def get_criterion_matrix(self, criterion_name: str, user_name: str):
        self.experts[user_name].get_comparisons(criterion_name)

    def set_method(self, method_name: str = "EVM"):
        self.method_name = method_name

    def calc_results(self):
        pass

    def get_result_matrix(self, criterion_name: str):
        pass

    def get_inconsistency_matrix(self, criterion_name: str):
        pass
