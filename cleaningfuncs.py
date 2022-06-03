import numpy as np


def percent_missing(df):
    """Takes DataFrame, prints percentage of data missing for each column."""
    for col in df.columns:
        pct_missing = np.round((np.mean(df[col].isnull()) * 100), decimals = 2)
        print('{} - {}%'.format(col, pct_missing))


def split_explode(df, col, delimiter):
    """Takes a DataFrame, column, and delimiter, splits column
    at delimiter and explodes rows.
    """
    df[col] = [item.split(delimiter) for item in df[col]]
    df = df.explode(col, ignore_index=True)
    return df


def dummy_variable(df, col, col_value, new_col):
    """Takes a DataFrame, column name, column value, and new column name.
    Returns DataFrame with dummy variable in new column with new column name
    that is 1 when the original column value equals col_value.
    """
    df[new_col] = 0
    df.loc[df[col] == col_value, new_col] = 1
    return df


def remove_strings(item, strings):
    """Takes a string item and a string or list of strings to remove,
    removes strings from item.
    """
    for string in strings:
        item = item.replace(string, '')
    return item
