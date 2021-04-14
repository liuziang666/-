from bs4 import BeautifulSoup
if __name__=="__main__":
    #将本地数据文档html加载到对象中
    fp=open('./dazhangwei.html','r',encoding='utf-8')
    sunp=BeautifulSoup(fp,'html')
    print(sunp)
