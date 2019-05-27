# coding=utf-8


import wx

# 自定义窗口类MyFrame
class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(parent=None,title="静态图片控件",size=(300,300))
        self.bmps = [wx.Bitmap('icon/bird5.gif',wx.BITMAP_TYPE_GIF),
                     wx.Bitmap('icon/bird4.gif',wx.BITMAP_TYPE_GIF),
                     wx.Bitmap('icon/bird3.gif',wx.BITMAP_TYPE_GIF)]
        self.Centre()
        self.panel = wx.Panel(parent=self)
        #创建垂直方向的Box布局管理器
        vbox = wx.BoxSizer(wx.VERTICAL)

        #vbox.Add(self.statictext,proportion=2,flag=wx.FIXED_MINSIZE | wx.TOP | wx.CENTER,border=10)
        b1 = wx.Button(parent=self.panel,id=1,label="Button1")
        #self.Bind(wx.EVT_BUTTON,self.on_click,b1)
        b2 = wx.Button(self.panel, id=2,label="Button2")
        self.Bind(wx.EVT_BUTTON, self.on_click, id=1,id2=2)

        self.image = wx.StaticBitmap(self.panel,-1,self.bmps[0])

        #添加静态文本和按钮到布局管理器中

        vbox.Add(b1, proportion=1, flag=wx.CENTER | wx.EXPAND)
        vbox.Add(b2, proportion=1, flag=wx.CENTER | wx.EXPAND)
        vbox.Add(self.image, proportion=3, flag=wx.CENTER)

        self.panel.SetSizer(vbox)

    def on_click(self,event):
        event_id = event.GetId()
        if event_id == 1:
            self.image.SetBitmap(self.bmps[1])
        else:
            self.image.SetBitmap(self.bmps[2])
            self.panel.Layout

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


