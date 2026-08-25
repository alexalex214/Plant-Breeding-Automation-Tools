# This python script creates a cluster tree with required method of clusterization

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage
from scipy.spatial.distance import pdist, squareform

# 1. Загрузите данные из Excel
file_path = 'C:/Users/yourcluster.xlsx'  # Укажите путь к вашему файлу
data = pd.read_excel(file_path)

# 2. Извлеките числовые данные (например, 'Number1' и 'Number2')
numeric_data = data[['Number1', 'Number2']].values  # Измените в соответствии с вашими данными
names = data['Name'].values  # Извлекаем имена образцов

# 3. Вычислите евклидовы расстояния
distances = pdist(numeric_data, metric='euclidean')  # Вычисление расстояний
distance_matrix = squareform(distances)  # Преобразование в матрицу

# 4. Сохраните матрицу расстояний в Excel
distance_df = pd.DataFrame(distance_matrix, index=names, columns=names)
distance_df.to_excel('C:/Users/distance_matrix.xlsx', sheet_name='Distances')

# 5. Выполните иерархическую кластеризацию: single, complete, average, weighted, centroid, median, ward
linked = linkage(numeric_data, method='average')

# 6. Постройте кластерное древо
plt.figure(figsize=(10, 7))
dendrogram(linked, labels=names)  # Используем названия для меток
plt.title("Cluster tree")
plt.xlabel("Name")
plt.ylabel("Distance")
plt.show()

