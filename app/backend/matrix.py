from typing import List

import numpy as np
import pandas as pd


class VotingMatrix:
    """
    The idea is to keep data as numpy matrix and if necessary convert them to pandas_frame.
    Format of array is:
      x/y   Movie 1 Movie 2 Movie 3
    Movie 1   1        4       2
    Movie 2   1/4      1      1/2
    Movie 3   1/2     1/2      1
    """

    def __init__(self, names: List[str]):
        self.names = names
        array = np.ones((len(names), len(names)))
        self.matrix = np.diag(array)

    def add_comparison(self, x: int, y: int, value: float):
        assert value != 0, "Value cannot be 0"
        self.matrix[x][y] = value
        self.matrix[y][x] = 1/value

    def calc_ranking(self, method: str = "EVM", need_all_values: bool = False) -> np.ndarray:
        """
        Calc matrix ranking based on voter preferences
        :param method: Method of ranking calculation EVM or GMM
        :param need_all_values: if true in matrix cannot be zero values
        :return: np.array of results: 1 - movie1, 2 - movie2
        """
        if method == "EVM":
            return self.__calc_ranking_evm(need_all_values)
        else:
            return self.__calc_ranking_gmm(need_all_values)

    def __calc_ranking_evm(self, need_all_values: bool = False) -> np.ndarray:
        """
        Calc matrix ranking based on voter preferences
        :param need_all_values: if true in matrix cannot be zero values
        :return: np.array of results: 1 - movie1, 2 - movie2
        """
        pass

    def __calc_ranking_gmm(self, need_all_values: bool = False) -> np.ndarray:
        """
        Calc matrix GMM ranking based on voter preferences
        :param need_all_values: if true in matrix cannot be zero values
        :return: np.array of results: 1 - movie1, 2 - movie2
        """
        pass

    def calc_inconsistency(self) -> np.array:
        pass

    def to_dataframe(self) -> pd.DataFrame:
        """
        :return: Returns data frame to display on app
        """
        return pd.DataFrame(data=self.matrix, index=self.names, columns=self.names)

    def get_filled_dataframe(self, filled_df: pd.DataFrame):
        self.matrix = filled_df.to_numpy()
