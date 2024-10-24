#Biblioteca
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df_clusterizacao_clusters = pd.read_pickle('df_clusterizacao_clusters.pkl')
print(df_clusterizacao_clusters.info())
print(df_clusterizacao_clusters.head())

sns.set(style='whitegrid')
fig, axs = plt.subplots(1, 3, figsize=(12, 4))

sns.countplot(x='RECENCIA', hue='cluster', data=df_clusterizacao_clusters, ax=axs[0], 
              palette='Set1', dodge=True, width=0.7)
axs[0].set_title('Contagem de Recência por Cluster')
axs[0].set_xlabel('Recência')
axs[0].set_ylabel('Contagem')

sns.countplot(x='FREQUENCIA', hue='cluster', data=df_clusterizacao_clusters, ax=axs[1], 
              palette='Set1', dodge=True, width=0.7)
axs[1].set_title('Contagem de Frequência por Cluster')
axs[1].set_xlabel('Frequência')
axs[1].set_ylabel('Contagem')

sns.countplot(x='VALOR_MONET', hue='cluster', data=df_clusterizacao_clusters, ax=axs[2], 
              palette='Set1', dodge=True, width=0.7)
axs[2].set_title('Contagem de Valor Monetário por Cluster')
axs[2].set_xlabel('Valor Monetário')
axs[2].set_ylabel('Contagem')
plt.tight_layout()
plt.show()
