#!/usr/bin/env python

#size=GetDefaultSize() , useful for consistency across frames

import wx

class ButtonFrame(wx.Frame):

    def __init__(self):
        wx.Frame.__init__(self, None, -1, 'ButtonExample', size=(300,100))
        panel = wx.Panel(self, -1)
        self.button = wx.Button(panel, -1, "Hello", pos=(50, 20))
        self.Bind(wx.EVT_BUTTON, self.OnClick, self.button)
        #set default for the dialog or frame, may be drawn differently
        #can be 'clicked' by pressing enter
        self.button.SetDefault()

    def OnClick(self, event):
        self.button.SetLabel("Clicked")

if __name__ == '__main__':
    app = wx.App(False)
    frame = ButtonFrame()
    frame.Show()
    app.MainLoop()
