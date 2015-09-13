#!/usr/bin/env python

import wx

class MouseEventFrame(wx.Frame):

    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, 'Emotional Button',
                size=(300,100))
        #EVT Handling procedure being explored below
        #Looking for the bound handler function...
        #...Goes from triggering object up the container hierarchy
        #Only instances of wx.CommandEvent propogate
        self.panel = wx.Panel(self)
        #Bind to panel
        self.button = wx.Button(self.panel, label="Hello!", pos=(100,15))
        #Bind to frame
        self.Bind(wx.EVT_BUTTON, self.OnButtonClick, self.button)
        #Bind to button
        #Mouse events are not subclasses of wx.CommandEvent,
        #...do not propogate up and not function or will affect whole frame
        self.button.Bind(wx.EVT_ENTER_WINDOW, self.OnEnterWindow)
        self.button.Bind(wx.EVT_LEAVE_WINDOW, self.OnLeaveWindow)

    def OnButtonClick(self, event):
        if self.panel.BackgroundColour != 'Red':
            self.panel.SetBackgroundColour('Red')
            self.panel.Refresh()
        else:
            self.panel.SetBackgroundColour('White')
            self.panel.Refresh()

    def OnEnterWindow(self, event):
        self.button.SetLabel("WHOOP!")
        #calling Skip requests further processing
        #invoking the default functionality not contained within the button
        event.Skip()

    def OnLeaveWindow(self, event):
        if self.panel.BackgroundColour != 'Red':
            self.button.SetLabel(":'(")
        if self.panel.BackgroundColour == 'Red':
            self.button.SetLabel(":D")
        event.Skip()

if __name__ == '__main__':
    app = wx.App(False)
    frame = MouseEventFrame(parent=None, id=-1)
    frame.Show()
    app.MainLoop()
