import math
import numpy as np
from scipy.integrate import dblquad


def spherical_shell_intersection_volume(R_in, R_out, h, r1, dr):
    """
    Вычисляет объем пересечения цилиндрической оболочки и сферической оболочки.

    Параметры:
    R_in - внутренний радиус цилиндрической оболочки
    R_out - внешний радиус цилиндрической оболочки
    h - высота цилиндрической оболочки
    r1 - внутренний радиус сферической оболочки
    dr - толщина сферической оболочки

    Возвращает:
    Объем пересечения (число)
    """
    r2 = r1 + dr  # внешний радиус сферической оболочки
    z_center = h / 2  # центр сферической оболочки по оси z
    print('r2: ', r2)
    print('(R_out-R_in)/2: ', (R_out-R_in)/2)
    print('h/2: ', h/2)

    if (r2<=((R_out-R_in)/2)) and (r2<=h/2):
        print('1 случай')
        return 4/3 * math.pi * (r2**3-r1**3)

    if (r1>=((R_out-R_in)/2)) and (r1>=h/2):
        print('2 случай')
        return 0

    # Функция, определяющая границы по z для интегрирования
    def z_limits(rho):
        dz = np.sqrt(max(r2 ** 2 - rho ** 2, 0))  # убеждаемся, что подкоренное выражение >= 0
        print('rho: ', rho)
        print('dz: ', dz)
        print('z_center - dz: ', z_center - dz)
        print('z_center + dz: ', z_center + dz)
        return z_center - dz, z_center + dz

    # Подынтегральная функция для вычисления объема пересечения
    def integrand(rho, z):
        distance_from_center = np.sqrt(rho ** 2 + (z - z_center) ** 2)
        # Проверка, попадает ли точка в сферическую и цилиндрическую оболочку
        if R_in <= rho <= R_out and r1 <= distance_from_center <= r2:
            return rho  # в полярных координатах для объема добавляется rho
        return 0

    # Интегрирование по rho и z для вычисления объема пересечения
    volume, error = dblquad(
        integrand,
        R_in, R_out,  # интегрирование по радиусу rho в пределах цилиндрической оболочки
        lambda rho: z_limits(rho)[0],  # нижний предел для z
        lambda rho: z_limits(rho)[1],  # верхний предел для z
        epsabs=1e-9, epsrel=1e-9  # установка высокой точности интеграции
    )

    return volume


# Пример использования:
# R_in = 3  # внутренний радиус цилиндра
# R_out = 7  # внешний радиус цилиндра
# h = 10  # высота цилиндра
# r1 = 4  # внутренний радиус сферической оболочки
# dr = 1  # толщина сферической оболочки
R_in = 0.1  # внутренний радиус цилиндра
R_out = 0.6  # внешний радиус цилиндра
h = 2  # высота цилиндра
r1 = 0.1  # внутренний радиус сферической оболочки
dr = 0.2  # толщина сферической оболочки

volume = spherical_shell_intersection_volume(R_in, R_out, h, r1, dr)
print(f"Объем пересечения: {volume:.4f}")
