#5 steps for every program

#1. import the necessary wxPython package
import wx

#2. Subclass the wxPython application class
class App(wx.App):

#3. Define an application initiation method
    def OnInit(self):
        frame = wx.Frame(parent=None, title='Bare')
        frame.Show()
        return True

#4. Create an application class instance
app = App()

#5. Enter the applications main event loop
app.MainLoop()
