import pandas as pd
import numpy as np
from sklearn.preprocessing import RobustScaler
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
import matplotlib.pyplot as plt

X = np.load('X_array.npy')

kmeans = KMeans(n_clusters=4, init='k-means++', n_init=10, max_iter=300, random_state=42)

kmeans_labels = kmeans.fit_predict(X)

kmeans_silhouette = silhouette_score(X, kmeans_labels)
print(f'Score de Silhueta para KMeans: {kmeans_silhouette:.4f}')

df_clusterizacao = pd.read_pickle('df_clusterizacao.pkl')
df_clusterizacao['cluster'] = kmeans_labels
print(df_clusterizacao.head())
df_clusterizacao.to_pickle('df_clusterizacao_clusters.pkl')