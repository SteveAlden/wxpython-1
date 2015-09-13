#Building on basicprogram.py
#Shebang line. It's polite.

#!/usr/bin/env python

#Docstring
"""Minimal.py is a starting pint for a wxPython program."""

import wx

#Subclass the wxPython frame class
class Frame(wx.Frame):
    pass

class App(wx.App):

    def OnInit(self):
        self.frame = Frame(parent=None, title='Minimal')
        self.frame.Show()
        #Optional method, as in this case it is set automatically
        self.SetTopWindow(self.frame)
        return True

#Python Idiom - allowing program to run if its being executed
# if imported, script would keep its name. If executed, renamed to '__main__'
if __name__ == '__main__':
    app = App()
    app.MainLoop()
