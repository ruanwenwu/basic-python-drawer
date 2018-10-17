# _*_ coding:utf-8 _*_

import requests
import chardet
import time
from bs4 import BeautifulSoup

class HtmlDownloader(object):
    def download(self,url):
        #kw = {'wd':'python'}
        headers = {
            'User-Agent':'User-Agent: Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)',
            #'upgrade-insecure-requests':'1',
            #'pragma':'no-cache',
            #'cookie':'_ga=GA1.2.885382235.1536301205; _gid=GA1.2.1466038820.1538177047',
            #'cache-control':'no-cache',
            #'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            #'accept-encoding':'gzip, deflate, br',
            #'accept-language':'zh-CN,zh;q=0.9',
            #'referer':'https://www.piaohua.com/'
        }

        # params 接收一个字典或者字符串的查询参数，字典类型自动转换为url编码，不需要urlencode()
        proxies = {
          #"http": "61.227.15.21:8088",
        }
        requests.DEFAULT_RETRIES = 5
        s = requests.session()
        s.keep_alive = False
        #time.sleep(5)
        try:
            response = requests.get(url,proxies=proxies,headers = headers,timeout=2)
            if response.status_code != 200 :
                print response.status_code
                return False
            else:
                s = response.content
                #print s
                return s
        except:
            print 'download error'
            return False
    

if __name__ == "__main__":
    a = HtmlDownloader()
    a.download("https://www.piaohua.com/html/xiju/2018/0927/41655.html")

