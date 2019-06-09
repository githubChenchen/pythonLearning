import requests,os
from bs4 import BeautifulSoup


def fanhao():
    url = 'http://www.d28k.com/cn/vl_genre.php'
    # http: // www.d28k.com / cn / vl_genre.php?g = cu
    params = {
        'mode': '',
        'g':'cu',
        'page':'1'
    }
    for i in range(1,11):
        filename = 'fanhao.txt'
        params['page'] = i
        res = requests.get(url,params)
        print(res.url)
        if res.status_code == 200:
            soup = BeautifulSoup(res.content,'lxml')
            fanhaoList = soup.find_all('div',class_ = 'video')
            for item in fanhaoList:
                with open(filename,'a',encoding='utf-8') as w:
                    w.write(item.string+'   ')
            with open(filename,'a',encoding='utf-8') as w2:
                w2.write('\n')

def tupian():
    url = 'http://www.d28k.com/cn/vl_genre.php'
    # http: // www.d28k.com / cn / vl_genre.php?g = cu
    params = {
        'mode': '',
        'g': 'cu',
        'page': '1'
    }
    res = requests.get(url, params)
    if res.status_code == 200:
        soup = BeautifulSoup(res.content,'lxml')
        fanhaolist = soup.find_all('div', class_='video')
        for item in fanhaolist:
            fanhaoTag = item.find('div',class_='id')
            fanhao = fanhaoTag.string
            pictureTag = item.find('img')
            srcUrl = pictureTag['src']
            srcUrl = 'http:'+srcUrl
            r = requests.get(srcUrl)
            targetDir = 'picture'
            filename = os.path.join(targetDir,fanhao+'.jpg')
            with open(filename,'wb') as f:
                f.write(r.content)


if __name__ == '__main__':
    # fanhao()
    tupian()