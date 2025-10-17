from utilix.data.type.dic.decorator.decorator import Decorator


class Objected(Decorator):

    def __getattr__(self, item: str):
        raw_dict = self.get_raw_dict()
        # handle get_<key>
        if item.startswith("get_"):
            key = item[4:]
            if key in raw_dict:
                value = raw_dict[key]
                if isinstance(value, dict):
                    return lambda: Objected(value)
                return lambda: value

        # handle set_<key>
        if item.startswith("set_"):
            key = item[4:]

            def setter(new_value):
                # If we're setting a dict, keep it as dict (not ObjectedObjected)
                data = new_value

            return setter

        raise AttributeError(f"{item} not found")

