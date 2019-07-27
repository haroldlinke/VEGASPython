# * Chop off the front and end of a clip by a specified length
# * 
# * Written By: Edward Troxel
# * www.jetdv.com/tts
# * Modified: 05-29-2003
# * Python adaptation By: Harold Linke
# * Date: October 6, 2018
# *
#
import clr
clr.AddReference('System.Windows.Forms')
import System.Windows.Forms
from System.Windows.Forms import *
clr.AddReference('ScriptPortal.Vegas')
import ScriptPortal.Vegas
from ScriptPortal.Vegas import *

clr.AddReference('System.Drawing')
import System.Drawing

class StringDialog (Form):

    def addTextControl(self,labelName, left, width, top, defaultValue):
        self.label = System.Windows.Forms.Label()
        self.label.AutoSize = True
        self.label.Text = labelName + ":"
        self.label.Left = left
        self.label.Top = top + 4
        self.Controls.Add(self.label)

        self.textbox = System.Windows.Forms.TextBox()
        self.textbox.Multiline = False
        self.textbox.Left = self.label.Right
        self.textbox.Top = top 
        self.textbox.Width = width - (self.label.Width)
        self.textbox.Text = defaultValue
        self.Controls.Add(self.textbox)

        return self.textbox

    def __init__(self,mainLabel, inputLabel, inputInit):
        self.Text = mainLabel
        self.FormBorderStyle = System.Windows.Forms.FormBorderStyle.FixedDialog
        self.MaximizeBox = False
        self.StartPosition = FormStartPosition.CenterScreen
        self.Width = 350
        self.Height = 160

        self.buttonWidth = 80
        self.buttonHeight = 24
        self.buttonTop = 60

        self.stringBox = self.addTextControl(inputLabel, 20, 200, 20, inputInit)

        self.okButton = System.Windows.Forms.Button()
        self.okButton.Text = "OK"
        self.okButton.Left = 240 - ((self.buttonWidth+20))
        self.okButton.Top = self.buttonTop
        self.okButton.Width = self.buttonWidth
        self.okButton.Height = self.buttonHeight
        self.okButton.DialogResult = System.Windows.Forms.DialogResult.OK
        self.AcceptButton = self.okButton
        self.Controls.Add(self.okButton)

        self.btnCancel = System.Windows.Forms.Button()
        self.btnCancel.Text = "Cancel"
        self.btnCancel.Left = 140 - ((self.buttonWidth+20))
        self.btnCancel.Top = self.buttonTop
        self.btnCancel.Width = self.buttonWidth
        self.btnCancel.Height = self.buttonHeight
        self.btnCancel.DialogResult = System.Windows.Forms.DialogResult.Cancel
        
#        self.AcceptButton = self.okButton
        self.Controls.Add(self.btnCancel)
        self.Controls.Add(self.okButton)

        self.label = System.Windows.Forms.Label()
        self.label.AutoSize = True
        self.label.Text = "Copyright 2018 Hlinke"
        self.label.Left = 20
        self.label.Top = 100
        self.Controls.Add(self.label)

def FromVegas(pyVEGAS):

    ChopDist = Timecode.FromString("00:00:01:00")

    dialog = StringDialog("Length to chop off from selected Events","Length (00:00:00:00)",ChopDist.ToString())

    dialogResult = dialog.ShowDialog()

    if System.Windows.Forms.DialogResult.OK == dialogResult:
          
        maxTime = dialog.stringBox.Text
    
        ChopDist = Timecode.FromString(maxTime)
 
      # Go through the list of Tracks
    for track in pyVEGAS.Project.Tracks:
        for evnt in track.Events:
            if (evnt.Selected):
                mtc = ChopDist.ToMilliseconds()
                dStart = evnt.Start.ToMilliseconds()
                dLength = evnt.Length.ToMilliseconds()
                dStart = dStart + mtc
                dLength = dLength - 2 * mtc

                evnt.AdjustStartLength(Timecode(dStart), Timecode(dLength), True)




if __name__ == "__main__":
    FromVegas(pyVEGAS)