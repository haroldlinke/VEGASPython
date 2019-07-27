# -*- coding: utf-8 -*-
#
#         VEGASSceneDetect: Python-Based Video Scene Detector
#   ---------------------------------------------------------------
#     [  Site: http://www.hlinke.de/   ]
#     [  Github: coming soon  ]
#     [  Documentation: coming soon    ]
#
#  Copyright (C) 2019 Harold Linke <http://www.hlinke.de>.
# VEGASSceneDetect is licensed under the BSD 3-Clause License; see the included
# LICENSE file
#
# VEGASSceneDetect is based on pySceneDetect by Brandon Castellano
#     [  Site: http://www.bcastell.com/projects/pyscenedetect/   ]
#     [  Github: https://github.com/Breakthrough/PySceneDetect/  ]
#     [  Documentation: http://pyscenedetect.readthedocs.org/    ]
#
# Adapted for VEGASPython and PyrhonNet by Harold Linke
# changes are marked with **VEGASPython**
#
# VEGASSceneDetect is licensed under the BSD 3-Clause License; see the included
# LICENSE file, or visit one of the following pages for details:
#  
#  to be added later
#  
# This software uses the pySceneDetect, PythonNet, OpenCV and NumPy libraries.
# See the included LICENSE files or one of the above URLs for more information.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.  IN NO EVENT SHALL THE
# AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN
# ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
# WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#

""" VEGASSceneDetect
This module implements the VEGAS video editor interface for pySceneDetect.
The module checks the Mediapool for selected clips and/or selected clips on the timeline
and starts the scene detetcion process. In the mdeiapool it creates subclips for each scene,
on theh timeline the clip is cut at every scene change.
"""

from __future__ import print_function
import os

import vpscenedetect
from vpscenedetect.video_manager import VideoManager
from vpscenedetect.scene_manager import SceneManager
from vpscenedetect.frame_timecode import FrameTimecode
# from scenedetect.stats_manager import StatsManager
from vpscenedetect.detectors import ContentDetector_VEGAS

import clr
clr.AddReference('ScriptPortal.Vegas')
import ScriptPortal.Vegas as VEGAS
from ScriptPortal.Vegas import *

STATS_FILE_PATH = 'testvideo.stats.csv'

pyVEGAS: Vegas

import json

class SD_Config():
    """ Configuration of VEGASScenDetect """

    def __init__(self):
        # type: 
        """ SDConfig Constructor Method (__init__)

        Arguments:
            None

        Raises:
            None
        """
        
        #**VEGASPython**
        filedir = os.path.dirname(os.path.realpath(__file__))
        filepath = os.path.join(filedir, 'VegasSceneDetect_config.json')

        with open(filepath, "r") as read_file:
            data = json.load(read_file)

        self.useHSV           = False    # define if HSV or BGR should be used for content analysis - BGR is faster
        self.showPreview      = True     # defines, that the preview if the analysed video shoul dbe shown
        self.previewFrameSkip = 100      # defines the number of frames skipped before the preview is updated - lower numbers make the preview smoother but cost processing time
        self.showFrameValues  = False    # the values calculated for each frame are shown - can be used to chek the threshold for a cut
        self.threshold        = 30       # threshold to detect a scene change
        self.min_scene_len    = 15       # minimal scen length
        self.processMediaPool = True     # detect scenes for selected clips in the mediapool
        self.processTimeline  = False    # Detect Scenes for selected clips onthe timeline
        self.progressBarLightness= 128   # defines the lightness opf the progress bar - 128 = grey - 255 = white - 0 = black

        try:
            if "useHSV" in data:
                self.useHSV           = data["useHSV"]    # define if HSV or BGR should be used for content analysis - BGR is faster
            if "showPreview" in data:
                self.showPreview      = data["showPreview"]     # defines, that the preview if the analysed video shoul dbe shown
            if "PreviewFrameSkip" in data:
                self.previewFrameSkip = data["PreviewFrameSkip"]      # defines the number of frames skipped before the preview is updated - lower numbers make the preview smoother but cost processing time
            if "showFrameValues" in data:
                self.showFrameValues  = data["showFrameValues"]    # the values calculated for each frame are shown - can be used to chek the threshold for a cut
            if "threshold" in data:
                self.threshold = data["threshold"]       # threshold that needs to be exceeded to determine a cut
            if "minSceneLength" in data:
                self.min_scene_len = data["minSceneLength"]
            if "processMediaPool" in data:
                self.processMediaPool = data["processMediaPool"]
            if "processTimeline" in data:
                self.processTimeline = data["processTimeline"]
            if "progressBarLightness" in data:
                self.progressBarLightness = data["progressBarLightness"]                 
            if "print_parameters" in data:
                print("Parameters: useHSV:",self.useHSV, " showPreview:", self.showPreview, " PreviewFrameSkip:", self.PreviewFrameSkip, " showFrameValues:", self.showFrameValues, " Threshold:",self.threshold)
   
        except:
            print ("Error in Config File")
            print(data)
            print("useHSV:",self.useHSV, " showPreview:", self.showPreview, " PreviewFrameSkip:", self.PreviewFrameSkip, " showFrameValues:", self.showFrameValues, " Threshold:",self.threshold)
        #**/VEGASPython**


sdConfig = SD_Config()

def createSubClips(trackEventList):
    """ creates subclips from the trackEventList entries

    Parameters:
        trackEventList
        
    return: 
        none

    Pre condition
        trackEventList contains all sub events 

    Post condition:
        all events defined in the tracklist are subclips in the mediapool
            
    """
    sceneNo = 0

    # print(trackEventList)

    for eventProp in trackEventList:
        if eventProp != []:
            mediafilename = eventProp[1] 
            if mediafilename != "":
                framerate     = eventProp[4] # FrameRate
                subClipStart  = Timecode.FromSeconds(eventProp[2]/framerate) # RecIn
                subClipLength = Timecode.FromSeconds(eventProp[3]/framerate) # length
                displayName   = os.path.basename(mediafilename) + " " + str(sceneNo)

                newSubClip    = Subclip(pyVEGAS.Project,mediafilename,subClipStart,subClipLength,False,displayName)
                sceneNo += 1
           
    return

def processMediaPool():
    """ creates subclips for all selected clips in the mediapool using scene detection

    Parameters:
        none
        
    return: 
        none

    Pre condition
        one or more clips are selected in the mediapool 

    Post condition:
        for all selected clips in the mediapool subclips have been created using scene detection
            
    """    

    mediapool = pyVEGAS.Project.MediaPool
    selmedia = mediapool.GetSelectedMedia() # type: List[Media_]
   
    index = 0
    for media in selmedia: # type: Media_
        print ("MediaPool:",media.FilePath)
        mediaFilename = media.FilePath
        mediaTimecodeIn = media.TimecodeIn
        mediaTimecodeOut = media.TimecodeOut
        videoStream   = media.GetVideoStreamByIndex(0)
        videooffset   = videoStream.Offset
        videoLength   = videoStream.Length
        videoWidth    = videoStream.Width
        videoHeight   = videoStream.Height
        videoFPS      = videoStream.FrameRate

        # Assign mediafile to Scenedetection VideoManager
        video_manager = VideoManager([mediaFilename])
    
        scene_manager = SceneManager()
       
        # Add ContentDetector algorithm (constructor takes detector options like threshold).
        scene_manager.add_detector(ContentDetector_VEGAS(threshold=sdConfig.threshold, min_scene_len=sdConfig.min_scene_len))
        base_timecode = video_manager.get_base_timecode()
        
        if mediaTimecodeIn > Timecode(): # if mediaTimecodeIn > 00:00:00
            startTime = FrameTimecode(timecode=int(mediaTimecodeIn.FrameCount), fps=videoFPS)
        else:
            startTime = None
        if mediaTimecodeOut > Timecode():# if mediaTimecodeOut > 00:00:00
            endTime = FrameTimecode(timecode=int(mediaTimecodeOut.FrameCount), fps=videoFPS)
        else:
            endTime = None

        try:
            # Set video_manager duration to read frames from startTime to endTime
            video_manager.set_duration(start_time=startTime, end_time=endTime)
            
            video_manager.set_downscale_factor() # use the standard downscale factors
           # Start video_manager.
            video_manager.start()

            pyVEGAS.UpdateUI()

            # Perform scene detection on video_manager.
            scene_manager.detect_scenes(frame_source=video_manager,showPreview = sdConfig.showPreview, previewFrameSkip=sdConfig.previewFrameSkip, progressBarLightness=sdConfig.progressBarLightness )

            # Obtain list of detected scenes.
            
            scene_list = scene_manager.get_scene_list(base_timecode)
           
            # Like FrameTimecodes, each scene in the scene_list can be sorted if the
            # list of scenes becomes unsorted.
            trackEventList = [] # list of event properties for the subclips

            print('List of scenes obtained:')
            for i, scene in enumerate(scene_list):
                print('    Scene %2d: Start %s / Frame %d, End %s / Frame %d' % (
                    i+1,
                    scene[0].get_timecode(), scene[0].get_frames(),
                    scene[1].get_timecode(), scene[1].get_frames(),))

 #           eventProperties: 
 #                  0:MediaType - Audio/Video
 #                  1:pathfilename
 #                  2:RecordIn (in frames) - start of subclip 
 #                  3:Length (in frames) - total length of SubClip
 #                  4:FrameRate
 #                  
                P_RecordIn  = scene[0].get_frames() # start of current scene
                P_Length    = scene[1].get_frames() - scene[0].get_frames()
                P_Filename = mediaFilename
                P_MediaType = "Video"
                mediaFrameRate  = videoFPS
 
                #                  0:Audio/Video  1:pathfilename  2:RecordIn  3:Length  4: FrameRate  
                eventProperties = [P_MediaType,   P_Filename,     P_RecordIn, P_Length, mediaFrameRate ]
        
                trackEventList.append(eventProperties)
           
            createSubClips(trackEventList)
            pyVEGAS.UpdateUI()
            print(len(trackEventList), "SubClips created")

        finally:
            video_manager.release()
    return

def processTimeline():

    """ creates subclips for all selected clips in the timeline using scene detection

    Parameters:
        none
        
    return: 
        none

    Pre condition
        one or more clips are selected in the timeline

    Post condition:
        for all selected clips in the timeline subclips have been created using scene detection
            
    """
    selEvent:List[TrackEvent_] = []
    track: Track_
    evnt: TrackEvent_
    
    
    for track in pyVEGAS.Project.Tracks: # type: Track_
        if track.MediaType == MediaType.Video:
            for evnt in track.Events: # type: TrackEvent_
                if (evnt.Selected):
                    if evnt.MediaType == MediaType.Video: # only video events
                        selEvent.append(evnt)
                
    for event in selEvent: # type: TrackEvent_
        activeTake = event.ActiveTake
        media      = activeTake.Media

        print ("Timeline: ",media.FilePath)
        mediaFilename = media.FilePath
        videoStream   = media.GetVideoStreamByIndex(0)
        takeOffset    = int (activeTake.Offset.FrameCount)
        takeLength    = int (activeTake.Length.FrameCount)
        videoWidth    = videoStream.Width
        videoHeight   = videoStream.Height
        videoFPS      = videoStream.FrameRate
        
        
        mediaTimecodeIn  = takeOffset
        mediaTimecodeOut = takeLength + mediaTimecodeIn
                
        video_manager = VideoManager([mediaFilename])
    
        scene_manager = SceneManager()

        # Add ContentDetector algorithm (constructor takes detector options like threshold).
        scene_manager.add_detector(ContentDetector_VEGAS(threshold=sdConfig.threshold, min_scene_len=sdConfig.min_scene_len))
        base_timecode = video_manager.get_base_timecode()
      

        if mediaTimecodeIn > 0: #Timecode():
            startTime = FrameTimecode(timecode=mediaTimecodeIn, fps=videoFPS)
        else:
            startTime = None
        if mediaTimecodeOut > 0:  #Timecode():
#            endTime = FrameTimecode(timecode=int(mediaTimecodeOut.FrameCount), fps=videoFPS)
            endTime = FrameTimecode(timecode=mediaTimecodeOut, fps=videoFPS)
        else:
            endTime = None

        try:
            # Set video_manager duration to read frames from startTime to endTime
            video_manager.set_duration(start_time=startTime, end_time=endTime)
            video_manager.set_downscale_factor()

           # Start video_manager.
            video_manager.start()
            
            pyVEGAS.UpdateUI()

            # Perform scene detection on clip.
            scene_manager.detect_scenes(frame_source=video_manager, showPreview = sdConfig.showPreview, previewFrameSkip=sdConfig.previewFrameSkip, progressBarLightness=sdConfig.progressBarLightness)

            # Obtain list of detected scenes. For cutting the timeline event in scenes the liit needs to be reverse
            scene_list = scene_manager.get_scene_list(base_timecode)
            
            scene_list.reverse() # Timeline events need to be cut from the end. The list needs to be reverse

            # handle Grouped video on the timeline
            groupEventList=[]
            eventisGrouped = event.IsGrouped

            if eventisGrouped: # cut all group members e.g. audio and video
                groupEventList = list(event.Group)
                
            for i, scene in enumerate(scene_list):
                print('    Scene %2d: Start %s / Frame %d, End %s / Frame %d' % (
                    i+1,
                    scene[0].get_timecode(), scene[0].get_frames(),
                    scene[1].get_timecode(), scene[1].get_frames(),))
                projectFramerate = pyVEGAS.Project.Video.FrameRate;
                cutTimecode = Timecode.FromFrames((scene[1].get_frames() - mediaTimecodeIn)*projectFramerate/videoFPS)
                
                if eventisGrouped: # cut all group members e.g. audio and video
                    splitgroupList=[]
                    for groupevent in groupEventList: # type: TrackEvent_
                        cutEvent = groupevent.Split(cutTimecode)
                        splitgroupList.append(cutEvent)
                    
                    # assign new TrackEventGroup
                    newTrackEventGroup = TrackEventGroup(pyVEGAS.Project)
                    pyVEGAS.Project.TrackEventGroups.BaseAdd(newTrackEventGroup)
                    
                    for groupevent in splitgroupList: # type: TrackEvent_
                        if groupevent:
                            result = groupevent.Group.BaseRemove(groupevent)
                            if newTrackEventGroup:
                                index = newTrackEventGroup.BaseAdd(groupevent)
                else:
                    dummyEvent = event.Split(cutTimecode)
        finally:
            video_manager.release()
    return

def FromVegas(myVEGAS: Vegas):
    global pyVEGAS
    
    pyVEGAS = myVEGAS
    # checki if MediaPool should be processed
    if sdConfig.processMediaPool:
        processMediaPool()

    # attention: Process timeline is very slow as the function for seeking the first fram of a clip is very slow
    # therefore the default is disabled - can be changed in config.json
    if sdConfig.processTimeline: 
        processTimeline()
   
    return
    

if __name__ == "__main__":
    FromVegas(pyVEGAS)