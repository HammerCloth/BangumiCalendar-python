import requests
from bs4 import BeautifulSoup

from iCal import iCal
from week import week

url = "http://bangumi.tv/calendar"

headers = {
    "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36",
    "Cookie": "chii_sid=H1LI6j; chii_sec_id=IzYtsAZndkyJf3CWdSC7%2BlxuGw%2FFeur7spG9SEg; chii_theme=dark; __utma=1.1194694437.1669987956.1669987956.1669987956.1; __utmc=1; __utmz=1.1669987956.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmt=1; __utmb=1.7.10.1669987956"
}
# todo 欠缺封装
# todo 超时重试机制
page = requests.get(url=url, headers=headers, )
page.encoding = 'utf-8'
content = page.content
soup = BeautifulSoup(content, "lxml")

calendar = {
    "mon": soup.select_one("dd.Mon"),
    "tue": soup.select_one("dd.Tue"),
    "wed": soup.select_one("dd.Wed"),
    "thu": soup.select_one("dd.Thu"),
    "fri": soup.select_one("dd.Fri"),
    "sat": soup.select_one("dd.Sat"),
}
week = week()
weekday = {
    "mon": week.Monday,
    "tue": week.Tuesday,
    "wed": week.Wednesday,
    "thu": week.Thursday,
    "fri": week.Friday,
    "sat": week.Saturday,
}

for key in calendar.keys():
    temp = calendar.get(key)
    temp = temp.select("li")
    list = []
    for i in temp:
        list.append(i.select_one("a").get_text() + "/" + i.select_one("em").get_text())
    calendar[key] = list

cal = iCal()

for key in calendar.keys():
    list = calendar[key]
    for i in list:
        cal.setEvent(i, weekday[key])

cal.display().write()
