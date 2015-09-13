#See finishedsketchwindow.py

#----------------------------------------------------------
import wx
import cPickle
import os

    self.filename = ""

#------------------------------------------------------------
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

    #??? How do new files
    def OnNew(self, event): pass
