#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os,shutil


def rename():
    filedirectory = r'C:\Users\Administrator\Desktop\diary'
    targetDirectory = r'E:\陈晨\新建文件夹\日记'
    fileList = os.listdir(filedirectory)
    for file in fileList:
        filename = os.path.join(filedirectory, file)
        with open(filename, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        flag = False
        newName = ''
        for line in lines:
            if r'标题:' == line.strip():
                flag = True
                continue
            if flag:
                newName = line.strip()+'.txt'
                break
        targetFile = os.path.join(targetDirectory,newName)
        shutil.copy(filename,targetFile)


if __name__ == '__main__':
    rename()