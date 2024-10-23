#Bibliotecas
import pandas as pd
import numpy as np
from sklearn.preprocessing import RobustScaler
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
import matplotlib.pyplot as plt

df_clusterizacao = pd.read_pickle('df_clusterizacao.pkl')
print(df_clusterizacao.info())

df_clusterizacao_limpo = df_clusterizacao.drop(['CUSTOMERID' , 'INVOICEDATE'], axis = 1)
print(df_clusterizacao_limpo.head())

scaler = RobustScaler()
X = scaler.fit_transform(df_clusterizacao_limpo)
print(X.shape)
np.save('X_array.npy', X)

k_valores = range(2, 20)
inercias = []
scores_silhueta = []

for k in k_valores:
    kmeans = KMeans(n_clusters=k, init = 'k-means++', n_init='auto', random_state=42)
    kmeans.fit(X)
    inercias.append(kmeans.inertia_)

    cluster_rotulos = kmeans.predict(X)
    media_silhueta = silhouette_score(X, cluster_rotulos)
    scores_silhueta.append(media_silhueta)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
ax1.plot(k_valores, inercias, marker='o')
ax1.set_title('Método do Cotovelo')
ax1.set_xlabel('Número de clusters, k')
ax1.set_ylabel('Inércia')
ax1.grid(True)

ax2.plot(k_valores, scores_silhueta, marker='o')
ax2.set_title('Método da Silhueta')
ax2.set_xlabel('Número de clusters, k')
ax2.set_ylabel('Média da Silhueta')
ax2.grid(True)
plt.show()
     