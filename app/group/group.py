class Group:
    def __init__(self, slug: str, title: str = None, **kwargs) -> None:
        self.slug = slug
        self.title = title if title else slug
        for [k, v] in kwargs.items():
            self.__setattr__(k, v)

    def to_json(self):
        return {"slug": self.slug, "title": self.title}
