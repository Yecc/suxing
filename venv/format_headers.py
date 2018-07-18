a = """
Accept: application/json, text/javascript
Accept-Encoding: gzip, deflate, br
Accept-Language: zh-CN,zh;q=0.9,en;q=0.8
Connection: keep-alive
Content-Type: application/x-www-form-urlencoded
Host: m.dianping.com
Origin: https://h5.dianping.com
Referer: https://h5.dianping.com/app/app-community-free-meal/index.html
User-Agent: Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1
"""

print({i.split(":",1)[0]:i.split(":")[1] for i in a.split("\n")[1:-1]})