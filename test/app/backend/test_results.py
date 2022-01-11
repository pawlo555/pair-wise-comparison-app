import numpy as np
import unittest

from app.backend.expert import Expert
from app.backend.criteria_hierarchy import CriteriaHierarchy
from app.backend.results import Results
from test.app.backend.test_matrix import compare


class TestResults(unittest.TestCase):

    def test_simple_results(self):

        criteria_hierarchy = CriteriaHierarchy()
        for i in range(1, 9):
            print(str(i))
            criteria_hierarchy.add_node(node_name=str(i), parent_name='Result', children_names=[])
        expert = Expert('Paweł', criteria_hierarchy=criteria_hierarchy, movies_names=[str(i) for i in range(1, 9)])
        criteria_hierarchy.criteria_list()

        expert.get_voting_matrix("1").matrix = np.array([[1, 1/7, 1/5],
                                                         [7, 1,   3],
                                                         [5, 1/3, 1]])

        expert.get_voting_matrix("2").matrix = np.array([[1,   5,   9],
                                                         [1/5, 1,   4],
                                                         [1/9, 1/4, 1]])

        expert.get_voting_matrix("3").matrix = np.array([[1,   4, 1/5],
                                                         [1/4, 1, 1/9],
                                                         [5,   9, 1]])

        expert.get_voting_matrix("4").matrix = np.array([[1,   9, 4],
                                                         [1/9, 1, 1/4],
                                                         [1/4, 4, 1]])

        expert.get_voting_matrix("5").matrix = np.array([[1, 1, 1],
                                                         [1, 1, 1],
                                                         [1, 1, 1]])

        expert.get_voting_matrix("6").matrix = np.array([[1,   6, 4],
                                                         [1/6, 1, 1/3],
                                                         [1/4, 3, 1]])

        expert.get_voting_matrix("7").matrix = np.array([[1,   9, 6],
                                                         [1/9, 1, 1/3],
                                                         [1/6, 3, 1]])

        expert.get_voting_matrix("8").matrix = np.array([[1, 1/2, 1/2],
                                                         [2, 1,   1],
                                                         [2, 1,   1]])

        expert.get_voting_matrix("Result").matrix = np.array([[1,   4,   7,   5,   8, 6,   6,   2],
                                                              [1/4, 1,   5,   3,   7, 6,   6,   1/3],
                                                              [1/7, 1/5, 1,   1/3, 5, 3,   3,   1/5],
                                                              [1/5, 1/3, 3,   1,   6, 3,   4,   1/2],
                                                              [1/8, 1/7, 1/5, 1/6, 1, 1/3, 1/4, 1/7],
                                                              [1/6, 1/6, 1/3, 1/3, 3, 1,   1/2, 1/5],
                                                              [1/6, 1/6, 1/3, 1/4, 4, 2,   1,   1/5],
                                                              [1/2, 3,   5,   2,   7, 5,   5,   1]])

        results = Results([expert], method="EVM")
        print(results.get_ranking('1'))
        print(results.get_result('Result'))
        self.assertTrue(compare(results.get_result('1'), np.array([[0.072, 0.649, 0.279]])))
        self.assertTrue(compare(results.get_result('2'), np.array([[0.743, 0.194, 0.063]])))
        self.assertTrue(compare(results.get_result('3'), np.array([[0.194, 0.063, 0.743]])))
        self.assertTrue(compare(results.get_result('4'), np.array([[0.717, 0.0658, 0.217]])))
        self.assertTrue(compare(results.get_result('5'), np.array([[0.333, 0.333, 0.333]])))
        self.assertTrue(compare(results.get_result('6'), np.array([[0.691, 0.0914, 0.217]])))
        self.assertTrue(compare(results.get_result('7'), np.array([[0.77, 0.068, 0.162]])))
        self.assertTrue(compare(results.get_result('8'), np.array([[0.2, 0.4, 0.4]])))
        self.assertTrue(compare(results.get_result('Result'), np.array([[0.346, 0.369, 0.284]])))
        self.assertTrue(
            compare(results.get_ranking('Result'), np.array([[0.345, 0.175, 0.062, 0.103, 0.019, 0.034, 0.041, 0.22]])))
