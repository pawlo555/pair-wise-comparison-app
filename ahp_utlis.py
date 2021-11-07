import pandas as pd
import numpy as np

from typing import List, Union


def get_columns_names(df: pd.DataFrame) -> Union[object, List[str]]:
    return df.columns.values.tolist()


def filter_dataframe_columns(df: pd.DataFrame, columns_to_stay: List[str]) -> pd.DataFrame:
    dataframe_columns_names = get_columns_names(df)
    columns_to_drop = set(dataframe_columns_names) - set(columns_to_stay)
    return df.drop(columns=columns_to_drop)


def get_final_ranking(df: pd.DataFrame, weights):
    data = df.to_numpy()
    return np.sum(data*weights, axis=-1)


def apply_ranking_to_dataframe(df: pd.DataFrame, weigth):
    result_dataframe = df.copy(deep=True)
    ranking = get_final_ranking(df, weigth)
    result_dataframe["Wyniki"] = ranking.tolist()
    result_dataframe = result_dataframe.sort_values("Wyniki", ascending=False)
    return result_dataframe


def calc_evm_ranking(preferences: np.ndarray) -> np.ndarray:
    n = preferences.shape[-1]
    geometric_average = np.prod(preferences, axis=-1)**(1/n)
    return geometric_average / np.sum(geometric_average)
