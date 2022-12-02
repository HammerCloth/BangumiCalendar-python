import requests
from bs4 import BeautifulSoup
import html5lib

from bangumi import bangumi


def getDoc(url):
    page = requests.get(url)
    content = page.content
    return content


def parse(contents):
    soup = BeautifulSoup(contents, 'html5lib')
    body = soup.select_one(".post-body")
    # items = body.select("div[style='float:left'],div[style='float:left']+div")
    items = body.select("div[style='float:left']+div")
    sequenceSize = 10
    list = []
    for div in items:
        titleCN = div.select_one(genSequence("p.title_cn_r", sequenceSize))
        titleCN = titleCN.get_text() if titleCN else "not anything"
        titleJP = div.select_one(genSequence("p.title_jp_r", sequenceSize))
        titleJP = titleJP.get_text() if titleJP else "not anything"
        type = div.select_one(genSequence("td.type_a_r", sequenceSize) + "," + genSequence("td.type_b_r", sequenceSize))
        type = type.getText() if type else "not anything"
        tags = div.select_one(genSequence("td.type_tag_r", sequenceSize))
        tags = tags.getText() if tags else "not anything"
        staff = div.select_one(genSequence("td.staff_r", sequenceSize))
        staff = staff.getText() if staff.getText() else "not anything"
        casts = div.select_one(genSequence("td.cast_r", sequenceSize))
        casts = casts.getText() if casts.get_text() else "not anything"
        broadcast = div.select_one(genSequence("p.broadcast_r", sequenceSize))
        broadcast = broadcast.getText() if broadcast.getText() else "not anything"
        broadcaseRemark = div.select_one(genSequence("p.broadcast_ex_r", sequenceSize))
        broadcaseRemark = broadcaseRemark.getText() if broadcaseRemark.getText() else "not anything"

        item = bangumi(titleCN, titleJP, type, tags, staff, casts, broadcast, broadcaseRemark)
        list.append(item)
    return list


def genSequence(css, num):
    res = css
    for i in range(num):
        t = i + 1
        temp = css + str(t)
        res = res + "," + temp
    return res


if __name__ == '__main__':
    url = "https://yuc.wiki/202301"
    con = getDoc(url)
    for i in parse(con):
        print(i)
