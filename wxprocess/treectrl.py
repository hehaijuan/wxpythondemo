# coding=utf-8


import wx

# 自定义窗口类MyFrame
class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(parent=None,title="树控件",size=(500,400))
        self.Centre()
        #self.panel = wx.Panel(parent=self)
        #创建垂直方向的Box布局管理器
        #vbox = wx.BoxSizer(wx.VERTICAL)

        splitter = wx.SplitterWindow(self)
        leftpanel = wx.Panel(splitter)
        rightpanel = wx.Panel(splitter)
        splitter.SplitVertically(leftpanel,rightpanel,200)
        splitter.SetMinimumPaneSize(80)

        self.tree = self.CreateTreeCtrl(leftpanel)
        self.Bind(wx.EVT_TREE_SEL_CHANGED,self.on_click,self.tree)
        vbox1 = wx.BoxSizer(wx.VERTICAL)
        vbox1.Add(self.tree, 1, flag=wx.ALL | wx.EXPAND, border=5)
        leftpanel.SetSizer(vbox1)

        vbox2 = wx.BoxSizer(wx.VERTICAL)
        self.content = wx.StaticText(rightpanel,label='右侧面板')
        vbox2.Add(self.content,flag=wx.ALL | wx.EXPAND,border=5)
        rightpanel.SetSizer(vbox2)

    def on_click(self,event):
        item = event.GetItem()
        self.content.SetLabel(self.tree.GetItemText(item))
    def CreateTreeCtrl(self,parent):
        tree = wx.TreeCtrl(parent)

        items = []

        imglist = wx.ImageList(16,16,True,2)
        imglist.Add(wx.ArtProvider.GetBitmap(wx.ART_FOLDER,size=wx.Size(16,16)))
        imglist.Add(wx.ArtProvider.GetBitmap(wx.ART_NORMAL_FILE,size=wx.Size(16,16)))

        tree.AssignImageList(imglist)

        root = tree.AddRoot("TreeRoot",image=0)


        items.append(tree.AppendItem(root, "Item 1", 0))

        items.append(tree.AppendItem(root, "Item 2", 0))
        items.append(tree.AppendItem(root, "Item 3", 0))
        items.append(tree.AppendItem(root, "Item 4", 0))
        items.append(tree.AppendItem(root, "Item 5", 0))

        for ii in range(len(items)):
            id = items[ii]
            tree.AppendItem(id, "Subitem1", 1)
            tree.AppendItem(id, "Subitem2", 1)
            tree.AppendItem(id, "Subitem3", 1)
            tree.AppendItem(id, "Subitem4", 1)
            tree.AppendItem(id, "Subitem5", 1)
        tree.Expand(root)
        tree.Expand(items[0])
        tree.Expand(items[3])
        tree.SelectItem(root)

        return tree


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


