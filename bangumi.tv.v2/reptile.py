import requests

from pojo import project, ep


class data:
    def __init__(self, userid) -> None:
        self.userid = userid
        self.preUrl = "Https://api.bgm.tv"
        self.epsUrl = self.preUrl + "/v0/episodes"
        self.projectUrl = self.preUrl + "/v0/users/" + userid + "/collections"
        self.headers = {
            "User-Agent": "HammerCloth/BangumiCalendar-python(https://github.com/HammerCloth/BangumiCalendar-python)",
            "Cookie": "chii_sid=H1LI6j; chii_sec_id=IzYtsAZndkyJf3CWdSC7%2BlxuGw%2FFeur7spG9SEg; chii_theme=dark; __utma=1.1194694437.1669987956.1669987956.1669987956.1; __utmc=1; __utmz=1.1669987956.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmt=1; __utmb=1.7.10.1669987956"
        }
        self.subjects = []
        self.epdict = {}

    def getsubjects(self):
        params = {
            "type": 3  # 表示在看
        }
        page = requests.get(url=self.projectUrl, headers=self.headers, params=params)
        projects = page.json()["data"]
        for i in projects:
            self.subjects.append(
                project(i["subject"]["name"], i["subject"]["name_cn"], i["subject"]["short_summary"], i["subject_id"]))

    def geteps(self):
        for i in self.subjects:
            temp = []
            params = {
                "subject_id": i.id
            }
            page = requests.get(url=self.epsUrl, headers=self.headers, params=params)
            eps = page.json()["data"]
            for j in eps:
                temp.append(ep(j["airdate"], j["name"], j["name_cn"], j["ep"]))
            self.epdict[i.id] = temp
