# coding=utf-8


import wx

# 自定义窗口类MyFrame
class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(parent=None,title="静态文本和按钮",size=(300,180))
        self.Centre()
        panel = wx.Panel(parent=self)
        vbox = wx.BoxSizer(wx.VERTICAL)
        self.statictext = wx.StaticText(parent=panel,label='StaticText1',style=wx.ALIGN_CENTER_HORIZONTAL)
        #vbox.Add(self.statictext,proportion=2,flag=wx.FIXED_MINSIZE | wx.TOP | wx.CENTER,border=10)
        b1 = wx.Button(parent=panel,label="OK")
        self.Bind(wx.EVT_BUTTON,self.on_click,b1)
        b2 = wx.ToggleButton(panel, -1, "ToggleButton")
        self.Bind(wx.EVT_BUTTON, self.on_click, b2)
        bmp = wx.Bitmap('icon/1.gif',wx.BITMAP_TYPE_GIF)
        b3 = wx.BitmapButton(panel,-1,bmp)
        self.Bind(wx.EVT_BUTTON,self.on_click,b3)

        #添加静态文本和按钮到布局管理器中
        vbox.Add(100,10,proportion=1,flag=wx.CENTER | wx.FIXED_MINSIZE)
        vbox.Add(self.statictext, proportion=1, flag=wx.CENTER | wx.FIXED_MINSIZE)
        vbox.Add(b1, proportion=1, flag=wx.CENTER | wx.EXPAND)
        vbox.Add(b2, proportion=1, flag=wx.CENTER | wx.EXPAND)
        vbox.Add(b3, proportion=1, flag=wx.CENTER | wx.EXPAND)

        panel.SetSizer(vbox)

    def on_click(self,event):
        self.statictext.SetLabelText('Hello,world.')

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


