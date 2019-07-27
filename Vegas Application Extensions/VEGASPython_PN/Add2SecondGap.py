# * Add 2 second gap between clips
# * 
# * Written By: Edward Troxel
# * www.jetdv.com/tts
# * Modified: 05-29-2003
# * Python adaptation By: Harold Linke
# * Date: October 6, 2018
# *
#
import clr
clr.AddReference('ScriptPortal.Vegas')
import ScriptPortal.Vegas
from ScriptPortal.Vegas import *

import sys

def FromVegas(myVEGAS: Vegas): 

    Gap = Timecode.FromString("00:00:02.00")
    #step through all selected video events
    for track in myVEGAS.Project.Tracks:
        tracktime = Gap
        for evnt in track.Events:
            evnt.AdjustStartLength(tracktime, evnt.Length, True)
            # workaround timecode + timecode is not possible
            tracktime = Timecode(tracktime.ToMilliseconds() + evnt.Length.ToMilliseconds() + Gap.ToMilliseconds())



if __name__ == "__main__":
    FromVegas(pyVEGAS)