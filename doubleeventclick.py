#!/usr/bin/env python

import wx

class DoubleEventFrame(wx.Frame):

    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, 'Frame with Button',
                size=(300,100))
        self.panel = wx.Panel(self, -1)
        self.button = wx.Button(self.panel, -1, "Click Me", pos=(100,15))
        #bind button click
        self.Bind(wx.EVT_BUTTON, self.OnButtonClick, self.button)
        #bind left button down event
        self.button.Bind(wx.EVT_LEFT_DOWN, self.OnMouseDown)

    def OnButtonClick(self, event):
        self.panel.SetBackgroundColour('Green')
        self.Refresh()

    def OnMouseDown(self, event):
        self.button.SetLabel("Again!")
        event.Skip()

if __name__ == '__main__':
    app = wx.App(False)
    frame = DoubleEventFrame(parent=None, id=-1)
    frame.Show()
    app.MainLoop()
