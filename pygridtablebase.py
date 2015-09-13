#!/usr/bin/env python

import wx
import wx.grid

#This is a Model class, use to seperate data from the display
class LineupTable(wx.grid.PyGridTableBase):

    #?? How would you pull this data from an external source
    data = (("CF", "Bob", "Dernier"), ("2B", "Ryne", "Sandbery"),
            ("LF", "Gary", "Matthews"), ("1B", "Leon", "Durham"),
            ("RF", "Keith", "Moreland"), ("3B", "Ron", "Cey"),
            ("C", "Jody", "Davis"), ("SS", "Larry", "Bowa"),
            ("P", "Rick", "Sutcliffe"))

    #Reversed. Interesting
    colLabels = ("Last", "First")

    def __init__(self):
        wx.grid.PyGridTableBase.__init__(self)

    # 5 Required Methods for PyGrid..., along with two for the labels
    def GetNumberRows(self):
        return len(self.data)

    def GetNumberCols(self):
        return len(self.data[0]) - 1

    def GetColLabelValue(self, col):
        return self.colLabels[col]

    def GetRowLabelValue(self, row):
        return self.data[row] [0]

    def IsEmptyCell(self, row, col):
        return False

    def GetValue(self, row, col):
        return self.data[row] [col + 1]

    def SetValue(self, row, col, value):
        pass

class SimpleGrid(wx.grid.Grid):
    def __init__(self, parent):
        wx.grid.Grid.__init__(self, parent, -1)
        self.SetTable(LineupTable())

class TestFrame(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent, -1, "A Grid", size=(275, 275))
        grid = SimpleGrid(self)

if __name__ == '__main__':
    app = wx.App(False)
    frame = TestFrame(None)
    frame.Show(True)
    app.MainLoop()
