import numpy as np
from sklearn.decomposition import PCA


# Предположим, что у нас есть массив точек в 3D
# points - это массив размера (n, 3), где n - количество точек
# Например:
# points = np.array([[x1, y1, z1], [x2, y2, z2], ..., [xn, yn, zn]])

def cylindrical_coordinates(points):
    # Центрирование точек
    points_centered = points - np.mean(points, axis=0)

    # Применяем PCA
    pca = PCA(n_components=3)
    pca.fit(points_centered)

    # Получаем первую главную компоненту, вдоль которой вытянута фигура
    w = pca.components_[0]

    # Вычисляем координату вдоль оси w для каждой точки (высота h)
    heights = points_centered @ w  # скалярное произведение для проекции

    # Получаем вторую и третью компоненты PCA (перпендикулярные к w)
    u = pca.components_[1]
    v = pca.components_[2]

    # Проекция точек на плоскость, перпендикулярную w, для угловой координаты
    x_proj = points_centered @ u
    y_proj = points_centered @ v

    # Вычисляем угол θ для каждой точки в плоскости, перпендикулярной w
    angles = np.arctan2(y_proj, x_proj)

    # Возвращаем координаты в цилиндрическом формате (высота, угол)
    cylindrical_coords = np.column_stack((heights, angles))

    return cylindrical_coords


# Пример использования:
points = np.random.rand(100, 3)  # замените на ваш массив точек
print(points)
cylindrical_coords = cylindrical_coordinates(points)

# cylindrical_coords теперь содержит две колонки:
# первая - это "высота" вдоль вытянутой оси w
# вторая - это угол в проекции на плоскость, перпендикулярную w
