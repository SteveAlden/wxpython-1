import wx

#Can have App or Frame subclasses in any order
class MyApp(wx.App):

    def OnInit(self):
        #Providing title, pos, size arguments for the custom frame initiation
        frame = MyFrame("Hello World", (50,60), (450,340))
        frame.Show()
        self.SetTopWindow(frame)
        return True

class MyFrame(wx.Frame):

    #?? self
    #Calling with arguments that the custom frame requires
    def __init__(self, title, pos, size):
        #Assume allows more customation than the default initiation
        #Arguments passed in the App subclass
        wx.Frame.__init__(self, None, -1, title, pos, size)
        #Declaring and adding the contents of a menu, before adding to menuBar
        menuFile = wx.Menu()
        # & allows you to access with ALT + Key
        #Setting the id to 1 for binding later
        menuFile.Append(1, "&About...")
        menuFile.AppendSeparator()
        #Setting the id to 2 for binding later
        menuFile.Append(2, "E&xit")
        #Creating menuBar
        menuBar = wx.MenuBar()
        #Adding the already created menu to the menuBar under File
        menuBar.Append(menuFile, "&File")
        self.SetMenuBar(menuBar)
        #This is so cool :)
        self.CreateStatusBar()
        self.SetStatusText("Welcome to wxPython!")
        #First binding of events to buttons :)
        #(Type of Event, action (in this case call function), binding target)
        self.Bind(wx.EVT_MENU, self.OnAbout, id=1)
        self.Bind(wx.EVT_MENU, self.OnQuit, id=2)

    def OnQuit(self, event):
        self.Close()

    def OnAbout(self, event):
        wx.MessageBox("This is a wxPython Hello World sample.",
                "About Hello World", wx.OK | wx.ICON_INFORMATION, self)

if __name__ == '__main__':
    #?? why False
    app = MyApp(False)
    app.MainLoop()
