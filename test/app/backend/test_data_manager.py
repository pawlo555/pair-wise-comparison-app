import unittest
import numpy as np

from app.backend.data_manager import DataManager
from test.app.backend.test_matrix import compare


class TestDataManager(unittest.TestCase):

    def test_car_ahp(self):
        manager = DataManager(api=False)

        # setting objects to compare
        manager.add_movie("Car 1")
        manager.add_movie("Car 2")
        manager.add_movie("Car 3")
        manager.add_movie("Car 4")

        # basic criteria
        manager.add_criterion("purchase price")
        manager.add_criterion("fuel costs")
        manager.add_criterion("maintenance cost")
        manager.create_complex_criterion("cost", ["purchase price", "fuel costs", "maintenance cost"])
        manager.add_criterion("safety")
        manager.add_criterion("design")
        manager.add_criterion("trunk size")
        manager.add_criterion("passenger capacity")
        manager.create_complex_criterion("capacity", ["trunk size", "passenger capacity"])
        manager.add_criterion("warranty")

        # create expert
        manager.add_expert("Ala")

        # initialize matrices
        manager.initialize_matrices()

        # getting matrix
        C11 = np.array([[1,   7/5, 4/9, 4/5],
                        [5/7, 1,   6/7, 7/6],
                        [9/4, 7/6, 1,   3/2],
                        [5/4, 6/7, 2/3, 1]])
        manager.pass_criterion_matrix("purchase price", "Ala", C11)

        C21 = np.array([[1,   7/3, 9/5, 2],
                        [3/7, 1,   8/5, 8/5],
                        [5/9, 5/8, 1,   2],
                        [1/2, 5/8, 1/2, 1]])
        manager.pass_criterion_matrix("fuel costs", "Ala", C21)

        C31 = np.array([[1,   7/5, 4/3, 5/9],
                        [5/7, 1,   2,   6/5],
                        [3/4, 1/2, 1,   3/2],
                        [9/5, 5/6, 2/3, 1]])
        manager.pass_criterion_matrix("maintenance cost", "Ala", C31)

        C41 = np.array([[1,   6/5, 2/3, 5/2],
                        [5/6, 1,   5/9, 7/5],
                        [3/2, 9/5, 1,   1],
                        [2/5, 5/7, 1,   1]])
        manager.pass_criterion_matrix("trunk size", "Ala", C41)

        C51 = np.array([[1,   9,   9,   3/8],
                        [1/9, 1,   2/3, 1/9],
                        [1/9, 3/2, 1,   1/9],
                        [8/3, 9,   9,   1]])
        manager.pass_criterion_matrix("passenger capacity", "Ala", C51)

        C12 = np.array([[1,   7,   8],
                        [1/7, 1,   3],
                        [1/8, 1/3, 1]])
        manager.pass_criterion_matrix("cost", "Ala", C12)

        C22 = np.array([[1,   2/5, 1/9, 1/7],
                        [5/2, 1,   1/9, 1/4],
                        [9,   9,   1,   5],
                        [7,   4,   1/5, 1]])
        manager.pass_criterion_matrix("safety", "Ala", C22)

        C32 = np.array([[1, 1/9, 1/9, 1/9],
                        [9, 1,   5,   9/8],
                        [9, 1/5, 1,   7/9],
                        [9, 8/9, 9/7, 1]])
        manager.pass_criterion_matrix("design", "Ala", C32)

        C42 = np.array([[1,   3],
                        [1/3, 1]])
        manager.pass_criterion_matrix("capacity", "Ala", C42)

        C52 = np.array([[1,   9,   4/3, 7/5],
                        [1/9, 1,   1/9, 1/9],
                        [3/4, 9,   1,   1/2],
                        [5/7, 9,   2,   1]])
        manager.pass_criterion_matrix("warranty", "Ala", C52)

        C13 = np.array([[1,   7/5, 5,   9/5, 8],
                        [5/7, 1,   9/5, 7/5, 5/4],
                        [1/5, 5/9, 1,   3/7, 3/4],
                        [5/9, 5/7, 7/3, 1,   7/9],
                        [1/8, 4/5, 4/3, 9/7, 1]])
        manager.pass_criterion_matrix("Result", "Ala", C13)

        # calculate:
        manager.set_method("EVM")
        manager.calc_results()

        # checks
        self.assertTrue(compare(manager.get_ranking("purchase price"), np.array([[0.208, 0.226, 0.343, 0.22]])))
        self.assertTrue(compare(manager.get_ranking("fuel costs"), np.array([[0.398, 0.24,  0.213, 0.146]])))
        self.assertTrue(compare(manager.get_ranking("maintenance cost"), np.array([[0.250, 0.279, 0.216, 0.253]])))
        self.assertTrue(compare(manager.get_ranking("trunk size"), np.array([[0.290, 0.211, 0.314, 0.183]])))
        self.assertTrue(compare(manager.get_ranking("passenger capacity"), np.array([[0.341, 0.043, 0.054, 0.563]]),
                                0.02))

        self.assertTrue(compare(manager.get_ranking("safety"), np.array([[0.041, 0.072, 0.663, 0.221]])))
        self.assertTrue(compare(manager.get_ranking("design"), np.array([[0.032, 0.481, 0.189, 0.295]])))
        self.assertTrue(compare(manager.get_ranking("warranty"), np.array([[0.368, 0.034, 0.248, 0.348]])))

        # higher rankings:
        self.assertTrue(compare(manager.get_ranking("cost"), np.array([[0.776, 0.153, 0.07]])))
        self.assertTrue(compare(manager.get_ranking("capacity"), np.array([[0.75, 0.25]])))

        self.assertTrue(compare(manager.get_ranking("Result"), np.array([[0.447, 0.193, 0.082, 0.155, 0.12]])))

        # final results:
        self.assertTrue(compare(manager.get_result_matrix("Result"), np.array([[0.21, 0.188, 0.354, 0.247]])))
