import numpy as np
from scipy.spatial import distance_matrix

# Параметры цилиндра
radius = 5  # Радиус цилиндра
height = 10  # Высота цилиндра
num_points = 100  # Количество точек

# Генерация случайных точек на поверхности цилиндра
np.random.seed(0)
theta = np.random.uniform(0, 2 * np.pi, num_points)  # Угловая координата
z = np.random.uniform(0, height, num_points)  # Высота

# Значения метрики для каждой точки
metrics = np.random.normal(loc=0, scale=1, size=num_points)

# Преобразование угловых координат в x и y для удобства расчета расстояний
x = radius * np.cos(theta)
y = radius * np.sin(theta)
points = np.vstack((x, y, z)).T

print('points: ', points)



# ВЫЧИСЛЕНИЕ ВЕСОВОЙ МАТРИЦЫ

# Задаем пороговое расстояние для окрестности
threshold_distance = 2.0  # Расстояние, до которого точки считаются соседями

# Вычисление матрицы расстояний
dist_matrix = distance_matrix(points, points)

# Создаем весовую матрицу на основе порога
W = (dist_matrix < threshold_distance).astype(int)
np.fill_diagonal(W, 0)  # Исключаем самих себя из соседей



# ВЫЧИСЛЕНИЕ АВТОКОРРЕЛЯЦИИ МОРАНА

def morans_i(metrics, W):
    n = len(metrics)
    mean_metric = np.mean(metrics)

    # Числитель Moran's I
    num = 0
    for i in range(n):
        for j in range(n):
            num += W[i, j] * (metrics[i] - mean_metric) * (metrics[j] - mean_metric)

    # Знаменатель Moran's I
    denom = np.sum((metrics - mean_metric) ** 2)

    # Число соседей
    W_sum = np.sum(W)

    # Рассчитываем Moran's I
    I = (n / W_sum) * (num / denom)
    return I


# Вычисление Moran's I для метрик
moran_i_value = morans_i(metrics, W)
print("Значение коэффициента Moran's I:", moran_i_value)

