"""
try out pandas
"""

import os

import pandas as pd


def test_read_csv():
    """read csv"""

    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, "organizations-1000.csv")
    df = pd.read_csv(file_path)  # type: ignore

    # print(df.head())
    # print(df.columns)
    # print(df.shape)
    # print(df.dtypes)
    # print(df.describe())
    # print(df.info())

    assert df["Number of employees"].sum() == 4964996

    sorted_df = df.sort_values(by="Number of employees", ascending=False)
    assert sorted_df["Name"].iloc[0] == "Walker Group"
    assert sorted_df["Number of employees"].iloc[0] == 9952
