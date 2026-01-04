import pickle
from typing import Dict, List, Tuple

from utilix.data.kind.pkl.module_path_remapping_unpickler import ModulePathRemappingUnpickler


class PickleFixer:
    def __init__(self, source_path: str, target_path: str):
        self._source_path = source_path
        self._target_path = target_path
        self._ordered_prefix_remap: List[Tuple[str, str]] = []
        self._qualified_class_remap: Dict[Tuple[str, str], str] = {}

    def add_prefix_remap(self, old_prefix: str, new_prefix: str) -> None:
        self._ordered_prefix_remap.append((old_prefix, new_prefix))

    def add_qualified_class_remap(self, old_module: str, class_name: str, new_module: str) -> None:
        self._qualified_class_remap[(old_module, class_name)] = new_module

    def run(self) -> None:
        with open(self._source_path, "rb") as file_handle:
            obj = ModulePathRemappingUnpickler(
                file_handle=file_handle,
                ordered_prefix_remap=self._ordered_prefix_remap,
                qualified_class_remap=self._qualified_class_remap,
            ).load()

        with open(self._target_path, "wb") as file_handle:
            pickle.dump(obj, file_handle, protocol=pickle.HIGHEST_PROTOCOL)


if __name__ == "__main__":
    source_pkl_path = "/home/donkarlo/Dropbox/phd/data/experiements/oldest/robots/uav1/mind/memory/explicit/long_term/episodic/experiences/normal/gaussianed_quaternion_kinematic_sliced_from_1_to_300000/gaussianed_quaternion_kinematic_sliced_from_1_to_300000.pkl"
    target_pkl_path = "/home/donkarlo/Dropbox/phd/data/experiements/oldest/robots/uav1/mind/memory/explicit/long_term/episodic/experiences/normal/gaussianed_quaternion_kinematic_sliced_from_1_to_300000/fixed_gaussianed_quaternion_kinematic_sliced_from_1_to_300000.pkl"

    fixer = PickleFixer(source_pkl_path, target_pkl_path)

    # Prefix remaps (more specific first)
    fixer.add_prefix_remap("robotix.mind.memory.trace", "robotix.trace")
    fixer.add_prefix_remap("robotix.mind.memory", "robotix.mind.cognition.process.kind.memory")

    # Qualified class remap(s): cover both possible module spellings that may appear
    # 1) After prefix remap (what you were trying)
    fixer.add_qualified_class_remap(
        old_module="robotix.trace.kind.gaussianed_quaternion_kinematic",
        class_name="GaussianedQuaternionKinematic",
        new_module="robotix.trace.kind.gaussianed_quaternion_kinematic.gaussianed_quaternion_kinematic",
    )

    # # 2) If the pickle actually stores the pre-remap module path
    # fixer.add_qualified_class_remap(
    #     old_module="robotix.mind.memory.trace.kind.lidar_scan_ranges",
    #     class_name="LidarScanRanges",
    #     new_module="robotix.trace.kind.lidar_scan_ranges.lidar_scan_ranges",
    # )
    #
    # # Optional: keep prefix too (harmless)
    # fixer.add_prefix_remap(
    #     "robotix.trace.kind.lidar_scan_ranges",
    #     "robotix.trace.kind.lidar_scan_ranges.lidar_scan_ranges",
    # )

    fixer.run()
