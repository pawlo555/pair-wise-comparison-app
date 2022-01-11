import numpy as np
import unittest

from app.backend.matrix import VotingMatrix
from app.backend.utils import aggregate_matrices
from test.app.backend.test_matrix import compare


class TestResults(unittest.TestCase):
    def test_aggregate_matrix(self):
        voting_matrix_1 = VotingMatrix(['_' for _ in range(3)])
        voting_matrix_1.matrix = np.array([[1, 2, 4 / 5],
                                           [1 / 2, 1, 1 / 4],
                                           [5 / 4, 4, 1]])
        voting_matrix_2 = VotingMatrix(['_' for _ in range(3)])
        voting_matrix_2.matrix = np.array([[1, 2, 1 / 4],
                                           [1 / 2, 1, 8 / 9],
                                           [4, 9 / 8, 1]])
        voting_matrix_3 = VotingMatrix(['_' for _ in range(3)])
        voting_matrix_3.matrix = np.array([[1, 1, 3 / 8],
                                           [1, 1, 2 / 5],
                                           [8 / 3, 5 / 2, 1]])
        voting_matrix_4 = VotingMatrix(['_' for _ in range(3)])
        voting_matrix_4.matrix = np.array([[1, 1, 3 / 7],
                                           [1, 1, 8 / 9],
                                           [7 / 3, 9 / 8, 1]])

        true_matrix = VotingMatrix(['_' for _ in range(3)])
        true_matrix.matrix = np.array([[1, 1.414, 0.423],
                                       [0.707, 1, 0.53],
                                       [2.361, 1.886, 1]])
        matrices_list = [voting_matrix_1, voting_matrix_2, voting_matrix_3, voting_matrix_4]
        voting_matrix_aggregated = aggregate_matrices(matrices_list)
        self.assertTrue(compare(voting_matrix_aggregated, true_matrix.calc_ranking()))
