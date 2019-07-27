# * Imports a Magix VPX Edl into the Vegas Timeline
# *
# * Revision Date: Jan 15,2019
# * Version:       1.0
# * Copyright:     Harold Linke 
# 
import clr
clr.AddReference('ScriptPortal.Vegas')
import ScriptPortal.Vegas
from ScriptPortal.Vegas import *

clr.AddReference('System.Windows.Forms')
import System.Windows.Forms
import os

pyVEGAS: Vegas

# List directories where missing media should be searched
searchDirList = ["F:\\data_archiv\\Videos1\\Original Videos", "E:\data_archiv\Video_Projekte\_all_video_projects", "E:\\MMserver_NAS3\\Musik"]
searchMissingMedia = True # set to TRUE if you want that VEGAS is looking for missing media

searchStringFilenameListStart = "Source Table Entries:"
searchStringFilenameListEnd = "Track"
searchStringTrackListStart = "Track"
searchStringTrackListEnd = "#Vol"


def check_filename(filename: str):
    """ checks if the filename is correct and adapts it if necessary

    Parameters:
        filename     - media filename
        
    return:
        string: updated filename
    """       
    # delete all invaild characters from filename
    filename = filename.strip() # remove leading and training blanks
    filename=filename.replace("\n","")
    filename=filename.replace("\r","")
    filename=filename.replace(">","")
    filename=filename.replace("'"," ")
    filename=filename.replace('"',' ')
    filename = filename.strip() # remove leading and training blanks
    #-----------------------------------------
    # check if filename needs to be adapted to new naming convention
    #
    # e.g. old naming convention: "     DV_D0017'20051022 16.44.03.avi     "
    #      new naming convention: "20051022164403_D0017.avi"
    #
    #-----------------------------------------
    testfilename = filename.lower()
    test1 = testfilename.find("dv_") # test for old filenames of DV files and correct them
    test2 = testfilename.find("d8_") # test for old filenames of DV files and correct them
    test3 = testfilename.find("video_") # test for old filenames of files with video_xx and correct them
           
             
    if test1 == 0 or test2 == 0 or test3 == 0:
        filename_comp = filename.split(" ")
        if len(filename_comp) >=2:
            filename_descr = filename_comp[0]
            filename_date  = filename_comp[1]
            filename_time  = filename_comp[2]
            filename_time_comp = filename_time.split(".")
                     
            filename = filename_date + filename_time_comp[0] + filename_time_comp[1] + filename_time_comp[2] + "_" + filename_descr + ".avi"

    return filename



class EDLFile:
    Filename = ""
    File = None
    fileIsOpen = False
    lastLineRead = ""
    filenamelist = [[0,"",0]] # list of filename items [id,filename,type]
    trackListEnd = False
    trackEventList = [[]]
    timeFactor = 48
    searchDirName = ""
    searchFileList = []  
    
    def __init__(self):
        self.trackListEnd = False

    def openFile (self,newfilename):
        """ open the edl file

        Parameters:
            newfilename - name of the file to open

        return:
            True:  File is open
            False: File could not be opened

        Post condition:
            text file with name newfilename is open for reading
        """
        self.File = open(newfilename)
        if (self.File != None):
            self.fileIsOpen = True
            self.filename = newfilename
        else:
            self.fileIsOpen = False
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
        self.File.close()

    def readNextNELine(self):
        """ read next not empty line from edl file

        Parameters:
            none

        return: 
            String: next not empty line from edl file

        Pre condition
            file was open for reading

        Post condition:
            file read pointer points to begin of line after the read line
        """
        line = self.File.readline()
        if line:
            while line =="" or line == "\n":
                line = self.File.readline()
                if line == None:
                    line = ""
                    break
        return line

    def findStartEventFilenameList(self):
        """ find the start of the event filename list in the edl file

        Parameters:
            none

        return: 
            Bool: True - start of the event filename list in the edl file found

        Pre condition
            file was open for reading

        Post condition:
            file read pointer points to begin of event filename list
        """
        line=self.readNextNELine()
        self.lastLineRead = line
        while line !="":
            if searchStringFilenameListStart in line:
                return True
            line=self.readNextNELine()
        return False

    def findNextEventFilename(self):
        """ find the next event filename in the edl file

        Parameters:
            none

        return: 
            Bool: True - event filename list continues
                  False - end of event file name list found

        Pre condition
            file was open for reading
            file read pointer points to lines in event file list (findStartEventFilenameList was executed before)

        Post condition:
            file read pointer points to end of event filename list and the begin of the Track list
            lastLineRead contains the last line read - needed at the end of the list, as this line starts the "Track" list
        """
        line=self.readNextNELine()
        self.lastLineRead = line
        if line != "":
            if line.find(searchStringFilenameListEnd) == 0: # "Track" at start of line
                return False
            else:
                itemstrings = line.split('"') # 1: id 2: filename 3:eventtype (Video,Audio)
                id = int(itemstrings[0])
                filenameelem=[id,itemstrings[1],itemstrings[2]]
                self.filenamelist.append(filenameelem)
        return True

    def createEventFilenameList(self):
        """ create the event filename list from the edl file

        Parameters:
            none

        return: 
            none

        Pre condition
            file was open for reading
            file read pointer points to lines before the event file list

        Post condition:
            file read pointer points to end of event filename list and the begin of the Track list
            lastLineRead contains the last line read - needed at the end of the list, as this line starts the "Track event list
            filenamelist contains the complete list of all mediafiles used in the edl file
        """
        nextLine = self.findStartEventFilenameList()
        while nextLine:
            nextLine = self.findNextEventFilename()
        return

    def searchFile(self,filePathName):
        """ search File

        Parameters:
            filePathName: Path and name of the file to search

            when the file was not found and searchMissingMedia = True the procedure looks in all subdirectories of the directories specified in searchDirList

        return: 
            original filePathName or updated filePathName with new path
            "" when file was not found

        Pre condition
            searchDirName and searchFileList contain the directry name and the file list of the last found filename or None

        Post condition:
            searchDirName and searchFileList contain the directry name and the file list of the found filename
            
        """
        fname = os.path.basename(filePathName)
        if os.path.isfile(filePathName):
            return filePathName
        elif searchMissingMedia and filePathName !="":
            fname = os.path.basename(filePathName)
            if fname.lower() in (name.lower() for name in self.searchFileList): # search in last directoy found
                return os.path.join(self.searchDirName, fname)
            for rootDir in searchDirList:
                print ("Search for ", fname, " in ", rootDir)
                for lookupDirName,subdirList, self.searchFileList in os.walk(rootDir):
                    if fname.lower() in (name.lower() for name in self.searchFileList):
                        self.searchDirName = lookupDirName
                        return os.path.join(self.searchDirName, fname)
        
            print (fname, " not found")
            openFileDialog2 = System.Windows.Forms.OpenFileDialog();
            openFileDialog2.Filter = "All files (*.*)|*.*";
            openFileDialog2.FilterIndex = 1;
            openFileDialog2.RestoreDirectory = True;
            openFileDialog2.AddExtension = True;
    #        openFileDialog2.InitialDirectory = self.searchDirName;
            openFileDialog2.FileName = fname
            openFileDialog2.Title = "Select File and Directory for : " + filePathName;

            if (openFileDialog2.ShowDialog() == System.Windows.Forms.DialogResult.OK):
                print (fname , "->", openFileDialog2.FileName)
                return openFileDialog2.FileName
        return filePathName
 
    
    def checkFileList(self):
        """ check if file exists

        Parameters:
            filePathName: Path and name of the file to check

            when the file was not found and searchMissingMedia = True the procedure looks in all subdirectories of the directories specified in searchDirList

        return: 
            original filePathName or updated filePathName with new path
            "" when file was not found

        Pre condition
            searchDirName and searchFileList contain the directry name and the file list of the last found filename or None

        Post condition:
            searchDirName and searchFileList contain the directry name and the file list of the found filename
            
        """
        for i, filePathName in enumerate(self.filenamelist):
            self.filenamelist[i][1] = self.searchFile(filePathName[1]) # search for file
        return
    
    def findStartTrackList(self):
        """ find the start of a track list in the edl file

        Parameters:
            none

        return: 
            Bool: True - track list start found
                  False - no tracklist found anymore

        Pre condition
            file was open for reading
            file read pointer points after the first line in the track event list with the "Track" keyword
            lastLineRead contains the last line read with the "Track" keyword

        Post condition:
            file read pointer points to first event in the event list for the track
            lastLineRead contains the last line read
            
        """
        if self.lastLineRead.find(searchStringFilenameListEnd) == 0: # "Track" at start of line
            line=self.readNextNELine()
            self.lastLineRead = line
            #skip the source and the header lines
            if line.find("#Source") == 0:
                line=self.readNextNELine()
                self.lastLineRead = line
                if line.find("#------") == 0:
                    return True
        return False

    def findNextTrackEvent(self):
        """ find the next event in the track list in the edl file

        Parameters:
            none

        return: 
            Bool: True - next event found
                  False - end of event list for this track reached

        Pre condition
            file was open for reading
            file read pointer points on the first line in the track event list
            lastLineRead contains the last line read

        Post condition:
            file read pointer points to next event in the event list for the track
            lastLineRead contains the last line read
            the event properties read from the edl file are appended to the trackEventList
            
        """
        line=self.readNextNELine()
        self.lastLineRead = line
        if line != "":
            if line.find(searchStringTrackListStart) == 0 or line.find(searchStringTrackListEnd) == 0: # # "Track" at start of line "#Volume" at start of line - end of tracklist
                return False
            else:
                itemstrings = line.split() # 0: id 1:track 2:Play-In 3: Play-Out 4:Record-In 5:Record-Out 6:Vol 7:MT 8:LK 9:FadeIn 10:% 11:CurveType 12:FadeOut 13:% 14:CurveType 15:Name
                # the definition of play-in play-out record-in and record out in the edl is different than in other edl files
                # play and record need to be exchanged to be standard complient
                # correct definition: 0: File-id 1:tracknumber 2:Record-In 3: Record-Out 4:Play-In 5:Play-Out 6:Vol 7:MT 8:LK 9:FadeIn 10:% 11:CurveType 12:FadeOut 13:% 14:CurveType 15:Name
                if len(itemstrings)>12:
                    fileProperties = self.filenamelist[int(itemstrings[0])]
                    trackType = "Video"
                    if "AUDIO" in fileProperties[2]:
                        trackType = "Audio"

                    P_MediaType    = trackType
                    P_Filename     = fileProperties[1]
                    P_Tracknumber  = int(itemstrings[1])
                    P_trackName    = "Track "+itemstrings[1]
                    P_RecordIn     = int(itemstrings[2])/self.timeFactor
                    P_PlayIn       = int(itemstrings[4])/self.timeFactor
                    P_Length       = int(itemstrings[5])/self.timeFactor - P_PlayIn
                    P_FadeIn       = int(itemstrings[9])/self.timeFactor
                    P_FadeOut      = int(itemstrings[12])/self.timeFactor
                
                    eventProperties = [P_MediaType, P_Filename, P_Tracknumber, P_trackName, P_RecordIn, P_PlayIn, P_Length, P_FadeIn, P_FadeOut]
                    self.trackEventList.append(eventProperties)
                    return True
        else:
            return False

    def getTrackEventList(self):
        """ get the track event list from the edl file

        Parameters
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
        trackEventList = []
        while self.findStartTrackList():
            while self.findNextTrackEvent():
                pass
        return self.trackEventList

    #*** Class EDLFile end *********


def checkFileExists(filePathName):
    """ check if file exists

    Parameters:
        filePathName: Path and name of the file to check

        when the file was not found

    return: 
        original filePathName or updated filePathName with new path
        "" when file was not found

 
    """
    
    
    fname = os.path.basename(filePathName)
    if os.path.isfile(filePathName):
        return filePathName
    else:
        return ""

  
def addTrackEvent(eventProp, track, mediaType,searchFile):
    """ add a video event to the track

    Parameters:
        eventProp: list of event properties
                   0:Audio/Video
                   1:pathfilename
                   2:Track number
                   3:Track name
                   4:RecordIn (in ms) - start of clip on timeline
                   5:PlayIn (in ms)  - start of event relativ to media start 
                   6:Length (in ms) - total length of Clip (includng fades and dissolve)
                   7:FadeIn (in ms) - length of FadeIn
                   8:FadeOut (in ms) - length of FadeOut
        track:     track, to which the event should be added
        mediaType: Video or Audio

    return: 
        none

    Pre condition
        track exists in VEGAS timeline

    Post condition:
        new video event with properties defined in eventProp is added to the track in the timeline
        if the mediafile is not existing dummy media is create
            
    """

    mediafilename = eventProp[1] 
    if mediafilename != "":
        if track.MediaType != mediaType:
            print("ERROR:", track.Name, ":", mediaType , "not valid")
        else:
            RecordIn = Timecode.FromMilliseconds(eventProp[4]) # RecIn
            PlayIn = Timecode.FromMilliseconds(eventProp[5]) # PlayIn
            eventLength = Timecode.FromMilliseconds(eventProp[6])
            FadeIn = Timecode.FromMilliseconds(eventProp[7]) # FadeIn
            FadeOut = Timecode.FromMilliseconds(eventProp[8]) # FadeOut
            curveType = CurveType.Slow # Standard Curve type for FadeIn, Fadeout

            checkedmediafilename = ""
            if searchFile:
                checkedmediafilename = checkFileExists(mediafilename)
            if checkedmediafilename == "":
                media = Media.CreateInstance(pyVEGAS.Project,mediafilename)
                mediastream = Media.CreateOfflineStream(media,mediaType)
                maxlength = eventLength
            else:
                media = Media.CreateInstance(pyVEGAS.Project,checkedmediafilename)

                if mediaType == MediaType.Video:
                    mediastream = media.GetVideoStreamByIndex(0)
                else:
                    mediastream = media.GetAudioStreamByIndex(0)
                maxlength = media.Length

            if mediastream != None:
                if mediaType == MediaType.Video:
                    Event = track.AddVideoEvent(RecordIn,maxlength) #add complete VideoClip on the timeline
                else:
                    Event = track.AddAudioEvent(RecordIn,maxlength) #add complete AudioClip on the timeline

            
                take = Event.AddTake(mediastream) # add mediastream to event
                dStart = Event.Start + PlayIn
                Event.AdjustStartLength(dStart, eventLength, True) # cut begin and/or end of Clip
                Event.Start = RecordIn # move clip to RecordIn timeline position

                Event.FadeIn.Curve=curveType
                Event.FadeOut.Curve=curveType
                Event.FadeIn.Length = FadeIn
                Event.FadeOut.Length = FadeOut
    return



def createTimeline(trackEventList):
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
    lastTrackNo = 0
#   print(trackEventList)

    for eventFileProp in trackEventList:
        searchFile = True
        if eventFileProp != []:
            curTrackNo = eventFileProp[2]
        
            if curTrackNo != lastTrackNo:
                # new track
                trackName = eventFileProp[3]
                print ("Track No:", curTrackNo)
                lastTrackNo = curTrackNo
                if eventFileProp[0] == "Audio":
                    mediaType = MediaType.Audio
                    eventTrack = pyVEGAS.Project.AddAudioTrack()
                    
                else:    
                    mediaType = MediaType.Video
                    eventTrack = pyVEGAS.Project.AddVideoTrack()
         
            if eventFileProp[0] != "Video" and eventFileProp[0] != "Audio":
                searchFile = False
            eventTrack.Name = trackName    
            addTrackEvent(eventFileProp, eventTrack, mediaType,searchFile)


def FromVegas (myVegas: Vegas):
    global pyVEGAS
    pyVEGAS = myVegas
    edlfile = EDLFile()

    openFileDialog1 = System.Windows.Forms.OpenFileDialog();
    openFileDialog1.Filter = "Magix VPX EDL(*.edl)|*.edl|All files (*.*)|*.*";
    openFileDialog1.FilterIndex = 1;
    openFileDialog1.RestoreDirectory = True;
    openFileDialog1.AddExtension = True;
#    openFileDialog1.InitialDirectory = "\\VEGASPython";
    openFileDialog1.Title = "Load Magix VPX EDL";

    if (openFileDialog1.ShowDialog() == System.Windows.Forms.DialogResult.OK):
        if edlfile.openFile(openFileDialog1.FileName):
            print("Create Filename list")
            edlfile.createEventFilenameList()
            print("Filename list created")
            print("Check Files")
            edlfile.checkFileList()
            print("Create Track Event list")
            trackEventList = edlfile.getTrackEventList()
            edlfile.closeFile()
            print("Track Event list created")
            print("Create Timeline")
            createTimeline(trackEventList)
            print("Timeline created")


    
