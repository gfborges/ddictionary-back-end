class Logger:
    def __init__(self, domain: str, cat: str, **kwargs) -> None:
        self.domain = domain
        self.cat = cat
        self.msgs = []
        for [k, v] in kwargs.items():
            self.__setattr__(k, v)

    def to_json(self):
        return vars(self) | {"_id": str(self._id)}

    def log(self, msg: dict):
        if msg not in self.msgs:
            self.msgs.insert(0, msg)
            self.msgs = self.msgs[:10]
