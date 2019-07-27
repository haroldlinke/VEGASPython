# This script will add markers between all events on the selected track
#
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

def FromVegas(pyVEGAS):

    for track in pyVEGAS.Project.Tracks:
        if track.Selected:
            for event in track.Events:
                myMarker = Marker(event.Start)
                pyVEGAS.Project.Markers.Add(myMarker)
                
if __name__ == "__main__":
    FromVegas(pyVEGAS)                