# * Deletes empty space between selected events
# * 
# This script will Delete Empty Space Between Events In Selected Tracks
#
#  written by Harold Linke 29/09/2018
#  based on JSCRIPT Written By: Philip 31/08/2003
#

import clr
clr.AddReference('ScriptPortal.Vegas')
import ScriptPortal.Vegas
from ScriptPortal.Vegas import *

def FromVegas(pyVEGAS):

    for track in pyVEGAS.Project.Tracks:
        
        if track.Selected:
            tracktime = Timecode.FromString("00:00:00:00")
            for event in track.Events:
                print ("tracktime: ",tracktime, " event len:",event.Length)
                event.AdjustStartLength(tracktime,event.Length,True)
                tracktime = Timecode(tracktime.ToMilliseconds() + event.Length.ToMilliseconds())
                
if __name__ == "__main__":
    FromVegas(pyVEGAS)