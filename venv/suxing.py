import requests
import json
from selenium import webdriver
import time

class G:
    pageEnd = False
    headers = {
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1',
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
    s = requests.session()

def get_pages_id(page_num):
    url = 'https://m.dianping.com/activity/static/list?page='+ str(page_num) +'&cityid=2&regionParentId=0&regionId=0&type=1&sort=0&filter=0'
    r = G.s.get(url, headers=G.headers)
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
    r = G.s.post(url, headers=G.headers, data=order_data)
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
    r = G.s.post(url, headers=G.headers, data=branch_data)
    print (r.text)
    branch_dict = json.loads(r.text)
    branch_id = branch_dict['data']['branchs'][0]['branchId']

    order_data = {
        'cx': None,
        'env': 1,
        'branchId': branch_id,
        'comboId': 1,
        'offlineActivityId': activityid,
        'passCardNo': None,
        'phoneNo': '186****0270',
        'source': 'null',
        'uuid': None
    }
    order_r = G.s.post(order_url, headers=G.headers, data=order_data)
    print (order_r.text)

def get_cookie():
    options = webdriver.ChromeOptions()
    options.add_argument('lang=zh_CN.UTF-8')
    options.add_argument('user-agent="Mozilla/5.0 (iPod; U; CPU iPhone OS 2_1 like Mac OS X; ja-jp) AppleWebKit/525.18.1 (KHTML, like Gecko) Version/3.1.1 Mobile/5F137 Safari/525.20"')


    driver = webdriver.Chrome(chrome_options=options)
    driver.get("https://mlogin.dianping.com/login/password")
    driver.find_element_by_xpath('//*[@id="login-form"]/div/div/div[1]/input').send_keys('18600440270')
    driver.find_element_by_xpath('//*[@id="login-form"]/div/div/div[2]/input').send_keys('yangsu0110')
    driver.find_element_by_id('login-button').click()

    time.sleep(15)
    cookie = driver.get_cookies()
    driver.quit()
    return cookie

def add_cookie(cookie):
    c = requests.cookies.RequestsCookieJar()
    for i in cookie:
        c.set(i["name"], i["value"])

    G.s.cookies.update(c)


def main():
    cookie = get_cookie()
    add_cookie(cookie)
    print ('cookie加载完成')
    for i in range(1, 10):
        parser_pages(get_pages_id(i))
        if G.pageEnd:
            break

    for activitysid in G.activitysid_list:
        order(activitysid)
main()