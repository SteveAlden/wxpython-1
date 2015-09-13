#!/usr/bin/env python

import wx
from wx.py.shell import ShellFrame
from wx.py.filling import FillingFrame

import images

class ToolbarFrame(wx.Frame):

    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, 'Toolbars',
                size=(300,200))
        panel = wx.Panel(self,-1)
        panel.SetBackgroundColour('White')

        statusBar = self.CreateStatusBar()
        toolbar = self.CreateToolBar()
        #?? Are these standardised for use. If so how use.
        toolbar.AddSimpleTool(wx.NewId(), images.getNewBitmap(),
                "New", "Long help for 'New'")
        #Mostly UK spelling, this is one US one
        toolbar.Realize()

        #This is a fake menu, it contains nothing but the title on the menubar
        menuBar = wx.MenuBar()
        menu1 = wx.Menu()
        menuBar.Append(menu1, "&File")
        #This is a filled out menu
        menu2 = wx.Menu()
        menu2.Append(wx.NewId(), "&Copy", "Copy in Status Bar")
        menu2.Append(wx.NewId(), "C&ut", "Don't run with scissors")
        menu2.Append(wx.NewId(), "Paste", "No Alt option for this one")
        #i can't spell separator
        menu2.AppendSeparator()
        menu2.Append(wx.NewId(), "&Options...", "Display Options")
        menuBar.Append(menu2, "&Edit")
        #There should normally be a load of bindings here for the menu items

        #new debug menu
        menu3 = wx.Menu()
        shell = menu3.Append(-1, "&wxPython shell", "Open wxPython shell frame")
        filling = menu3.Append(-1, "&Namespace viewer",
                "Open Namespace Viewer frame")
        menuBar.Append(menu3, "&Debug")
        #bindings have missed from previous menus
        self.Bind(wx.EVT_MENU, self.OnShell, shell)
        self.Bind(wx.EVT_MENU, self.OnFilling, filling)

        #Finished the menubar
        self.SetMenuBar(menuBar)

    def OnCloseMe(self, event):
        self.Close(True)

    #?? Difference between close and destroy?
    def OnCloseWindow(self,event):
        self.Destroy()

    def OnShell(self, event):
        frame = ShellFrame(parent=self)
        frame.Show()

    def OnFilling(self, event):
        frame = FillingFrame(parent=self)
        frame.Show()

if __name__ == '__main__':
    app = wx.App(False)
    app.frame = ToolbarFrame(parent=None, id=-1)
    app.frame.Show()
    app.MainLoop()
