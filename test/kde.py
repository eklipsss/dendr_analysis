import numpy as np
import seaborn as sns
import matplotlib
import matplotlib.pyplot as plt

# Генерация случайных данных (например, нормально распределенные данные)
data = np.random.normal(loc=0, scale=1, size=1000)
data = np.random.exponential(size=1000)
data = np.array([])
for i in range(100):
    data = np.append(data, i)
print(data)
# Построение графика KDE
sns.kdeplot(data, bw_adjust=0.5)  # bw_adjust управляет шириной ядра
plt.title("Kernel Density Estimation")
plt.xlabel("Value")
plt.ylabel("Density")
plt.show()
print(sns.__version__)
print(matplotlib.__version__)

# import numpy as np
# from sklearn.neighbors import KernelDensity
# import matplotlib.pyplot as plt
# from mpl_toolkits.mplot3d import Axes3D
# from mpl_toolkits.mplot3d import axes3d
#
#
# def kde_3d(points, bandwidth=1.0, grid_size=100):
#     """
#     Функция для оценки плотности распределения точек в 3D-пространстве с помощью KDE.
#
#     :param points: Массив точек (n, 3), каждая точка содержит координаты x, y, z.
#     :param bandwidth: Параметр сглаживания для KDE (чем больше, тем более сглаженная плотность).
#     :param grid_size: Размер сетки для визуализации плотности.
#     :return: Координаты сетки (X, Y, Z) и оценка плотности на этой сетке.
#     """
#     # Определим границы для сетки
#     x_min, x_max = np.min(points[:, 0]), np.max(points[:, 0])
#     y_min, y_max = np.min(points[:, 1]), np.max(points[:, 1])
#     z_min, z_max = np.min(points[:, 2]), np.max(points[:, 2])
#
#     # Генерация сетки для вычисления плотности
#     x_grid = np.linspace(x_min, x_max, grid_size)
#     y_grid = np.linspace(y_min, y_max, grid_size)
#     z_grid = np.linspace(z_min, z_max, grid_size)
#     X, Y, Z = np.meshgrid(x_grid, y_grid, z_grid)
#
#     # Преобразуем сетку в массив для оценки плотности
#     grid_points = np.vstack([X.ravel(), Y.ravel(), Z.ravel()]).T
#
#     # Создаем и обучаем модель KDE
#     kde = KernelDensity(bandwidth=bandwidth, kernel='gaussian')
#     kde.fit(points)
#
#     # Оценка плотности на сетке
#     log_density = kde.score_samples(grid_points)
#     density = np.exp(log_density).reshape(X.shape)
#
#     return X, Y, Z, density
#
#
# # Пример использования
# if __name__ == "__main__":
#     # Генерируем случайные точки в 3D-пространстве
#     np.random.seed(42)
#     points = np.random.rand(100, 3) * 10  # 100 точек в пределах 10x10x10
#
#     # Оценка плотности с помощью KDE
#     X, Y, Z, density = kde_3d(points, bandwidth=0.5, grid_size=50)
#
#     # Визуализация плотности в 3D
#     fig = plt.figure()
#     ax = fig.add_subplot(111, projection='3d')
#
#     X, Y, Z = axes3d.get_test_data(0.05)
#
#     # Отображаем изоповерхности плотности
#     print("X: ", X)
#     print("Z: ", Z)
#
#     print(len(density), density)
#     ax.contour(X, Y, Z)
#     # ax.contour3D(X, Y, Z, density, 50, cmap='viridis')
#
#     ax.set_xlabel('X')
#     ax.set_ylabel('Y')
#     ax.set_zlabel('Z')
#     plt.show()




# import matplotlib.pyplot as plt
#
# from matplotlib import cm
# from mpl_toolkits.mplot3d import axes3d
#
# ax = plt.figure().add_subplot(projection='3d')
# X, Y, Z = axes3d.get_test_data(0.05)
#
# print("X: ", X)
# print("Z: ", Z)
#
# ax.contour(X, Y, Z, cmap=cm.coolwarm)  # Plot contour curves
#
# plt.show()