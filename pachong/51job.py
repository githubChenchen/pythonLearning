import requests,re
from bs4 import BeautifulSoup
import pandas as pd
from pyecharts.charts import Line
from pyecharts import options as opts
import matplotlib.pyplot as plt


def salary_python(page):
    """
    获取前程无忧上前page页的Python职位对应的公司名称以及薪水
    :param page: 页数
    :return:返回公司名称与薪水对应的字典
    """
    urlpri = 'https://search.51job.com/list/070200,000000,0000,00,9,99,Python,2,{page}.html'
    info = {}
    for i in range(1,page+1):
        url = urlpri.format(**{'page':i})
        res = requests.get(url)
        if res.status_code == 200:
            soup = BeautifulSoup(res.content, 'lxml')
            jobList = soup.find_all('div', class_='el')
            for job in jobList:
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
    return info


def cleanData(dict):
    """
    清理获取的数据，薪水全部转化为float，单位为 元/月
    :param dict: 获取的原始数据
    :return: 返回处理过的数据
    """
    nameList = list(dict.keys())
    salary = list(dict.values())
    salaryList = []
    for item in salary:
        salaryItem = handle_salary(item)
        salaryList.append(salaryItem)

    dataDict = {}
    for i in range(len(nameList)):
        dataDict[nameList[i]] = salaryList[i]

    dataDictNew = {}
    for key,value in dataDict.items():
        if isinstance(value,float):
            dataDictNew[key] = value
    data = {'name': list(dataDictNew.keys()), 'salary': list(dataDictNew.values())}
    df = pd.DataFrame(data)
    return df


def handle_salary(s):
    """
    将str类型的薪水表述，转化为flaot类型，并全部转化为 元/月为单位
    :param s: 字符串类型数据
    :return: float类型薪水
    """
    if r'万' in s and r'月' in s:
        matchwMouth1 = re.match(r'(\d+\.*\d*)\-(\d+\.*\d*)', s, re.I)
        matchwMouth2 = re.match(r'(\d+\.*\d*)', s, re.I)
        if matchwMouth1:
            sMin = float(matchwMouth1.group(1))
            sMax = float(matchwMouth1.group(2))
            salary = (sMax+sMin)/2.0
            return round(salary*10000, 2)
        elif matchwMouth2:
            salary = float(matchwMouth2.group(1))
            return round(salary*10000, 2)
        else:
            return s
    elif r'万' in s and r'年' in s:
        matchwYear1 = re.match(r'(\d+\.*\d*)\-(\d+\.*\d*)', s, re.I)
        matchwYear2 = re.match(r'(\d+\.*\d*)', s, re.I)
        if matchwYear1:
            sMin = float(matchwYear1.group(1))
            sMax = float(matchwYear1.group(2))
            salary = (sMax + sMin) / (2.0*12)
            return round(salary*10000, 2)
        elif matchwYear2:
            salary = float(matchwYear2.group(1))/12.0
            return round(salary*10000, 2)
        else:
            return s
    elif r'千' in s and r'月' in s:
        matchqMouth1 = re.match(r'(\d+\.*\d*)\-(\d+\.*\d*)', s, re.I)
        matchqMouth2 = re.match(r'(\d+\.*\d*)', s, re.I)
        if matchqMouth1:
            sMin = float(matchqMouth1.group(1))
            sMax = float(matchqMouth1.group(2))
            salary = (sMax + sMin) / 2.0
            return round(salary*1000, 2)
        elif matchqMouth2:
            salary = float(matchqMouth2.group(1))
            return round(salary*1000, 2)
        else:
            return s
    elif r'百' in s and r'天' in s:
        matchbDay1 = re.match(r'(\d+\.*\d*)\-(\d+\.*\d*)', s, re.I)
        matchbDay2 = re.match(r'(\d+\.*\d*)', s, re.I)
        if matchbDay1:
            sMin = float(matchbDay1.group(1))
            sMax = float(matchbDay1.group(2))
            salary = (sMax + sMin) / 2.0
            return round(salary*3000, 2)
        elif matchbDay2:
            salary = float(matchbDay2.group(1))
            return round(salary*3000, 2)
        else:
            return s
    elif r'天' in s:
        matchbDay1 = re.match(r'(\d+\.*\d*)\-(\d+\.*\d*)', s, re.I)
        matchbDay2 = re.match(r'(\d+\.*\d*)', s, re.I)
        if matchbDay1:
            sMin = float(matchbDay1.group(1))
            sMax = float(matchbDay1.group(2))
            salary = (sMax + sMin) / 2.0
            return round(salary*30, 2)
        elif matchbDay2:
            salary = float(matchbDay2.group(1))
            return round(salary*30, 2)
        else:
            return s
    elif r'月' in s:
        if r'万' in s and r'月' in s:
            matchMouth1 = re.match(r'(\d+\.*\d*)\-(\d+\.*\d*)', s, re.I)
            matchMouth2 = re.match(r'(\d+\.*\d*)', s, re.I)
            if matchMouth1:
                sMin = float(matchMouth1.group(1))
                sMax = float(matchMouth1.group(2))
                salary = (sMax + sMin) / 2.0
                return round(salary, 2)
            elif matchMouth2:
                salary = float(matchMouth2.group(1))
                return round(salary, 2)
            else:
                return s
    elif r'年' in s:
        matchYear1 = re.match(r'(\d+\.*\d*)\-(\d+\.*\d*)', s, re.I)
        matchYear2 = re.match(r'(\d+\.*\d*)', s, re.I)
        if matchYear1:
            sMin = float(matchYear1.group(1))
            sMax = float(matchYear1.group(2))
            salary = (sMax + sMin) / (2.0 * 12)
            return round(salary, 2)
        elif matchYear2:
            salary = float(matchYear2.group(1)) / 12.0
            return round(salary, 2)
        else:
            return s
    else:
        return s


def saveDataCsv(df):
    """
    保存数据到csv文件中
    :param df: dataframe类型数据
    :return:
    """
    filename = 'python_51job_salary.csv'
    try:
        df.to_csv(filename, encoding='gbk')
    except UnicodeEncodeError:
        print("编码错误, 该数据无法写到文件中, 直接忽略该数据")


def over(df, num):
    """
    计算高于num的工资所占比例
    :param df: 原始数据，dataframe类型
    :param num: 高于工资
    :return: 比例
    """
    salaryList = df.salary.tolist()
    overList = [x for x in salaryList if x>num]
    over = len(overList)*1.0/len(salaryList)
    return over


if __name__ == '__main__':
    salaryDict = salary_python(3) #获取前三页工资，原始数据
    dfSalary = cleanData(salaryDict) #处理过的数据

    print(over(dfSalary,10000))  #工资高于10000职位所占比例

    li = dfSalary.salary.tolist()
    line = (
        Line().
            add_xaxis(dfSalary.name.tolist()).
            add_yaxis('python', li).
            set_global_opts(title_opts=opts.TitleOpts(title='python工资分布'))
    )
    line.render()

    saveDataCsv(dfSalary)  #保存数据到csv
    dfSalary.plot()
    plt.show()  #绘制折现图表

    print(dfSalary.describe())