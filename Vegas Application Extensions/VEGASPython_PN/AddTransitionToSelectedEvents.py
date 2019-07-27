# add a selected transition between all selected events

import clr
clr.AddReference('System.Windows.Forms')
import System.Windows.Forms as WinForms
from System.Windows.Forms import *
#lr.AddReference('ScriptPortal.Vegas')
import ScriptPortal.Vegas
from ScriptPortal.Vegas import *
import random

# * Written By: Edward Troxel
# * www.jetdv.com/tts
# * Modified: 7/16/2003 
# * Python adaptation By: Harold Linke
# * Date: October 6, 2018
# 

import System.Windows.Forms
clr.AddReference('System.Drawing')
import System.Drawing

class TransitionDialog (Form):

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


    def addComboBox(self,left,width,top):
        self.transList = ComboBox()

        self.transList.DropDownWidth = width
        self.transList.Location = System.Drawing.Point(left, top)
        self.transList.Size = System.Drawing.Size(280, 21)
        self.transList.TabIndex = 7
        self.Controls.Add(self.transList)

        return self.transList



    def __init__(self,overlapTime):
        self.Text = "Add Transitions to adjacent events"
        self.FormBorderStyle = System.Windows.Forms.FormBorderStyle.FixedDialog
        self.MaximizeBox = False
        self.StartPosition = FormStartPosition.CenterScreen
        self.Width = 500
        self.Height = 140

        self.buttonWidth = 80
        self.buttonHeight = 24
        self.buttonTop = 60

        self.overlapTimeBox = self.addTextControl("Overlap Time (ms)", 320, 140, 20, str(overlapTime))
        self.m_transList = self.addComboBox(20,80,20) 

        self.okButton = System.Windows.Forms.Button()
        self.okButton.Text = "OK"
        self.okButton.Left = self.Width - ((self.buttonWidth+20))
        self.okButton.Top = self.buttonTop
        self.okButton.Width = self.buttonWidth
        self.okButton.Height = self.buttonHeight
        self.okButton.DialogResult = System.Windows.Forms.DialogResult.OK
        self.AcceptButton = self.okButton
        self.Controls.Add(self.okButton)

        self.label = System.Windows.Forms.Label()
        self.label.AutoSize = True
        self.label.Text = "Copyright 2018 Hlinke"
        self.label.Left = 20
        self.label.Top = 80
        self.Controls.Add(self.label)

def FromVegas(pyVEGAS):
    overlapTime = 1000;
    
    dialog = TransitionDialog(overlapTime)
    
    bFade = False; #Only true if the first list item is chosen
    
    dialog.m_transList.Items.Add("Standard Cross Fade")
    
    for trans in pyVEGAS.Transitions:
        if trans.IsContainer: # transition is a directory name
            dialog.m_transList.Items.Add("**" + trans.Name)
        else:    
            dialog.m_transList.Items.Add(trans.Name)
    
    dialog.m_transList.SelectedIndex = 0
    dialogResult = dialog.ShowDialog()
    iTrans = dialog.m_transList.SelectedIndex
    
    if System.Windows.Forms.DialogResult.OK == dialogResult:
        if (iTrans == 0):
            bFade = True
            
        if(iTrans > 1):
            plugIn = pyVEGAS.Transitions.GetChild(iTrans-1)
        
        overlapTime = int(dialog.overlapTimeBox.Text)
        
        startoffset = overlapTime;
       
        for track in pyVEGAS.Project.Tracks:
            for ev in track.Events:
                if ev.Selected:
                    ev.FadeIn.Curve = CurveType.Smooth
    
                    startTime = ev.Start.ToMilliseconds()
                    length = ev.Length.ToMilliseconds()
    
                    if startTime > startoffset:     
                        startTime = startTime - startoffset
                        startoffset = startoffset + overlapTime
    
                        ev.AdjustStartLength(Timecode.FromMilliseconds(startTime), Timecode.FromMilliseconds(length), False)
    
                    pyVEGAS.UpdateUI();
    
                    if ((ev.MediaType == MediaType.Video) and not bFade):
                        
                        if not plugIn.IsContainer:
                            fx = Effect(plugIn)
                            ev.FadeIn.Transition = fx
                        else:
                            print(plugIn.Name, "is no VideoFx")
     
            startoffset = overlapTime # new track
            
            
if __name__ == "__main__":
    FromVegas(pyVEGAS)                        

    
    
    
    

