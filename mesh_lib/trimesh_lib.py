import trimesh
import numpy as np
from scipy.spatial import ConvexHull
import pyvista as pv
import pymeshfix


# Параметры сферической оболочки
R_inner = 5.5  # внутренний радиус сферы
R_outer = 6.0 # внешний радиус сферы
# R_inner = 29.0   # внутренний радиус сферы
# R_outer = 29.5 # внешний радиус сферы
# R_inner = 29.5   # внутренний радиус сферы
# R_outer = 30.0 # внешний радиус сферы
# R_inner = 20.0   # внутренний радиус сферы
# R_outer = 20.5  # внешний радиус сферы


# Параметры цилиндрической оболочки
# r_inner = 0.9441932676943663   # внутренний радиус цилиндра
# r_outer = 2.2630931528081675  # внешний радиус цилиндра
# height = 38.87591808962762  # высота цилиндра

# r_inner = 0.2   # внутренний радиус цилиндра
# r_outer = 0.3  # внешний радиус цилиндра
# height = 2  # высота цилиндра
r_inner = 0.9439909078537088   # внутренний радиус цилиндра
r_outer = 2.2628907929675064  # внешний радиус цилиндра
height = 38.844623180860204  # высота цилиндра

# Расчет смещения центра сферической оболочки
sphere_center_offset = (r_inner + r_outer) / 2.0


# Создание сферической оболочки
def create_spherical_shell(inner_radius, outer_radius, center=(0, 0, 0)):
    outer_sphere = trimesh.creation.icosphere(radius=outer_radius, subdivisions=3)
    if inner_radius == 0.0:
        outer_sphere.apply_translation(center)
        return outer_sphere
    inner_sphere = trimesh.creation.icosphere(radius=inner_radius, subdivisions=3)
    outer_sphere.apply_translation(center)
    inner_sphere.apply_translation(center)
    # Создание оболочки разностью внешней и внутренней сфер
    spherical_shell = outer_sphere.difference(inner_sphere)
    return spherical_shell


# Создание цилиндрической оболочки
def create_cylindrical_shell(inner_radius, outer_radius, height):
    outer_cylinder = trimesh.creation.cylinder(radius=outer_radius, height=height, sections=50)
    inner_cylinder = trimesh.creation.cylinder(radius=inner_radius, height=height, sections=50)
    # Разность между внешним и внутренним цилиндрами создаст оболочку
    cylindrical_shell = outer_cylinder.difference(inner_cylinder)
    return cylindrical_shell


# Функция для нахождения объема пересечения методом Монте-Карло
def intersection_volume(shell1, shell2, num_samples=10000):
    # Генерируем случайные точки в пределах ограничивающего параллелепипеда
    # bounds_min = np.minimum(shell1.bounds[0], shell2.bounds[0])
    # bounds_max = np.maximum(shell1.bounds[1], shell2.bounds[1])
    bounds_min = np.array(shell1.bounds[0])
    bounds_max = np.array(shell1.bounds[1])
    print(bounds_min, bounds_max)

    # Случайные точки внутри ограничивающего параллелепипеда
    random_points = np.random.uniform(bounds_min, bounds_max, (num_samples, 3))

    # Проверяем, сколько точек попадают в обе оболочки
    in_shell1 = shell1.contains(random_points)
    # print('in_shell1: ', in_shell1)
    in_shell2 = shell2.contains(random_points)
    # print('in_shell2: ', in_shell2)
    in_both_shells = in_shell1 & in_shell2  # точки в пересечении
    # print('in_both_shells: ', in_both_shells)

    # Оцениваем объем пересечения
    bbox_volume = np.prod(bounds_max - bounds_min)
    intersection_volume = bbox_volume * np.sum(in_both_shells) / num_samples
    return intersection_volume

# Функция для сохранения сетки в формате .off
def save_mesh_to_off(mesh, filename):
    mesh.export(filename, file_type="off")
    print(f"Сохранено в {filename}")


def get_pv_mesh(mesh_trimesh):
    # Получаем вершины
    vertices = mesh_trimesh.vertices

    # Преобразуем faces в формат, ожидаемый PyVista: [3, v1, v2, v3, 3, v4, v5, v6, ...]
    faces = np.hstack([[3] + face.tolist() for face in mesh_trimesh.faces])

    # Создаем PyVista PolyData
    pv_mesh = pv.PolyData(vertices, faces)

    return pv_mesh


print(sphere_center_offset)
# Создаем сферическую и цилиндрическую оболочки
spherical_shell = create_spherical_shell(R_inner, R_outer, center=(0, sphere_center_offset, 0))
# spherical_shell = create_spherical_shell(R_inner, R_outer, center=(0, sphere_center_offset, -height/2))
cylindrical_shell = create_cylindrical_shell(r_inner, r_outer, height)



pv_spherical_shell = get_pv_mesh(spherical_shell)
pv_cylindrical_shell = get_pv_mesh(cylindrical_shell)

# Находим пересечение двух моделей
intersection_mesh = pv_spherical_shell.boolean_intersection(pv_cylindrical_shell)

fill_intersection_mesh = intersection_mesh.fill_holes(hole_size=5.0)
# fill_intersection_mesh = intersection_mesh

# Вычисляем объем пересечения
intersection_volume = fill_intersection_mesh.volume

print('intersection_volume: ', intersection_volume)



# Находим объем пересечения
# volume_of_intersection = intersection_volume(spherical_shell, cylindrical_shell)
# print(f"Объем пересечения сферической и цилиндрической оболочек: {volume_of_intersection:.3f}")

# Сохраняем оболочки в файлы .off
save_mesh_to_off(spherical_shell, "spherical_shell_trimesh.off")
save_mesh_to_off(cylindrical_shell, "cylindrical_shell_trimesh.off")

# Визуализация оболочек и их пересечения
# spherical_shell.show()
# cylindrical_shell.show()

# Задаем цвет для сферической оболочки (например, красный)
spherical_color = trimesh.visual.ColorVisuals(vertex_colors=np.array([[255, 0, 0, 255]] * spherical_shell.vertices.shape[0]))

# Задаем цвет для цилиндрической оболочки (например, синий)
cylindrical_color = trimesh.visual.ColorVisuals(vertex_colors=np.array([[0, 0, 255, 255]] * cylindrical_shell.vertices.shape[0]))

# Применяем материалы к геометриям
spherical_shell.visual = spherical_color
cylindrical_shell.visual = cylindrical_color

# Создаем сцену
scene = trimesh.Scene()

# Добавляем оба объекта на сцену
scene.add_geometry(spherical_shell)
scene.add_geometry(cylindrical_shell)

# Используем встроенный визуализатор Trimesh для отображения сцены
scene.show()

plotter = pv.Plotter()

plotter.add_mesh(pv_spherical_shell, color="red", opacity=0.5, show_edges=True)
plotter.add_mesh(pv_cylindrical_shell, color="green", opacity=0.5, show_edges=True)

# plotter.add_mesh(fill_intersection_mesh, color="green", opacity=0.5, show_edges=True)

plotter.add_axes()

plotter.show()

# k = 2 * volume_of_intersection
# print(k)
