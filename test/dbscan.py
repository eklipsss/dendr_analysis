import numpy as np
from sklearn.cluster import DBSCAN
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Генерация случайных точек в 3D пространстве
np.random.seed(0)
points = np.random.rand(100, 3)  # 100 точек с тремя координатами
print(points)
# points = [[]]


# Параметры DBSCAN
eps = 0.2  # максимальное расстояние между двумя точками для их объединения в один кластер
min_samples = 3  # минимальное количество точек для формирования кластера

# Кластеризация с использованием DBSCAN
db = DBSCAN(eps=eps, min_samples=min_samples).fit(points)
labels = db.labels_

# Количество кластеров (исключая шум)
n_clusters = len(set(labels)) - (1 if -1 in labels else 0)
print(f'Количество кластеров: {n_clusters}')

# Визуализация результатов кластеризации
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

unique_labels = set(labels)
print(len(unique_labels))
colors = plt.cm.Spectral(np.linspace(0, 1, len(unique_labels)))

for k, col in zip(unique_labels, colors):
    if k == -1:
        # Черный цвет для шума
        col = [0, 0, 0, 1]

    class_member_mask = (labels == k)
    xyz = points[class_member_mask]
    ax.scatter(xyz[:, 0], xyz[:, 1], xyz[:, 2], c=[col], label=f'Cluster {k}')

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.legend()
plt.show()