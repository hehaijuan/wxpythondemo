# coding=utf-8


import wx

# 自定义窗口类MyFrame
class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(parent=None,title="鼠标事件处理",size=(300,180))
        self.Center()
        panel = wx.Panel(parent=self)
        self.Bind(wx.EVT_LEFT_DOWN,self.on_left_down)
        self.Bind(wx.EVT_LEFT_UP, self.on_left_up)
        self.Bind(wx.EVT_MOTION, self.on_mouse_move)
    def on_left_down(self,evt):
        print('鼠标按下')
    def on_left_up(self,evt):
        print('鼠标释放')
    def on_mouse_move(self,event):
        if event.Dragging() and event.LeftIsDown():
            pos = event.GetPosition()
            print(pos)


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


