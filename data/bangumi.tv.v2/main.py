from reptile import data

'''
step 1 通过用户名获取订阅的番组id
step 2 通过番组id获取章节信息
step 3 将信息进行整合导出到ics
'''

if __name__ == '__main__':
    userid = "746322"
    data = data(userid)
    # step 1 通过用户名获取订阅的番组id
    data.getsubjects()
    # step 2 通过番组id获取章节信息
    data.geteps()
