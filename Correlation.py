import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import numpy as np

data = pd.read_csv('Travel review.csv', encoding='utf-8')
data = data.drop(data.columns[25], axis=1)
data = data.drop(['User'], axis=1)
data.fillna(data.mean(), inplace=True)


def graph():
    sns.heatmap(data.corr(), annot=True)
    plt.show()
    df = data.corr()
    df.index = range(0, len(df))
    df.rename(columns=dict(zip(df.columns, df.index)), inplace=True)
    df = df.astype(object)

    for i in range(0, len(df)):

        for j in range(0, len(df)):

            if i != j:

                df.iloc[i, j] = (i, j, df.iloc[i, j])
            else:

                df.iloc[i, j] = (i, j, 0)

    df_list = []

    for sub_list in df.values:
        df_list.extend(sub_list)

    plot_df = pd.DataFrame(df_list)

    fig = plt.figure()
    ax = Axes3D(fig)

    ax.plot_trisurf(plot_df[0], plot_df[1], plot_df[2], cmap=cm.jet, linewidth=0.2)

    plt.show()


def calculate_mean_value_corr():

    positive = []
    sum = 0
    for a in range(len(attractions)):
        for b in range(a + 1, len(attractions)):
            correlation = np.corrcoef(attractions[a], attractions[b])[0][1]
            if correlation > 0 and correlation != 1:
                sum = sum + correlation
                positive.append(attractions[a].name + ' ' + attractions[b].name)

    return sum / len(positive)

def correlations():

    attractions = [attraction for (a, attraction) in data.iteritems()]

    positive_final = []

    mean_value = calculate_mean_value_corr()

    for a in attractions:
        for b in attractions:

            correlation = np.corrcoef(a, b)[0][1]
            if correlation != 1 and correlation > mean_value:
                positive_final.append(a.name + ' ' + b.name)

    return positive_final


if __name__ == "__main__":
    correlations()
    graph()
