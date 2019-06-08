import requests,re
import pandas as pd
from bs4 import BeautifulSoup


houseInfoList = []

def get_prize(url, page):
    # url = 'https://nj.lianjia.com/ershoufang/jiangning/pg{page}/'
    header = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'}
    houseInfoList = []

    for i in range(1,page+1):
        urlreal = url.format(**{'page':i})
        r = requests.get(urlreal,headers=header,timeout=30)
        if r.status_code == 200:
            soup = BeautifulSoup(r.content,'lxml')
            sellListContent = soup.find('ul', class_ = 'sellListContent')
            sellList = sellListContent.find_all('li', class_ = 'clear')
            for item in sellList:
                houseInfo = item.find('div', class_ = 'houseInfo')
                infoStr = houseInfo.getText()
                infoList = infoStr.split('|')
                unitPrice = item.find('div', class_='unitPrice')
                if unitPrice:
                    price = unitPrice.find('span').string
                if(len(infoList))>6:
                    for i in range(0,len(infoList)-6):
                        infoList.pop()
                if len(infoList)<6:
                    for i in range(0,6-len(infoList)):
                        infoList.append(' ')
                infoList.append(price)
                houseInfoList.append(infoList)
    return houseInfoList

        # print(soup.text)
        # next_page1 = soup.find_all('a',attrs={'class':'on'})
        # next_page = soup.find_all('div',class_='page-box')
        # pageList = list(next_page.children)
        # for page in pageList:
        #     print(page.string)
        # if next_page:
        #     next_url = next_page['href']
        #     get_prize(next_url,header)


def handle_data(dataList):
    data_list = []
    for item in dataList:
        item[-1] = handle_price(item[-1])
        data_list.append(item)

    colList = ['小区','户型','大小','方向','装修','电梯','单价']
    priceDf = pd.DataFrame(data_list,columns=colList)
    return priceDf


def handle_price(price):
    matchPrice = re.match(r'单价(\d+)\S+',price,re.I)
    price = float(matchPrice.group(1))
    return price


def between(min, max, data):
    newList = []
    for item in data:
        if item>min and item<max:
            newList.append(item)
    a = len(newList)/len(data)
    return a



def saveDataCsv(df):
    """
    保存数据到csv文件中
    :param df: dataframe类型数据
    :return:
    """
    filename = 'nanjing_house_price.csv'
    try:
        df.to_csv(filename, encoding='gbk')
    except UnicodeEncodeError:
        print("编码错误, 该数据无法写到文件中, 直接忽略该数据")


if __name__ == '__main__':
    # url = 'https://nj.lianjia.com/ershoufang/pg1/'
    # header = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'}
    # url = 'https://nj.lianjia.com/ershoufang/jiangning/pg{page}/'

    url = 'https://zj.lianjia.com/ershoufang/jurong/pg{page}/'

    dataList = get_prize(url,10)
    df = handle_data(dataList)
    data = df.单价.tolist()
    # print(between(0,30000,data))
    saveDataCsv(df)
    print(df.describe())
    # print(123)
