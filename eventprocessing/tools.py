# coding=utf-8


import wx

# 创建应用程序对象
app = wx.App()
#创建窗口对象
frm = wx.Frame(None,title="NATS",size=(400,300),pos=(100,100))

frm.Show()

app.MainLoop()


