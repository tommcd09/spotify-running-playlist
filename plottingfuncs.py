import matplotlib.pyplot as plt
import seaborn as sns


def simple_boxplot(df, col, title, x=None, ax=None):
    """Takes a DataFrame, column name, title, and optional y and ax,
    plots seaborn boxplot.
    """
    g = sns.boxplot(x=x, y=col, data=df, ax=ax)
    g.set_title(title)
    g.set_ylabel('')


def multiple_boxplots(df, cols, nrows, ncols, figsize):
    """Takes DataFrame, list of columns, number of rows and columns of plots,
    and figure size tuple, plots boxplot for each column.
    """
    fig, axs = plt.subplots(nrows=nrows, ncols=ncols, figsize=figsize)
    for col, ax in zip(cols, axs.ravel()):
        sns.boxplot(y=col, data=df, ax=ax)
        ax.set_title(col.capitalize())
        ax.set_ylabel('')
