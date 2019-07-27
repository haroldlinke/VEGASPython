# * Imports a Pinnacle Studio Scenefile into the Vegas Mediabin
# *
# * Revision Date: Jan 19,2019
# * Version:       1.0
# * Copyright:     Harold Linke 
# 

import clr
clr.AddReference('System.Windows.Forms')

clr.AddReference('ScriptPortal.Vegas')
import ScriptPortal.Vegas
from ScriptPortal.Vegas import *

clr.AddReference('System.Drawing')
import System.Drawing
import System.Windows.Forms as WinForms
import os
import codecs
import xml.etree.ElementTree as ET
import struct
import array
import sys



# List directories where missing media should be searched
searchDirList = ["F:\\data_archiv\\Videos1\\Original Videos", "E:\data_archiv\Video_Projekte\_all_video_projects", "E:\\MMserver_NAS3\\Musik"]
searchMissingMedia = True # set to TRUE if you want that VEGAS is looking for missing media

samplerate = 1000
mediaArchive = []
#mediaArchive.append(0)
mediaFileList = []
#mediaFileList.append(" ")
Entrycount = 0
#titlepath_1 = "E:\data_archiv\Video_Projekte\_all_video_projects\snapshots"
#titlepath_2 = ".Movie_Schnappschuss.jpg"
#titlereplace = ".Movie.axp"
#dummyfilename = "E:\data_archiv\Video_Projekte\_all_video_projects\snapshots\dummy.jpg"
#titlesnapshotnumber = 1
#titlefilename = "dummy"

#projectfile = None

#titlesnapshotnumber = 1
#titlefilename = ""
pyVEGAS = None

class StudioFile:
    input = None
    Filename = ""
    fileIsOpen = False
    lastLineRead = ""
    filenamelist = [[0,"",0]] # list of filename items [id,filename,type]
    trackListEnd = False
    trackEventList = [[]]
    timeFactor = 48
    root = None
    P_old_FadeOut = 0
    searchDirName = ""
    searchFileList = []

    
    
    def __init__(self):
        self.trackListEnd = False

    def openFile (self,Projectfilename):
        """ open the edl file

        Parameters:
            newfilename - name of the file to open

        return:
            True:  File is open
            False: File could not be opened

        Post condition:
            text file with name newfilename is open for reading
        """
        try:
            print(Projectfilename)
            with open(Projectfilename, "r") as self.input:
                data = self.input.read()

            self.filename = Projectfilename
            self.input.close()

            # Decode binary data as utf-16.
            #data16 = data.decode("utf-16")


            #data8 = data.decode("utf-8")
            data8 = data[data.find("<"):] # remove trailing chars 

            self.root = ET.fromstring(data8) # parse xml file
            self.fileIsOpen = True
        except:
            self.fileIsOpen = False
            print ("Unexpected error:", sys.exc_info()[0])
            # raise 

        return self.fileIsOpen

    def closeFile(self):
        """ close the edl file

        Parameters:
            none

        return:
            none

        Pre condition
            file was open for reading

        Post condition:
            text file with name newfilename is closed
        """
        #self.File.close()
        pass

        #---------------------------------------------
        # Function: writeTrackInfo
        #
        # writes the EDL trackinfo for one track
        #        

    def writeTrackInfo(self, SceneDescriptor,mediaFilename):
        if os.path.isfile(mediaFilename):
            media = Media.CreateInstance(pyVEGAS.Project,mediaFilename)
            mediaLength = media.Length.FrameCount
            mediastream = media.GetVideoStreamByIndex(0)
            mediaFrameRate = mediastream.FrameRate

            lastScenePos = 0
            for item in SceneDescriptor.iter("Scene"):
 
                scenePos=int(item.attrib['pos']) # start position of next scene in Frames

                if scenePos > 0:

                    P_RecordIn  = lastScenePos # start of current scene
                    P_RecordOut = scenePos  # end of current scene
                    P_Length    = P_RecordOut - P_RecordIn
                    P_Filename = mediaFilename
                    P_MediaType = "Video"
 
                    #                  0:Audio/Video  1:pathfilename  2:RecordIn  3:Length  4: FrameRate
                    eventProperties = [P_MediaType,   P_Filename,     P_RecordIn, P_Length, mediaFrameRate ]
                    self.trackEventList.append(eventProperties)
                    lastScenePos = scenePos
        
            # write last scene
            P_RecordIn  = lastScenePos # start of current scene
            P_RecordOut = mediaLength  # end of current scene
            P_Length    = P_RecordOut - P_RecordIn
            P_Filename = mediaFilename
            P_MediaType = "Video"
 
            #                  0:Audio/Video  1:pathfilename  2:RecordIn  3:Length  4: FrameRate  
            eventProperties = [P_MediaType,   P_Filename,     P_RecordIn, P_Length, mediaFrameRate ]
            self.trackEventList.append(eventProperties)
        else:
            print(mediaFilename, " not found")
        
        return
        #-----------------------------------------------
    

    def getTrackEventList(self,filename):
        """ get the track event list from the edl file

        Parameters:
            none

        return: 
            trackEventList with all events and all tracks defined in the edl file

        Pre condition
            file was open for reading
            file read pointer points the start of the edl file
 
        Post condition:
            file read pointer points to theend event list for the last track
            lastLineRead contains the last line read
            all event properties read from the edl file are appended to the trackEventList for all tracks
            
        """
        for SceneDescriptor in self.root.iter("SceneList"):
                    
            self.writeTrackInfo(SceneDescriptor,filename)
 
        return self.trackEventList

    #*** Class StudioFile end *********


def addTrackEvent(eventProp, sceneNo):
    """ add a video event to the track

    Parameters:
        eventProp: list of event properties
                   0:Audio/Video
                   1:pathfilename
                   2:RecordIn (in frames) - start of subclip 
                   3:Length (in frames) - total length of SubClip 
                   
        sceneNo:   number of scene event
 
    return: 
        none

    Pre condition
        media file exists

    Post condition:
        new subclip with properties defined in eventProp is created
    """

    mediafilename = eventProp[1] 
    if mediafilename != "":
        framerate = eventProp[4] # pyVEGAS.Project.Video.FrameRate

        subClipStart = Timecode.FromSeconds(eventProp[2]/framerate) # RecIn
        subClipLength = Timecode.FromSeconds(eventProp[3]/framerate) # length
        displayName = os.path.basename(mediafilename) + " " + str(sceneNo)

        newSubClip = Subclip(pyVEGAS.Project,mediafilename,subClipStart,subClipLength,False,displayName)

        
    return

def createSubClips(trackEventList):
    """ creates the timeline from the trackEventList entries

    Parameters:
        trackEventList
        
    return: 
        none

    Pre condition
        trackEventList contains all events from the edl file

    Post condition:
        all tracks and events defined in the edl file are added to the timeline
            
    """
    sceneNo = 0

    # print(trackEventList)

    for eventFileProp in trackEventList:
        if eventFileProp != []:
          
           addTrackEvent(eventFileProp,sceneNo)
           sceneNo += 1
            
    return

def FromVegas (myVEGAS):
    
    global pyVEGAS

    pyVEGAS = myVEGAS

    studioFile = StudioFile()

    openFileDialog1 = WinForms.OpenFileDialog();
    openFileDialog1.Filter = "Media File with PinnStudio Scenelist(*.scn.xml)|*.scn.xml|All files (*.*)|*.*";
    openFileDialog1.FilterIndex = 1;
    openFileDialog1.RestoreDirectory = True;
    openFileDialog1.AddExtension = False;
#    openFileDialog1.InitialDirectory = "\\VEGASPython";
    openFileDialog1.Title = "Load Pinnacle Studio Scenefile"

    if (openFileDialog1.ShowDialog() == WinForms.DialogResult.OK):
        sceneFilename    = openFileDialog1.FileName
        mediaFilePath    = os.path.dirname(sceneFilename)
        mediaFilename    = sceneFilename.replace(".scn.xml","")
        
        
        if studioFile.openFile(sceneFilename):
            print("Import Studio Movie started: ", sceneFilename)
 
            print("Create Track Event list")
            trackEventList = studioFile.getTrackEventList(mediaFilename)
            studioFile.closeFile()
            print("Track Event list created")

            print("Create SubClips")
            createSubClips(trackEventList)
            print("SubClips created")

    
    
            
if __name__ == "__main__":
    FromVegas(pyVEGAS)    
