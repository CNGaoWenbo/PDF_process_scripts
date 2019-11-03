# -*- coding: utf-8 -*-
"""
Created on Sat Oct 12 22:59:02 2019

@author: asdqw
"""
#批量下载
import urllib.request
import os
root_url = 'http://weilab.nju.edu.cn/pub/'

def getFile(url):
    file_name = url.split('/')[-1]
    u = urllib.request.urlopen(url)#获取pdf下载的url
    f = open(file_name, 'wb')#打开pdf

    block_sz = 8192
    while True:
        buffer = u.read(block_sz)#存储url数据
        if not buffer:
            break

        f.write(buffer)#写入文件
    f.close()
    print ("Sucessful to download" + " " + file_name)


os.chdir(os.path.join(os.getcwd(), 'pdf_download'))#在当前目录创建文件夹pdf_download

for i in range(40):
    num = i+42
    url = root_url+str(num)+'.pdf'#匹配pdf下载url的格式http://weilab.nju.edu.cn/pub/21.pdf
    getFile(url)
#合并处理
import os
import PyPDF2
pdfFR = PyPDF2.PdfFileReader
pdfFM = PyPDF2.PdfFileMerger()
pdfFW = PyPDF2.PdfFileWriter()
os.chdir('E:\\资料、文档\\代码\\pdf_download')#切换到pdf文件夹
path = os.getcwd()


for i in range(40):
    num = i+42
    file_name = str(num)+'.pdf'
    file = PyPDF2.PdfFileReader(file_name)
    num_pages = pdfFR.getNumPages(file)

    for index in range(0,num_pages):#reader的addpage模块逐页获取
        page = pdfFR.getPage(file,index)
        pdfFW.addPage(page)
    page0 = pdfFR.getPage(file,0)#在文末追加首页,方便复制标题
    pdfFW.addPage(page0)
    pdfFW.addBlankPage()#加空白页

with open(path + "\\Merged_add.pdf", 'wb') as write_out_file:
    pdfFW.write(write_out_file)#写入文档
