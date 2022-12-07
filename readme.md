# 基于GitHub Action建立bgm番剧Mac日历订阅服务

​	通过bgm开放的api，获取用户所有在看的番剧id以及相关章节信息，生成ics文件，然后通过github中的文件链接，导入到mac自带的日历中，实现日历订阅，不需要专门的服务器来实现。

## 项目目录

```shell
.
├── .github  
│   └── workflows
│       └── python-app.yml  // github action配置文件
├── BEGIN:VCALENDAR.ics     // ics文件初始化模版
├── target.ics              // 生成的目标ics文件
├── requirements.txt        // github action python依赖配置文件
├── iCal.py                 // ics文件生成脚本类
├── main.py                 // main
├── pojo.py                 // python 一些用于存储信息的类
├── reptile.py              // bgm api调用，并解析响应
├── readme.md    
└── util.py                 // 工具类 
```

## 项目配置流程

#### 1. fork项目到你的仓库中

#### 2. 在GitHub setting 中配置sercet

```yaml
name ： USERID
value ： 你的bgm用户id
```

#### 3. 在系统日历中订阅如下链接

> 你也可以直接下载下来target.ics文件拖到日历中，但是这样就无法自动更新了

```python
https://raw.githubusercontent.com/{你的github用户名}/BangumiCalendar-python/main/target.ics
```

