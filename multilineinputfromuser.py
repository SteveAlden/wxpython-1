#!/usr/bin/env python

import wx

class TextFrame(wx.Frame):

    def __init__(self):
        wx.Frame.__init__(self, None, -1, 'Text Entry Example',
                    size=(300,250))
        panel = wx.Panel(self, -1)

        multiLabel = wx.StaticText(panel, -1, "Multi-line")
        multiText = wx.TextCtrl(panel, -1,
                    "Here is a looooooooooooong line "
                    "of text set in the control.\n\n"
                    "See that it wrapped, and that "
                    "this line is after the blank",
                    size=(200,100), style=wx.TE_MULTILINE)
        multiText.SetInsertionPoint(0)

        richLabel = wx.StaticText(panel, -1, "Rich Text")
        richText = wx.TextCtrl(panel, -1,
                "If supported by the native control, "
                "this is reversed, and this is in a different font.",
                size=(200,100), style=wx.TE_MULTILINE|wx.TE_RICH2)
        richText.SetInsertionPoint(0)

        #Setting text styles, based on locations (characters + spaces)
        #(start, end, style)
        richText.SetStyle(44, 52, wx.TextAttr("white", "black"))

        #Creating a font, points can be used to +/- the size
        points = richText.GetFont().GetPointSize()
        f = wx.Font(points + 8, wx.ROMAN, wx.ITALIC, wx.BOLD, True)

        #Setting a style in the new font
        #(col of text, col of background, font)
        richText.SetStyle(68, 82, wx.TextAttr("blue",
                wx.NullColour, f))

        sizer = wx.FlexGridSizer(cols=2, hgap=6, vgap=6)
        sizer.AddMany([multiLabel, multiText, richLabel, richText])
        panel.SetSizer(sizer)

        e = wx.FontEnumerator()
        e.EnumerateFacenames()
        fontList = e.GetFacenames()

        for font in fontList:
            print font + "\n"

if __name__ == '__main__':
    app = wx.App(False)
    frame = TextFrame()
    frame.Show()
    app.MainLoop()
