# coding=utf-8


import wx

# 自定义窗口类MyFrame
class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(parent=None,title="一对一事件处理",size=(400,300),pos=(100,100))
        self.Center()
        panel = wx.Panel(parent=self)
        self.statictext = wx.StaticText(parent=panel,pos=(110,20))
        b = wx.Button(parent = panel,label = "OK",pos = (100,50))
        self.Bind(wx.EVT_BUTTON,self.on_click,b)
    def on_click(self,event):
        print(type(event))
        self.statictext.SetLabelText('Hello world')
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


