import unittest
import numpy as np

from app.backend.matrix import VotingMatrix


def compare(true: np.ndarray, result: np.ndarray, difference: float = 0.001):
    comparisons = np.abs(true - result) < difference
    print(comparisons)
    print(result)
    print(true)
    return np.all(comparisons)


class TestVotingMatrix(unittest.TestCase):

    def test_calc_evm_zeros(self):
        voting_matrix = VotingMatrix(['_' for _ in range(5)])
        voting_matrix.matrix = np.array([[1,   2/3, 0, 0,   9],
                                         [3/2, 1,   0, 7/4, 0],
                                         [0,   0,   1, 0,   1/3],
                                         [0,   4/7, 0, 1,   9],
                                         [1/9, 0,   3, 1/9, 1]])
        result = voting_matrix.calc_ranking()

        self.assertTrue(compare(result, np.array([0.275, 0.429, 0.0098, 0.255, 0.0294])))

    def test_calc_evm_non_zeros(self):
        voting_matrix = VotingMatrix(['_' for _ in range(3)])
        voting_matrix.matrix = np.array([[1, 2, 3], [1/2, 1, 4], [1/3, 1/4, 1]])
        result = voting_matrix.calc_ranking()

        self.assertTrue(compare(result, np.array([0.517, 0.358, 0.124])))
