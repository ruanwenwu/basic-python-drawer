#!/usr/bin/python
# -*- coding:utf-8 -*-
import pymysql
import time
import chardet
class MysqlLink(object):
    def __init__(self):
        self.link = self.createLink()
        #print "我们"
        #name="我们"
        #print type(name)
    def createLink(self):
        conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='', db='movie')
        return conn
    def getAllMovie(self):
        cursor = self.link.cursor()
        cursor.execute("select * from movies")
        a = cursor.fetchall()
        cursor.close()
    def getAllMovied(self):
        cursor = self.link.cursor()
        cursor.execute("set names utf8")
        cursor.execute("select * from movies")
        a = cursor.fetchall()
        #print a
        cursor.close()

    #检查url是否满足条件
    def checkUrlStatus(self,url):
        cursor=self.link.cursor()
        cursor.execute("set names utf8")
        sql = "select * from urls where url='%s'" % (url);
        cursor.execute(sql)
        a = cursor.fetchall()
        cursor.close()
        if len(a)>0:
            return False
        return True

    #添加url
    def addUrl(self,url,type,smallpic):
        cursor=self.link.cursor()
        cursor.execute("set names utf8")
        sql = "insert into urls (`url`,`type`,`smallpic`) values ('%s','%s','%s')" % (url,type,smallpic);
        #print sql
        try:
            cursor.execute(sql)
            self.link.commit()
        except:
            self.link.rollback()
        cursor.close()

    #获取url
    def getOneUrl(self):
        cursor=self.link.cursor()
        cursor.execute("set names utf8")
        sql = "select * from urls where status = 0 and downloadfail =0 limit 1"
        try:
             cursor.execute(sql)
             a = cursor.fetchone()
             return a
        except:
            return False

    def updateDirindex(self):
        cursor = self.link.cursor()
        cursor.execute("set names utf8")
        sql = "update `dir_index` set `id`=`id`+1"
        try:
            cursor.execute(sql)
        except:
            return False

    def getDirindex(self):
        cursor = self.link.cursor()
        cursor.execute("set names utf8")
        sql = "select id from dir_index limit 1"
        try:
            cursor.execute(sql)
            a = cursor.fetchone()
            return a[0]
        except:
            return False

    def checkHasNewurl(self):
        cursor = self.link.cursor()
        cursor.execute("set names utf-8")
        sql = "select * from urls where ";

    def addMovies(self,data):
        #print data
        cursor = self.link.cursor()
        cursor.execute("set names utf8")
        nowtime = time.strftime("%Y-%m-%d %X",time.localtime())
        #sql = "insert into `movie`.`movies`( `name`, `transname`, `age`, `country`, `type`, `language`, `website`, `dabue`, `dbscore`, `dburl`, `duration`, `director`, `playwriter`, `actor`, `brief`, `pic`, `smallpic`, `pubdate`, `mtime`, `ctime`, `downloadurl`) values ('"+data['name']+"','"+data['translame']+"',"+data['country']+"','"+data['ctype']+"','"+data['language']+"','"+data['officalsite']+"','"+data['pubdated']+"','"+data['score']+"','"+data['idburl']+"','"+data['duration']+"','"+data['director']+"','"+data['scriptor']+"','"+data['actor']+"','"+data['brief']+"','"+data['pic']+"','"+data['smallpic']+"','"+data['pubdate']+"','"+nowtime+"','"+nowtime+"','"+data['downloadurl']+"')"#,str(data['age']),data['country'],data['ctype'],data['language'],data['officalsite'],data['pubdated'],data['score'],data['idburl'],data['duration'],data['director'],data['scriptor'],data['actor'],data['brief'],data['pic'],data['smallpic'],data['pubdate'],nowtime,nowtime,data['downloadurl'])"
        sql = "insert into `movies` (`name`,`transname`,`age`,`country`,`type`,`language`,`website`, `dabue`,`dbscore`, `dburl`, `duration`, `director`,`playwriter`, `actor`,`brief`, `pic`, `smallpic`, `pubdate`, `mtime`, `ctime`,`downloadurl`,`etype`,`sourcepic`) values ('"+data['name']+"','"+data['translame']+"','"+data['age']+"','"+data['country']+"','"+data['ctype']+"','"+data['language']+"','"+data['officalsite']+"','"+data['pubdated']+"','"+data['score']+"','"+data['idburl']+"','"+data['duration']+"','"+data['director']+"','"+data['scriptor']+"','"+data['actor']+"','"+data['brief']+"','"+data['pic']+"','"+data['smallpic']+"','"+data['pubdate']+"','"+nowtime+"','"+nowtime+"','"+data['downloadurl']+"','"+data['etype']+"','"+data['sourcepic']+"')"
        #sql="sdfdf"
        #print sql
        try:
            cursor.execute(sql)
            self.link.commit()
            cursor.close()
        except:
            return False

    def addMovie(self,data):
        #print data
        cursor = self.link.cursor()
        cursor.execute("set names utf8")
        nowtime = time.strftime("%Y-%m-%d %X",time.localtime())
        #sql = "insert into `movie`.`movies`( `name`, `transname`, `age`, `country`, `type`, `language`, `website`, `dabue`, `dbscore`, `dburl`, `duration`, `director`, `playwriter`, `actor`, `brief`, `pic`, `smallpic`, `pubdate`, `mtime`, `ctime`, `downloadurl`) values ('"+data['name']+"','"+data['translame']+"',"+data['country']+"','"+data['ctype']+"','"+data['language']+"','"+data['officalsite']+"','"+data['pubdated']+"','"+data['score']+"','"+data['idburl']+"','"+data['duration']+"','"+data['director']+"','"+data['scriptor']+"','"+data['actor']+"','"+data['brief']+"','"+data['pic']+"','"+data['smallpic']+"','"+data['pubdate']+"','"+nowtime+"','"+nowtime+"','"+data['downloadurl']+"')"#,str(data['age']),data['country'],data['ctype'],data['language'],data['officalsite'],data['pubdated'],data['score'],data['idburl'],data['duration'],data['director'],data['scriptor'],data['actor'],data['brief'],data['pic'],data['smallpic'],data['pubdate'],nowtime,nowtime,data['downloadurl'])"
        sql = "insert into `movies` (`name`, `pubdate`, `pic`, `smallpic`,  `mtime`, `ctime`,`downloadurl`,`etype`,`pagesource`,`oricontent`) values ('"+data['title']+"','"+data['pubdate']+"','"+data['sourcepic']+"','"+data['smallpic']+"','"+nowtime+"','"+nowtime+"','"+data['downloadurl']+"','"+data['etype']+"','"+data['url']+"','"+data['oricontent']+"')"
        #sql="sdfdf"
        #print sql
        try:
            cursor.execute(sql)
            self.link.commit()
            cursor.close()
        except:
            print sql
            #exit()
    def updateUrl(self,url):
        cursor = self.link.cursor()
        cursor.execute("set names utf8")
        nowtime = time.strftime("%Y-%m-%d %X", time.localtime())
        sql = "update urls set status = 1 where url = '%s'" % (url)
        print sql
        try:
            cursor.execute(sql)
            self.link.commit()
        except:
            print sql
    def markFail(self,url):
        cursor = self.link.cursor()
        cursor.execute("set names utf8")
        nowtime = time.strftime("%Y-%m-%d %X", time.localtime())
        sql = "update urls set status = 1,downloadfail=1 where url = '%s'" % (url)
        # print sql
        try:
            cursor.execute(sql)
            self.link.commit()
        except:
            print sql
if __name__ == "__main__":
    db = MysqlLink()
    #db.getAllMovie()
    #db.getAllMovied()
    #a = db.checkUrlStatus("https://www.piaohua.com")
    #db.addUrl("http://ruanwenwu.cn",2)
    a = db.getOneUrl()
    print a