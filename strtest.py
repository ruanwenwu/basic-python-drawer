# -*- coding:utf-8 -*-
import re

def parseContent(str):
    if str is None:
        return False
    print type(str)
    str = str.encode("utf-8")
    print type(str)
    dataArr = str.split('◎')

    res = {}
    for dl in dataArr:
        #res = {}
        dl = re.sub(r"　　","",dl)
        startpointRes = re.search("\s|　",dl)#.span()[0]
        if startpointRes is None:
            continue
        else:
            startpoint = startpointRes.span()[0]
        value = dl[startpoint:]
        keyv  = dl[:startpoint]
        if(not keyv):
            continue
        keyv = re.sub(r"\s|　|\t| ","",keyv)
        value= re.sub(r"\t|\r|\n|　|","",value)
        print keyv+'-'+value
        mtype = getType(keyv)
        #print type(value)
        res[mtype] =value
    #print res
    return res

def getType(name):
    if name == "片名":
        return "name"
    elif name == "译名" or name=="又名":
        return "translame"
    elif name == "国家" or name=="产地":
        return "country"
    elif name== "电影类型" or name=="类别" or name=="类型":
        return "ctype" #中文类型
    elif name == "语言":
        return "language"
    elif name=="官方网站":
        return "officalsite"
    elif name=="上映日期":
        return "pubdated"
    elif name=="iMDB评分" or name == "豆瓣评分":
        return "score"
    elif name=="iMDB链接" or name=="豆瓣链接":
        return "idburl"
    elif name=="ＩＭＤＢ":
        return "imdburl"
    elif name=="片长" or name=="时长":
        return "duration"
    elif name=="导演":
        return "director"
    elif name == "编剧":
        return "scriptor"
    elif name == "演员" or name == "主演":
        return "actor"
    elif name == "简介":
        return "brief"
    elif name== "年代":
        return "age"
    elif name=="获奖情况":
        return "reward"
    #print keyv+"-"+value

def strtest():
    str = '''
    ◎片　　名　江湖儿女 江湖儿女
◎又　　名　金钱与爱情 / 灰烬是最洁白的 / Ash is Purest White / Money & Love / Les Eternels
◎年　　代　2018
◎国　　家　中国大陆 / 法国 / 日本
◎类　　型　爱情 犯罪 
◎语　　言　汉语普通话
◎上映日期　2018-09-21(中国大陆) / 2018-05-11(戛纳电影节)
◎豆瓣评分　7.8 分 / （总分10分）
◎豆瓣链接　http://movie.douban.com/subject/26972258/
◎ＩＭＤＢ　http://www.imdb.com/title/tt7298400
◎时　　长　141分钟 / 137分钟(中国大陆)
◎导　　演　贾樟柯
◎主　　演　赵涛
　　　　　  廖凡
　　　　　  徐峥
　　　　　  梁嘉艳
　　　　　  刁亦男
　　　　　  张一白
　　　　　  丁嘉丽
　　　　　  张译
　　　　　  董子健
　　　　　  李宣
　　　　　  查娜
　　　　　  冯家妹
　　　　　  冯小刚
 
◎获奖情况　第71届戛纳电影节 主竞赛单元 金棕榈奖(提名) 贾樟柯
 
◎简　　介　
故事起始于2001年的山西大同，模特巧巧（赵涛 饰）与出租车公司老板斌哥（廖凡 饰）是一对恋人，斌哥每天在外面呼朋唤友，巧巧希望能够尽快进入婚姻。一次，斌哥在街头遭到竞争对手的袭击，巧巧为了保护斌哥街头开枪，被判刑五年。巧巧出狱以后，开始寻找斌哥以便重新开始，然而事情却发生了意想不到的变化。
    ''';
    dataArr = str.split('◎')
    if len(dataArr) > 0:
        for dl in dataArr:
            dl = re.sub(r"\t|\s\n")
