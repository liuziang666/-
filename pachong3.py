import requests
import json
if __name__=='__main__':
    #找出主页与分页的不同，在于id

    url='http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsList'
    param={
    'on': 'true',
    'page': '1',
    'pageSize': '15',
     'productName': '',
    'conditionType': '1',
    'applyname': '',
    'applysn': '',
    }
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_1_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36'}
    json_ids = requests.post(url=url, params=param, headers=headers).json()
    id_list=[]#存储ID
    all_list=[]#存储所有数据详情,列表
    for dic in json_ids["list"]:#将list字典遍历
        id_list.append(dic['ID'])#找到其中的ID
    print(id_list)
    #获取企业详情数据
    post_url='http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsById'
    name1 = []
    for id in id_list:#将ID设置为动态参数遍历
        params={
        'id': id
        }
        data_json=requests.post(url=post_url,params=params,headers=headers).json()
        name1.append(data_json['businessPerson'])
        print(data_json['businessPerson'])
        #print(data_json)
        all_list.append(data_json)
    fp=open('./all_data.json','w',encoding='utf-8')
    json.dump(all_list,fp=fp,ensure_ascii=False)
    print('over')
    print(name1)


