# coding=utf-8


import wx

# 自定义窗口类MyFrame
class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(parent=None,title="StaticBox布局",size=(300,180))
        self.Center()
        panel = wx.Panel(parent=self)
        vbox = wx.BoxSizer(wx.VERTICAL)
        self.statictext = wx.StaticText(parent=panel,label='单击')
        vbox.Add(self.statictext,proportion=2,flag=wx.FIXED_MINSIZE | wx.TOP | wx.CENTER,border=10)
        b1 = wx.Button(parent=panel,id=10,label="Button1")
        b2 = wx.Button(parent=panel, id=11, label="Button2")
        self.Bind(wx.EVT_BUTTON, self.on_click, id=10,id2=20)

        sb = wx.StaticBox(panel,label="按键框")
        hsbox = wx.StaticBoxSizer(sb,wx.HORIZONTAL)
        hsbox.Add(b1,0,wx.BI_EXPAND | wx.BOTTOM,5)
        hsbox.Add(b2, 0, wx.BI_EXPAND | wx.BOTTOM, 5)
        vbox.Add(hsbox,proportion=1,flag=wx.CENTER)
        panel.SetSizer(vbox)
    def on_click(self,event):
        event_id = event.GetId()
        print(type(event_id))
        if event_id == 10:
            self.statictext.SetLabelText('Button1 单击')
        else:
            self.statictext.SetLabelText('Button2 单击')

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


