# coding:utf-8
import mysql_link
import hashlib
import os
import time
import Cvt
import html_downloader
class HtmlOutputer(object):
    def __init__(self):
        self.datas = []
        self.mysqlLink = mysql_link.MysqlLink()
        self.downloader = html_downloader.HtmlDownloader()

    def collect_data(self,data):
        if data is None:
            return
        self.datas.append(data)
        
    def output_html(self):
        fout = open('output.html' , 'w')
        fout.write('<html>')
        fout.write("<meta charset='utf-8'/>")
        fout.write('<body>')
        fout.write('<table border="1">')
        for data in self.datas:
            fout.write('<tr>')
            fout.write("<td>%s</td>" % data['url'])
            fout.write("<td>%s</td>" % data['title'].encode('utf-8'))
            fout.write("<td>%s</td>" % data['summary'].encode('utf-8'))
            fout.write('</tr>')
        fout.write("</table>")
        fout.write('</body>')
        fout.write('</html>')
        fout.close()

    def savePic(self,url):
            if url is None:
                return
            img = self.downloader.download(url)
            if not img:
                return {"big": url, "little": url}
            try:
                picIndex = self.mysqlLink.getDirindex()
                self.mysqlLink.updateDirindex()  # 更新index
                picInfo = os.path.splitext(url)
                picName = picInfo[0]
                picExt  = picInfo[1]
                ho = hashlib.md5(picName+str(int(time.time())))
                picname = ho.hexdigest()
                dir = "/data/piaohua/%s/" % (picIndex)
                if os.path.isdir(dir) != True:
                    os.makedirs(dir)

                file = dir + picname + picExt
                #print file
                with open(file,'wb') as f:
                    f.write(img)
                #b保存缩略图
                little = Cvt.dengbi(file,201,0)
                return {"big":file,"little":little}
            except:
                return {"big":url,little:url}
    def addMovie(self,data):
        self.mysqlLink.addMovie(data)


if __name__ == "__main__":
    print "我"
    #outer = HtmlOutputer()
    #outer.savePic("http://tu.totheglory.im:8182/files/154/kazenoiro.jpg")



