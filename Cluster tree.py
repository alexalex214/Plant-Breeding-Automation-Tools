# This python script creates a cluster tree with required method of clusterization

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage
from scipy.spatial.distance import pdist, squareform

# 1. Upload data from Excel
file_path = 'C:/Users/yourcluster.xlsx'  # Path to a file
data = pd.read_excel(file_path)

# 2. Extract numeric data (e.g. 'Number1' and 'Number2')
numeric_data = data[['Number1', 'Number2']].values  # Change according to the uploaded data
names = data['Name'].values

# 3. Calculate Euclidean distances
distances = pdist(numeric_data, metric='euclidean')
distance_matrix = squareform(distances)

# 4. Save distance matrix in Excel
distance_df = pd.DataFrame(distance_matrix, index=names, columns=names)
distance_df.to_excel('C:/Users/distance_matrix.xlsx', sheet_name='Distances')

# 5. Perform hierarchical clustering methods could be: single, complete, average, weighted, centroid, median, ward
linked = linkage(numeric_data, method='average')

# 6. Build a cluster tree
plt.figure(figsize=(10, 7))
dendrogram(linked, labels=names)
plt.title("Cluster tree")
plt.xlabel("Name")
plt.ylabel("Distance")
plt.show()
