#!/usr/bin/env python
import wx
import wx.html
import cPickle
import os

from sketchwindow import SketchWindow
from controlpanel import ControlPanel


class SketchFrame(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent, -1, "Sketch Frame",
                    size = (800,600))
        self.filename = ""
        self.sketch = SketchWindow(self, -1)
        self.sketch.Bind(wx.EVT_MOTION, self.OnSketchMotion)
        self.initStatusBar()
        self.createMenuBar()
        self.createToolBar()
        self.createPanel()

    #Statusbar method
    def initStatusBar(self):
        self.statusbar = self.CreateStatusBar()
        self.statusbar.SetFieldsCount(3)
        self.statusbar.SetStatusWidths([-1, -2, -3])

    def OnSketchMotion(self, event):
        self.statusbar.SetStatusText("Pos: %s" % str(event.GetPositionTuple()))
        self.statusbar.SetStatusText("Current Pts: %s" % len(self.sketch.curLine), 1)
        self.statusbar.SetStatusText("Line Count: %s" % len(self.sketch.lines), 2)
        event.Skip()

    #Menus are length 2, items length 3 or 4
    def menuData(self):
        return [("&File", (
                    ("&New", "New Sketch file", self.OnNew),
                    ("&Open", "Open Sketch file", self.OnOpen),
                    ("&Save", "Save Sketch file", self.OnSave),
                    ("", "", ""),
                    ("&Color", (
                        ("&Black", "", self.OnColor, wx.ITEM_RADIO),
                        ("&Red", "", self.OnColor, wx.ITEM_RADIO),
                        ("&Green", "", self.OnColor, wx.ITEM_RADIO),
                        ("&Blue", "", self.OnColor, wx.ITEM_RADIO),
                        ("&Other...", "", self.OnOtherColor, wx.ITEM_RADIO))),
                    ("", "", "",),
                    ("About...", "Show about window", self.OnAbout),
                    ("&Quit", "Quit", self.OnCloseWindow)))]

    def createMenuBar(self):
        menuBar = wx.MenuBar()
        for eachMenuData in self.menuData():
            menuLabel = eachMenuData[0]
            menuItems = eachMenuData[1]
            menuBar.Append(self.createMenu(menuItems), menuLabel)
        self.SetMenuBar(menuBar)

    #if piece of data is length 2, meant to be a submenu.
    #break up and recursively call createMenu and append
    def createMenu(self, menuData):
        menu = wx.Menu()
        for eachItem in menuData:
            if len(eachItem) == 2:
                label = eachItem[0]
                subMenu = self.createMenu(eachItem[1])
                menu.AppendMenu(wx.NewId(), label, subMenu)
            else:
                self.createMenuItem(menu, *eachItem)
        return menu

    #??? huh
    def createMenuItem(self, menu, label, status, handler, kind=wx.ITEM_NORMAL):
        if not label:
            menu.AppendSeparator()
            return
        menuItem = menu.Append(-1, label, status, kind)
        self.Bind(wx.EVT_MENU, handler, menuItem)

    def createToolBar(self):
        toolbar = self.CreateToolBar()
        for each in self.toolbarData():
            self.createSimpleTool(toolbar, *each)
        toolbar.AddSeparator()
        for each in self.toolbarColorData():
            self.createColorTool(toolbar, each)
        toolbar.Realize()

    def createSimpleTool(self, toolbar, label, filename, help, handler):
        if not label:
            toolbar.AddSeparator()
            return
        bmp = wx.Image(filename, wx.BITMAP_TYPE_BMP).ConvertToBitmap()
        tool = toolbar.AddSimpleTool(-1, bmp, label, help)
        self.Bind(wx.EVT_MENU, handler, tool)

    def toolbarData(self):
        return (("New", "new.bmp", "Create new sketch", self.OnNew),
                ("", "", "", ""),
                ("Open", "open.bmp", "Open existing sketch", self.OnOpen),
                ("Save", "save.bmp", "Save existing sketch", self.OnSave))

    def createColorTool(self, toolbar, color):
        bmp = self.MakeBitmap(color)
        newId = wx.NewId()
        tool = toolbar.AddRadioTool(-1, bmp, shortHelp=color)
        self.Bind(wx.EVT_MENU, self.OnColor, tool)

    def MakeBitmap(self, color):
        bmp = wx.EmptyBitmap(16, 15)
        dc = wx.MemoryDC()
        dc.SelectObject(bmp)
        dc.SetBackground(wx.Brush(color))
        dc.Clear()
        dc.SelectObject(wx.NullBitmap)
        return bmp

    def toolbarColorData(self):
        return ("Black", "Red", "Green", "Blue")

    def SaveFile(self):
        if self.filename:
            data = self.sketch.GetLinesData()
            f = open(self.filename, 'w')
            cPickle.dump(data, f)
            f.close()

    def ReadFile(self):
        if self.filename:
            try:
                f = open(self.filename, 'r')
                data = cPickle.load(f)
                f.close()
                self.sketch.SetLinesData(data)
            except cPickle.UnpicklingError:
                wx.MessageBox("%s is not a sketch file." % self.filename,
                        "oops!", style=wx.OK|wx.ICON_EXCLAMATION)

    def OnNew(self, event): pass

    #limit the file selection to .x files
    wildcard = "Sketch files (*.sketch)|*.sketch|All files (*.*)|*.*"

    def OnOpen(self, event):
        #USE style = wx.MULTIPLE to allow selection of multiple files
        dlg = wx.FileDialog(self, "Open sketch files...",
                    os.getcwd(), style = wx.OPEN,
                    wildcard = self.wildcard)
        if dlg.ShowModal() == wx.ID_OK:
            self.filename = dlg.GetPath()
            self.ReadFile()
            self.SetTitle(self.title + ' -- ' + self.filename)
        dlg.Destroy()

    def OnSave(self, event):
        if not self.filename:
            self.OnSaveAs(event)
        else:
            self.SaveFile()

    def OnSaveAs(self, event):
        dlg = wx.FileDialog(self, "Save sketch as...",
                    os.getcwd(),
                    style=wx.SAVE | wx.OVERWRITE_PROMPT,
                    wildcard=self.wildcard)
        if dlg.ShowModal() == wx.ID_OK:
            filename = dlg.GetPath()
            if not os.path.splitext(filename) [1]:
                filename = filename + '.sketch'
            self.filename = filename
            self.SaveFile()
            self.SetTitle(self.title + ' -- ' + self.filename)
        dlg.Destroy()

    def OnColor(self, event):
        menubar = self.GetMenuBar()
        itemId = event.GetId()
        item = menubar.FindItemById(itemId)
        if not item:
            toolbar = self.GetToolBar()
            item = toolbar.FindById(itemId)
            color = item.GetShortHelp()
        else:
            color = item.GetLabel()
        self.sketch.SetColor(color)

    def OnOtherColor(self, event):
        dlg = wx.ColourDialog(self)
        dlg.GetColourData().SetChooseFull(True)
        if dlg.ShowModal() == wx.ID_OK:
            self.sketch.SetColor(dlg.GetColourData().GetColour())
        dlg.Destroy()

    #create the background panel that grids are added to
    def createPanel(self):
        controlPanel = ControlPanel(self, -1, self.sketch)
        box = wx.BoxSizer(wx.HORIZONTAL)
        # (object to be added, stretchfactor (+ve is relative), bitmask flag)
        # verticalbox (stretchfactor = vertical change, flag = horizontal change)
        # horizontalbox (stretchfactor = horizontal change, flag = vertical change)
        # EXPAND = totally fill available space
        # controlPanel = no horizontal change, expand to fill vertical
        box.Add(controlPanel, 0, wx.EXPAND)
        box.Add(self.sketch, 1, wx.EXPAND)
        self.SetSizer(box)

    def OnCloseWindow(self, event):
        self.Destroy()

    def OnAbout(self, event):
        dlg = SketchAbout(self)
        dlg.ShowModal()
        dlg.Destroy()

class SketchAbout(wx.Dialog):
    text = '''
<html>
<body bgcolor="#ACAA60">
<center><table bgcolor="#455481" width="100%" cellspacing="0"
cellpadding="0" border="1">
<tr>
<td align="center"><h1>Sketch!</h1></td>
</tr>
</table>
</center>
<p><b>Sketch</b> is a demonstration program for <b>wxPython In Action</b>
Chapter 7.  It is based on the SuperDoodle demo included with wxPython,
available at http://www.wxpython.org/
</p>

<p><b>SuperDoodle</b> and <b>wxPython</b> are brought to you by
<b>Robin Dunn</b> and <b>Total Control Software</b>, Copyright
&copy; 1997-2006.</p>
</body>
</html>
'''

    def __init__(self, parent):
        wx.Dialog.__init__(self, parent, -1, 'About Sketch',
                          size=(440, 400) )

        html = wx.html.HtmlWindow(self)
        html.SetPage(self.text)
        button = wx.Button(self, wx.ID_OK, "Okay")

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(html, 1, wx.EXPAND|wx.ALL, 5)
        sizer.Add(button, 0, wx.ALIGN_CENTER|wx.ALL, 5)

        self.SetSizer(sizer)
        self.Layout()

#a rewrite to involve the splashscreen, as declared in the OnInit during startup
class SketchApp(wx.App):

    def OnInit(self):
        image = wx.Image("splash.png", wx.BITMAP_TYPE_PNG)
        png = image.ConvertToBitmap()
        wx.SplashScreen(png, wx.SPLASH_CENTRE_ON_SCREEN | wx.SPLASH_TIMEOUT, 1200,
                    None, -1)
        wx.Yield()

        #(None) and (True) when you have sub classes to the frame
        frame = SketchFrame(None)
        frame.Show(True)
        self.SetTopWindow(frame)
        return True

if __name__ == '__main__':
    #?? why still false when not calling wx.App(False) any longer
    app = SketchApp(False)
    app.MainLoop()
