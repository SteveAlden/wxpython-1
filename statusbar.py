#!/usr/bin/env python

# Use PopStatusText(field=0) and PushStatusText(text, field=0)
# ... allow you to return to the previous status, after temporarily displaying new text

        #Statusbar method
        '''def initStatusBar(self):
            self.statusbar = self.CreateStatusBar()
            self.statusbar.SetFieldsCount(3)
            self.statusbar.SetStatusWidths([-1, -2, -3])'''

import wx
from sketchwindow import SketchWindow

class SketchFrame(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent, -1, "Sketch Frame",
                    size = (800,600))
        self.sketch = SketchWindow(self, -1)
        self.sketch.Bind(wx.EVT_MOTION, self.OnSketchMotion)
        self.statusbar = self.CreateStatusBar()
        self.statusbar.SetFieldsCount(3)
        #-n is a relative size, positive n is an absolute
        #-n will resize with the application
        self.statusbar.SetStatusWidths([-1, -2, -3])


    def OnSketchMotion(self, event):
        #nice string conversion
        self.statusbar.SetStatusText("Pos: %s" % str(event.GetPositionTuple()))
        self.statusbar.SetStatusText("Current Pts: %s" % len(self.sketch.curLine), 1)
        self.statusbar.SetStatusText("Line Count: %s" % len(self.sketch.lines), 2)
        #so that the line will actually be drawn
        event.Skip()

if __name__ == '__main__':
    app = wx.App(False)
    frame = SketchFrame(None)
    frame.Show(True)
    app.MainLoop()
