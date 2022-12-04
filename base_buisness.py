from utils import set_value

_EXCLUDE_KEY_ = ['tablename', 'columns', 'values']


class BaseTable:

    def __init__(self):
        self.columns = None
        self.values = None

    def creteField(self, frormat):
        self._colums(frormat)
        self._values()

    def _colums(self, frormat):
        result = list()
        for k in self.__dict__.keys():
            if k not in _EXCLUDE_KEY_:
                if k in frormat:
                    result.append(f'"{k}"')
                else:
                    result.append(k)
        self.columns = ",".join(result)

    def _values(self):
        result = list()
        for k, v in self.__dict__.items():
            if k not in _EXCLUDE_KEY_:
                result.append(f"{set_value(v)}")
        self.values = ",".join(result)
