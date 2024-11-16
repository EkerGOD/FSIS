class Field(dict):
    """帮助识别属性"""

class BaseItem:
    def __init__(self):
        for n in dir(self):
            v = getattr(self, n)
            if isinstance(v, Field):
                self.__dict__[n] = None

    def keys(self):
        return self.__dict__.keys()

    def items(self):
        return self.__dict__.items()

    def __getitem__(self, key):
        if key in self.__dict__:
            return self.__dict__[key]
        raise KeyError(f"{key} does not exist.")

    def __setitem__(self, key, value):
        if hasattr(self, key):  # 确保只能设置已定义的类属性
            self.__dict__[key] = value
        else:
            raise KeyError(f"{key} is not a valid field.")

    def __repr__(self):
        return f"{self.__class__.__name__}({self.__dict__})"