import numpy as np
from scipy.spatial import distance


def pair_correlation_function_3d(points, r_max, dr):
    distances = distance.pdist(points)
    distances = distance.squareform(distances)
    num_points = len(points)

    r = np.arange(0, r_max, dr)
    g_r = np.zeros_like(r)

    for i in range(num_points):
        for j in range(i + 1, num_points):
            d = distances[i, j]
            if d < r_max:
                bin_index = int(d // dr)
                g_r[bin_index] += 2  # Учитываем пары точек (i, j) и (j, i)

    volume = (4 / 3) * np.pi * (np.arange(1, len(r) + 1) * dr) ** 3 - (4 / 3) * np.pi * (np.arange(len(r)) * dr) ** 3
    density = num_points / (4 / 3 * np.pi * r_max ** 3)
    g_r = g_r / (density * volume * num_points)

    return r, g_r


# Пример данных
points = np.random.rand(100, 3) * 10  # 100 случайных точек в кубе 10x10x10
print(points)
r_max = 5
dr = 0.1

r, g_r = pair_correlation_function_3d(points, r_max, dr)

# Визуализация
import matplotlib.pyplot as plt

plt.plot(r, g_r)
plt.xlabel('Расстояние r')
plt.ylabel('g(r)')
plt.title('Функция парной корреляции для 3D')
plt.show()