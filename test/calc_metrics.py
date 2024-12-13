from spine_metrics import SpineMetricDataset, MeshDataset
import numpy as np
from CGAL.CGAL_Polyhedron_3 import Polyhedron_3

# from CGAL.CGAL_Polyhedron_3 import Polyhedron_3
from typing import List, Tuple, Dict, Set, Iterable, Callable

from pathlib import Path


V_F = Tuple[np.ndarray, np.ndarray]
#
# dataset_path = "example_dendrite"
# metrics_path = f"{dataset_path}/metrics.csv"
#
# scale = (1, 1, 1)
#
# classification_save_path = "output/manual_classification.json"
#
# classes = ["Stubby", "Mushroom", "Thin", "Filopodia", "Outlier"]
#
#
# # from notebook_widgets import SpineMeshDataset
# # from spine_segmentation import apply_scale
class SpineMeshDataset:
    # spine name -> Polyhedron_3
    spine_meshes: MeshDataset
    # dendrite name -> Polyhedron_3
    dendrite_meshes: MeshDataset
    spine_to_dendrite: Dict[str, str]
    dendrite_to_spines: Dict[str, Set[str]]
    # spine name -> v f
    spine_v_f: Dict[str, V_F]
    # dendrite name -> v f
    dendrite_v_f: Dict[str, V_F]

    def __init__(self, spine_meshes: MeshDataset = None, dendrite_meshes: MeshDataset = None,
                 spine_to_dendrite: Dict[str, str] = None) -> None:
        if spine_meshes is None:
            spine_meshes = {}
        if dendrite_meshes is None:
            dendrite_meshes = {}
        if spine_to_dendrite is None:
            spine_to_dendrite = {}

        # set fields
        self.spine_meshes = spine_meshes
        self.dendrite_meshes = dendrite_meshes
        self.spine_to_dendrite = spine_to_dendrite

        # generate mapping of dendrites to their spines
        self.dendrite_to_spines = {name: set() for name in dendrite_meshes.keys()}
        for (spine_name, dendrite_name) in spine_to_dendrite.items():
            self.dendrite_to_spines[dendrite_name].add(spine_name)

        # calculate 'meshplot' mesh representations
        self._calculate_v_f()


    def load(self, folder_path: str = "output",
             spine_file_pattern: str = "**/spine_*.off") -> "SpineMeshDataset":
        spine_meshes = {}
        dendrite_meshes = {}
        spine_to_dendrite = {}
        path = Path(folder_path)
        spine_names = list(path.glob(spine_file_pattern))
        for spine_name in spine_names:
            spine_meshes[str(spine_name)] = Polyhedron_3(str(spine_name))
            dendrite_path = str(spine_name.parent) + "\\surface_mesh.off"
            if dendrite_path not in dendrite_meshes:
                dendrite_meshes[dendrite_path] = Polyhedron_3(dendrite_path)
            spine_to_dendrite[str(spine_name)] = dendrite_path
        self.__init__(spine_meshes, dendrite_meshes, spine_to_dendrite)
        return self
#
# # load meshes
# spine_dataset = SpineMeshDataset().load(dataset_path)
#
# # apply scale along z axis
# spine_dataset.apply_scale(scale)
#
# # load metrics
# spine_metrics = SpineMetricDataset().load(metrics_path)
# spine_metrics = spine_metrics.get_spines_subset(spine_dataset.spine_meshes.keys())
# spine_metrics = spine_metrics.get_metrics_subset(['OldChordDistribution'])

from spine_metrics import SpineMetricDataset
dataset_path = "example_dendrite"

spine_dataset = SpineMeshDataset().load(dataset_path)
print(spine_dataset)
#
# # chord method parameters
# num_of_chords = 30000
# num_of_bins = 100
#
# # calculate metrics
# metric_names = ["OldChordDistribution", "OpenAngle", "CVD", "AverageDistance",
#                 "LengthVolumeRatio", "LengthAreaRatio", "JunctionArea",
#                 "Length", "Area", "Volume", "ConvexHullVolume", "ConvexHullRatio"]
# metric_params = [{"num_of_chords": num_of_chords, "num_of_bins": num_of_bins},
#                  {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}]
# spine_metrics = SpineMetricDataset()
# spine_metrics.calculate_metrics(spine_dataset.spine_meshes, metric_names, metric_params)
# spine_metrics.save(f"{dataset_path}/metrics.csv")
#
# spine_metrics.get_metrics_subset(["OldChordDistribution"]).save_as_array(f"{dataset_path}/chords.csv")