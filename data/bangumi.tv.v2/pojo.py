class project:
    def __init__(self, name="", name_cn="", summary="", id=0):
        self.name = name
        self.name_cn = name_cn
        self.summary = summary
        self.id = id

    def __str__(self) -> str:
        return self.name + "\t" + self.name_cn + "\t" + self.summary + "\t" + str(self.id)


class ep:
    def __init__(self, airdate="", name="", name_cn="", ep=""):
        self.ep = ep
        self.name_cn = name_cn
        self.name = name
        self.airdate = airdate
