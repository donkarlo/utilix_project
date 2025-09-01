class Value:
    def __init__(self, raw_value:str):
        yaml = Yaml()
        if not yaml.validate(raw_value):
            raise ValueError(f"{raw_value} is not a valid Yaml string")
        self._raw_value = raw_value