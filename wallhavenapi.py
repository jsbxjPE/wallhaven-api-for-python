import requests
import json

global path_url
global url_id

def search_x(search, page, purity, x_api):
    global path_url
    global url_id
    path_url = []
    url_id = []
    if purity == 'sfw':
        purity = '111'
    elif purity == 'sketchy':
        purity = '010'
    elif purity == 'nsfw':
        purity = '001'
    else:
        return 'Not have purity.'
    header = {
        'X-API':x_api
    }
    for i in range(int(page)):
        wall_url = 'https://wallhaven.cc/api/v1/search?q={}&page={}&purity={}}'.format(search,str(i+1),str(purity))
        data = json.loads(requests.get(url=wall_url, headers=header).text)
        if data['data'] == []:
            return 'Data no data.'
        for i in data['data']:
            path_url.append(i['path'])
            url_id.append(i['id'])
    return [path_url, url_id]
def search(search, page, purity):
    global path_url
    global url_id
    path_url = []
    url_id = []
    if purity == 'sfw':
        purity = '111'
    elif purity == 'sketchy':
        purity = '010'
    else:
        return 'Not have purity.'
    for i in range(int(page)):
        wall_url = 'https://wallhaven.cc/api/v1/search?q={}&page={}&purity={}'.format(search,str(i+1),str(purity))
        data = json.loads(requests.get(url=wall_url).text)
        if data['data'] == []:
            return 'Data no data.'
        for i in data['data']:
            path_url.append(i['path'])
            url_id.append(i['id'])
    return [path_url, url_id]

def download_x(dir_name, x_api):
    global path_url
    header = {
        'X-API':x_api
    }
    num = 0
    max_num = len(path_url)
    for i in path_url:
        content = requests.get(url=i, headers=header).content
        name = '{}/{}.jpg'.format(dir_name, url_id[num])
        with open(name, 'wb') as f:
            f.write(content)
        num = num + 1
    return 'Download ok'
def download(dir_name):
    global path_url
    num = 0
    max_num = len(path_url)
    for i in path_url:
        content = requests.get(url=i).content
        name = '{}/{}.jpg'.format(dir_name, url_id[num])
        with open(name, 'wb') as f:
            f.write(content)
        num = num + 1
    return 'Download ok'
