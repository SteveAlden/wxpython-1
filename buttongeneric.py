#!/usr/bin/env python

import wx
import wx.lib.buttons as buttons

class GenericButtonFrame(wx.Frame):

    def __init__(self):
        wx.Frame.__init__(self, None, -1, 'Generic Button Example',
                size = (500,400))
        panel = wx.Panel(self, -1)

        #Can also have rows=x. Can cause errors if set wrongly
        #Don't need the n = ... part, but helped for troubleshooting
        sizer = wx.FlexGridSizer(cols=3, vgap=20, hgap=20)
        b = wx.Button(panel, -1, "A wx.Button")
        b.SetDefault()
        sizer.Add(b)

        #Interesting, can reuse b, now that it is saved to sizer
        b = wx.Button(panel, -1, "non-default wx.Button")
        sizer.Add(b)

        sizer.Add((10,10))

        b = buttons.GenButton(panel, -1, 'Generic Button')
        sizer.Add(b)

        b = buttons.GenButton(panel, -1, 'disabled Generic')
        b.Enable(False)
        sizer.Add(b)

        b = buttons.GenButton(panel, -1, 'bigger')
        b.SetFont(wx.Font(20, wx.SWISS, wx.NORMAL, wx.BOLD, False))
        b.SetBezelWidth(5)
        #?? Does capitalisation matter
        b.SetBackgroundColour("Navy")
        b.SetForegroundColour("white")
        b.SetToolTipString("This is a BIG button...")
        sizer.Add(b)

        bmp = wx.Image("bitmap.bmp", wx.BITMAP_TYPE_BMP).ConvertToBitmap()
        b = buttons.GenBitmapButton(panel, -1, bmp)
        sizer.Add(b)

        b = buttons.GenBitmapToggleButton(panel, -1, bmp)
        sizer.Add(b)

        b = buttons.GenBitmapTextButton(panel, -1, bmp,
            "Bitmapped Text", size=(175,175))
        #?? What do again
        b.SetUseFocusIndicator(False)
        sizer.Add(b)

        b = buttons.GenToggleButton (panel, -1, "ToggleButton")
        sizer.Add(b)

        panel.SetSizer(sizer)

if __name__ == '__main__':
    app = wx.App(False)
    frame = GenericButtonFrame()
    frame.Show()
    app.MainLoop()
