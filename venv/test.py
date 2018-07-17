from selenium import webdriver
import time
import requests

class G:
    s = requests.session()
    headers = {
        'Accept': ' application/json, text/javascript', 'Accept-Encoding': ' gzip, deflate, br',
        'Accept-Language': ' zh-CN,zh;q=0.9,en;q=0.8', 'Connection': ' keep-alive',
        'Content-Type': ' application/x-www-form-urlencoded', 'Host': ' m.dianping.com', 'Origin': ' https',
        'Referer': ' https',
        'User-Agent': ' Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1'
    }

def get_cookie():
    options = webdriver.ChromeOptions()
    options.add_argument('lang=zh_CN.UTF-8')
    options.add_argument('user-agent="Mozilla/5.0 (iPod; U; CPU iPhone OS 2_1 like Mac OS X; ja-jp) AppleWebKit/525.18.1 (KHTML, like Gecko) Version/3.1.1 Mobile/5F137 Safari/525.20"')


    driver = webdriver.Chrome(chrome_options=options)
    driver.get("https://mlogin.dianping.com/login/password")
    driver.find_element_by_xpath('//*[@id="login-form"]/div/div/div[1]/input').send_keys('18600440270')
    driver.find_element_by_xpath('//*[@id="login-form"]/div/div/div[2]/input').send_keys('yangsu0110')
    driver.find_element_by_id('login-button').click()

    time.sleep(20)
    cookie = driver.get_cookies()
    driver.quit()
    print (cookie)
    return cookie

def add_cookie(cookie):
    c = requests.cookies.RequestsCookieJar()
    for i in cookie:
        c.set(i["name"], i["value"])

    G.s.cookies.update(c)

    r = G.s.get('https://m.dianping.com/activity/static/list?page=1&cityid=2&regionParentId=0&regionId=0&type=0&sort=0&filter=0')
    print (r.text)

def main():
    cookie = get_cookie()
    add_cookie(cookie)

main()
