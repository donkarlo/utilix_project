import pickle


class ModulePathRemappingUnpickler(pickle.Unpickler):
    def find_class(self, module, name):
        if module == "sensorx.type.lidar.observation.observation" and name == "Observation":
            module = "sensorx.kind.lidar.observation.observation"
        return super().find_class(module, name)


def load_with_remap(file_object):
    return ModulePathRemappingUnpickler(file_object).load()


with open(
        "/home/donkarlo/Dropbox/phd/data/experiements/oldest/robots/uav1/mind/memory/long_term/explicit/episodic/normal/lidar_scan_ranges_sliced_from_1_to_300000/lidar_scan_ranges_sliced_from_1_to_300000.pkl",
        "rb") as file_handle:
    ram = load_with_remap(file_handle)

with open(
        "/home/donkarlo/Dropbox/phd/data/experiements/oldest/robots/uav1/mind/memory/long_term/explicit/episodic/normal/lidar_scan_ranges_sliced_from_1_to_300000/new_lidar_scan_ranges_sliced_from_1_to_300000.pkl",
        "wb") as file_handle:
    pickle.dump(ram, file_handle, protocol=pickle.HIGHEST_PROTOCOL)