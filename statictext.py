import wx

#research wx.lib.stattext.GenStaticText class
# more consistent across platform and recieves mouse events ...
# ... could bind to status bar, display what to do next

class StaticTextFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1, 'Static Text Example',
                size=(400,300))
        panel = wx.Panel(self, -1)

        # x = ... (PLAY WITH RED AND WHITE HERE)
        wx.StaticText(panel, -1, "This is an example of static text",
                (100,10))

        rev = wx.StaticText(panel, -1, "Static Text with Reversed Colours",
                (100,30))
        rev.SetForegroundColour('white')
        rev.SetBackgroundColour('red')

        #when doing center or right aligned text ...
        # explicitly set the size of the control in the constructor
        center = wx.StaticText(panel, -1, "align center", (100, 50),
                (160, -1), wx.ALIGN_CENTER)
        center.SetForegroundColour('white')
        center.SetBackgroundColour('black')

        right = wx.StaticText(panel, -1, "align right", (100, 70),
                (160, -1), wx.ALIGN_RIGHT)
        right.SetForegroundColour('white')
        right.SetBackgroundColour('black')

        #?? Could use native font, using - FontFromNativeInfo

        '''Options for font : (+- on Win10)
            +wx.FONTFAMILY_DEFAULT
            -wx.FONTFAMILY_DECORATIVE  A decorative font.
            +wx.FONTFAMILY_ROMAN 	A formal, serif font.
            -wx.FONTFAMILY_SCRIPT 	A handwriting font.
            -wx.FONTFAMILY_SWISS 	A sans-serif font.
            +wx.FONTFAMILY_MODERN 	Usually a fixed pitch font.
            -wx.FONTFAMILY_TELETYPE 	A teletype font.'''

        str = "You can also change the font."
        text = wx.StaticText(panel, -1, str, (20,100))
        font = wx.Font(18, wx.FONTFAMILY_ROMAN, wx.ITALIC, wx.NORMAL)
        text.SetFont(font)

        wx.StaticText(panel, -1,
                "Your text\ncan be split\n"
                "over multiple lines\n\neven blank ones", (20, 150))

        wx.StaticText(panel, -1,
                "Multi-line text\ncan also\n"
                "be right aligned\n\neven with a blank.", (220, 150),
                style=wx.ALIGN_RIGHT)

if __name__ == '__main__':
    app = wx.App(False)
    frame = StaticTextFrame()
    frame.Show()
    app.MainLoop()
