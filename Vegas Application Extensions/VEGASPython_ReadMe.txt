Version 1.00 - June 30th, 2019
Author: Harold Linke

For more details check: https://www.hlinke.de/dokuwiki/doku.php?id=en:vegas_python

This is a Vegas pro Custom Command Extension adding a Python Scripting Interpreter and some features to VEGAS 

Installation:

All files and directories in the zip file must be copied to one of these folders :

C:\Users\<username>\Documents\Vegas Application Extensions\  
C:\Users\<username>\AppData\Local\Vegas Pro\Application Extensions\
C:\Users\<username>\AppData\Local\Vegas Pro\Application Extensions\
C:\ProgramData\Vegas Pro\Application Extensions\

I'm using on a Win10 system : 
C:\Users\Harold\Documents\Vegas Application Extensions

or 

C:\ProgramData\Vegas Pro\Application Extensions\

If the 'Application Extensions' folder does not jet exist, it must be allocated with exact the name as specified in the list above.

---------------------------------------------------------------------------
For VEGAS Users:

VEGASPython extends VEGAS with following functions:

Simple functions to demonstrate the principle:
- Add2SecondGap
- AddMarkersAtInterval
- AddMarkersToEvents
- AddRegionsToEvent
- AddTransitionToSelectedEvents
- Audit_Event_Levels
- Chopoff_BeginandEndofEvent_PN
- DeleteEmptySpaceBetweenEvents
- LimitSelectedEventLength
- LimitSelectedEventLengthto4Seconds

New functions only available with VEGASPython
- VegasSceneDetect

VEGASSceneDetect creates subclips of a mediaclip from the Mediapool or on the Timeline based on scene changes.

Usage: Select clips in the mediapool or select clips on the timeline
Call the VEGAS Extension: VEGASScenedetect

A window with the preview of the clip will open. The white bar at the top of the screen shows the progress of the scene detection.
Pressing ESC when the preview window is active aborts the scenedetection process.

VEGASScenedetect is based on PyScenedetect by Brandon Castellano

The commands can be found in VEGAS under the menu point: Extra / Extensions

----------------------------------------------------------------------
For VEGAS Script Developers:

VEGASPython Interactive Windows

VEGASPython includes an interactive window for Python developers.
VEGASPython interactive window is activated via the 'View' / 'Extensions' tab. 

A VEGAS dockable window opens. The window can float over VEGAS or can be integrated into the VEGAS layout as any other VEGAS window.

The VEGASPython window shows two textboxes:

- Input PYTHON Comands
- Output
 
and a menu with two items "File" and "Execute VEGASPython Script".

Python comands are entered in the textbox "Input". Several lines can be entered one after each other. It is possible to copy a complete PYTHON Script from another editor via CTRL+C and CTRL+V.
The PYTHON commands will be executed by clicking on the menu "Execute VEGASPython Script".

All output from PYTHON print statements and all error messages will be shown in the "Output" textbox.


VEGASPython scripts:

VEGASPython scripts are located in the subfolder VEGASPYTHON_PN.You can edit them or create your own with any Python Editor available.

VEGASPython is based on Python 3.7.3 and PythonNet.
Python and PythonNet are included in the download file. There is no need to install anything else.
The Python directory is:  "Application Extension"-Folder\Python37

The Python implementation includes follwing additional modules:
- openCV
- NumPy
- Scenedetect

If you have already another Python installation it will be ignored.

As of version 0.92 a configuration file is provided that allows you to change the Python directory.

For more details see https://www.hlinke.de/dokuwiki/doku.php?id=en:vegas_python_dev

---------------------------------------------
How to access VEGAS from Python:

The VEGAS API can be accessed directly by using the build-in variable "pyVEGAS".
All VEGAS API items are available.

Example for a simple script that can be used in the interactive window:

print("pyVEGAS.Version)

This command prints the current VEGAS version into the output window.

A more complex script:

import clr
clr.AddReference('ScriptPortal.Vegas')
import ScriptPortal.Vegas
from ScriptPortal.Vegas import *

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


A script that is used as an extension needs to be included in a function FromVegas. See example below.

import clr
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

The script needs to be saved in the VEGASPYTHON_PN subdirectory. 


-------------------------------------------------------------------------------------
New in Version 1.00:
For user:

VEGASScenedetect:
New functions: 
- PreviewWindow shows first frame of each scene (marked with red line below the frame) 
- PreviewWindow ProgressBar shows cuts
- Grouping of clips is maintained - e.g. video and sound clip

Bug corretion:
- wrong behavior when project framerate and clip media framerate were different

For Developers:
- VEGASPython Scrits can be called as commandline argument
- VEGASPython Scripts now behave like other VEGAS scripts - the interaktive window is not popping up anymore, but can stil be used for error messages
- improved stability

------------------------------------------------------------------------------------
New in Version 0.92:

For user:

VEGASScenedetect:
New functions: 
- split clips on timeline based on scene changes


For Developers:
- enhanced debugging support, configurable via config file
- support for debugging with WING Python IDE
- Configure CPython directory

------------------------------------------------------------------------------------

New in Version 0.90:

For user:

VEGASScenedetect:
New functions: 
- split mediapool clips into sub clips based on scene changes


For Developers:
- VEGASPython is now based on PYTHONNet and CPython - Full compatibility with standard CPython packages and modules

