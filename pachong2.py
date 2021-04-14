import requests
import json
if __name__=="__main__":
    url='https://movie.douban.com/j/chart/top_list'
    param={
    "type":"24",
    'interval_id':'100:90',
    'action':'',
    'start':'1',#第几个电影开始起，一次取20个
    'limit':'20',
    }
    headers={'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_1_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36'}
    response=requests.get(url=url,params=param,headers=headers)
    list_data =response.json() #返回的是列表用list_data
    fp=open('./dianying.json','w',encoding='utf-8')
    json.dump(list_data,fp=fp,ensure_ascii=False)
    print('over!!!')