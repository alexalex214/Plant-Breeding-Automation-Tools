#This script performs principal component analysis (PCA) and creates a dendrogram cluster tree based on Warden's method. For that you need to change data path and output paths

import pandas as pd
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage

data = pd.read_excel('C:/file_path/1.xlsx')

features = ['Trait 1', 'Trait 2']  # Удалены лишние квадратные скобки

pca = PCA(n_components=2)

principal_components = pca.fit_transform(data[features])  # Используйте features без лишних скобок

pca_df = pd.DataFrame(principal_components, columns=['PC1', 'PC2'])

pca_df['Genotype'] = data['Genotype']

print(pca_df.head())

plt.figure(figsize=(8, 6))
plt.scatter(pca_df['PC1'], pca_df['PC2'])

for i, genotype in enumerate(pca_df['Genotype']):
    plt.text(pca_df['PC1'][i], pca_df['PC2'][i], genotype)

plt.xlabel('PC1')
plt.ylabel('PC2')
plt.title('PCA of Genotype Data')
plt.show()

pca_df.to_excel('C:/file_path/pca_results.xlsx')
pca_df.to_csv('C:/file_path/pca_results.txt')

plt.figure(figsize=(10, 7))
linked = linkage(principal_components, method='ward')
dendrogram(linked, orientation='top', labels=pca_df['Genotype'].values, distance_sort='descending', show_leaf_counts=True)

plt.title('Hierarchical Clustering Dendrogram')
plt.xlabel('Genotypes')
plt.ylabel('Distance')
plt.show()
