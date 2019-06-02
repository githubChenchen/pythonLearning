import jieba,os
import jieba.posseg as jp
from collections import Counter
from pyecharts.charts import WordCloud
from pyecharts import options as opts

def word_cloud():
    filedir = u'E:\陈晨\新建文件夹\diary'
    li = os.listdir(filedir)
    wordList = []
    for item in li:
        filename = os.path.join(filedir,item)
        with open(filename,'r', encoding='utf-8') as f:
            fr = f.read()
            jplist = jp.lcut(fr)
            for item in jplist:
                item = item.__dict__
                if item['flag'] == 'a':
                    wordList.append(item['word'])
    count = Counter(wordList)


if __name__ == '__main__':
    word_cloud()