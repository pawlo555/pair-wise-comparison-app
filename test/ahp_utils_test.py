import unittest
import pandas as pd
import numpy as np

import ahp_utlis as utils


def get_test_dataframe() -> pd.DataFrame:
    data = {'first': [1, 2, 3],
            'second': [1/2, 1, 3],
            'third': [1/3, 2/3, 1]}
    return pd.DataFrame(data)


class TestAHPUtils(unittest.TestCase):

    def test_get_columns_names(self):
        df = get_test_dataframe()
        true = ['first', 'second', 'third']

        result = utils.get_columns_names(df)
        self.assertEqual(true, result)

    def test_filter_dataframe_columns(self):
        df = get_test_dataframe()
        true = ['first']

        not_to_drop = ['first', 'last']
        filter_df = utils.filter_dataframe_columns(df, not_to_drop)
        result = utils.get_columns_names(filter_df)
        self.assertEqual(true, result)

    def test_get_final_ranking(self):
        pass

    def apply_ranking_to_dataframe(self):
        pass

    def test_calc_evm_ranking(self):
        preferences = np.array([[1, 2, 8], [1/2, 1, 4], [1/8, 1/4, 1]])
        geometric_average = np.array([16, 2, 1/32])**(1/3)
        true = geometric_average / np.sum(geometric_average)

        result = utils.calc_evm_ranking(preferences)
        self.assertTrue(np.all((true - result) < np.finfo(np.float32).eps))

    def test_calc_consistency_ratio(self):
        preferences = np.array([[1, 2, 8], [1/2, 1, 4], [1/8, 1/4, 1]])
        evm = utils.calc_evm_ranking(preferences)
        true = 0.0
        result = utils.calc_consistency_ratio(preferences, evm)
        self.assertAlmostEqual(true, result, 5)


if __name__ == '__main__':
    unittest.main()
