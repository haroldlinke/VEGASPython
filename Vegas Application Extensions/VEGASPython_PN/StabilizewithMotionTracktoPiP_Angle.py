# Copies the Location data (animation keyframes) from the first mask
# * of the selected video events Bezier Masking FX to a selected
# * video events Picture-In-Picture (PiP) FX
# * To use this script:
# * 1) Create track motion on an event using Bezier mask FX
# * 2) Apply a PiP FX to the event (from a different track) that you want to follow along with the motion on the original event
# * 3) Adjust location, scale and angle of PiP FX for a certain point in time.
# * 4) Select both events (hold ctrl key)
# * 5) Run the script
# *
# * Revision Date: Sep 5 2018
# * Copyright: MAGIX AG  
# 

#/// <summary>
##/// Returns the first selected event that's under the cursor
##/// </summary>
##/// <returns>The first selected event or null if no event selected</returns>

import clr
#clr.AddReference('VEGASPythonTools')
#import VegasPythonTools
#from VegasPythonTools import *

clr.AddReference('ScriptPortal.Vegas')
import ScriptPortal.Vegas as VEGAS
from ScriptPortal.Vegas import *

clr.AddReference("System.Windows.Forms")
import System.Windows.Forms as WinForms

def FromVegas (myVegas):
    missingSelectionString = "Please select the video event to which you ve applied tracking and the overlapping video event on a different track that holds the media you want to pin to the tracking."
    missingTrackingDataString = "You must first apply the Bezier masking plug-in to one of the selected events and add motion tracking data for Mask 1."
    missingPipFxString = "You must first add the Picture in Picture plug-in to the event that you want to pin to the motion tracked event."
    TrackingDataCopiedString = "Tracking Data has been copied to PIP FX to stabilize Clip"
    pipScale=None
    pipAngle=None
 
    selEvent = []
    
    for track in myVegas.Project.Tracks: # type: Track_
        if track.MediaType == MediaType.Video:
            for evnt in track.Events: # type: TrackEvent_
                if (evnt.Selected):
                    if evnt.MediaType == MediaType.Video: # only video events
                        selEvent.append(evnt)

    bezierEvent = None

    if (len(selEvent) != 1):
        WinForms.MessageBox.Show(missingSelectionString, "No or more than one selected event", WinForms.MessageBoxButtons.OK, WinForms.MessageBoxIcon.Warning)
    else:
        hasBezierFx = False
        for trackEvent in selEvent:
            fxList = trackEvent.Effects
            # bezierFX = fxList.Find(x => (x.PlugIn.UniqueID == "{Svfx:com.sonycreativesoftware:bzmasking}"));
            for bezierFX in fxList:
                if bezierFX.PlugIn.UniqueID == "{Svfx:com.sonycreativesoftware:bzmasking}":
                    hasBezierFx=True;
                    break

            if hasBezierFx:
                ofxList = bezierFX.OFXEffect.Parameters
                BezierParamLoc = None
                hasParamLoc = False
                
                #  BezierParamLoc = ofxList.Find(x => (x.Name == "Location_0"))

                for BezierParamLoc in ofxList:
                    if BezierParamLoc.Name == "Location_0":
                        hasParamLoc = True
                        bezierEvent = trackEvent
                        break
                hasAngle = False
                angleTracking = None
                for paramAngle in ofxList:
                    if paramAngle.Name == "Angle_0":
                        angleTracking = paramAngle
                        break
                hasWidth = False
                widthTracking = None
                for paramWidth in ofxList:
                    if paramWidth.Name == "Width_0":
                        widthTracking = paramWidth
                        break
        if not hasBezierFx:
            WinForms.MessageBox.Show(missingTrackingDataString, "VEGAS B\u00E9zier Masking not applied", WinForms.MessageBoxButtons.OK, WinForms.MessageBoxIcon.Warning)
        else:
            if (BezierParamLoc == None) or (len(BezierParamLoc.Keyframes) == 0):
                WinForms.MessageBox.Show(missingTrackingDataString, "No tracking data", WinForms.MessageBoxButtons.OK, WinForms.MessageBoxIcon.Warning) 
            else:
                #print(BezierParamLoc.Name)
                
                #print("KeyFrames:", len(BezierParamLoc.Keyframes))
                if (angleTracking == None) or (len(angleTracking.Keyframes) == 0):
                    hasAngle=False
                else:
                    hasAngle=True
                if (widthTracking == None) or (len(widthTracking.Keyframes) == 0):
                    hasWidth=False
                else:
                    hasWidth=True

                hasPipFx = False
                for pipFX in fxList:
                    if pipFX.PlugIn.UniqueID == "{Svfx:com.sonycreativesoftware:pictureinpicture}":
                        hasPipFx=True
                        break

                if (hasPipFx):
                    ofxList = pipFX.OFXEffect.Parameters
                    hasParamLoc = False
                    pipScale = 1
                    for paramScale in ofxList:
                        if paramScale.Name == "Scale":
                            pipScale = paramScale.Value
                            pipParamScale = paramScale
                            break
                    for pipparamAngle in ofxList:
                        if pipparamAngle.Name == "Angle":
                            pipAngle = pipparamAngle
                            break
                    for pipparamLoc in ofxList:
                        if pipparamLoc.Name == "Location":
                            hasParamLoc = True
                            break
                        else:
                            pipparamLoc = None

                    if hasParamLoc:
                        pipLocationAtCursorPosition = pipparamLoc.GetValueAtTime(Timecode(myVegas.Transport.CursorPosition.ToMilliseconds() - bezierEvent.Start.ToMilliseconds()))
                        bezierLocationAtCursorPosition = BezierParamLoc.GetValueAtTime(Timecode(myVegas.Transport.CursorPosition.ToMilliseconds() - bezierEvent.Start.ToMilliseconds()))
                        
                        pipparamLoc.Keyframes.clear()
                        
                        print("Set Location Keyframe:")
                        curposX = bezierLocationAtCursorPosition.X
                        initlocX = pipLocationAtCursorPosition.X
                        curposY = bezierLocationAtCursorPosition.Y
                        initlocY = pipLocationAtCursorPosition.Y                                
                        
                        for BLkeyframe in BezierParamLoc.Keyframes: # type:OFXDouble2DKeyframe
                            tmpkeyframe = BezierParamLoc.GetValueAtTime(BLkeyframe.Time)
                            tmpkeyframe.X = (curposX-tmpkeyframe.X) * pipScale + initlocX
                            tmpkeyframe.Y = (curposY-tmpkeyframe.Y) * pipScale + initlocY
                            #print(tmpValue.X,",",tmpValue.Y)
                            pipparamLoc.SetValueAtTime(BLkeyframe.Time, tmpkeyframe)

                    pipAngle.Keyframes.clear()
                    # hasAngle = False
                    if hasAngle:
                        print("Set Angle Keyframe:")
                        for pipkeyframe in angleTracking.Keyframes:
                            #print(pipkeyframe.Time)
                            tmpValue = -angleTracking.GetValueAtTime(pipkeyframe.Time)
                            pipAngle.SetValueAtTime(pipkeyframe.Time, tmpValue)
                    
                    #hasWidth = False 
 
                    if hasWidth:
                        initWidthAtCursorPosition = widthTracking.GetValueAtTime(Timecode(myVegas.Transport.CursorPosition.ToMilliseconds() - bezierEvent.Start.ToMilliseconds()))
                        pipParamScale.Keyframes.clear()
                        print("Set Scale Keyframe:")
                        for widthkeyframe in widthTracking.Keyframes:
                        #   print(keyframe.Time)
                            tmpWidth = widthTracking.GetValueAtTime(widthkeyframe.Time)
                            tmpScale = pipScale
                            if tmpWidth > 0:
                                tmpScale = initWidthAtCursorPosition/tmpWidth
                            pipParamScale.SetValueAtTime(widthkeyframe.Time, tmpScale)
                else:
                    WinForms.MessageBox.Show(missingPipFxString, "No PiP FX", WinForms.MessageBoxButtons.OK, WinForms.MessageBoxIcon.Warning)

                WinForms.MessageBox.Show(TrackingDataCopiedString, "Clip Stabilization Finished", WinForms.MessageBoxButtons.OK, WinForms.MessageBoxIcon.Warning)                    



    
    
    
