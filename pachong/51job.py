import requests
from bs4 import BeautifulSoup


def salarySinglePage(url, params):
    res = requests.get(url,params=params)
    infoList = []
    if res.status_code == 200:
        soup = BeautifulSoup(res.content, 'lxml')
        jobList = soup.find_all('div', class_='el')
        for job in jobList:
            info = {}
            companyName = ''
            salary = ''
            companyTag = job.find('span', class_='t2')
            if companyTag:
                companyTag1 = companyTag.find('a')
                if companyTag1:
                    companyName = companyTag1.string
            salaryTag = job.find('span', class_='t4')
            if salaryTag:
                salary = salaryTag.string
            if companyName and salary:
                info[companyName] = salary
                infoList.append(info)
    return infoList


def pythonSalary(page):
    url = 'https://search.51job.com/list/070200,000000,0000,00,9,99,Python,2,1.html'
    params = {
        'lang': 'c',
        'stype': '',
        'postchannel': '0000',
        'workyear': '99',
        'cotype': '99',
        'degreefrom': '99',
        'jobterm': '99',
        'companysize': '99',
        'providesalary': '99',
        'lonlat': '0%2C0',
        'radius': '-1',
        'ord_field': '0',
        'confirmdate': '9',
        'fromType': '',
        'dibiaoid': '0',
        'address': '',
        'line': '',
        'specialarea': '00',
        'from': '',
        'welfare': ''
    }



if __name__ == '__main__':
    pythonSalary()