from utilityx.data.storage.decorator import MultiDocYamlFile


class Factory:
    @staticmethod
    def get_multi_doc_yaml_file(file_path:str) -> MultiDocYamlFile:
        file = File(OsPath(file_path))
        source = Source(SupportingStorage.FILE, SupportingFormat.YAML)
        return MultiDocYamlFile(United(Partial(source)), file)

