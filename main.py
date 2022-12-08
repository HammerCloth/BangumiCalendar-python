import util
from iCal import iCal
from reptile import data

'''
step 1 通过用户名获取订阅的番组id
step 2 通过番组id获取章节信息
step 3 将信息进行整合导出到ics
'''

if __name__ == '__main__':
    userid = "746322"
    # userid = os.environ["USERID"]
    data = data(userid)
    # step 1 通过用户名获取订阅的番组id
    data.getsubjects()
    # step 2 通过番组id获取章节信息
    data.geteps()
    # 将信息进行整合导出到ics
    icl = iCal()
    for key in data.subjects:
        for i in data.epdict[key.id]:
            # 判定日历格式是否正确
            if len(i.airdate) == 10:
                icl.setEvent(summary=util.genSummary(key.name, key.name_cn, i.ep),
                             time=util.genDate(i.airdate),
                             uuid=util.genUUID(key.id, i.ep, userid),
                             descripion=util.genDec(key.summary, i.name_cn))

    icl.write()
