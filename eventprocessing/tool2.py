# coding=utf-8


import wx

# 自定义窗口类MyFrame
class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(parent=None,title="第一个GUI程序",size=(400,300),pos=(100,100))
        self.Center()
        panel = wx.Panel(parent=self)
        statictext = wx.StaticText(parent=panel,label="Hello World!",pos=(10,10))
class App(wx.App):

    def OnInit(self):
        frame = MyFrame()
        frame.Show()
        return True

    def OnExit(self):
        print('应用程序退出')
        return 0


if __name__ == '__main__':
    app = App()
    app.MainLoop()

app.MainLoop()


