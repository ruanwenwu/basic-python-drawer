# coding:utf-8
import urlparse
from bs4 import BeautifulSoup
import re
import html_downloader
import mysql_link
import html_outputer
import strtest
import types
class HtmlParser(object):
    def __init__(self):
        self.mysqlLink = mysql_link.MysqlLink()
        self.outputer  = html_outputer.HtmlOutputer()

    def parse(self ,page_url,urltype, html_cont):
        #print html_cont
        if page_url is None or html_cont is None:
            return

        soup = BeautifulSoup(html_cont,"html.parser")
        new_urls = self._get_new_urls(page_url, soup)
        #print new_urls
        if urltype == "detail":
            new_data = self._get_new_data_simple(page_url, soup)
        else:
            new_data = False
        return new_urls,new_data
    
    def _get_new_urls(self,page_url,soup):
        new_urls = []
        links = soup.find_all('a',href=re.compile(r"/html/[a-z]+\/index\.html"))    #目录
        for link in links:
            new_url = link['href']
            new_full_url = urlparse.urljoin(page_url,new_url)
            if re.search(r"lianxuju|zongyijiemu",new_full_url) is not None:
                continue
            new_urls.append({"url":new_full_url,"type":"category"})
        detailLinks = soup.find_all('a', href=re.compile(r"/html/[a-z]+\/\d{4}\/\d{4}\/\d+\.html"))  # 详情
        for dlink in detailLinks:
            #print dlink
            childImgs = dlink.find_all("img")
            childImg = ''
            if len(childImgs)>0:
                childImg = childImgs[0]['src']
            new_durl = dlink['href']
            new_dfull_url = urlparse.urljoin(page_url, new_durl)
            if re.search(r"lianxuju|zongyijiemu",new_dfull_url) is not None:
                continue
            new_urls.append({"url": new_dfull_url, "type": "detail","orismall":childImg})
        pagelinks = soup.find_all('a',href=re.compile(r"list_\d+\.html"))
        for plink in pagelinks:
            new_purl = plink['href']
            new_pfull_url = urlparse.urljoin(page_url, new_purl)
            if re.search(r"lianxuju|zongyijiemu", new_pfull_url) is not None:
                continue
            new_urls.append({"url": new_pfull_url, "type": "category"})
        return new_urls
    
    def _get_new_data(self,page_url,soup):
        res_data = {}
        typeses = re.search(r'html\/([a-z]+)', page_url)    #类型匹配
        if typeses is not None:
            entype = typeses.group(1)
        else:
            entype = ""
        res_data['url'] = page_url
        title_node = soup.find('div', class_="m-text1").find("h1")  #找到标题
        title =  title_node.get_text()
        ftpurls = soup.select('.bot a')
        ftpurl = ''
        if len(ftpurls) > 0:
            for x in ftpurls:
                if x['href'] == "/":
                    continue
                ftpurl += x['href']+"|"
        pubdateNode = soup.select(".info > span:nth-of-type(2)")[0].get_text()  #找到时间
        pubdate =  pubdateNode[-10:]
        videoimgArr = soup.select(".txt > img") #下载图片
        videoimg = None
        sourceImg = '';
        if len(videoimgArr) > 0:
            videoimg = videoimgArr[0]['src']
        if videoimg is not None:
            if re.match("http",videoimg) is None:
                videoimg = urlparse.urljoin(page_url,videoimg)
                print videoimg
            print videoimg
            sourceImg = videoimg
            picInfo = self.outputer.savePic(videoimg)
            res_data['pic'] = picInfo['big']
            res_data['smallpic'] = picInfo['little']
        #获取影片信息
        divs = soup.select(".txt div")
        contentstr = ""
        for subd in divs:
            contentstr += subd.get_text()
        otherData = strtest.parseContent(contentstr)
        otherData['url'] = page_url
        otherData['title'] = title
        otherData['pubdate'] = pubdate
        otherData['downloadurl'] = ftpurl
        if res_data.has_key("pic"):
            otherData['pic'] = res_data['pic']
        else:
            otherData['pic'] = ""
        if res_data.has_key("smallpic"):
            otherData['smallpic'] = res_data['smallpic']
        else:
            otherData['smallpic'] = ''
        otherData['etype'] = entype
        otherData['sourcepic'] = sourceImg
        #print otherData
        keys = ['name','translame','age','country','ctype','language','officalsite','pubdated','score','idburl','duration','director','scriptor','actor','brief','pic','smallpic','pubdate','downloadurl']
        #遍历键，没有的键，设置为空
        for x in keys:
            if x not in otherData.keys():
                print x
                otherData[x] = ''
        for j in otherData.keys():
            if isinstance(otherData[j], unicode):
                otherData[j] = otherData[j].encode("utf-8")
            otherData[j] =  re.sub(r"'","\\\'",otherData[j])
            otherData[j] = re.sub(r"\"", "\\\"", otherData[j])
            otherData[j] = re.sub(r"\(","\\\(",otherData[j])
            otherData[j] = re.sub(r"\)", "\\\)", otherData[j])
        print otherData
        return otherData

    def _get_new_data_simple(self,page_url,soup):
        try:
            otherData={}
            title_node = soup.find("h1")  # 找到标题
            title = title_node.get_text()
            title = re.sub(r"(BD|HD).*$","",title)
            typeses = re.search(r'html\/([a-z]+)', page_url)  # 类型匹配
            if typeses is not None:
                entype = typeses.group(1)
            else:
                entype = ""
            ftpurls = soup.select('a[href^="ftp"]')
            ftpurl = ''
            if len(ftpurls) > 0:
                ftpurl = ftpurls[0]['href']
            pubdateNode = soup.select(".info > span:nth-of-type(2)")[0].get_text()  # 找到时间
            pubdate = pubdateNode[-10:]
            videoimgArr = soup.select(".txt > img")  # 下载图片
            sourceImg = '';
            if len(videoimgArr) > 0:
                sourceImg = videoimgArr[0]['src']
            divs = soup.select(".txt")
            contentstr = ""
            for subd in divs:
                contentstr += str(subd)
            otherData['url'] = page_url
            otherData['title'] = title
            otherData['etype'] = entype
            otherData['pubdate'] = pubdate
            otherData['downloadurl'] = ftpurl
            otherData['sourcepic'] = sourceImg
            otherData['oricontent'] = contentstr
            #print contentstr
            for j in otherData.keys():
                if isinstance(otherData[j], unicode):
                    otherData[j] = otherData[j].encode("utf-8")
                otherData[j] = re.sub(r"\\","",otherData[j])
                otherData[j] =  re.sub(r"'","\\'",otherData[j])
                otherData[j] = re.sub(r"\"", "\\\"", otherData[j])
                otherData[j] = re.sub(r"\(","\\\(",otherData[j])
                otherData[j] = re.sub(r"\)", "\\\)", otherData[j])
            #print otherData
            return otherData
        except:
            return None
if __name__ == "__main__":
    parObj = HtmlParser()
    downloader = html_downloader.HtmlDownloader()
    s = downloader.download("https://www.piaohua.com/html/kongbu/2016/1121/31536.html")
    parObj.parse("https://www.piaohua.com/html/kongbu/2016/1121/31536.html","detail",s)
    
    



