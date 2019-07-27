# * Limit the length of all selected clips to 4 Seconds
# * 
# * Author: Harold Linke
# * Date: October 7, 2018
# * 
# * based on JScript script by: Edward Troxel
# * www.jetdv.com/tts
# * Modified: 05-29-2003
# *



import clr
clr.AddReference('System.Windows.Forms')
import System.Windows.Forms

clr.AddReference('ScriptPortal.Vegas')
import ScriptPortal.Vegas
from ScriptPortal.Vegas import *

def FromVegas(pyVEGAS):
   # adapt this value to your needs
    maxLength = Timecode.FromString("00:00:04:00")
 
  # Go through the list of Tracks
    for track in pyVEGAS.Project.Tracks:
        for evnt in track.Events:
            if (evnt.Selected):
                dLength = evnt.Length
                if dLength > maxLength:
                    dLength = maxLength
                dStart = evnt.Start
                evnt.AdjustStartLength(dStart, dLength, True)

if __name__ == "__main__":
    FromVegas(pyVEGAS)