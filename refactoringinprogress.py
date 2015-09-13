#FIRST TRY - Extracting the button code into its own method (function)

def createButtonBar(self):
    firstButton = wx.Button(panel, -1, "FIRST")
    self.Bind(wx.EVT_BUTTON, self.OnFirst, firstButton)
    prevButton = wx.Button(panel, -1, "<< PREV", pos=(80,0))
    self.Bind(wx.EVT_BUTTON, self.OnPrev, prevButton)
    nextButton = wx.Button(panel, -1, "NEXT>>", pos=(160,0))
    self.Bind(wx.EVT_BUTTON, self.OnNext, nextButton)
    lastButton = wx.Button(panel, -1, "LAST", pos=(240,0))
    self.Bind(wx.EVT_BUTTON, self.OnLast, lastButton)

#----------------------------------------------------------------------

#SECOND TRY -locate the commonality. Factor out that portion into a generic
# method and call repeatedly

#?? how do we know to need (self, panel)
# CALLS FUNCTION, PASSES VALUES, WAITS FOR RETURN
def createButtonBar(self, panel):
    self.buildOneButton(panel, "FIRST", self.OnFirst)
    self.buildOneButton(panel, "<<PREV", self.OnPrev, (80,00))
    self.buildOneButton(panel, "NEXT>>", self.OnNext, (160,0))
    self.buildOneButton(panel, "LAST", self.OnLast, (240,0))

#build off arguments already passing to wx.Button
#FUNCTION TAKES VALUES, CREATES OBJECT, MUST RETURN TO CALLER
def buildOneButton(self, parent, label, handler, pos=(0,0)):
    button = wx.Button(parent, -1, label, pos)
    self.Bind(wx.EVT_BUTTON, handler, button)
    return button

#This eliminates the local variables/need for variable names ...
# ...massively cutting down on code errors and copy/paste issues
# additionally can now move buildOneButton to a utility module to be used ...
# ...across projects

#------------------------------------------------------------------------

#THIRD TRY - get rid of "magic literals" hardcoded constants, multiple locations
#Seperate the DATA, from the PROCESSING

#These two variables, as pos arg can be reinserted and pos is generated
#Its a return because you are giving something back
#Because separated data, could now store externally and just pull in
def buttonData(self):
    #can just insert new buttons at any position
    return (("FIRST", self.OnFirst),
            ("<<PREV", self.OnPrev),
            ("NEXT>>", self.OnNext),
            ("LAST", self.OnLast))

#yPos declared, as does not change/need to be manipulated
#Calling button data, does not take any args from it
#Makes sense as script is run south, not north
def createButtonBar(self, panel, yPos=0):
    xPos = 0
    #for each pair of data, not for each value
    for eachLabel, eachHandler in self.buttonData():
        pos = (xPos, yPos)
        button = self.buildOneButton(panel, eachLabel, eachHandler,pos)
        #Just have to take GetSize as a given until find origins
        xPos += button.GetSize().width

def buildOneButton(self, parent, label, handler, pos=(0,0)):
    button = wx.Button(parent, -1, label, pos)
    self.Bind(wx.EVT_BUTTON, handler, button)
    return button
