import requests
import json

class G:
    pageEnd = False
    headers = {
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1',
        'Cookie': '_lxsdk_cuid=161c5833a08c8-01effa25717221-326a7d04-13c680-161c5833a09c8; _lxsdk=161c5833a08c8-01effa25717221-326a7d04-13c680-161c5833a09c8; _hc.v=b03e110a-3a63-63bb-9cc7-b4f281bcc057.1519437168; ctu=ea699dee96a1f9175dbf280cc9dc03d29c3387333a91cd8cea05f785d0fa67b6; s_ViewType=10; aburl=1; cy=2; cye=beijing; switchcityflashtoast=1; logan_custom_report=; m_flash2=1; PHOENIX_ID=0a48418d-164a10b027c-bcde5; default_ab=citylist%3AA%3A1%7Cindex%3AA%3A1%7CshopList%3AA%3A1%7Cmyinfo%3AA%3A1; cityid=2; _lx_utm=utm_source%3Dnull; msource=default; chwlsource=default; source=m_browser_test_22; pvhistory="6L+U5ZuePjo8L3N1Z2dlc3QvZ2V0SnNvbkRhdGE/Xz0xNTMxNzMxMDUzNjEyJmNhbGxiYWNrPVplcHRvMTUzMTczMTA1MjMwOD46PDE1MzE3MzEwNTM2NjZdX1s="; ua=18600440270; ctu=e8eab73b92acdb0e3bace69f8b77856bdfd8855ae8f2f7cd9992f50ed5f29d74ec5cdf35fea34b351766ac93c87f1f7b; dper=984a7d02654b9ae7b44d068f11939febb83e5fbe3fa87389fe74444b3a6f24e190fb4857e20bb10fd711782cd261602972c13084b68bc088c80909e8c37ed523c150e58e30471d593dccf9822721d242cd16e6920fa256fd8eb89a53de1adf41; ll=7fd06e815b796be3df069dec7836c3df; logan_session_token=nadmmcrdnzqu1qi3n68n; _lxsdk_s=164a1b4c892-b40-938-5aa%7C%7C242',
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
    url = 'https://m.dianping.com/activity/static/list?page='+ str(page_num) +'&cityid=2&regionParentId=0&regionId=0&type=1&sort=0&filter=0'
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