#To do anything inside the frame, need to lay a panel over it
#This panel can be customised and added to without messing with background code
#Also first button :)

#REMEMBER axis are flipped. Across and Down | Starting from the top left

#!/usr/bin/env python

import wx
#Using the equivalent of PySimpleApp rather than write an App subclass

class PanelButton(wx.Frame):

    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, 'Frame with Panel and Button',
                size=(400,100))
        #creating first panel
        #as a single child window it is automatically resized
        panel = wx.Panel(self)
        #adding first button, this size makes rectangle, and pos approx middle
        button = wx.Button(panel, label="Close", pos=(150,20),
                size=(40,30))
        #more binding
        self.Bind(wx.EVT_BUTTON, self.OnCloseMe, button)
        self.Bind(wx.EVT_CLOSE, self.OnCloseWindow)

    #is (self, event) the standard for bound events?
    def OnCloseMe(self, event):
        self.Close(True)

    def OnCloseWindow(self, event):
        self.Destroy()

if __name__ == '__main__':
    #wx.PySimpleApp() is now depreciated
    #Replaced with wx.App(False)
    app = wx.App(False)
    frame = PanelButton(parent=None, id=-1)
    frame.Show()
    app.MainLoop()
