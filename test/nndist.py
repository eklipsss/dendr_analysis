import numpy as np
from scipy.spatial import distance


def nearest_neighbor_distance(points):
    """
    Вычисляет среднее расстояние до ближайшего соседа для набора точек в 3D пространстве.

    :param points: numpy массив размером (N, 3), где N - количество точек.
    :return: Среднее расстояние до ближайшего соседа.
    """
    num_points = len(points)
    if num_points < 2:
        raise ValueError("Должно быть как минимум две точки для вычисления расстояний.")

    # Вычисляем все попарные расстояния
    distances = distance.pdist(points)
    distances = distance.squareform(distances)

    # Находим минимальное расстояние для каждой точки (исключая расстояние до самой себя)
    min_distances = np.min(distances + np.eye(num_points) * distances.max(), axis=1)

    # Вычисляем среднее минимальное расстояние
    mean_nndist = np.mean(min_distances)

    return mean_nndist


# Пример данных
points = np.random.rand(100, 3) * 10  # 100 случайных точек в кубе 10x10x10

# Вычисление среднего расстояния до ближайшего соседа
mean_nndist = nearest_neighbor_distance(points)
print(f"Среднее расстояние до ближайшего соседа: {mean_nndist:.4f}")