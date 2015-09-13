#!/usr/bin/env python

#3 subclasses in total = the wx.Frame subclass
#2 subclasses with the simplest grid
#ALTERNATIVE is using a custom data class - see pages 135 to 139

import wx
import wx.grid
import generictable

data = (("Bob", "Dernier"), ("Ryne", "Sandberg"),
        ("Gary", "Matthews"), ("Leon", "Durham"),
        ("Keith", "Moreland"), ("Ron", "Cey"),
        ("Jody", "Davis"), ("Larry", "Bowa"),
        ("Rick", "Sutcliffe"))
#Reverse
colLabels = ("Last", "First")
#Right Order
rowLabels=("CF", "2B", "LF", "1B", "RF", "3B", "C", "SS", "F")

class SimpleGrid(wx.grid.Grid):
    def __init__(self, parent):
        wx.grid.Grid.__init__(self, parent, -1)
        #THE IMPORTANT LINE
        tableBase = generictable.GenericTable(data, rowLabels, colLabels)
        self.SetTable(tableBase)

class TestFrame(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent, -1, "A Grid", size=(275, 275))
        grid = SimpleGrid(self)

if __name__ == '__main__':
    app = wx.App(False)
    #?? Because of the grid and pulling in the other subclasses
    frame = TestFrame(None)
    frame.Show(True)
    app.MainLoop()
