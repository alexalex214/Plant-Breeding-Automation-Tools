# This script creates bar graphs and bell curve (normal distribution curve). I did it for two populations, but you can add more

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Чтение данных из Excel
file_path = 'C:/Users/21.xlsx'  # замените на путь к вашему файлу
data = pd.read_excel(file_path)

# Разделяем данные по популяциям
population_B = data[data['Population'] == 'B']['Number']
population_R = data[data['Population'] == 'R']['Number']

# Настройка параметров для нормального распределения
mu_B, sigma_B = np.mean(population_B), np.std(population_B)
mu_R, sigma_R = np.mean(population_R), np.std(population_R)

# Построение гистограммы и кривой нормального распределения
plt.figure(figsize=(10, 6))

count_B, bins_B, ignored_B = plt.hist(population_B, bins=20, density=True, color='blue', alpha=0.6, label='Population B')
count_R, bins_R, ignored_R = plt.hist(population_R, bins=20, density=True, color='red', alpha=0.6, label='Population R')

# Графики для нормального распределения
plt.plot(bins_B, 1/(sigma_B * np.sqrt(2 * np.pi)) * np.exp(-(bins_B - mu_B)**2 / (2 * sigma_B**2)), color='blue')
plt.plot(bins_R, 1/(sigma_R * np.sqrt(2 * np.pi)) * np.exp(-(bins_R - mu_R)**2 / (2 * sigma_R**2)), color='red')

# Настройки графика
plt.title('Histogram and Normal Distribution for Populations B and R')
plt.xlabel('Number')
plt.ylabel('Density')
plt.legend()

# Показать график
plt.show()
