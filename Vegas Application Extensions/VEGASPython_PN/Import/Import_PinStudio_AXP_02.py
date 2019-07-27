# * Imports a Pinnacle Studio Project into the Vegas Timeline
# *
# * Revision Date: Jan 19,2019
# * Version:       1.0
# * Copyright:     Harold Linke 
# 
import clr
clr.AddReference('ScriptPortal.Vegas')
import ScriptPortal.Vegas
from ScriptPortal.Vegas import *

clr.AddReference('System.Windows.Forms')
import System.Windows.Forms as WinForms
import os
import codecs
import xml.etree.ElementTree as ET
import struct
import array

pyVEGAS: Vegas

# List directories where missing media should be searched
searchDirList = ["F:\\data_archiv\\Videos1\\Original Videos", "E:\data_archiv\Video_Projekte\_all_video_projects", "E:\\MMserver_NAS3\\Musik"]
searchMissingMedia = True # set to TRUE if you want that VEGAS is looking for missing media

samplerate = 1000
mediaArchive = []
#mediaArchive.append(0)
mediaFileList = []
#mediaFileList.append(" ")
Entrycount = 0
titlepath_1 = "E:\data_archiv\Video_Projekte\_all_video_projects\snapshots"
titlepath_2 = ".Movie_Schnappschuss.jpg"
titlereplace = ".Movie.axp"
dummyfilename = "E:\data_archiv\Video_Projekte\_all_video_projects\snapshots\dummy.jpg"
titlesnapshotnumber = 1
titlefilename = "dummy"

projectfile = None

titlesnapshotnumber = 1
titlefilename = ""


def check_filename(filename):
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
    test4 = testfilename.find("v00") # test for old filenames of files with v00xx and correct them
          
             
    if test1 == 0 or test2 == 0 or test3 == 0 or test4==0:
        filename_comp = filename.split(" ")
        if len(filename_comp) >=2:
            filename_descr = filename_comp[0]
            filename_date  = filename_comp[1]
            filename_time  = filename_comp[2]
            filename_time_comp = filename_time.split(".")
                     
            filename = filename_date + filename_time_comp[0] + filename_time_comp[1] + filename_time_comp[2] + "_" + filename_descr + ".avi"
  
    return filename


def hex_to_float(hexstr):
    """ calculates the float value of a hex representation used in Studio XML

    Parameters:
        hexstr     - string with Hexvalue e.g. "400fae147ae147ae(3.96)"
        
    return:
        float value of hextring multplied by samplerate e.g. 1000 for VEGAS
    """       

    hexvalue = hexstr.split('(')[0]

    if hexvalue =='0':
        hexvalue='0000000000000000'

    somebytes=bytearray.fromhex(hexvalue)
    
    result = struct.unpack('>d', somebytes)

    if samplerate == 1:
        calc = result[0]
    else:
        calc = int(result[0]*samplerate)

    if calc <0:
        calc = 0;
    return calc

#---------------------------------------------
def getItemAttribute(item, attribute):
    """ get the attribute from timecode Objects 

    Parameters:
        item     - timeline object
        attribue - attribute to look for
    return:
        attribute value
        or
        0 when attribute not found

            
    """       
    if attribute in item.attrib:
        sValue = item.attrib[attribute];
        iValue = hex_to_float(sValue)
    else:
        iValue = 0
    return iValue
        


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
            with open(Projectfilename, "rb") as self.input:
                data = self.input.read()

            self.filename = Projectfilename
            self.input.close()

            # Decode binary data as utf-16.
            data16 = data.decode("utf-16")

            binPos1 = data16.find("<BinaryArchive>")
            if binPos1 >= 0:
                binPos2 = data16.find("</BinaryArchive>")+len("</BinaryArchive>")

                studioBinary = data16[binPos1+1:binPos2] #save BinaryContent for later use

                data16 = data16[:binPos1] + data16[(binPos2+1):] # remove binary content from data - the content disturbes the XML parser

            self.root = ET.fromstring(data16) # parse xml file
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
        mediaArchive.append("0000")
        mediaFileList.append(dummyfilename)
    
        for DirectoryElem in self.root.iter("Directory"):
            directory = DirectoryElem.attrib['Path']
            directory = directory.replace('/','\\')
        
            for FileElem in DirectoryElem.iter("File"):

                filename = check_filename(FileElem.text)
                 
                FileId=FileElem.attrib['FileID']
    
                mediaArchive.append(FileId)
                mediaFileList.append(directory+filename)
 
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
        if os.path.isfile(filePathName):
            return filePathName
        elif searchMissingMedia:
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
        openFileDialog2 = WinForms.OpenFileDialog();
        openFileDialog2.Filter = "All files (*.*)|*.*";
        openFileDialog2.FilterIndex = 1;
        openFileDialog2.RestoreDirectory = True;
        openFileDialog2.AddExtension = True;
#        openFileDialog2.InitialDirectory = self.searchDirName;
        openFileDialog2.FileName = fname
        openFileDialog2.Title = "Select File and Directory for : " + filePathName;

        if (openFileDialog2.ShowDialog() == WinForms.DialogResult.OK):
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
        for i, filePathName in enumerate(mediaFileList):
            mediaFileList[i] = self.searchFile(filePathName) # search for file
        return

        #---------------------------------------------
        # Function: writeTrackInfo
        #
        # writes the EDL trackinfo for one track
        #        

    def writeTrackInfo(self, TrackDescriptor, Tracknumber, TrackType):
        global Entrycount
        global titlesnapshotnumber
  
        trackName=TrackDescriptor.findtext("./Name") + "-" + str(Tracknumber)
        firstItemInTrack=True

        for item in TrackDescriptor.iter("Item"):
            clipname=item.findtext("./EntryData/Object/CNGTrackClip/Clip/Object/CNGObject/Name")

            clipObject=item.find("./EntryData/Object/CNGTrackClip/Clip/Object")

            if (clipObject):
                try:
                    classname=clipObject.attrib['ClassName']

                    if classname == "CIMGEWP": # Titles without Media
                        clipMedia = None
                    else:         
                        clipMedia=clipObject.find("./CNGMediaSource/Media")

                    if clipMedia==None:
                        clipref="0000"
                    else:
                        clipref=clipMedia.attrib['Reference']
                except:
                    print ("Exception1: ", item)

                S_MarkInvalue  = getItemAttribute(item,'MarkIn')
                S_MarkOutvalue = getItemAttribute(item,'MarkOut')
                S_RecInvalue   = getItemAttribute(item,'RecIn')

                S_FadeInvalue  = getItemAttribute(item,'FadeIn')
                S_FadeOutvalue = getItemAttribute(item,'FadeOut')
             
                if clipname==None:
                    clipname = "Title"

                clipname=clipname.replace("'"," ")
                clipname=clipname.replace('"',' ')

                Source_num = mediaArchive.index(clipref)
 
                P_PlayIn   = S_MarkInvalue
                P_PlayOut  = S_MarkOutvalue
                P_RecordIn = S_RecInvalue
                P_Length   = P_PlayOut - P_PlayIn
                if S_FadeInvalue > 0:
                    P_FadeIn = S_FadeInvalue - S_MarkInvalue # P_FadeIn is length of FadeIn
                else:
                    P_FadeIn = 0
 
                if S_FadeOutvalue > 0:
                    P_FadeOut  = S_MarkOutvalue - S_FadeOutvalue
                else:
                    P_FadeOut = 0
 
                if clipref==None:
                    P_Filename = dummyfilename
                else:
                    P_Filename = mediaFileList[Source_num]            
            
                if TrackType == "V":
                    P_MediaType= "Video"
                    if classname=="CIMGEWP": # object is a title
                        P_Filename = "Title" + str(titlesnapshotnumber)
                        P_MediaType = "Title"
                        titlesnapshotnumber+=1                
                else:
                    P_MediaType= "Audio"

                # handle dissolve according to Studio way of handling it
                # if last event has fadeOut and current event has no fadeIn then the length of the current event has to be extended by the fadeOut and the start needs to be shifted by the fadeOut to create the overlap
                # if current event has fadeIn and the last event has no fadeOut then the length of the last event has to be extended by the fadeIn to create the overlap
                if not firstItemInTrack:
                    lastEventFadeOut = self.trackEventList[-1][8]
                    if lastEventFadeOut > 0 and P_FadeIn == 0:
                        if P_PlayIn >= lastEventFadeOut: # only when there is sufficient "meat"
                            P_RecordIn = P_RecordIn - lastEventFadeOut
                            P_PlayIn   = P_PlayIn - lastEventFadeOut
                            P_Length   = P_Length + lastEventFadeOut

                    if lastEventFadeOut == 0 and P_FadeIn > 0:
                        self.trackEventList [-1][6] = self.trackEventList [-1][6] + P_FadeIn

                #                  0:Audio/Video  1:pathfilename  2:Track number 3:Track name 4:RecordIn  5:PlayIn  6:Length  7:FadeIn  8:FadeOut 
                eventProperties = [P_MediaType,   P_Filename,     Tracknumber,   trackName,   P_RecordIn, P_PlayIn, P_Length, P_FadeIn, P_FadeOut]
                self.trackEventList.append(eventProperties)
                firstItemInTrack = False
        return
        #-----------------------------------------------
    

    def getTrackEventList(self):
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
        trackDescriptorList = []
        for TrackDescriptor in self.root.iter("TrackDescriptor"):
            trackDescriptorList.append(TrackDescriptor)
         
        Tracknumber = 1
            
        for TrackDescriptor in reversed(trackDescriptorList):
            Category = TrackDescriptor.attrib["Categories"]
        
            Trackname=TrackDescriptor.findtext("./Name")
        
            if Category.find("Video")>=0:
                self.writeTrackInfo(TrackDescriptor,Tracknumber,'V')
                Tracknumber +=1
            
            if Category.find("Audio")>=0:    
                self.writeTrackInfo(TrackDescriptor,Tracknumber,'A')
                Tracknumber +=1
 
        return self.trackEventList

    #*** Class StudioFile end *********


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
#    print(trackEventList)

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
            
    return

def FromVegas (myVegas: Vegas):
    
    global pyVEGAS
    
    pyVEGAS = myVegas
    studioFile = StudioFile()

    openFileDialog1 = WinForms.OpenFileDialog();
    openFileDialog1.Filter = "Pinnacle Studio Movie(*.axp)|*.axp|All files (*.*)|*.*";
    openFileDialog1.FilterIndex = 1;
    openFileDialog1.RestoreDirectory = True;
    openFileDialog1.AddExtension = True;
#    openFileDialog1.InitialDirectory = "\\VEGASPython";
    openFileDialog1.Title = "Load Pinnacle Studio Movie";

    if (openFileDialog1.ShowDialog() == WinForms.DialogResult.OK):
        if studioFile.openFile(openFileDialog1.FileName):
            print("Import Studio Movie started: ", openFileDialog1.FileName)
            
            print("Create Filename list")
            studioFile.createEventFilenameList()
            print("Filename list created")
            print("Check Files")
            studioFile.checkFileList()
            print("Create Track Event list")
            trackEventList = studioFile.getTrackEventList()
            studioFile.closeFile()
            print("Track Event list created")

            print("Create Timeline")
            createTimeline(trackEventList)
            print("Timeline created")



    
    
    
