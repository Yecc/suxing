a = """Accept: application/json, text/javascript
Accept-Encoding: gzip, deflate, br
Accept-Language: zh-CN,zh;q=0.9,en;q=0.8
Connection: keep-alive
Content-Type: application/x-www-form-urlencoded
Cookie: _lxsdk_cuid=161ad130f75c8-099dd9fd58f3c6-32687a04-1fa400-161ad130f76c8; _lxsdk=161ad130f75c8-099dd9fd58f3c6-32687a04-1fa400-161ad130f76c8; _hc.v=015b9cac-41f5-50c9-5b9f-5485f7ac38f0.1519027163; s_ViewType=10; _dp.ac.v=66165a86-31be-4f3b-a52c-5f6f4be762d8; ctu=ea699dee96a1f9175dbf280cc9dc03d2019db2f32c6c52c19b366f24102e115d; aburl=1; switchcityflashtoast=1; cye=beijing; default_ab=citylist%3AA%3A1%7Cshop%3AA%3A1%7Cindex%3AA%3A1%7CshopList%3AA%3A1%7Cmyinfo%3AA%3A1; cityid=2; dper=984a7d02654b9ae7b44d068f11939feb1bd55f79f66c05b375c5ed96d6b7b9b52294deeb51f23985b1a6200dd0b5ecfca53ea0412df9d83be78380965cc9563574f47844f9ed48ebc54692da37e00b658480dfa64b318e713104dd37c9fbc1cd; ua=18600440270; ll=7fd06e815b796be3df069dec7836c3df; cy=2; _lx_utm=utm_source%3Dnull; _lxsdk_s=164a6a7ccee-792-144-0a0%7C%7C31
Host: m.dianping.com
Origin: https://h5.dianping.com
Referer: https://h5.dianping.com/app/app-community-free-meal/index.html
User-Agent: Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1"""

print({i.split(":",1)[0]:i.split(":")[1] for i in a.split("\n")[1:-1]})