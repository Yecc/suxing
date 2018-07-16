import requests
import json

class G:
    pageEnd = False
    headers = {
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1',
        'Cookie': '_lxsdk_cuid=161ad130f75c8-099dd9fd58f3c6-32687a04-1fa400-161ad130f76c8; _lxsdk=161ad130f75c8-099dd9fd58f3c6-32687a04-1fa400-161ad130f76c8; _hc.v=015b9cac-41f5-50c9-5b9f-5485f7ac38f0.1519027163; s_ViewType=10; _dp.ac.v=66165a86-31be-4f3b-a52c-5f6f4be762d8; ctu=ea699dee96a1f9175dbf280cc9dc03d2019db2f32c6c52c19b366f24102e115d; aburl=1; switchcityflashtoast=1; cy=2; cye=beijing; default_ab=citylist%3AA%3A1%7Cshop%3AA%3A1%7Cindex%3AA%3A1%7CshopList%3AA%3A1%7Cmyinfo%3AA%3A1; cityid=2; _lx_utm=utm_source%3Dnull; _lxsdk_s=164a3623554-78b-bd-e41%7C%7C29; dper=984a7d02654b9ae7b44d068f11939feb1bd55f79f66c05b375c5ed96d6b7b9b52294deeb51f23985b1a6200dd0b5ecfca53ea0412df9d83be78380965cc9563574f47844f9ed48ebc54692da37e00b658480dfa64b318e713104dd37c9fbc1cd; ll=7fd06e815b796be3df069dec7836c3df; ua=18600440270',
        'Host': 'm.dianping.com',
        'Referer': 'https://h5.dianping.com/app/app-community-free-meal/index.html',
        'Origin': 'https://h5.dianping.com',
        'Accept': 'application/json, text/javascript',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'Connection': 'keep - alive',
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    activitysid_list = []

def get_pages_id(page_num):
    url = 'https://m.dianping.com/activity/static/list?page='+ str(page_num) +'&cityid=2&regionParentId=0&regionId=0&type=2&sort=0&filter=0'
    r = requests.get(url, headers=G.headers)
    return r.text

def parser_pages(id_str):
    id_dict = json.loads(id_str)
    isend = id_dict['data']['pageEnd']
    activitys = id_dict['data']['mobileActivitys']
    for activity in activitys:
        if activity['applyed'] == False:
            print ('新增',activity['title'])
            G.activitysid_list.append(activity['offlineActivityId'])
    if isend:
        G.pageEnd = True

def order(activityid):
    url = 'https://m.dianping.com/mobile/dinendish/apply/doApplyActivity'
    order_data = {
        'cx': None,
        'env': 1,
        'offlineActivityId': activityid,
        'passCardNo': None,
        'phoneNo': '186****0270',
        'source': 'null',
        'uuid': None
    }
    r = requests.post(url, headers=G.headers, data=order_data)
    code_dict = json.loads(r.text)
    print(r.text)
    branch_code = code_dict['data']['code']
    if branch_code == 200:
        print ('成功-',activityid)
    if branch_code == 402:
        branch_case(activityid)

def branch_case(activityid):
    print ('---------处理分店---------')
    url = 'https://m.dianping.com/mobile/dinendish/apply/getPreApply'
    order_url = 'https://m.dianping.com/mobile/dinendish/apply/doApplyActivity'
    branch_data = {
        'activityId': activityid,
        'env': '1'
    }
    r = requests.post(url, headers=G.headers, data=branch_data)
    print (r.text)
    branch_dict = json.loads(r.text)
    branch_id = branch_dict['data']['branchs'][0]['branchId']

    order_data = {
        'cx': None,
        'env': 1,
        'branchId': branch_id,
        'offlineActivityId': activityid,
        'passCardNo': None,
        'phoneNo': '186****0270',
        'source': 'null',
        'uuid': None
    }
    order_r = requests.post(order_url, headers=G.headers, data=order_data)
    print (order_r.text)

def main():
    for i in range(1, 10):
        parser_pages(get_pages_id(i))
        if G.pageEnd:
            break

    for activitysid in G.activitysid_list:
        order(activitysid)
main()