#!/usr/bin/python
# -*- coding: UTF-8 -*-

import wx,shutil,os,time,threading


def zipDir(dirPath,outPath):
    t = time.strftime('%Y%m%d%H%M%S',time.localtime())
    if os.path.isdir(dirPath) and os.path.isdir(outPath):
        name = os.path.join(outPath,t)
        shutil.make_archive(name,'zip',dirPath)


class Backup(wx.Frame):
    def __init__(self, parent, id, title):
        wx.Frame.__init__(self, parent, id, title, size=(500, 180))
        self.pnl = wx.Panel(self)

        self.makeMenu()
        self.makePannel()

        self.SetMaxSize((500,180))
        self.Center()
        self.Show()

    def makePannel(self):

        font = wx.Font(14, wx.DEFAULT, wx.NORMAL, wx.NORMAL)

        hboxBackPath = wx.BoxSizer(wx.HORIZONTAL)
        hboxTargetPath = wx.BoxSizer(wx.HORIZONTAL)
        hboxTime = wx.BoxSizer(wx.HORIZONTAL)
        hboxButton = wx.BoxSizer(wx.HORIZONTAL)
        vBox = wx.BoxSizer(wx.VERTICAL)

        backupPathTxt = wx.StaticText(self.pnl, label=u"备份路径:", size=(100, 30))
        backupPathTxt.SetFont(font)
        self.backupPathT = wx.TextCtrl(self.pnl, wx.ID_ANY, style=wx.TE_READONLY)
        button1 = wx.Button(self.pnl, -1, label="...", size=(30, 28))
        self.Bind(wx.EVT_BUTTON,self.chooseBackPath,button1)
        hboxBackPath.Add(backupPathTxt, proportion=2, flag=wx.LEFT, border=2)
        hboxBackPath.Add(self.backupPathT, proportion=8, flag=wx.LEFT, border=10)
        hboxBackPath.Add(button1, proportion=0, flag=wx.LEFT, border=2)

        targetPathTxt = wx.StaticText(self.pnl, label=u"目标路径:", size=(100, 30))
        targetPathTxt.SetFont(font)
        self.targetPathT = wx.TextCtrl(self.pnl, wx.ID_ANY, style=wx.TE_READONLY)
        button2 = wx.Button(self.pnl, -1, label="...", size=(30, 28))
        self.Bind(wx.EVT_BUTTON, self.chooseTargetPath, button2)
        hboxTargetPath.Add(targetPathTxt, proportion=2, flag=wx.LEFT, border=2)
        hboxTargetPath.Add(self.targetPathT, proportion=8, flag=wx.LEFT, border=10)
        hboxTargetPath.Add(button2, proportion=0, flag=wx.LEFT, border=2)

        timePathTxt = wx.StaticText(self.pnl, label=u"间隔时间(min):", size=(150, 30))
        timePathTxt.SetFont(font)
        self.timePathT = wx.TextCtrl(self.pnl, wx.ID_ANY)
        hboxTime.Add(timePathTxt, proportion=2, flag=wx.LEFT, border=2)
        hboxTime.Add(self.timePathT, proportion=4, flag=wx.LEFT, border=2)

        self.buttonStart = wx.Button(self.pnl, -1, label="开始备份", size=(70, 50))
        buttonExit = wx.Button(self.pnl, -1, label="结束退出", size=(70, 50))
        self.Bind(wx.EVT_BUTTON, self.OnQuit, buttonExit)
        self.Bind(wx.EVT_BUTTON, self.start, self.buttonStart)
        hboxButton.Add(self.buttonStart, proportion=0, flag=wx.RIGHT, border=2)
        hboxButton.Add(buttonExit, proportion=0, flag=wx.RIGHT, border=2)

        vBox.Add(hboxBackPath,proportion=1, flag=wx.LEFT, border=2)
        vBox.Add(hboxTargetPath,proportion=1, flag=wx.LEFT, border=2)
        vBox.Add(hboxTime,proportion=1, flag=wx.LEFT, border=2)
        vBox.Add(hboxButton, proportion=1, flag=wx.LEFT, border=2)

        self.SetSizer(vBox)

    def makeMenu(self):
        menuBar = wx.MenuBar()
        exitMenu = wx.Menu()
        fitem = exitMenu.Append(wx.ID_EXIT, "Quit", "Quit Applications")
        self.Bind(wx.EVT_MENU, self.OnQuit, fitem)
        menuBar.Append(exitMenu,"&quit")

        self.SetMenuBar(menuBar)

    def OnQuit(self, e):
        self.Close()

    def chooseBackPath(self,event):
        dlg = wx.DirDialog(self,u"选择文件夹",style=wx.DEFAULT_DIALOG_STYLE)
        if dlg.ShowModal() == wx.ID_OK:
            self.backupPathT.SetValue(dlg.GetPath())
        dlg.Destroy()

    def chooseTargetPath(self,event):
        dlg = wx.DirDialog(self,u"选择文件夹",style=wx.DEFAULT_DIALOG_STYLE)
        if dlg.ShowModal() == wx.ID_OK:
            self.targetPathT.SetValue(dlg.GetPath())
        dlg.Destroy()

    def vaildate(self):
        back = self.backupPathT.GetValue()
        target = self.targetPathT.GetValue()
        time:str = self.timePathT.GetValue()
        if len(back)==0 or len(target)==0 or len(time)==0:
            msg = wx.MessageDialog(None,u'填写信息不全，请重新填写！',u'警告',wx.OK)
            msg.ShowModal()
            return False
        if not time.isdigit():
            msg = wx.MessageDialog(None, u'时间格式不正确，请重新填写', u'警告', wx.OK)
            msg.ShowModal()
            return False
        return True

    def zipfile(self):
        if self.vaildate():
            zipDir(self.backupPathT.GetValue(),self.targetPathT.GetValue())
            t = threading.Timer(int(self.timePathT.GetValue())*60,self.zipfile)
            t.start()

    def start(self,event):
        if self.vaildate():
            self.buttonStart.Enable(False)
            self.zipfile()

if __name__ == '__main__':
    app = wx.App()
    Backup(None, -1, '备份文件')
    app.MainLoop()
