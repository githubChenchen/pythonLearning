import tkinter
top=tkinter.Tk()
label1=tkinter.Label(top,text='hello world')
label1.pack()#进行简单布局
top.geometry('400x300+150+200')#窗口布局，长400，宽300，距离屏幕左侧150，上方200
top.mainloop()#主事件循环

