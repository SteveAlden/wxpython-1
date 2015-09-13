#for all fonts on system

import wx

e = wx.FontEnumerator()
e.EnumerateFacenames()
fontList = e.GetFacenames()

print fontList


# see multilineinputfromuser
