# This script will add regions for all events on the selected track
# 
# By Harold Linke 29/09/2018
# based on Jscript by John Meyer 11/4/2003 (with ideas from Edward Troxel's "Markers to Events" script)
#
#

import clr
clr.AddReference('ScriptPortal.Vegas')
import ScriptPortal.Vegas
from ScriptPortal.Vegas import *

def FromVegas(pyVEGAS):
    
    for track in pyVEGAS.Project.Tracks:
        if track.Selected:
            RegionNumber = 1
            for event in track.Events:
                myRegion = Region(event.Start,event.Length,str(RegionNumber));#Insert a region over this event
                pyVEGAS.Project.Regions.Add(myRegion)
                
if __name__ == "__main__":
    FromVegas(pyVEGAS)                