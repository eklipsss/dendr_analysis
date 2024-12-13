#
# import pyvista as pv
# import numpy as np
# from pandas.core.computation.expr import intersection
#
# # Параметры сферической оболочки
# R_inner = 6.0  # внутренний радиус сферы
# R_outer = 5.0  # внешний радиус сферы
#
# # Параметры цилиндрической оболочки
# r_inner = 3.0  # внутренний радиус цилиндра
# r_outer = 4.0  # внешний радиус цилиндра
# height = 8.0  # высота цилиндра
#
# # Расчет смещения центра сферической оболочки
# sphere_center_offset = (r_inner + r_outer) / 2.0
#
#
# # Создание сферической оболочки
# def create_spherical_shell(inner_radius, outer_radius, center=(0, 0, 0)):
#     plotter1 = pv.Plotter()
#
#     # Внешняя сфера
#     outer_sphere = pv.Sphere(radius=outer_radius, center=center, theta_resolution=60, phi_resolution=60)
#     print('v: ', outer_sphere.volume)
#     print(outer_sphere.n_points)
#     print(outer_sphere)
#     # outer_sphere = outer_sphere.triangulate()
#     if outer_sphere is not None and outer_sphere.n_points > 0:
#         print('if')
#         plotter1.add_mesh(outer_sphere, color="blue", opacity=0.5, show_edges=True)
#     # Внутренняя сфера
#     inner_sphere = pv.Sphere(radius=inner_radius, center=center, theta_resolution=60, phi_resolution=60)
#     # inner_sphere = inner_sphere.triangulate()
#     if inner_sphere is not None and outer_sphere.n_points > 0:
#         plotter1.add_mesh(inner_sphere, color="green", opacity=0.5, show_edges=True)
#
#     plotter1.add_axes()
#     plotter1.show()
#
#     # Создаем оболочку путем вычитания внутренней сферы из внешней
#     spherical_shell = outer_sphere.boolean_difference(inner_sphere)
#     return spherical_shell
#
#
# # Создание цилиндрической оболочки с триангуляцией
# def create_cylindrical_shell(inner_radius, outer_radius, height, sphere_center_offset):
#     # Внешний цилиндр
#     outer_cylinder = pv.Cylinder(radius=outer_radius, height=height, center=(0, 0, 0), direction=(0, 0, 1),
#                                  resolution=60)
#     outer_cylinder = outer_cylinder.triangulate()  # Триангуляция внешнего цилиндра
#
#     # Внутренний цилиндр
#     inner_cylinder = pv.Cylinder(radius=inner_radius, height=height, center=(0, 0, 0), direction=(0, 0, 1),
#                                  resolution=60)
#     inner_cylinder = inner_cylinder.triangulate()  # Триангуляция внутреннего цилиндра
#
#     # Создаем оболочку путем вычитания внутреннего цилиндра из внешнего
#     cylindrical_shell = outer_cylinder.boolean_difference(inner_cylinder)
#     return cylindrical_shell
#
# def inter_v(sp_inn_r, sp_out_r, c_inn_r, c_out_r, height, center=(0, 0, 0)):
#     # Внешняя сфера
#     outer_sphere = pv.Sphere(radius=sp_out_r, center=center, theta_resolution=60, phi_resolution=60)
#
#     # Внутренняя сфера
#     inner_sphere = pv.Sphere(radius=sp_inn_r, center=center, theta_resolution=60, phi_resolution=60)
#
#     # Внешний цилиндр
#     outer_cylinder = pv.Cylinder(radius=c_out_r, height=height, center=(0, 0, 0), direction=(0, 0, 1),
#                                  resolution=60)
#     outer_cylinder = outer_cylinder.triangulate()  # Триангуляция внешнего цилиндра
#
#     # Внутренний цилиндр
#     inner_cylinder = pv.Cylinder(radius=c_inn_r, height=height, center=(0, 0, 0), direction=(0, 0, 1),
#                                  resolution=60)
#     inner_cylinder = inner_cylinder.triangulate()  # Триангуляция внутреннего цилиндра
#
#     # Создаем оболочку путем вычитания внутреннего цилиндра из внешнего
#     # cylindrical_shell = outer_cylinder.boolean_difference(inner_cylinder)
#     # intersection1 = cylindrical_shell.boolean_intersection(inner_sphere)
#
#
#     cylindrical_shell = pv.CylinderStructured(radius=np.linspace(2, 4), height=height)
#
#     sphere_shell = pv.SolidSphere(outer_radius=3.0, inner_radius=1.0,)
#
#     plt = pv.Plotter()
#
#     # if intersection1 is not None and intersection1.n_points > 0:
#     #     print('int_if')
#     #     plt.add_mesh(intersection1, color="red", opacity=0.5, show_edges=True)
#
#     # if sphere_shell is not None and sphere_shell.n_points > 0:
#     #     print('int_if')
#     #     plt.add_mesh(sphere_shell, color="red", opacity=0.5, show_edges=True)
#     #
#     # if cylindrical_shell is not None and cylindrical_shell.n_points > 0:
#     #     print('int_if')
#     #     plt.add_mesh(cylindrical_shell, color="green", opacity=0.5, show_edges=True)
#
#
#     cylindrical_shell = cylindrical_shell.extract_surface().triangulate()
#     sphere_shell = sphere_shell.extract_surface().triangulate()
#
#     # intersection = cylindrical_shell.boolean_difference(sphere_shell)
#     intersection = cylindrical_shell.intersection(sphere_shell)
#     cylindrical_shell.save("cylindrical_shell.obj")
#     sphere_shell.save("sphere_shell.obj")
#
#     plt.add_axes()
#     plt.show()
#
#     return intersection
#
#
# # Функция для нахождения объема пересечения двух оболочек
# def intersection_volume(shell1, shell2):
#     # Пересечение двух оболочек
#     shell1 = shell1.triangulate()
#     shell2 = shell2.triangulate()
#     # shell1 = shell1.extract_surface().triangulate().cast_to_unstructured_grid()
#     # shell2 = shell2.extract_surface().triangulate().cast_to_unstructured_grid()
#
#     intersection = shell1.boolean_intersection(shell2)
#     if intersection is not None:
#         # Вычисляем объем пересечения
#         volume = intersection.volume
#         return volume
#     else:
#         # Если пересечения нет, возвращаем объем 0
#         return 0.0
#
#
# # Создаем сферическую и цилиндрическую оболочки
# intersection = inter_v(R_inner, R_outer, r_inner, r_outer, height, center=(0, 0, sphere_center_offset))
#
#
# # spherical_shell = create_spherical_shell(R_inner, R_outer, center=(0, 0, sphere_center_offset))
# # cylindrical_shell = create_cylindrical_shell(r_inner, r_outer, height, sphere_center_offset)
#
# # Находим объем пересечения
# # volume_of_intersection = intersection_volume(spherical_shell, cylindrical_shell)
# # print(f"Объем пересечения сферической и цилиндрической оболочек: {volume_of_intersection:.3f}")
#
# # Визуализация оболочек и их пересечения
# plotter = pv.Plotter()
# #
# # if spherical_shell is not None and spherical_shell.n_points > 0:
# #     plotter.add_mesh(spherical_shell, color="blue", opacity=0.5, show_edges=True)
# #
# # if cylindrical_shell is not None and cylindrical_shell.n_points > 0:
# #     plotter.add_mesh(cylindrical_shell, color="red", opacity=0.5, show_edges=True)
# print(intersection)
# if intersection[2] is not None :
#     plotter.add_mesh(intersection[2], color="red", opacity=0.5, show_edges=True)
#
# # Добавляем пересечение к визуализации, если оно есть
# # if volume_of_intersection > 0:
# #     intersection = spherical_shell.boolean_intersection(cylindrical_shell)
# #     plotter.add_mesh(intersection, color="green", opacity=0.5, show_edges=True)
#
# plotter.add_axes()
# plotter.show()

import trimesh
import pyvista as pv
import numpy as np


# Загрузка файла .off с помощью trimesh и конвертация в pyvista PolyData
def load_off_as_pyvista_mesh(filename):
    # Загружаем .off файл с помощью trimesh
    mesh_trimesh = trimesh.load(filename)

    # Получаем вершины
    vertices = mesh_trimesh.vertices

    # Преобразуем faces в формат, ожидаемый PyVista: [3, v1, v2, v3, 3, v4, v5, v6, ...]
    faces = np.hstack([[3] + face.tolist() for face in mesh_trimesh.faces])

    # Создаем PyVista PolyData
    pv_mesh = pv.PolyData(vertices, faces)
    return pv_mesh

# Загрузка двух моделей
spherical_shell = load_off_as_pyvista_mesh('spherical_shell_trimesh.off')
cylindrical_shell = load_off_as_pyvista_mesh('cylindrical_shell_trimesh.off')

# # Используем pyvista
# pv_spherical_shell = pv.PolyData(spherical_shell.vertices, spherical_shell.faces.reshape(-1, 4)[:, 1:])
# pv_cylindrical_shell = pv.PolyData(cylindrical_shell.vertices, cylindrical_shell.faces.reshape(-1, 4)[:, 1:])

# Находим пересечение двух моделей
intersection_mesh = spherical_shell.boolean_intersection(cylindrical_shell)

# Вычисляем объем пересечения
intersection_volume = intersection_mesh.volume

print('intersection_volume: ', intersection_volume)