import requests
#UA伪装，门户网站的服务器会检测对应载体的身份标识，如果检测载体的身份标识为某一浏览器，表示正常
#但是不是基于某一浏览器，表示爬虫，拒绝本次请求
#UA:user-angent请求载体的身份标识
if __name__=="__main__":
   url = 'https://chrome.google.com/webstore/category/extensions?'
   #UA将对应的user-agent封装到一个字典中
   header={
      'user-anger':'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_1_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36'
   }

   #处理URL携带的参数：封装到字典中
   kw=input('enter a world:')
   param={'hl':kw}
   response=requests.get(url=url,params=param,headers=header)#发起请求#get返回一个响应对象#并且携带参数param#header指定的载体的头信息
   page_text=response.text#获取字符串形式相应数据
   print(page_text)
   filname=kw+'.html'
   with open(filname,'w',encoding='utf-8') as fp:
       fp.write(page_text)

#rqq = requests.get(url)
#print('响应码：', rqq.status_code) #查看响应码
#rqq.encoding = 'gbk'  #设置网页中文编码，设置和网页的一样，否则会乱码
#rqq.text  #解析网页



