import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans, AgglomerativeClustering
import scipy.cluster.hierarchy as shc


def readData():
    data = pd.read_csv('Travel review.csv', encoding='utf-8')
    data = data.drop(data.columns[25], axis=1)
    data = data.drop(['User'], axis=1)
    data.fillna(data.mean(), inplace=True)
    return data


def graph():
    X = np.array(readData())
    kmeans = KMeans(n_clusters=7)
    kmeans.fit(X)
    print(kmeans.cluster_centers_)
    print(kmeans.labels_)
    plt.scatter(X[:, 0], X[:, 1], c=kmeans.labels_, cmap='rainbow')
    plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], color='black')
    # if it is required to save picture in directory, activate following command
    # plt.savefig('clustering.png', bbox_inches='tight')
    plt.show()


def dendogramAndClusters():
    data = readData().iloc[:, 1:25].values
    plt.figure(figsize=(10, 7))
    plt.title("Dendogram")
    dend = shc.dendrogram(shc.linkage(data, method='ward'))
    plt.show()
    cluster = AgglomerativeClustering(n_clusters=7, affinity='euclidean', linkage='ward')
    print(pd.DataFrame(cluster.fit_predict(data)))
    plt.figure(figsize=(10, 7))
    plt.scatter(data[:, 0], data[:, 1], c=cluster.labels_, cmap='rainbow')
    plt.show()

if __name__ == "__main__":
    graph()
    dendogramAndClusters()