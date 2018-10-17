#!/usr/bin/python
# -*- coding:utf-8 -*-
'''
Created on 2016年8月10日

@author: ruanwenwu
'''
import mysql_link
class UrlManager(object):
    def __init__(self):
        self.mysqlLink = mysql_link.MysqlLink()

    def add_new_url(self,url,type,smallpic):
        if url is None:
            return
        if self.mysqlLink.checkUrlStatus(url):
            self.mysqlLink.addUrl(url,type,smallpic)

    def add_new_urls(self,urls):
        if len(urls) == 0:
            return False
        for url in urls:
            smallpic = url.get("orismall","")
            self.add_new_url(url['url'],url['type'],smallpic)
    def get_new_url(self):
        newUrl =  self.mysqlLink.getOneUrl()
        return newUrl

    def updateUrl(self,url):
        self.mysqlLink.updateUrl(url)

    def markFailUrl(self,url):
        self.mysqlLink.markFail(url)

    

    
    



