import requests,os
from bs4 import BeautifulSoup


def search(url,params,picDir,pageStart=1,pageStop=1):
    domain_name = 'http://www.q30x.com/cn'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'}

    for i in range(pageStart,pageStop+1):
        params['page'] = i
        try:
            res = requests.get(url, params=params, headers=headers, timeout=30)
        except:
            continue
        if res.status_code == 200:
            soup = BeautifulSoup(res.content, 'lxml')
            videoList = soup.find_all('div', class_='video')
            for video in videoList:
                a = video.find('a')
                fanhao = a.find('div',class_='id').string
                urlPic = a['href']
                urlPicWhole = urlPic.replace('.',domain_name,1)
                resPic = requests.get(urlPicWhole,headers=headers)
                if resPic.status_code == 200:
                    soupPic = BeautifulSoup(resPic.content, 'lxml')
                    targetPicTag = soupPic.find('img', id='video_jacket_img')
                    targetPicUrl = targetPicTag['src']
                    targetPicUrl = 'http:'+targetPicUrl
                    restargetPic = requests.get(targetPicUrl,headers=headers)
                    if restargetPic.status_code == 200:
                        if not os.path.exists(picDir):
                            os.mkdir(picDir)
                        filename = os.path.join(picDir,fanhao+'.jpg')
                        with open(filename,'wb') as f:
                            f.write(restargetPic.content)


        # print('sccess')


if __name__ == '__main__':
    url = 'http://www.q30x.com/cn/vl_genre.php'
    params = {
        'g':'cu',
        'page':1
    }
    picDir = u'E:\陈晨\gitWorkspace\pythonLearning\picture'
    search(url,params=params, picDir=picDir, pageStart=4, pageStop=10)
    #http://www.q30x.com/cn/?v=javli6djzu