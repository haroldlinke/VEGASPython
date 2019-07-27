# VEGASPython
Provides Python Support for VEGAS Video Editor

homepage: https://www.hlinke.de/dokuwiki/doku.php?id=en:vegas_python

## Introduction

VEGAS Pro allows the control of the application via scripting. PYTHON is an easy to learn powerful programming language that is more and more used for scripting of applications. In the 3D and video editing area some application use already PYTHON for scripting.

Goal of this VEGAS extension is to provide PYTHON scripting to VEGAS allowing to provide new features to the VEGAS users based on Python solutions.

The extension provides two options:

    for users
        new features like VEGASScenedetect
    for developers
        an interactive dockable VEGASPython Window
        executing Scripts located in a specific folder and integrate them into the VEGAS User Interface like other C# Scripts

## Download and Installation

if you want to test VEGASPython you need following items:

      Magix VEGAS Pro: https://www.vegascreativesoftware.com/gb/vegas-pro/product-comparison/

      VEGASPython: https://www.hlinke.de/dokuwiki/doku.php?id=en:vegas_python_download

Unfortunately the complete ZIP file is too big to be provided in GITHUB.
All file from the ZIP file are available here except a complete Python37 installation includeing NumPy and OpenCV for python.

## VEGASPYTHON for Users 

Please find details for users on the following page:
https://www.hlinke.de/dokuwiki/doku.php?id=en:vegas_python_users

## VEGASPython for Developers 
Please find details for developers on the following page: 

https://www.hlinke.de/dokuwiki/doku.php?id=en:vegas_python_dev

## VEGASPython Interactive Window

VEGASPython includes an interactive window.
VEGASPython interactive window is activated via the 'View' / 'Extensions' tab. 

A VEGAS dockable window opens. The window can float over VEGAS or can be integrated into the VEGAS layout as any other VEGAS window.

The VEGASPython window shows two textboxes:

  - Input PYTHON Commands
  - Output
 
and a menu with two items "File" and "Execute VEGASPython Script".

Python comands are entered in the textbox "Input". Several lines can be entered one after each other. It is possible to copy a complete PYTHON Script from another editor via CTRL+C and CTRL+V.
The PYTHON commands will be executed by clicking on the menu "Execute VEGASPython Script".

All output from PYTHON print statements and all error messages will be shown in the "Output" textbox.

VEGASPython is based on Python 3.7.3 and PythonNet.

The VEGAS API can be accessed directly by using the build-in variable "pyVEGAS".
All VEGAS API items are available.

### Examples ###
Example for a simple script that can be used in the interactive window:

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


----

VEGAS also supports extension scripts that can be called via the VEGAS user interface or a shortcut key.
A script that should be used as an extension needs to be included in a function FromVegas. See example below.

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


## Python Debugging

VEGASPython is embedded in VEGAS. This can create issues for some Python debuggers.
I am using the WING Python IDE https://wingware.com/.
There is a free version (WING IDE Personal) for non-comercial use and a professional version available. 
Other debuggers may work as well, but I have not tested them.
If you have experience with another debugger, please inform me and I will add this information to this chapter.

## Debugging using WING Python IDE

For debugging VEGASPython scripts with WING IDE please follow following steps:

  - copy the file wingdbstub.py from the wing IDE program directory to the VEGASPython_PN directory, where your VEGASPython code is located.
  - open wingdbstub.py and change the line: "kEmbedded = 0" to "kEmbedded = 1"
  - add the following line at the begin of the python code: "import wingdbstub"
  - Turn on listening for externally initiated debug connections in Wing, which is most easily done by clicking on the bug icon in the lower left of the main window and selecting "Accept Debug Connections" in the popup menu that appears.

Load the Python Script into Wing IDE and set breakpoints.

Start the script from VEGAS extension menu. (It is not possible to debug interactive scripts from the interactive window)

When you do changes to the script VEGAS needs to be restarted to load the updated script. (or you change the option in the config file)

## The VEGASPYTHON Config File 
In the main directory where you extrcated the ZIP file you will find the file VEGASPython_CONFIG.JSON.
This file provides important config parameters to support the debugging:

This is the content of the file:

      {

          {
          "PythonPath": "",
          "debugmode": false,
          "debugprecmd": "import wingdbstub;print ('Wing Debug started')",
          "debugpostcmd": "print ('Debug ended')",
          "debugusereload": true
          }
      }

If you are familiar with JSON files you will know that the structure has to be maintained. Otherwise the parameters will not be recognized any more. Change value only between the "" or change true to false or viceversa.

### Description of the Config parameters
#### PythonPath 
as default Python is installed in the subdirectory \Python37 of the VEGASPython installation directory.
This is good for users who do not want to deal with Python.
If you have your own Python Installation(it must be Python 3.7.x) the you can here specify the directory where it resides.

  Example:
  "PythonPath": "C:\\Python37"

If the parameter is empty 

Do not forget to double "\" in the Path.

#### debugmode
debugmode is the main switch for the debugging parameters.

  "debugmode": false

  The debug parameters are ignored

  "debugmode": true

  The debug parameters are used.

#### debugprecmd 

Defines Python commands that need to be executed before the start of the Python script.
Here you can add commands that are needed by the debugger to start the debugging and connect with the embedded Python interpreter.

Example:

  "debugprecmd": "import wingdbstub;print ('Wing Debug started')"

  Imports the wingdbstub.py that is needed by WING Python IDE to start the debugging. You can remove this when you do not use WING Python IDE.

#### debugpostcmd 

Defines Python commands that need to be executed after the end of the Python script.
Here you can add commands that are needed by the debugger to stop the debugging.

Example:

  "debugpostcmd": "print ('Debug ended')"

#### debugusereload 

As explained above you need to restart VEGAS after any change in the Python script.

To avoid this restart and reduce the turn arround times VEGASPython can use the "reload" command to load a script.

Reloading a module is not a clean concept and can create some issue. Please read the chapter reload() in the Python documentation before using this fundtion:
https://docs.python.org/3/library/imp.html?highlight=reload#imp.reload

example:

  "debugusereload": true


