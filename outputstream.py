#Print statement order shows the app cycle

#!/usr/bin/env python

import wx
import sys

class Frame(wx.Frame):

    def __init__(self, parent, id, title):
    #THIRD
        print "Frame __init__"
        wx.Frame.__init__(self, parent, id, title)

class App(wx.App):

    #Default setting for the redirect, is set here
    def __init__(self, redirect=True, filename=None):
    #FIRST
        print "App __init__"
        wx.App.__init__(self, redirect, filename)

    #SECOND
    def OnInit(self):
        print "OnInit"
        self.frame = Frame(parent=None, id=-1, title='Startup')
        self.frame.Show()
        self.SetTopWindow(self.frame)
    #FOURTH
        print >> sys.stderr, "A pretend error message."
        return True

    def OnExit(self):
    #SIXTH
        print "End of log. Date is..."
        print "OnExit"

if __name__ == '__main__':
    #Set redirect to false to get all the output to the console
    #Set to (True, "output") will send to a file named output
    #How to do error logs
    app = App(True, "logs")
    #FIFTH
    print "Before the MainLoop"
    app.MainLoop()
    #SEVENTH
    print "After the MainLoop"
