import os
import numpy as np
import trimesh as tm
import skeletor as sk

import pymeshfix


def load_off(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

        if 'OFF' != lines[0].strip():
            raise Exception('Not a valid OFF header')

        n_verts, n_faces, _ = map(int, lines[1].strip().split())
        print(lines[1])
        verts = []
        faces = []

        for i in range(2, 2 + n_verts):
            # print(i, lines[i])
            verts.append(list(map(float, lines[i].strip().split())))

        for i in range(2 + n_verts, 2 + n_verts + n_faces):
            face_data = list(map(int, lines[i].strip().split()[1:]))
            faces.append(face_data)

        # for i in range(3, 3 + n_verts):
        #     # print(i, lines[i])
        #     verts.append(list(map(float, lines[i].strip().split())))
        #
        # for i in range(3 + n_verts, 3 + n_verts + n_faces):
        #     face_data = list(map(int, lines[i].strip().split()[1:]))
        #     faces.append(face_data)

        return np.array(verts), np.array(faces)


def remove_spines_from_main(vertices_main, faces_main, vertices_spines):
    vertices_main_dict = {tuple(v): i for i, v in enumerate(vertices_main)}
    vertices_to_remove = set()

    for verts in vertices_spines:
        for vert in verts:
            if tuple(vert) in vertices_main_dict:
                vertices_to_remove.add(vertices_main_dict[tuple(vert)])

    vertices_clean = [v for i, v in enumerate(vertices_main) if i not in vertices_to_remove]
    index_map = {i: new_i for new_i, i in enumerate(set(range(len(vertices_main))) - vertices_to_remove)}

    faces_clean = []
    for face in faces_main:
        if all(v in index_map for v in face):
            faces_clean.append([index_map[v] for v in face])

    return np.array(vertices_clean), np.array(faces_clean)


def fill_holes_with_pymeshfix(vertices, faces):
    mf = pymeshfix.MeshFix(vertices, faces)
    mf.repair(verbose=False)  # Заполняем дыры
    return mf.v, mf.f  # Возвращаем отремонтированные вершины и грани


def save_off(file_path, vertices, faces):
    with open(file_path, 'w') as file:
        file.write('OFF\n')
        file.write(f'{len(vertices)} {len(faces)} 0\n')
        for vert in vertices:
            file.write(f'{" ".join(map(str, vert))}\n')
        for face in faces:
            file.write(f'3 {" ".join(map(str, face))}\n')


def save_skeleton(file_path, vertices, edges):
    np.savez(file_path, vertices=vertices, edges=edges)


def plot_skeleton_with_trimesh(vertices, edges, title="Skeleton"):
    """
    Отображение скелета с использованием trimesh.
    """
    lines = [[vertices[edge[0]], vertices[edge[1]]] for edge in edges]
    skeleton_lines = tm.load_path(lines)
    skeleton_lines.show()


def process_folder(folder_path):
    # Загружаем основной mesh
    vertices_main, faces_main = load_off(os.path.join(folder_path, 'surface_mesh.off'))

    # Ищем все файлы, начинающиеся на "spine_"
    spine_files = [f for f in os.listdir(folder_path) if f.startswith('spine_') and f.endswith('.off')]
    vertices_spines = []

    for i, file in enumerate(spine_files):
        file_path = os.path.join(folder_path, file)
        verts_spine, faces_spine = load_off(file_path)
        vertices_spines.append(verts_spine)

    # Удаляем шипики с основной поверхности
    vertices_clean, faces_clean = remove_spines_from_main(vertices_main, faces_main, vertices_spines)

    # Используем pymeshfix для заполнения дыр
    vertices_repaired, faces_repaired = fill_holes_with_pymeshfix(vertices_clean, faces_clean)

    save_off(os.path.join(folder_path, 'clean_surface_mesh_with_patches.off'), vertices_repaired, faces_repaired)

    # Получаем имя папки
    folder_name = os.path.basename(folder_path)

    # Формируем имя skeleton файла с именем папки
    skeleton_file = f'skeleton_data_{folder_name}.npz'

    mesh = tm.Trimesh(vertices=vertices_repaired, faces=faces_repaired)

    fixed = sk.pre.fix_mesh(mesh, remove_disconnected=5, inplace=False)
    skel = sk.skeletonize.by_wavefront(fixed, waves=1, step_size=1)

    print("Vertices:\n", skel.vertices)
    print("Edges:\n", skel.edges)

    save_skeleton(skeleton_file, skel.vertices, skel.edges)
    plot_skeleton_with_trimesh(skel.vertices, skel.edges)


if __name__ == "__main__":
    # folder = 'orig'  # имя папки
    folder = 'ex'  # имя папки
    process_folder(folder)

