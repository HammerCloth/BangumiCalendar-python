class bangumi:
    def __init__(self, titleCN, titleJP, type="", tags="", staff="", casts="", broadcast="", broadcaseRemark=""):
        self.broadcaseRemark = broadcaseRemark
        self.broadcast = broadcast
        self.casts = casts
        self.staff = staff
        self.tags = tags
        self.titleCN = titleCN
        self.titleJP = titleJP
        self.type = type

    def __str__(self) -> str:
        return "titleCN: " + self.titleCN + "\n" + "titleJP: " + self.titleJP + "\n" + "type: " + self.type + "\n" + "tags: " + self.tags + "\n" + "staff: " + self.staff + "\n" + "casts: " + self.casts + "\n" + "broadcast: " + self.broadcast + "\n" + "broadcaseRemark:" + self.broadcaseRemark
