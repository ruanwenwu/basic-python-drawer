# -*- coding:utf-8 -*-
from __future__ import division
import cv2
import os


def read_img(source_imgpath):
    img = cv2.imread(source_imgpath, 1)
    return img


'''缩放'''
def crop_img(img,imgurl, new_x, new_y):
    print new_x,new_y
    res = cv2.resize(img, (new_x, new_y), interpolation=cv2.INTER_AREA) #见下
    #解析目录与
    filename,fileext = os.path.splitext(imgurl)
    furl = filename+ str(new_x) + '_' + str(new_y) +'.jpg'
    cv2.imwrite(furl, res)
    return furl


def dengbi(img,width,height):
    imgInfo = read_img(img)
    if imgInfo is None:
        return ''
    oheight, owidth = imgInfo.shape[0:2]
    if(width and not height):
        width = width
        height = int((width/owidth)*oheight)
    else:
        print 1

    litleUrl = crop_img(imgInfo,img,width,height)
    return litleUrl



if __name__ == '__main__':
    #img = read_img("/data/piaohua/1/a1f35a9477dd4b5c801192649918d0a2.jpg")
    dengbi("/data/piaohua/1/a1f35a9477dd4b5c801192649918d0a2.jpg",201,0)
    #print(img.shape)
    #crop_img(img, 64, 64)
    #width,height = img.shape[0:2]
    #print width,height