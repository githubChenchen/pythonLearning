#!/usr/bin/python
# -*- coding: UTF-8 -*-

import wx,wx.grid,re


class RegexFrame(wx.Frame):
    def __init__(self, parent, id, title):
        self.start = 0
        wx.Frame.__init__(self, parent, id, title, size=(1300, 800))
        self.pnl = wx.Panel(self)

        self.makeMenu()
        self.makePannel()

        # self.SetMaxSize((500,180))
        self.Center()
        self.Show()

    def makeMenu(self):
        menuBar = wx.MenuBar()
        exitMenu = wx.Menu()
        fitem = exitMenu.Append(wx.ID_EXIT, "Quit", "Quit Applications")
        self.Bind(wx.EVT_MENU, self.OnQuit, fitem)
        menuBar.Append(exitMenu, "&quit")

        self.SetMenuBar(menuBar)

    def makePannel(self):
        # font = wx.Font(14, wx.DEFAULT, wx.NORMAL, wx.NORMAL)

        vbox_mode = wx.BoxSizer(wx.VERTICAL)
        hbox_1 = wx.BoxSizer(wx.HORIZONTAL)
        vbox_1 = wx.BoxSizer(wx.VERTICAL)
        hbox_2 = wx.BoxSizer(wx.HORIZONTAL)
        hbox_button = wx.BoxSizer(wx.HORIZONTAL)
        vbox = wx.BoxSizer(wx.VERTICAL)

        self.checkbox_I = wx.CheckBox(self.pnl, -1, "不区分大小写", (60, 20), (200, 20))
        self.checkbox_M = wx.CheckBox(self.pnl, -1, "多行匹配", (60, 20), (200, 20))
        self.assist_txt = wx.TextCtrl(self.pnl, -1, style=wx.TE_MULTILINE|wx.TE_WORDWRAP, size=(250,300))
        vbox_mode.Add(self.checkbox_I,proportion=1, flag=wx.TOP, border=10)
        vbox_mode.Add(self.checkbox_M,proportion=1, flag=wx.TOP, border=10)
        vbox_mode.Add(self.assist_txt,proportion=17, flag=wx.TOP, border=10)

        self.target_text = wx.TextCtrl(self.pnl, wx.ID_ANY, style=wx.TE_MULTILINE|wx.TE_RICH2|wx.HSCROLL, size=(600,550))
        self.result_table = wx.grid.Grid(self.pnl,-1)
        self.row_len = 24
        self.result_table.CreateGrid(self.row_len,1)
        self.result_table.SetRowSize(0, 20)
        self.result_table.SetColSize(0, 300)
        for i in range(self.row_len):
            self.result_table.SetReadOnly(row=i, col=0)
            self.result_table.SetRowLabelValue(i,"group "+str(i))
        self.result_table.SetColLabelValue(0,"结果")
        self.Bind(wx.grid.EVT_GRID_CELL_LEFT_CLICK, self.show_value, self.result_table)
        # self.result_table.SetCellValue(0,0,"fnauhwiughvieifuHFQFHIUEQHGbecbhedhuqhfuiqbhbvheuighufsjdhfuhegwghwufbubefquhgqghqenfuqhfuqhqgqueihfwuhgeuwbiuewgbwriughwuhf")
        hbox_2.Add(self.target_text,proportion=0, flag=wx.LEFT, border=2)
        hbox_2.Add(self.result_table,proportion=0, flag=wx.LEFT, border=2)

        self.regex_txt = wx.TextCtrl(self.pnl, wx.ID_ANY, style=wx.TE_MULTILINE, size=(1000,60))
        vbox_1.Add(self.regex_txt, proportion=0, flag=wx.TOP, border=2)
        vbox_1.Add(hbox_2, proportion=0, flag=wx.TOP, border=2)

        hbox_1.Add(vbox_mode, proportion=1, flag=wx.LEFT, border=2)
        hbox_1.Add(vbox_1, proportion=4, flag=wx.LEFT, border=2)

        self.search_button = wx.Button(self.pnl, -1, label="开始查找", size=(70, 50))
        self.reset_button = wx.Button(self.pnl, -1, label="重置", size=(70, 50))
        self.Bind(wx.EVT_BUTTON, self.start_search, self.search_button)
        hbox_button.Add(self.search_button, proportion=0, flag=wx.LEFT, border=400)
        hbox_button.Add(self.reset_button, proportion=0, flag=wx.LEFT, border=400)

        vbox.Add(hbox_1, proportion=4, flag=wx.TOP, border=10)
        vbox.Add(hbox_button, proportion=1, flag=wx.TOP, border=10)

        self.SetSizer(vbox)

    def start_search(self,event):
        regex:str = self.regex_txt.GetValue()
        target:str = self.target_text.GetValue()
        target = target[self.start:]
        if len(regex.strip())==0 or len(self.target_text.GetValue().strip())==0:
            msg = wx.MessageDialog(None, u'正则表达式，目标字符串不能为空！', u'警告', wx.OK)
            msg.ShowModal()
            return

        if self.checkbox_I.GetValue() and self.checkbox_M.GetValue():
            pattern = re.compile(regex,re.I|re.M)
        elif (not self.checkbox_I.GetValue()) and self.checkbox_M.GetValue():
            pattern = re.compile(regex,re.M)
        elif self.checkbox_I.GetValue() and (not self.checkbox_M.GetValue()):
            pattern = re.compile(regex,re.I)
        else:
            pattern = re.compile(regex)

        try:
            result = pattern.search(target)
            if result:
                start = result.start()+self.start
                end = result.end()+self.start
                self.target_text.SetStyle(start,end,wx.TextAttr("white","black"))
                for i in range(self.row_len):
                    try:
                        group = result.group(i)
                    except:
                        break
                    if group:
                        self.result_table.SetCellValue(i, 0, result.group(i))
                self.start += result.end()
            else:
                self.start = 0
                for i in range(self.row_len):
                    self.result_table.SetCellValue(i, 0, "")
                self.target_text.SetStyle(0,len(self.target_text.GetValue()),wx.TextAttr("black", "white"))
                msg = wx.MessageDialog(None, u'查找完毕！', u'提示', wx.OK)
                msg.ShowModal()
                return
        except Exception as e:
                msg = wx.MessageDialog(None, u'正则表达式填写有误，请重新填写！', u'警告', wx.OK)
                msg.ShowModal()
                return

    def show_value(self,event):
        result = self.result_table.GetCellValue(event.GetRow(),event.GetCol())
        self.assist_txt.SetValue(result)

    def OnQuit(self, e):
        self.Close()


if __name__ == '__main__':
    app = wx.App()
    RegexFrame(None, -1, '正则匹配工具')
    app.MainLoop()



