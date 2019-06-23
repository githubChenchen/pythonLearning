import requests,re
from bs4 import BeautifulSoup


def get_Info_single(url):
    # url = 'http://www.segou4.com/thread-28.html'
    header = {
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'
    }
    res = requests.get(url, headers=header)
    if res.status_code == 200:
        domainName = 'http://www.segou4.com'
        soup = BeautifulSoup(res.content,'lxml')
        pic_list = soup.find('ol',class_='pic-list')
        liList = pic_list.find_all('li')
        for item in liList:
            a = item.find('a')
            name = a['title']
            name_match = re.match(r'(\S+)\s+\S+',name,re.I)
            real_name = name_match.group(1)
            item_url = domainName+a['href']
            item_res = requests.get(item_url, headers=header)
            if item_res.status_code == 200:
                item_soup = BeautifulSoup(item_res.content, 'lxml')
                play_list = item_soup.find('div',class_='play-list')
                item_li = play_list.find('li')
                item_link = item_li.find('a')
                link = domainName+item_link['href']
                info = real_name+' = '+link
                with open('Info.txt','a',encoding='utf-8') as f:
                    f.write(info)
                    f.write('\n')


def get_info(page):
    url = 'http://www.segou4.com/thread-28-{page}.html'
    for i in range(1,page):
        url = url.format(**{'page':i})
        get_Info_single(url)


def main():
    get_info(10)


if __name__ == '__main__':
    main()