#Box sizer code


self.createPanel()

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


    #using a veritcal box sizer
    #dont need to specify
    #4th arg is border width around item
    #wx.ALL - one of the flags to govern which sides to apply the borders
def layout(self, colorGrid, thicknessGrid):
    box = wx.BoxSizer(wx.VERTICAL)
    box.Add(colorGrid, 0, wx.ALL, self.SPACING)
    box.Add(thicknessGrid, 0, wx.ALL, self.SPACING)
    self.SetSizer(box)
    #Fit - resize to fit the minimum size needed by the sizer
    box.Fit(self)

#Add(size, proportion=0, flag=0, border=0, userData=None)
#Adds exmpty space to be used as a separator

#Layout() forces sizer to recalculate, call post dynamically adding or removing
# .... children
