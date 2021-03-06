import numpy as np

from typing import List, Dict
from app.backend.criteria_hierarchy import CriteriaHierarchy
from app.backend.matrix import VotingMatrix


def calc_results(rankings: Dict[str, np.ndarray], criteria_hierarchy: CriteriaHierarchy) -> Dict[str, np.array]:
    """
    Calculates results matrix based on matrix rankings and criteriaHierarchy

    :param rankings: Dictionary of matrices rankings
    :param criteria_hierarchy: Hierarchy of criteria
    :return: Dictionary with AHP results of comparisons per criterion
    """
    results = {}
    criterion_levels = criteria_hierarchy.get_criterion_levels()
    for level in sorted(criterion_levels.keys(), reverse=True):
        for criterion_name in criterion_levels[level]:
            if not criteria_hierarchy.node_dict[criterion_name].get_children():
                results[criterion_name] = rankings[criterion_name]
            else:
                node = criteria_hierarchy.node_dict[criterion_name]
                children_names = node.get_children_names()
                children_results = [results[name].T for name in children_names]
                matrix = np.concatenate(children_results, axis=-1).T
                results[criterion_name] = np.matmul(rankings[criterion_name], matrix)
    return results


def calc_aggregate_rankings(matrices: List[VotingMatrix], method: str) -> np.ndarray:
    """
    Calculates the aggregated rankings from lists of matrices.

    :param matrices: List of AHP matrices
    :param method: Method used to calculate AHP - EVM or GMM
    :return: Aggregated matrix for specified list
    """

    if all([np.count_nonzero(matrix == 0) == 0 for matrix in matrices]):  # all data are filled
        return aggregate_matrices(matrices, method)
    else:
        return aggregate_rankings(matrices, method)


def aggregate_rankings(matrices: List[VotingMatrix], method: str = "EVM") -> np.ndarray:
    """
    Aggregates list of ranking into one

    :param matrices: List of AHP matrices
    :param method: Method used to calculate AHP - EVM or GMM
    :return: Aggregated matrix for specified list
    """
    rankings = [matrix.calc_ranking(method) for matrix in matrices]
    stacked = np.stack(rankings)
    return np.mean(stacked, axis=-1)


def aggregate_matrices(matrices: List[VotingMatrix], method: str = "EVM") -> np.ndarray:
    """
    Perform aggregation of matrices using geometric average in order to aggregate different experts

    :param matrices: List of voting matrices
    :param method: Method used to calculate AHP - EVM or GMM
    :return: Aggregated matrix for specified list
    """
    aggregated_matrices = [voting_matrix.matrix for voting_matrix in matrices]
    last_dim = len(aggregated_matrices)
    aggregated_matrices = np.stack(aggregated_matrices, axis=-1)
    aggregated_matrices = np.power(aggregated_matrices, 1/last_dim)
    aggregated_matrix = np.prod(aggregated_matrices, axis=-1)
    voting_matrix = VotingMatrix(matrices[0].names)
    voting_matrix.matrix = aggregated_matrix
    return voting_matrix.calc_ranking(method)
