# Add Marker at 5 seconds interval
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
      # Change this value to be the desired interval
      # Format:  hh:mm:ss:ff (hours:minutes:seconds:frames)      
      Interval = "00:00:05:00"
      
      IncTime=Timecode.FromString(Interval)
      CurrTime = IncTime
      EndTime = pyVEGAS.Project.Length
      
      while CurrTime < EndTime:
            # Put a marker at the interval point
            myMarker = Marker(CurrTime)
            pyVEGAS.Project.Markers.Add(myMarker)
            CurrTime = Timecode(CurrTime.ToMilliseconds() + IncTime.ToMilliseconds())
            
            
if __name__ == "__main__":
      FromVegas(pyVEGAS)