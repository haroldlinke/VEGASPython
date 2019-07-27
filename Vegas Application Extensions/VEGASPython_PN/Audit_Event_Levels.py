# * Find all events where opacity or audio level are sligthly changed
#*
# * This script finds all events where the opacity level has been 
# * set to a level only slightly less than 100%, or the audio level
# * set to slightly less than 0dB. This usually is not intentional
# * and results from accidentally moving the opacity or volume 
# * line while moving an event. Without this script, such 
# * an accident is very difficult to detect, and can result in 
# * long rendering times.
# * 
# * Written By: John H. Meyer
# * Date: November 11, 2003
# * Python adaptation By: Harold Linke
# * Date: October 6, 2018
# *
#


import clr
clr.AddReference('System.Windows.Forms')
import System.Windows.Forms

clr.AddReference('ScriptPortal.Vegas')
import ScriptPortal.Vegas
from ScriptPortal.Vegas import *

import math

def FromVegas(pyVEGAS):

    # Change this line if you want a different threshold
    Opacity = 0.90;
    EventLevel = 0.50; 
    
    OpacityMessage=""
    TrackUnits= ""
    
    for track in pyVEGAS.Project.Tracks:
        for evnt in track.Events:
            evnt.Selected = False
    
            # De-select events in order to make problem events stand out
            # (Problem events WILL be selected) 
    
            # If gain is less than 100% (or 0dB), but greater than the threshhold ...
            if (evnt.FadeIn.Gain > Opacity) and (evnt.FadeIn.Gain < 1) : 
                #   Highlight the "suspect" event
                pyVEGAS.SelectionStart = evnt.Start
                pyVEGAS.SelectionLength = evnt.Length
                pyVEGAS.Cursor = evnt.Start
                evnt.Selected = True 
                pyVEGAS.UpdateUI() 
    
                # Create error message to display in message box.
                if track.IsVideo():     
                    TrackUnits = "100%"
                    EventLevel = 100 * evnt.FadeIn.Gain
                    OpacityMessage = "This event is set to: " + str(int(EventLevel*100)/100)
                    OpacityMessage = OpacityMessage + "%. Do you want to set to " + TrackUnits + "?"
            
                else:
                    TrackUnits = "0dB";
                    EventLevel = 20 * math.log (evnt.FadeIn.Gain);
                    OpacityMessage = "This event is set to: " + str(int(EventLevel*100)/100)
                    OpacityMessage = OpacityMessage + "dB. Do you want to set to " + TrackUnits + "?";
            
    
    
                msgBoxResult = System.Windows.Forms.MessageBox.Show(OpacityMessage, "Region Selected", System.Windows.Forms.MessageBoxButtons.YesNo);
                if (msgBoxResult == System.Windows.Forms.DialogResult.Yes): 
                    evnt.FadeIn.Gain = 1      # Correct the problem
    
            evnt.Selected = False; # Clear all event selections
    
            #  // End While eventEnum
    # End While trackEnum
    
    System.Windows.Forms.MessageBox.Show("Don't forget to check all track header levels.","Completed",System.Windows.Forms.MessageBoxButtons.OK,System.Windows.Forms.MessageBoxIcon.Information);


if __name__ == "__main__":
    FromVegas(pyVEGAS)                        

