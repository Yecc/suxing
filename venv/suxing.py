import requests
import json

class G:
    pageEnd = False

def get_pages_id(page_num):
    url = 'https://m.dianping.com/activity/static/list?page='+ str(page_num) +'&cityid=2&regionParentId=0&regionId=0&type=1&sort=0&filter=0'
    r = requests.get(url)
    return r.text

def parser_pages(id_str):
    id_dict = json.loads(id_str)
    isend = id_dict['data']['pageEnd']
    activity_id = id_dict['data']['mobileActivitys'][0]
    print (activity_id)
    if isend:
        G.pageEnd = True
def main():
    for i in range(1, 10):
        parser_pages(get_pages_id(i))
        if G.pageEnd:
            break
main()