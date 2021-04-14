import re
import requests
import os

if __name__=="__main__":
    #创建一个文件夹储存图片
    if not os.path.exists('./tupian'):
        os.mkdir('./tupian')
    url='https://www.qiushibaike.com/imgrank/page/%d/'
    # pageNum = 1
    for pageNum in range(3):
        # 对应页码的url
        new_url = format(url % pageNum)

#     <div class="thumb">
#
# <a href="/article/124171066" target="_blank">
# <img src="//pic.qiushibaike.com/system/pictures/12417/124171066/medium/ZXOLLA2Q2X45ZCQ3.jpg" alt="糗事#124171066" class="illustration" width="100%" height="auto">
# </a>
# </div>

    headers = {
        'User-Agent': 'https://www.baidu.com/'
    }
    #对整张数据爬取
    page_text=requests.get(url=new_url,headers=headers).text
    #正则表达式
    ex='<div class="thumb">.*?<img src="(.*?)" alt.*?</div>'
    #ex = '<div class="thumb">[\s\S]*?<img src="(.*?)" alt'
    img_list=re.findall(ex,page_text,re.S)
    print(img_list)
    for scr in img_list:
        src= 'http'+scr#拼接完整的地址
        reponse=requests.get(url=src,headers=headers).content
        #生成图片名称
        img_name=src.split('/')[-1]
        img_all=img_name+'./tupian'
        with open(img_all) as fp:
            fp.write(img_all)
            print(img_all,"over!!!")



