# coding:utf-8
import url_manager
import html_downloader
import html_parser
import html_outputer
import time
import sys

class SpiderMain(object):
    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()
        
    def craw(self, root_url):
        while True:

            new_url_res = self.urls.get_new_url()
            if not new_url_res:
                break
            new_url = new_url_res[1]
            if not new_url:
                print 'no more links to craw!!!'
                break
            try:
                print 'craw:  %s'  % (new_url)
                html_cont = self.downloader.download(new_url)
                if not html_cont:
                    print "fail"+new_url
                    #下载失败，跳过这个url
                    self.urls.markFailUrl(new_url)
                    continue
                urltype   = new_url_res[3]
                #print urltype
                new_urls,new_data = self.parser.parse(new_url,urltype,html_cont)
                self.urls.add_new_urls(new_urls)    #添加url
                if new_data:
                    #print new_data
                    new_data['smallpic'] = new_url_res[4]
                    self.outputer.addMovie(new_data)
                #操作完毕更新连接状态
                self.urls.updateUrl(new_url)
                #time.sleep(1)
            except:
                self.urls.markFailUrl(new_url)
                continue
                #print 'failed'

                #self.outputer.output_html()
if __name__ == "__main__":
    root_url = "https://www.piaohua.com"
    reload(sys)
    sys.setdefaultencoding('utf8')
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)