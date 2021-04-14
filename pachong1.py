import requests
import json
#解析百度翻译，网页上刷新数据解析，阿贾克斯请求
if __name__=="__main__":
    #制定URL
    post_url='https://fanyi.baidu.com/sug'
    #post请求参数处理
    word=input('word:')
    data1={
      'kw':word
    }
    #进行UA伪装
    headers = {
        'user-anger': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_1_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36'

    }
    #请求发送
    response=requests.post(url=post_url,data=data1,headers=headers)
    dic_obj=response.json()#获取数据，返回的是obj对象（确认返回类型是json类型）
    filename=word+'.json'
    fp=open(filename,'w',encoding='utf-8')
    json.dump(dic_obj,fp=fp,ensure_ascii=False)
    print(dic_obj)
