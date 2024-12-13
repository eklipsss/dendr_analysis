import numpy as np


def cylindrical_to_flat(cylindrical_points):
    """
    Преобразует множество точек с поверхности цилиндра в плоскость.

    Параметры:
        cylindrical_points (list of tuples): Список точек, заданных в цилиндрических координатах (r, theta, z).

    Возвращает:
        flat_points (list of tuples): Список точек в плоских координатах (x_flat, y_flat).
    """
    flat_points = []
    for r, theta, z in cylindrical_points:
        # Разворачиваем цилиндр на плоскости
        x_flat = r * theta
        y_flat = z
        flat_points.append((x_flat, y_flat))
    return flat_points


# Пример точек в цилиндрических координатах
cylindrical_points = [
    (1, 0, 0),
    (1, np.pi / 4, 0),
    (1, np.pi / 2, 0),
    (1, 3 * np.pi / 4, 0),
    (1, np.pi, 0),
    (1, 0, 1),
    (1, np.pi / 4, 1),
    # и так далее
]

# Преобразуем точки
flat_points = cylindrical_to_flat(cylindrical_points)

# Выводим результат
print("Точки на плоскости:", flat_points)
