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

    def test_calc_gmm_zeros(self):
        voting_matrix = VotingMatrix(['_' for _ in range(5)])
        voting_matrix.matrix = np.array([[1,   2/3, 0, 0,   9],
                                        [3/2, 1,   0, 7/4, 0],
                                        [0,   0,   1, 0,   1/3],
                                        [0,   4/7, 0, 1,   9],
                                        [1/9, 0,   3, 1/9, 1]])
        result = voting_matrix.calc_ranking(method='GMM')

        self.assertTrue(compare(result, np.array([0.275, 0.429, 0.0098, 0.255, 0.0294])))

    def test_calc_gmm_non_zeros(self):
        voting_matrix = VotingMatrix(['_' for _ in range(3)])
        voting_matrix.matrix = np.array([[1, 4, 5/3, 6/7, 2],
                                         [1/4, 1,   6/5, 5/9, 3/5],
                                         [3/5, 5/6, 1,   1/3, 1/2],
                                         [7/6, 9/5, 3,   1,   4/9],
                                         [1/2, 5/3, 2,   9/4, 1]])
        result = voting_matrix.calc_ranking(method="GMM")

        self.assertTrue(compare(result, np.array([0.3015, 0.1169, 0.1127, 0.2276, 0.2413])))

    def test_inconsistency(self):
        voting_matrix = VotingMatrix(['_' for _ in range(7)])
        voting_matrix.matrix = np.array([[1,   7,   1/6, 1/2, 1/4, 1/6, 4],
                                         [1/7, 1,   1/3, 5,   1/5, 1/7, 5],
                                         [6,   3,   1,   6,   3,   2,   8],
                                         [2,   1/5, 1/6, 1,   8,   1/5, 8],
                                         [4,   5,   1/3, 1/8, 1,   1/9, 2],
                                         [6,   7,   1/2, 5,   9,   1,   2],
                                         [1/4, 1/5, 1/8, 1/8, 1/2, 1/2, 1]])
        self.assertTrue(voting_matrix.calc_inconsistency()-0.53 < 0.01)

    def test_ones(self):
        voting_matrix = VotingMatrix(['_' for _ in range(3)])
        voting_matrix.matrix = np.array([[1, 1, 1],
                                         [1, 1, 1],
                                         [1, 1, 1]])
        result = voting_matrix.calc_ranking()
        print(result)
        self.assertTrue(compare(result, np.array([[0.333, 0.333, 0.333]])))

    def test_golden_wang(self):
        voting_matrix = VotingMatrix(['_' for _ in range(4)])
        voting_matrix.matrix = np.array([[1,   4, 1/3, 1/4],
                                         [1/4, 1, 1/4, 1],
                                         [3,   4, 1,   1/4],
                                         [4,   1, 4,   1]])
        inconsistency = voting_matrix.calc_inconsistency("GMM")
        self.assertAlmostEqual(0.52, inconsistency, 2)

    def test_to_pandas(self):
        names_list = ["One", "Two", "Three"]
        voting_matrix = VotingMatrix(names_list)
        df = voting_matrix.to_dataframe()
        print(df)
        self.assertEqual(set(df.keys()), set(names_list))
        self.assertEqual(set(df.index), set(names_list))
        self.assertEqual(set(df.keys()), set(names_list))
