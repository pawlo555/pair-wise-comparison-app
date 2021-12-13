import unittest
import numpy as np

from app.backend.matrix import VotingMatrix


def compare(true: np.ndarray, result: np.ndarray, difference: float = 0.001):
    comparisons = true - result < difference
    return np.all(comparisons)


class TestVotingMatrix(unittest.TestCase):

    def test_calc_evm(self):
        voting_matrix = VotingMatrix(['1', '2', '3'])
        voting_matrix.matrix = np.array([[1, 2, 3], [1/2, 1, 4], [1/3, 1/4, 1]])
        result = voting_matrix.calc_ranking()

        self.assertTrue(compare(result, np.array([0.806, 0.558, 0.193])))
