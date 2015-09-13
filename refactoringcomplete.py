#!/usr/bin/env python

import wx

class RefactoringExample(wx.Frame):
    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, 'Refactor Example',
                size=(340,200))
        panel = wx.Panel(self,-1)
        panel.SetBackgroundColour("White")
        self.Bind(wx.EVT_CLOSE, self.OnCloseWindow)
        self.createMenuBar()
        self.createButtonBar(panel)
        self.createTextFields(panel)

    def menuData(self):
        return (("&File",
                    ("&Open", "Open in status bar", self.OnOpen),
                    ("&Quit", "Quit", self.OnCloseWindow)),
                ("&Edit",
                    ("&Copy", "Copy", self.OnCopy),
                    ("C&ut", "Cut", self.OnCut),
                    ("&Paste", "Paste", self.OnPaste),
                    #?? Separator
                    ("", "", ""),
                    ("&Options...", "DisplayOptions", self.OnOptions)))

    #File and Edit
    def createMenuBar(self):
        menuBar = wx.MenuBar()
        #example of camel naming system, see local variable
        for eachMenuData in self.menuData():
            menuLabel = eachMenuData[0]
        #1: = 1 onwards
            menuItems = eachMenuData[1:]
            menuBar.Append(self.createMenu(menuItems), menuLabel)
        self.SetMenuBar(menuBar)

    #Open and Quit, Copy to Options
    def createMenu(self, menuData):
        menu = wx.Menu()
        for eachLabel, eachStatus, eachHandler in menuData:
            if not eachLabel:
                menu.AppendSeparator()
                continue
            menuItem = menu.Append(-1, eachLabel, eachStatus)
            self.Bind(wx.EVT_MENU, eachHandler, menuItem)
        return menu

    #See refactoringinprogress.py
    def buttonData(self):
        return (("FIRST", self.OnFirst),
                ("<<PREV", self.OnPrev),
                ("NEXT>>", self.OnNext),
                ("LAST", self.OnLast))

    def createButtonBar(self, panel, yPos=0):
        xPos = 0
        for eachLabel, eachHandler in self.buttonData():
            pos = (xPos, yPos)
            button = self.buildOneButton(panel, eachLabel, eachHandler,pos)
            xPos += button.GetSize().width

    def buildOneButton(self, parent, label, handler, pos=(0,0)):
        button = wx.Button(parent, -1, label, pos)
        self.Bind(wx.EVT_BUTTON, handler, button)
        return button

    def textFieldData(self):
        return (("First Name", (10,50)),
                ("Last Name", (10,80)))

    def createTextFields(self, panel):
        for eachLabel, eachPos in self.textFieldData():
            self.createCaptionedText(panel, eachLabel, eachPos)

    def createCaptionedText(self, panel, label, pos):
        static = wx.StaticText(panel, wx.NewId(), label, pos)
        static.SetBackgroundColour("White")
        textPos = (pos[0] + 75, pos[1])
        wx.TextCtrl(panel, wx.NewId(), "", size=(100, -1), pos=textPos)

    # Just grouping the empty event handlers together
    def OnPrev(self, event): pass
    def OnNext(self, event): pass
    def OnLast(self, event): pass
    def OnFirst(self, event): pass
    def OnOpen(self, event): pass
    def OnCopy(self, event): pass
    def OnCut(self, event): pass
    def OnPaste(self, event): pass
    def OnOptions(self, event): pass
    def OnCloseWindow(self, event):
        self.Destroy()

if __name__ == '__main__':
    app = wx.App(False)
    frame = RefactoringExample(parent=None, id=-1)
    frame.Show()
    app.MainLoop()
