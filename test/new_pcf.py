import numpy as np

def compute_pcf(spines, dr, max_r):
    """
    Вычисление функции парной корреляции (PCF).

    :param spines: Список координат частиц в виде массива numpy (N x 3).
    :param dr: Толщина сферической оболочки.
    :param max_r: Максимальное значение радиуса, до которого вычисляется PCF.
    :return: Массив значений r и соответствующих значений PCF.
    """
    # Инициализация переменных
    n = len(spines)
    print("spines: ", spines)
    print("spines.max(axis=0): ", spines.max(axis=0))
    print("spines.min(axis=0): ", spines.min(axis=0))
    print("(spines.max(axis=0) - spines.min(axis=0)).prod(): ", (spines.max(axis=0) - spines.min(axis=0)).prod())
    density = n / (spines.max(axis=0) - spines.min(axis=0)).prod()
    r_values = np.arange(0, max_r, dr)
    pcf_values = np.zeros_like(r_values, dtype=float)

    # Основной цикл по значениям r
    for i, r in enumerate(r_values):
        shell_volume = 4 * np.pi * r**2 * dr
        count = 0

        # Цикл по всем частицам
        for spine in spines:
            distances = np.linalg.norm(spines - spine, axis=1)
            count += np.sum((distances >= r) & (distances < r + dr))

        # Вычисление PCF для текущего значения r
        pcf_values[i] = count / (n * shell_volume * density)

    return r_values, pcf_values

# Пример использования функции
particles = np.random.rand(1000, 3)  # Генерация случайных частиц в объеме 1x1x1
dr = 0.01
max_r = 0.5
r_values, pcf_values = compute_pcf(particles, dr, max_r)

# Вывод результатов
import matplotlib.pyplot as plt
plt.plot(r_values, pcf_values)
plt.xlabel('r')
plt.ylabel('g(r)')
plt.title('Pair Correlation Function')
plt.show()