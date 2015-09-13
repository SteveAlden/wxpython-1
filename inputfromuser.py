import wx

#Validator argument can be used with TextCtrl to filter the input
#EVT_TEXT_MAXLEN - specify using SetMaxLength(), display a warning message when hit

class TextFrame(wx.Frame):

    def __init__(self):
        wx.Frame.__init__(self, None, -1, 'Text Entry Example', size=(500,300))
        panel = wx.Panel(self, -1)

        #Pairs of Label and Text
        basicLabel = wx.StaticText(panel, -1, "Basic Control:")
        basicText = wx.TextCtrl(panel, -1, "I've entered some text!",
                    size=(300,100))
        basicText.SetInsertionPoint(0)

        #TE_PASSWORD - masked
        pwdLabel = wx.StaticText(panel, -1, "Password:")
        pwdText = wx.TextCtrl(panel, -1, "password", size=(175, -1),
                    style=wx.TE_PASSWORD)

        sizer = wx.FlexGridSizer(cols=2, hgap=6, vgap=6)
        #Interesting. Adding multiple at once.
        #?? Available with other grids
        sizer.AddMany([basicLabel, basicText, pwdLabel, pwdText])
        panel.SetSizer(sizer)

if __name__ == '__main__':
    app = wx.App(False)
    frame = TextFrame()
    frame.Show()
    app.MainLoop()
