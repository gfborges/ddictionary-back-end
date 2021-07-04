class Domain:
    def __init__(self, **domain):
        self.name = domain.get("name")
        self.password = domain.get("password").encode()
        self.id = domain.get("_id")

    def __dict__(self):
        return {
            "name": self.name,
            "id": str(self.id),
        }

    def to_json(self):
        return self.__dict__()
