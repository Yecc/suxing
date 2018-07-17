from selenium import webdriver
import time

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

print (cookie)