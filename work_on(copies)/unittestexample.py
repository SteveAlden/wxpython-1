#!/user/bin/env python

import unittest
import modelExample
import wx

#Declaring a test case (a subclass)
class TestExample(unittest.TestCase):

    #set up for each test
    #ensure that all tests start with app in the same state
    def setUp(self):
        self.app = wx.App(False)
        self.frame = modelExample.ModelExample(parent=None, id=-1)

    #tear down after each test
    #does any clean up necessary to keep system state consistent test to test
    def tearDown(self):
        self.frame.Destroy()

    #declaring a test
    #take no arguments
    #self.frame.model... refers to the test and its generated variables
    def testModel(self):
        self.frame.OnBarney(None)
        #?? why frame.model.first
        #assertion that could fail
        #optional msg argument in case of failure
        self.assertEqual("Barney", self.frame.model.first,
                msg="First is wrong.")
        self.assertEqual("Rubble", self.frame.model.last)

    def testEvent(self):
        #walking through the panel's children list until find the button
        #Once found, assign button to each and break
        panel = self.frame.GetChildren()[0]
        for each in panel.GetChildren():
            if each.GetLabel() == "Wilmafy":
                wilma = each
                break
        #creating the wx.CommandEvent to be sent from the button
        #wx.wx.EVT_COMMAND_BUTTON_CLICKED is the integer constant for Button binder object
        #integer constants found in wxPython source file (wx.py)
        event = wx.CommandEvent(wx.wxEVT_COMMAND_BUTTON_CLICKED, wilma.GetId())
        wilma.GetEventHandler().ProcessEvent(event)

        #as the event has the same id, it now has all the relevant features needed
        self.assertEqual("Wilma", self.frame.model.first)
        self.assertEqual("Flintstone", self.frame.model.last)

#creating a test suite
#creates an instance of the class for each test
#takes the class and a string as arguments
#all tests with that string as the prefix, are incorporated into the suite
def suite():
    suite = unittest.makeSuite(TestExample, 'test')
    return suite

if __name__ == '__main__':
    #starting the test, pass it the name of the suite in a string
    unittest.main(defaultTest = 'suite')
