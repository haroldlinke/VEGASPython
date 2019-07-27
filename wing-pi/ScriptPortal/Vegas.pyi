# coding: utf-8
# AUTO-GENERATED FILE -- DO NOT EDIT

"""  """

class AppChangeFlag(Enum):
  """ 
  Enumeration of application change flags
  
  enum (flags) AppChangeFlag, values: AnyRuler (1), DeviceAndRemove (2), EventRecord (4), Frame (8), MarkerSelect (4194304), MarkRule (16), MediaPool (32), None (0), PeaksBuilt (64), PosFmt (128), PresetCount (256), RippleRuler (1048576), Toolbar (512), TrackFocus (1024), TrackKeyframe (2048), TrackSelect (4096), TrimmerKillFocus (8192), TrimmerSetFocus (16384), ValidatePreviews (32768), VideoPreview (65536), VideoPreview_DeferedPaint (2097152), VideoPreviewOpen (524288), VideoPreviewResize (131072), VideoSeek (262144)
  
   """

  AnyRuler = None
  DeviceAndRemove = None
  EventRecord = None
  Frame = None
  MarkRule = None
  MarkerSelect = None
  MediaPool = None
  PeaksBuilt = None
  PosFmt = None
  PresetCount = None
  RippleRuler = None
  Toolbar = None
  TrackFocus = None
  TrackKeyframe = None
  TrackSelect = None
  TrimmerKillFocus = None
  TrimmerSetFocus = None
  ValidatePreviews = None
  VideoPreview = None
  VideoPreviewOpen = None
  VideoPreviewResize = None
  VideoPreview_DeferedPaint = None
  VideoSeek = None
 
class AppSkinColorID(Enum):
  """ 
  
  enum AppSkinColorID, values: Background (15), ButtonFace (0), ButtonHighlight (3), ButtonShadow (2), ButtonText (1), ControlDark (7), ControlDarkDark (6), ControlLight (4), ControlLightLight (5), GrayText (8), Highlight (9), HighlightText (10), MenuBackground (11), MenuText (12), WindowBackground (13), WindowText (14)
  
   """

  Background = None
  ButtonFace = None
  ButtonHighlight = None
  ButtonShadow = None
  ButtonText = None
  ControlDark = None
  ControlDarkDark = None
  ControlLight = None
  ControlLightLight = None
  GrayText = None
  Highlight = None
  HighlightText = None
  MenuBackground = None
  MenuText = None
  WindowBackground = None
  WindowText = None
 

class ArchiveProjectFlags(Enum):
  """ 
  
  enum (flags) ArchiveProjectFlags, values: All (1), None (0), NoSpacesInMediaFiles (1)
  
   """

  All = None
  NoSpacesInMediaFiles = None
  None_ = None

class AudioBusMode(Enum):
  """ 
  
  enum AudioBusMode, values: Internal_00 (0), Internal03 (3), Internal04 (4), Internal05 (5), Internal06 (6), Stereo (1), Surround (2), Undefined (7)
  
   """

  Internal03 = None
  Internal04 = None
  Internal05 = None
  Internal06 = None
  Internal_00 = None
  Stereo = None
  Surround = None
  Undefined = None

class AudioBusTrack(BusTrack):
  """ Represents an audio bus track.
  AudioBusTrack(project: Project)  """

  AddFXClassID = property(None, None, None,
                          """  """
                          )

  BusType = property(None, None, None,
                     """  """
                     )


  def CanAddEnvelope(self: AudioBusTrack, type: EnvelopeType) -> bool:
    """ CanAddEnvelope(self: AudioBusTrack, type: EnvelopeType) -> bool
     """
    import System
    return System.Boolean()

  Description: str
  
  def Equals(self: AudioBusTrack, obj: object) -> bool:
    """ Determines whether the specified object is equal to the current AudioBusTrack.
          Parameters:
            obj: Object to compare with the current AudioBusTrack.
     """
    import System
    return System.Boolean()

  def GetHashCode(self: AudioBusTrack) -> int:
    """ Serves as a hash function for AudioBusTrack objects, suitable for use in hashing algorithms and data structures like a hash table.
     """
    import System
    return System.int()

  def GetRenderEnabled(self, arg0, arg1):
    """ GetRenderEnabled(self: AudioBusTrack, mix: int) -> bool
     """
    return None

  def GetRenderOrder(self, arg0, arg1):
    """ GetRenderOrder(self: AudioBusTrack, mix: int) -> int
     """
    return 1

  Index: int
  
  def IsAudio(self: AudioBusTrack) -> bool:
    """ Indicates whether the media type of the bus track is audio
     """
    import System
    return System.Boolean()

  def IsMaster(self: AudioBusTrack) -> bool:
    """ Indicates whether the audio bus track is the master bus.
     """
    import System
    return System.Boolean()

  def IsVideo(self: AudioBusTrack) -> bool:
    """ Indicates whether the bus track is the master video bus.
     """
    import System
    return System.Boolean()

  MediaType: MediaType_
  
  MonoRenderEnabled: bool
  
  MonoRenderOrder: int
  
  Mute: bool
  
  Name: str
  
  PanType: PanType_
   
  RENDER_MIX_5DOT1 = 6
  RENDER_MIX_MONO = 1
  RENDER_MIX_STEREO = 2

  def ReferenceEquals(objA: object, objB: object) -> bool:
    """ ReferenceEquals(objA: object, objB: object) -> bool
     """
    return None

  def SetRenderEnabled(self: AudioBusTrack, mix: int, value: bool):
    """ SetRenderEnabled(self: AudioBusTrack, mix: int, value: bool) """
    pass

  def SetRenderOrder(self: AudioBusTrack, mix: int, value: int):
    """ SetRenderOrder(self: AudioBusTrack, mix: int, value: int) """
    pass

  Solo: bool
  
  StereoRenderEnabled: bool
  
  StereoRenderOrder:  int
  
  SurroundRenderEnabled:  bool
  
  SurroundRenderOrder: int
    

class AudioCDProperties(object):
  """ Represents a project's audio CD properties. """

  FirstTrack: int
  
  def ReferenceEquals(objA: object, objB: object) -> bool:
    """ ReferenceEquals(objA: object, objB: object) -> bool
     """
    return None

  UPC: str
  
class AudioChannelFlags(Enum):
  """ Enumeration of audio channel flags (speaker positions).
  
  enum (flags) AudioChannelFlags, values: SpeakerBackCenter (256), SpeakerBackLeft (16), SpeakerBackRight (32), SpeakerFrontCenter (4), SpeakerFrontLeft (1), SpeakerFrontLeftOfCenter (64), SpeakerFrontRight (2), SpeakerFrontRightOfCenter (128), SpeakerLowFrequency (8), SpeakerSideLeft (512), SpeakerSideRight (1024), SpeakerTopBackCenter (65536), SpeakerTopBackLeft (32768), SpeakerTopBackRight (131072), SpeakerTopCenter (2048), SpeakerTopFrontCenter (8192), SpeakerTopFrontLeft (4096), SpeakerTopFrontRight (16384)
  
   """
  SpeakerBackCenter = None
  SpeakerBackLeft = None
  SpeakerBackRight = None
  SpeakerFrontCenter = None
  SpeakerFrontLeft = None
  SpeakerFrontLeftOfCenter = None
  SpeakerFrontRight = None
  SpeakerFrontRightOfCenter = None
  SpeakerLowFrequency = None
  SpeakerSideLeft = None
  SpeakerSideRight = None
  SpeakerTopBackCenter = None
  SpeakerTopBackLeft = None
  SpeakerTopBackRight = None
  SpeakerTopCenter = None
  SpeakerTopFrontCenter = None
  SpeakerTopFrontLeft = None
  SpeakerTopFrontRight = None

  
class AudioEvent(TrackEvent):
  """ Represents an audio event.
  
      AudioEvent(project: Project, start: Timecode, length: Timecode, name: str)
   """

  Channels: ChannelRemapping
  
  ClassicAttribute: ClassicStretchAttributes
  
  Effects: Effects_
   
  ElastiqueAttribute:  ElastiqueStretchAttributes
  
  FormantLock: bool
  
  FormantShift: float
  
  InvertPhase:  bool
   
  def IsAudio(self: AudioEvent) -> bool:
    """ IsAudio(self: AudioEvent) -> bool
     """
    import System
    return System.Boolean()

  def IsVideo(self: AudioEvent) -> bool:
    """ IsVideo(self: AudioEvent) -> bool
     """
    import System
    return System.Boolean()

  MediaType: MediaType_
  
  Method:  TimeStretchPitchShift
  
  Normalize:  bool
  
  NormalizeGain: float
  
  PitchLock: bool
  
  PitchSemis:  float
  
  def RecalculateNorm(self: AudioEvent) -> float:
    """ RecalculateNorm(self: AudioEvent) -> float
     """
    import System
    return System.Double()

  def ReferenceEquals(objA: object, objB: object) -> bool):
    """ ReferenceEquals(objA: object, objB: object) -> bool
     """
    return None

  def SetNormalize(self: AudioEvent, normalize: bool, gain: float):
    """ Set normalization values for the audio event.
          Parameters:
            - normalize: A value that indicates whether audio is normalized.
            - gain: The gain used to normalize the audio. """
    import System
    return System.Void()

  
class AudioFXBusTrack(project: Project, plugin: PlugInNode):
  """ Represents an assignable audio effect bus track.
  AudioFXBusTrack(project: Project, plugin: PlugInNode)
   """

  Effects: Effects
  
  def GetRenderEnabled(self, arg0, arg1):
    """ GetRenderEnabled(self: AudioFXBusTrack, mix: int) -> bool
     """
    return None

  def GetRenderOrder(self, arg0, arg1):
    """ GetRenderOrder(self: AudioFXBusTrack, mix: int) -> int
     """
    return 1

    def ReferenceEquals(objA: object, objB: object) -> bool:
    """ ReferenceEquals(objA: object, objB: object) -> bool
     """
    return None

  def SetRenderEnabled(self, arg0, arg1, arg2):
    """ SetRenderEnabled(self: AudioFXBusTrack, mix: int, value: bool) """
    pass

  def SetRenderOrder(self, arg0, arg1, arg2):
    """ SetRenderOrder(self: AudioFXBusTrack, mix: int, value: bool)SetRenderOrder(self: AudioBusTrack, mix: int, value: int) """
    pass

  

class AudioProperties(object):
  """ Base class for objects that represent audio properties. """

  BitDepth: int

  SampleRate: int
  

class AudioResampleQuality(Enum):
  """ 
  
  enum AudioResampleQuality, values: Best (2), Good (1), Preview (0)
  
   """

  Best = None
  Good = None
  Preview = None

class AudioStream(MediaStream):
  """  """

  AverageDataRate: int
  
  BitDepth: int
  
  Channels:  int
  
  Format:  str
  
  MediaType:  MediaType_
  
  SampleRate:  int
  

class AudioTrack(Track):
  """ AudioTrack(project: Project, index: int, name: str)
  AudioTrack(index: int, name: str)
  AudioTrack(index: int)
  AudioTrack()
   """

  def AddAudioEvent(self):
    """ AddAudioEvent(self: AudioTrack) -> AudioEvent
    AddAudioEvent(self: AudioTrack, start: Timecode, length: Timecode) -> AudioEvent
     """
    import ScriptPortal.Vegas
    return ScriptPortal.Vegas.AudioEvent()

  ArmRecord: bool
  

  BusTrack: BusTrack_
  
  InvertPhase:  bool
  
  def IsAudio(self: AudioTrack) -> bool:
    """ IsAudio(self: AudioTrack) -> bool
     """
    import System
    return System.Boolean()

  def IsVideo(self: AudioTrack) -> bool:
    """ IsVideo(self: AudioTrack) -> bool
     """
    import System
    return System.Boolean()

  MediaType: MediaType_
  
  PanCenter: Single
  
  PanX:  Single
  
  PanY:  Single
  
  
  Volume: Single
 
  

class AutomationControlAutomationState(Enum):
  """ 
  
  enum AutomationControlAutomationState, values: Armed (2), Off (0), Reading (1), Writing (3)
  
   """

  Armed = None
  Off = None
  Reading = None
  Writing = None
  
class AutomationReadWriteState(Enum):
  """ 
  
  enum AutomationReadWriteState, values: Off (0), Read (1), Write (2)
  
   """

  Off = None

  Read = None


  Write = None
  value__ = None

class AutomationWritingMode(Enum):
  """ 
  
  enum AutomationWritingMode, values: Latch (1), Touch (0)
  
   """

  Latch = None
  Touch = None

  

class BackgroundProjectActiveState(object):
  """ This class is used just with the Project.CreateBackgroundProjectActiveState() method. 
  Call that method in a using() block to make the specified project temporarily active 
  in Vegas, then when this object is disposed at the end of the block the previously 
  active project will be restored. The main reason why you would use this 
  is to gain access to the BusTracks object, which is only available for 
  the active project. 
  It is legal to nest this call or invoke it on a project that is otherwise 
  already active -- in that case, it just does nothing.  """

  def Dispose(self):
    """ Dispose(self: BackgroundProjectActiveState) """
    import System
    return System.Void()

  def ReferenceEquals(objA: object, objB: object) -> bool:
    """ ReferenceEquals(objA: object, objB: object) -> bool
     """
    return None

class BaseList(object):
  """ Base class for most collections in the Vegas object model. """

  def Add(self: BaseList[T], item: object) -> int:
    """ Add(self: BaseList[T], item: object) -> int
    Add(self: BaseList[T], item: T) """
    import System
    return System.int()

  def BaseAdd(self: BaseList[T], item: T) -> int:
    """ BaseAdd(self: BaseList[T], item: T) -> int
     """
    return 1

  def BaseCopy(self: BaseList[T], array: Array, index: int):
    """ BaseCopy(self: BaseList[T], array: Array, index: int) """
    pass

  def BaseIndex(self: BaseList[T], item: T) -> int:
    """ BaseIndex(self: BaseList[T], item: T) -> int
     """
    return 1

  def BaseRemove(self: BaseList[T], item: T) -> bool:
    """ BaseRemove(self: BaseList[T], item: T) -> bool
     """
    return None

  def CheckItemRange(self: BaseList[T], index: int):
    """ CheckItemRange(self: BaseList[T], index: int) """
    pass

  def Clear(self: BaseList[T]):
    """ Clear(self: BaseList[T]) """
    import System
    return System.Void()

  def Contains(self: BaseList[T], item: object) -> bool:
    """ Contains(self: BaseList[T], item: object) -> bool
    Contains(self: BaseList[T], item: T) -> bool
     """
    import System
    return System.Boolean()

  def CopyTo(self: BaseList[T], array: Array, index: int)CopyTo(self: BaseList[T], array: Array[T], index: int):
    """ CopyTo(self: BaseList[T], array: Array, index: int)CopyTo(self: BaseList[T], array: Array[T], index: int) """
    import System
    return System.Void()

  Count: int
  
  def GetCount(self: BaseList[T]) -> int:
    """ GetCount(self: BaseList[T]) -> int
     """
    return 1

  def GetEnumerator(self: BaseList[T]) -> IEnumerator[T]:
    """ GetEnumerator(self: BaseList[T]) -> IEnumerator[T]
     """
    import System.Collections.Generic
    return System.Collections.Generic.IEnumerator`1()

  def GetItem(self: BaseList[T], index: int) -> T:
    """ GetItem(self: BaseList[T], index: int) -> T
     """
    return None

  def IndexOf(self: BaseList[T], item: object) -> int:
    """ IndexOf(self: BaseList[T], item: object) -> int
    IndexOf(self: BaseList[T], item: T) -> int
     """
    import System
    return System.int()

  def Insert(self: BaseList[T], index: int, item: object):
    """ Insert(self: BaseList[T], index: int, item: object)
    Insert(self: BaseList[T], index: int, item: T) """
    import System
    return System.Void()

  IsFixedSize: bool
  
  IsReadOnly:  bool
  
  IsSynchronized:  bool
  
  Item = None

  def ReferenceEquals(objA: object, objB: object) -> bool:
    """ ReferenceEquals(objA: object, objB: object) -> bool
     """
    return None

  def Remove(self: BaseList[T], item: T) -> bool:
    """ Remove(self: BaseList[T], item: T) -> bool
    Remove(self: BaseList[T], item: object) """
    import System
    return System.Boolean()

  def RemoveAt(self: BaseList[T], index: int):
    """ RemoveAt(self: BaseList[T], index: int) """
    import System
    return System.Void()

  SyncRoot:  object
  

class BaseMarkerList(BaseList[T]):
  """  """

  def BaseAdd(self, arg0=None, arg1=None):
    """ BaseAdd(self: BaseMarkerList[T], item: T) -> int
     """
    return 1

  def BaseIndex(self, arg0=None, arg1=None):
    """ BaseIndex(self: BaseMarkerList[T], item: T) -> int
     """
    return 1

  def BaseRemove(self, arg0=None, arg1=None):
    """ BaseRemove(self: BaseMarkerList[T], item: T) -> bool
     """
    return None

  def GetCount(self, arg0=None):
    """ GetCount(self: BaseMarkerList[T]) -> int
     """
    return 1

  def GetItem(self, arg0=None, arg1=None):
    """ GetItem(self: BaseMarkerList[T], index: int) -> T
     """
    return None

  def InitializeItem(self, arg0=None, arg1=None, arg2=None):
    """ InitializeItem(self: BaseMarkerList[T], item: T, markerID: int) """
    pass

  def ReferenceEquals(objA: object, objB: object) -> bool:
    """ ReferenceEquals(objA: object, objB: object) -> bool
     """
    return None

  myCOM = None
  myMarkerType = None
  myProject = None

class BaseMediaMarkerList(BaseMarkerList[T]):
  """ BaseMediaMarkerList[T]()
   """

  def BaseIndex(self, arg0=None, arg1=None):
    """ BaseIndex(self: BaseMediaMarkerList[T], item: T) -> int
     """
    return 1

  def InitializeItem(self, arg0=None, arg1=None, arg2=None):
    """ InitializeItem(self: BaseMediaMarkerList[T], item: T, markerID: int) """
    pass

  def ReferenceEquals(objA: object, objB: object) -> bool:
    """ ReferenceEquals(objA: object, objB: object) -> bool
     """
    return None

  myCOM = None
  myMarkerType = None
  myMediaID = None
  myProject = None

class BaseTrackMotionKeyframe(object):
  """ Base class for all track motion keyframes. """

  def Equals(self: BaseTrackMotionKeyframe, that: object) -> bool:
    """ Equals(self: BaseTrackMotionKeyframe, that: object) -> bool
     """
    import System
    return System.Boolean()

  
  Height: float
  
  Index: int
  
  def IsValid(self: BaseTrackMotionKeyframe) -> bool:
    """ IsValid(self: BaseTrackMotionKeyframe) -> bool
     """
    import System
    return System.Boolean()

  def MembersEqual(self: BaseTrackMotionKeyframe, that: BaseTrackMotionKeyframe) -> bool:
    """ MembersEqual(self: BaseTrackMotionKeyframe, that: BaseTrackMotionKeyframe) -> bool
     """
    return None

  OrientationZ: float
  
  Position: Timecode
  
  PositionX:  float
  
  PositionY:  float
  
  RotationOffsetX: float

  RotationOffsetY: float
  
  RotationZ: float
  
  Selected: bool
  
  
  Smoothness: float
  
  Type: VideoKeyframeType
  
  Width: float
  
  

class BaseTrackMotionKeyframeList(BaseList[T]):
  """ Base class for lists of track motion keyframes.   """

  def BaseIndex(self, arg0=None, arg1=None):
    """ BaseIndex(self: BaseTrackMotionKeyframeList[T], item: T) -> int
     """
    return 1

  def BaseRemove(self, arg0=None, arg1=None):
    """ BaseRemove(self: BaseTrackMotionKeyframeList[T], item: T) -> bool
     """
    return None

  def Clear(self):
    """ Clear(self: BaseTrackMotionKeyframeList[T]) """
    import System
    return System.Void()

  def GetCount(self, arg0=None):
    """ GetCount(self: BaseTrackMotionKeyframeList[T]) -> int
     """
    return 1

  def GetItem(self, arg0=None, arg1=None):
    """ GetItem(self: BaseTrackMotionKeyframeList[T], index: int) -> T
     """
    return None

  def ReferenceEquals(objA: object, objB: object) -> bool:
    """ ReferenceEquals(objA: object, objB: object) -> bool
     """
    return None

 
class BeatValue(Enum):
  """ Enumeration of beat values.
  
  enum BeatValue, values: Eighth (8), Half (2), Invalid (0), Quarter (4), Sixteenth (16), ThirtySecond (32), Whole (1)
  
   """

  Eighth = None
  Half = None
  Invalid = None
  Quarter = None
  Sixteenth = None
  ThirtySecond = None
  Whole = None


class BoolListSetting(ListSetting[bool]):
  """ BoolListSetting(name: str)
   """

  def ItemFromString(self, arg0, arg1):
    """ ItemFromString(self: BoolListSetting, s: str) -> bool
     """
    return None

  def ItemToString(self, arg0, arg1):
    """ ItemToString(self: BoolListSetting, item: bool) -> str
     """
    return ""

  Name = None

  def ReferenceEquals(objA: object, objB: object) -> bool:
    """ ReferenceEquals(objA: object, objB: object) -> bool
     """
    return None

  Value = None

class BoolSetting(XmlSetting):
  """ BoolSetting(name: str, val: bool)
   """

  def FromString(self, value):
    """ FromString(self: BoolSetting, value: str) """
    import System
    return System.Void()

  Name = None

  def ReferenceEquals(objA: object, objB: object) -> bool:
    """ ReferenceEquals(objA: object, objB: object) -> bool
     """
    return None

  def ToString(self):
    """ ToString(self: BoolSetting) -> str
     """
    import System
    return System.String()

  Value = None

class BurgerMenuConfig(object):
  """ BurgerMenuConfig()
   """

  def AddItem(self, isOn, name):
    """ AddItem(self: BurgerMenuConfig, isOn: bool, name: str) """
    import System
    return System.Void()

  CancelDlg: bool
  
  def ClearItems(self):
    """ ClearItems(self: BurgerMenuConfig) """
    import System
    return System.Void()

  Description:  str
  
  def GetCount(self, count):
    """ GetCount(self: BurgerMenuConfig) -> int
     """
    import System
    return System.Void()

  def GetItem(self, name, isOn):
    """ GetItem(self: BurgerMenuConfig, name: str) -> bool
     """
    import System
    return System.Void()

  def GetItemByIndex(self, index, name, isOn):
    """ GetItemByIndex(self: BurgerMenuConfig, index: int) -> (str, bool)
     """
    import System
    return System.Void()

  def GetItems(self):
    """ GetItems(self: BurgerMenuConfig) -> Dictionary[str, bool]
     """
    import System.Collections.Generic
    return System.Collections.Generic.Dictionary`2()

  def ReferenceEquals(objA: object, objB: object) -> bool:
    """ ReferenceEquals(objA: object, objB: object) -> bool
     """
    return None

  def SetItem(self, name, set):
    """ SetItem(self: BurgerMenuConfig, name: str, set: bool) """
    import System
    return System.Void()

  Title:  str
   
class BusTrack_(object):
  """ Represents a bus track. """

  Description:  str
    

  Effects: Effects_
   
  

  Envelopes:  Envelopes_
  

  def Equals(self, that):
    """ Equals(self: BusTrack, that: object) -> bool
     """
    import System
    return System.Boolean()

  def GetHashCode(self):
    """ GetHashCode(self: BusTrack) -> int
     """
    import System
    return System.int()

  Index:  int
  
  def IsAudio(self: BusTrack) -> bool:
    """ IsAudio(self: BusTrack) -> bool
     """
    import System
    return System.Boolean()

  def IsMaster(self: BusTrack) -> bool:
    """ IsMaster(self: BusTrack) -> bool
     """
    import System
    return System.Boolean()

  def IsValid(self: BusTrack) -> bool:
    """ IsValid(self: BusTrack) -> bool
     """
    import System
    return System.Boolean()

  def IsVideo(self: BusTrack) -> bool:
    """ IsVideo(self: BusTrack) -> bool
     """
    import System
    return System.Boolean()

  MediaType:  MediaType_
   
  def MembersEqual(self, arg0, arg1):
    """ MembersEqual(self: BusTrack, that: BusTrack) -> bool
     """
    return None

  Name: str 

  Project:  Project_
   

  def ReferenceEquals(objA: object, objB: object) -> bool:
    """ ReferenceEquals(objA: object, objB: object) -> bool
     """
    return None

  def Validate(self, arg0):
    """ Validate(self: BusTrack) """
    pass

  

class BusTracks(BaseList[BusTrack]):
  """ Collection of bus tracks. """

  def BaseAdd(self: BusTracks, item: BusTrack) -> int:
    """ BaseAdd(self: BusTracks, item: BusTrack) -> int
     """
    return 1

  def BaseIndex(self: BusTracks, item: BusTrack) -> int:
    """ BaseIndex(self: BusTracks, item: BusTrack) -> int
     """
    return 1

  def BaseRemove(self: BusTracks, item: BusTrack) -> bool:
    """ BaseRemove(self: BusTracks, item: BusTrack) -> bool
     """
    return None

  def Clear(self: BusTracks):
    """ Clear(self: BusTracks) """
    import System
    return System.Void()

  def GetCount(self, arg0):
    """ GetCount(self: BusTracks) -> int
     """
    return 1

  def GetItem(self, arg0, arg1):
    """ GetItem(self: BusTracks, index: int) -> BusTrack
     """
    return None

  def ReferenceEquals(objA: object, objB: object) -> bool:
    """ ReferenceEquals(objA: object, objB: object) -> bool
     """
    return None

class BusType(Enum):
  """ 
  
  enum BusType, values: All (4), FXBus (2), SubBus (1), Unknown (0), VideoBus (3)
  
   """

  All = None
  FXBus = None
  SubBus = None
  Unknown = None
  VideoBus = None
  

class CDMarker(Marker):
  """ CDMarker()
  CDMarker(position: Timecode)
  CDMarker(position: Timecode, label: str)
   """

  def Equals(self, obj):
    """ Equals(self: CDMarker, obj: object) -> bool
     """
    import System
    return System.Boolean()

  def GetHashCode(self):
    """ GetHashCode(self: CDMarker) -> int
     """
    import System
    return System.int()

  def ReferenceEquals(objA: object, objB: object) -> bool:
    """ ReferenceEquals(objA: object, objB: object) -> bool
     """
    return None

  

class CDMarkerList(BaseMarkerList[CDMarker]):
  """ CDMarkerList()
   """

  def ReferenceEquals(objA: object, objB: object) -> bool:
    """ ReferenceEquals(objA: object, objB: object) -> bool
     """
    return None

 

class CDRegion(Region):
  """ Represents a CD track region marker.
  CDRegion()
  CDRegion(position: Timecode, length: Timecode)
  CDRegion(position: Timecode, length: Timecode, label: str)
   """

  def Equals(self, obj):
    """ Equals(self: CDRegion, obj: object) -> bool
     """
    import System
    return System.Boolean()

  def GetHashCode(self):
    """ GetHashCode(self: CDRegion) -> int
     """
    import System
    return System.int()

  def ReferenceEquals(objA: object, objB: object) -> bool:
    """ ReferenceEquals(objA: object, objB: object) -> bool
     """
    return None

  myCOM = None
  myMarkerID = None
  myProject = None

class CDRegionList(BaseMarkerList[CDRegion]):
  """ CDRegionList()
   """

  def ReferenceEquals(objA: object, objB: object) -> bool:
    """ ReferenceEquals(objA: object, objB: object) -> bool
     """
    return None

  


class CaptionDoubleClickEventArgs(EventArgs):
  """ CaptionDoubleClickEventArgs(size: Size)
   """

  ControlSize:  Size
  
  Empty = None
  GenericSizeChange: bool
  

  NoSizeChange:  bool
  

  def ReferenceEquals(objA: object, objB: object) -> bool:
    """ ReferenceEquals(objA: object, objB: object) -> bool
     """
    return None

class CaptionDoubleClickEventHandler(MulticastDelegate):
  """ CaptionDoubleClickEventHandler(object: object, method: IntPtr)
   """

  def BeginInvoke(self, sender, args, callback, object):
    """ BeginInvoke(self: CaptionDoubleClickEventHandler, sender: object, args: CaptionDoubleClickEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult
     """
    import System
    return System.IAsyncResult()

  def Combine(self, arg0, arg1):
    """ Combine(a: Delegate, b: Delegate) -> Delegate
    Combine(*delegates: Array[Delegate]) -> Delegate
     """
    return None

  def CreateDelegate(self, arg0, arg1, arg2):
    """ CreateDelegate(type: Type, target: object, method: str) -> Delegate
    CreateDelegate(type: Type, target: object, method: str, ignoreCase: bool) -> Delegate
    CreateDelegate(type: Type, target: object, method: str, ignoreCase: bool, throwOnBindFailure: bool) -> Delegate
    CreateDelegate(type: Type, target: Type, method: str) -> Delegate
    CreateDelegate(type: Type, target: Type, method: str, ignoreCase: bool) -> Delegate
    CreateDelegate(type: Type, target: Type, method: str, ignoreCase: bool, throwOnBindFailure: bool) -> Delegate
    CreateDelegate(type: Type, method: MethodInfo, throwOnBindFailure: bool) -> Delegate
    CreateDelegate(type: Type, firstArgument: object, method: MethodInfo) -> Delegate
    CreateDelegate(type: Type, firstArgument: object, method: MethodInfo, throwOnBindFailure: bool) -> Delegate
    CreateDelegate(type: Type, method: MethodInfo) -> Delegate
     """
    return None

  def EndInvoke(self, result):
    """ EndInvoke(self: CaptionDoubleClickEventHandler, result: IAsyncResult) """
    import System
    return System.Void()

  def Invoke(self, sender, args):
    """ Invoke(self: CaptionDoubleClickEventHandler, sender: object, args: CaptionDoubleClickEventArgs) """
    import System
    return System.Void()

  def ReferenceEquals(objA: object, objB: object) -> bool:
    """ ReferenceEquals(objA: object, objB: object) -> bool
     """
    return None

  def Remove(self, arg0, arg1):
    """ Remove(source: Delegate, value: Delegate) -> Delegate
     """
    return None

  def RemoveAll(self, arg0, arg1):
    """ RemoveAll(source: Delegate, value: Delegate) -> Delegate
     """
    return None

class CaptureDockWnd(DockableControl):
  """ CaptureDockWnd()
   """

  AppWindowClosed = None
  AppWindowClosing = None

  class AppWindowClosingEventArgs(CancelEventArgs):
    """ AppWindowClosingEventArgs(hwndApp: IntPtr)
     """

    Empty = None

    def ReferenceEquals(objA: object, objB: object) -> bool:
      """ ReferenceEquals(objA: object, objB: object) -> bool
       """
      return None

  AutoSizeChanged = None
  AutoValidateChanged = None
  BackColorChanged = None
  BackgroundImageChanged = None
  BackgroundImageLayoutChanged = None

  def BatchCapture(self: CaptureDockWnd, count: int, mediaList: Array[CaptureMediaInfo], feedback: IVidCapFeedback):
    """ BatchCapture(self: CaptureDockWnd, count: int, mediaList: Array[CaptureMediaInfo], feedback: IVidCapFeedback) """
    import System
    return System.Void()

  BindingContextChanged = None
  CaptionDoubleClick = None
  CausesValidationChanged = None
  ChangeUICues = None
  CheckForIllegalCrossThreadCalls = False
  Click = None
  ClientSizeChanged = None
  Closed = None
  Closing = None
  ContextMenuChanged = None
  ContextMenuStripChanged = None

  class ControlAccessibleObject(AccessibleObject):
    """ ControlAccessibleObject(ownerControl: Control)
     """

    DefaultAction = property(None, None, None,
                             """ Get: DefaultAction(self: ControlAccessibleObject) -> str
                             
                              """
                             )

    Description = property(None, None, None,
                           """ Get: Description(self: ControlAccessibleObject) -> str
                           
                            """
                           )


    def GetHelpTopic(self, fileName):
      """ GetHelpTopic(self: ControlAccessibleObject) -> (int, str)
       """
      import System
      return System.int()

    Handle = property(None, None, None,
                      """ Get: Handle(self: ControlAccessibleObject) -> IntPtr
                      
                      Set: Handle(self: ControlAccessibleObject) = value
                       """
                      )

    Help = property(None, None, None,
                    """ Get: Help(self: ControlAccessibleObject) -> str
                    
                     """
                    )

    KeyboardShortcut = property(None, None, None,
                                """ Get: KeyboardShortcut(self: ControlAccessibleObject) -> str
                                
                                 """
                                )

    Name = property(None, None, None,
                    """ Get: Name(self: ControlAccessibleObject) -> str
                    
                    Set: Name(self: ControlAccessibleObject) = value
                     """
                    )


    def NotifyClients(self, accEvent):
      """ NotifyClients(self: ControlAccessibleObject, accEvent: AccessibleEvents)NotifyClients(self: ControlAccessibleObject, accEvent: AccessibleEvents, childID: int)NotifyClients(self: ControlAccessibleObject, accEvent: AccessibleEvents, objectID: int, childID: int) """
      import System
      return System.Void()

    Owner = property(None, None, None,
                     """ Get: Owner(self: ControlAccessibleObject) -> Control
                     
                      """
                     )

    Parent = property(None, None, None,
                      """ Get: Parent(self: ControlAccessibleObject) -> AccessibleObject
                      
                       """
                      )


    def ReferenceEquals(objA: object, objB: object) -> bool:
      """ ReferenceEquals(objA: object, objB: object) -> bool
       """
      return None

    Role = property(None, None, None,
                    """ Get: Role(self: ControlAccessibleObject) -> AccessibleRole
                    
                     """
                    )


    def ToString(self):
      """ ToString(self: ControlAccessibleObject) -> str
       """
      import System
      return System.String()

  ControlAdded = None

  class ControlCollection(ArrangedElementCollection):
    """ ControlCollection(owner: Control)
     """

    def Add(self, value):
      """ Add(self: ControlCollection, value: Control) """
      import System
      return System.Void()

    def AddRange(self, controls):
      """ AddRange(self: ControlCollection, controls: Array[Control]) """
      import System
      return System.Void()

    def Clear(self):
      """ Clear(self: ControlCollection) """
      import System
      return System.Void()

    def Contains(self, control):
      """ Contains(self: ControlCollection, control: Control) -> bool
       """
      import System
      return System.Boolean()

    def ContainsKey(self, key):
      """ ContainsKey(self: ControlCollection, key: str) -> bool
       """
      import System
      return System.Boolean()

    def Find(self, key, searchAllChildren):
      """ Find(self: ControlCollection, key: str, searchAllChildren: bool) -> Array[Control]
       """
      import System.Windows.Forms
      return System.Windows.Forms.Control[]()

    def GetChildIndex(self, child):
      """ GetChildIndex(self: ControlCollection, child: Control) -> int
      GetChildIndex(self: ControlCollection, child: Control, throwException: bool) -> int
       """
      import System
      return System.int()

    def GetEnumerator(self):
      """ GetEnumerator(self: ControlCollection) -> IEnumerator
       """
      import System.Collections
      return System.Collections.IEnumerator()

    def IndexOf(self, control):
      """ IndexOf(self: ControlCollection, control: Control) -> int
       """
      import System
      return System.int()

    def IndexOfKey(self, key):
      """ IndexOfKey(self: ControlCollection, key: str) -> int
       """
      import System
      return System.int()

    Item = None
    Owner = property(None, None, None,
                     """ Get: Owner(self: ControlCollection) -> Control
                     
                      """
                     )


    def ReferenceEquals(objA: object, objB: object) -> bool:
      """ ReferenceEquals(objA: object, objB: object) -> bool
       """
      return None

    def Remove(self, value):
      """ Remove(self: ControlCollection, value: Control) """
      import System
      return System.Void()

    def RemoveAt(self, index):
      """ RemoveAt(self: ControlCollection, index: int) """
      import System
      return System.Void()

    def RemoveByKey(self, key):
      """ RemoveByKey(self: ControlCollection, key: str) """
      import System
      return System.Void()

    def SetChildIndex(self, child, newIndex):
      """ SetChildIndex(self: ControlCollection, child: Control, newIndex: int) """
      import System
      return System.Void()

  ControlRemoved = None
  CursorChanged = None
  DefaultBackColor = None
  DefaultFont = None
  DefaultForeColor = None
  DefaultSize = property(None, None, None,
                         """  """
                         )

  DisplayName = property(None, None, None,
                         """ Get: DisplayName(self: CaptureDockWnd) -> str
                         
                          """
                         )


  def Dispose(self):
    """ Dispose(self: CaptureDockWnd, disposing: bool) """
    import System
    return System.Void()

  Disposed = None
  DockChanged = None

  class DockPaddingEdges(object):
    """  """

    All = property(None, None, None,
                   """ Get: All(self: DockPaddingEdges) -> int
                   
                   Set: All(self: DockPaddingEdges) = value
                    """
                   )

    Bottom = property(None, None, None,
                      """ Get: Bottom(self: DockPaddingEdges) -> int
                      
                      Set: Bottom(self: DockPaddingEdges) = value
                       """
                      )


    def Equals(self, other):
      """ Equals(self: DockPaddingEdges, other: object) -> bool
       """
      import System
      return System.Boolean()

    def GetHashCode(self):
      """ GetHashCode(self: DockPaddingEdges) -> int
       """
      import System
      return System.int()

    Left = property(None, None, None,
                    """ Get: Left(self: DockPaddingEdges) -> int
                    
                    Set: Left(self: DockPaddingEdges) = value
                     """
                    )


    def ReferenceEquals(objA: object, objB: object) -> bool:
      """ ReferenceEquals(objA: object, objB: object) -> bool
       """
      return None

    Right = property(None, None, None,
                     """ Get: Right(self: DockPaddingEdges) -> int
                     
                     Set: Right(self: DockPaddingEdges) = value
                      """
                     )


    def ToString(self):
      """ ToString(self: DockPaddingEdges) -> str
       """
      import System
      return System.String()

    Top = property(None, None, None,
                   """ Get: Top(self: DockPaddingEdges) -> int
                   
                   Set: Top(self: DockPaddingEdges) = value
                    """
                   )


  class DockPaddingEdgesConverter(TypeConverter):
    """ DockPaddingEdgesConverter()
     """

    def GetProperties(self, context, value, attributes):
      """ GetProperties(self: DockPaddingEdgesConverter, context: ITypeDescriptorContext, value: object, attributes: Array[Attribute]) -> PropertyDescriptorCollection
       """
      import System.ComponentModel
      return System.ComponentModel.PropertyDescriptorCollection()

    def GetPropertiesSupported(self, context):
      """ GetPropertiesSupported(self: DockPaddingEdgesConverter, context: ITypeDescriptorContext) -> bool
       """
      import System
      return System.Boolean()

    def ReferenceEquals(objA: object, objB: object) -> bool:
      """ ReferenceEquals(objA: object, objB: object) -> bool
       """
      return None

    class SimplePropertyDescriptor(PropertyDescriptor):
      """  """

      def FindMethod(self, arg0, arg1, arg2=None, arg3=None):
        """ FindMethod(componentClass: Type, name: str, args: Array[Type], returnType: Type) -> MethodInfo
        FindMethod(componentClass: Type, name: str, args: Array[Type], returnType: Type, publicOnly: bool) -> MethodInfo
         """
        return None

      def GetInvokee(self, arg0, arg1):
        """ GetInvokee(componentClass: Type, component: object) -> object
         """
        return None

      def GetSite(self, arg0):
        """ GetSite(component: object) -> ISite
         """
        return None

      def ReferenceEquals(objA: object, objB: object) -> bool:
        """ ReferenceEquals(objA: object, objB: object) -> bool
         """
        return None

    class StandardValuesCollection(object):
      """ StandardValuesCollection(values: ICollection)
       """

      def CopyTo(self, array, index):
        """ CopyTo(self: StandardValuesCollection, array: Array, index: int) """
        import System
        return System.Void()

      Count = property(None, None, None,
                       """ Get: Count(self: StandardValuesCollection) -> int
                       
                        """
                       )


      def GetEnumerator(self):
        """ GetEnumerator(self: StandardValuesCollection) -> IEnumerator
         """
        import System.Collections
        return System.Collections.IEnumerator()

      Item = None

      def ReferenceEquals(objA: object, objB: object) -> bool:
        """ ReferenceEquals(objA: object, objB: object) -> bool
         """
        return None

  DockWindowID:  int
  DoubleClick = None
  DpiChangedAfterParent = None
  DpiChangedBeforeParent = None
  DragDrop = None
  DragEnter = None
  DragLeave = None
  DragOver = None
  EnabledChanged = None
  Enter = None
  FontChanged = None
  ForeColorChanged = None

  def FromChildHandle(self, arg0):
    """ FromChildHandle(handle: IntPtr) -> Control
     """
    return None

  def FromHandle(self, arg0):
    """ FromHandle(handle: IntPtr) -> Control
     """
    return None

  GiveFeedback = None
  GotFocus = None

  def HandleAppActivated(self, arg0, arg1, arg2):
    """ HandleAppActivated(self: CaptureDockWnd, sender: object, args: EventArgs) """
    pass

  def HandleAppDeactivate(self, arg0, arg1, arg2):
    """ HandleAppDeactivate(self: CaptureDockWnd, sender: object, args: EventArgs) """
    pass

  def HandleAppSkinChanged(self, sender, args):
    """ HandleAppSkinChanged(self: CaptureDockWnd, sender: object, args: EventArgs) """
    import System
    return System.Void()

  HandleCreated = None
  HandleDestroyed = None

  def HandleProjectOpened(self, arg0, arg1, arg2):
    """ HandleProjectOpened(self: CaptureDockWnd, sender: object, args: EventArgs) """
    pass

  def HandleProjectSaving(self, sender, args):
    """ HandleProjectSaving(self: CaptureDockWnd, sender: object, args: EventArgs) """
    import System
    return System.Void()

  HelpRequested = None
  IDW_Capture = None
  ImeModeChanged = None

  def InitCaptureController(self, arg0):
    """ InitCaptureController(self: CaptureDockWnd) """
    pass

  def InitSettings(self, arg0):
    """ InitSettings(self: CaptureDockWnd) """
    pass

  Invalidated = None
  IsFocusPane = None

  def IsKeyLocked(self, arg0):
    """ IsKeyLocked(keyVal: Keys) -> bool
     """
    return None

  def IsMnemonic(self, arg0, arg1):
    """ IsMnemonic(charCode: Char, text: str) -> bool
     """
    return None

  KeyDown = None
  KeyPress = None
  KeyUp = None

  def KillFocus(self):
    """ KillFocus(self: CaptureDockWnd) """
    import System
    return System.Void()

  Layout = None
  Leave = None
  Load = None
  Loaded = None
  LocationChanged = None
  LostFocus = None
  MarginChanged = None
  ModifierKeys = None
  MouseButtons = None
  MouseCaptureChanged = None
  MouseClick = None
  MouseDoubleClick = None
  MouseDown = None
  MouseEnter = None
  MouseHover = None
  MouseLeave = None
  MouseMove = None
  MousePosition = None
  MouseUp = None
  MouseWheel = None
  Move = None

  def OnAppWindowClosed(self, arg0, arg1):
    """ OnAppWindowClosed(self: CaptureDockWnd, args: EventArgs) """
    pass

  def OnAppWindowClosing(self, arg0, arg1):
    """ OnAppWindowClosing(self: CaptureDockWnd, args: CancelEventArgs) """
    pass

  def OnCaptionDoubleClick(self, arg0, arg1):
    """ OnCaptionDoubleClick(self: CaptureDockWnd, args: CaptionDoubleClickEventArgs) """
    pass

  def OnClosed(self, arg0, arg1):
    """ OnClosed(self: CaptureDockWnd, args: EventArgs) """
    pass

  def OnClosing(self, arg0, arg1):
    """ OnClosing(self: CaptureDockWnd, args: CancelEventArgs) """
    pass

  def OnLoad(self, arg0, arg1):
    """ OnLoad(self: CaptureDockWnd, args: EventArgs) """
    pass

  def OnLoaded(self, arg0, arg1):
    """ OnLoaded(self: CaptureDockWnd, args: EventArgs) """
    pass

  PaddingChanged = None
  Paint = None
  ParentChanged = None
  ParentWindowChanged = None
  PersistDockWindowState: bool
  
  PreviewKeyDown = None
  QueryAccessibilityHelp = None
  QueryContinueDrag = None

  def ReadyToClose(self):
    """ ReadyToClose(self: CaptureDockWnd) """
    import System
    return System.Void()

  def ReferenceEquals(objA: object, objB: object) -> bool:
    """ ReferenceEquals(objA: object, objB: object) -> bool
     """
    return None

  def ReflectMessage(self, arg0, arg1):
    """ ReflectMessage(hWnd: IntPtr, m: Message) -> (bool, Message)
     """
    return (None, None)

  RegionChanged = None
  Resize = None
  RightToLeftChanged = None
  Scroll = None
  ScrollStateAutoScrolling = 1
  ScrollStateFullDrag = 16
  ScrollStateHScrollVisible = 2
  ScrollStateUserHasScrolled = 8
  ScrollStateVScrollVisible = 4

  def SetFocus(self):
    """ SetFocus(self: CaptureDockWnd) """
    import System
    return System.Void()

  SizeChanged = None
  StyleChanged = None
  SystemColorsChanged = None
  TabIndexChanged = None
  TabStopChanged = None
  TextChanged = None
  Validated = None
  Validating = None
  VisibleChanged = None
  WindowMove = None
  myInstanceName = None
  myVegas = None

class ChannelRemapping(Enum):
  """ 
  Enumeration of audio channel remapping modes.
  enum ChannelRemapping, values: DisableLeft (1001), DisableRight (1002), Mono (1005), MuteLeft (1003), MuteRight (1004), None (1000), Swap (1006)
  
   """

  DisableLeft = None
  DisableRight = None
  Mono = None
  MuteLeft = None
  MuteRight = None
  None_ = None
  Swap = None




class CommandCategory(Enum):
  """ 
  Custom command categories
  enum CommandCategory, values: Edit (0), MAX (4), Script (3), Tools (2), Unknown (-1), View (1)
  
   """

  Edit = None
  MAX = None
  Script = None
  Tools = None
  Unknown = None
  View = None


class CommandMarker(Marker):
  """ Represents a command marker.
  CommandMarker()
  CommandMarker(position: Timecode)
  CommandMarker(position: Timecode, cmd: MarkerCommandType, param: str)
  CommandMarker(position: Timecode, cmd: MarkerCommandType, param: str, comment: str)
   """

  CommandParameter: str
   
  CommandType:   MarkerCommandType
  
  Comment: str
  

  def Equals(self, obj):
    """ Equals(self: CommandMarker, obj: object) -> bool
     """
    import System
    return System.Boolean()

  def GetHashCode(self):
    """ GetHashCode(self: CommandMarker) -> int
     """
    import System
    return System.int()

  Label:  str
   
  def SetCommand(self: CommandMarker, cmdType: MarkerCommandType, param: str):
    """ SetCommand(self: CommandMarker, cmdType: MarkerCommandType, param: str) """
    import System
    return System.Void()

  

class CommandMarkerList(BaseMarkerList[CommandMarker]):
  """ List of CommandMarker objects.
  CommandMarkerList()
   """

  def ReferenceEquals(objA: object, objB: object) -> bool:
    """ ReferenceEquals(objA: object, objB: object) -> bool
     """
    return None

  

class CommunityID(Enum):
  """ 
  
  enum CommunityID, values: CID_FACEBOOK (17), CID_UNKNOWN (0), CID_VIMEO (16), CID_YOUTUBE (1)
  
   """

  CID_FACEBOOK = None
  CID_UNKNOWN = None
  CID_VIMEO = None
  CID_YOUTUBE = None

  

class CompositeMode(Enum):
  """ 
  Video track composite modes.
  enum CompositeMode, values: Add (4), Burn (12), Custom (1), Cut (7), Darken (13), Difference (15), DifferenceSquared (16), Dodge (11), HardLight (10), Invalid (0), Lighten (14), Multiply (6), Overlay (9), Screen (8), SrcAlpha (2), SrcAlpha3D (3), Subtract (5)
  
   """

  Add = None
  Burn = None
  Custom = None
  Cut = None
  Darken = None
  Difference = None
  DifferenceSquared = None
  Dodge = None
  HardLight = None
  Invalid = None
  Lighten = None
  Multiply = None
  Overlay = None
  Screen = None
  SrcAlpha = None
  SrcAlpha3D = None
  Subtract = None


class CurveType(Enum):
  """ 
  Enumeration of envelope curve types.
  enum CurveType, values: Fast (2), Invalid (-10), Linear (1), None (0), Sharp (-4), Slow (-2), Smooth (4)
  
   """

  Fast = None
  Invalid = None
  Linear = None
  None_ = None
  Sharp = None
  Slow = None
  Smooth = None


class CustomCommand(object):
  """ Represents a command that extends or customizes the Vegas application.
  CustomCommand(category: CommandCategory, name: str)
   """

  def AddChild(self, child):
    """ AddChild(self: CustomCommand, child: CustomCommand) -> bool
     """
    import System
    return System.Boolean()

  CanAddToKeybindings: bool
   

  CanAddToMenu:  bool
  
  CanAddToToolbar: bool
  
  Category: CommandCategory
  
  def CategoryDisplayName(category: CommandCategory) -> str:
    """ CategoryDisplayName(category: CommandCategory) -> str
     """
    import System
    return System.String()

  Checked: bool

  DisplayName:  str
   
  Enabled: bool
  
  FullDisplayName: str

  FullName: str
  
  def GetChildren(self: CustomCommand) -> ICollection[CustomCommand]:
    """ GetChildren(self: CustomCommand) -> ICollection[CustomCommand]
     """
    import System.Collections.Generic
    return System.Collections.Generic.ICollection`1()

  def HasChildren(self: CustomCommand) -> bool:
    """ HasChildren(self: CustomCommand) -> bool
     """
    import System
    return System.Boolean()

  ID:  int
  
  IconFile:  str
  
  def InvokeCommand(self: CustomCommand):
    """ InvokeCommand(self: CustomCommand) """
    import System
    return System.Void()

  Invoked = None
  MenuItemName = property(None, None, None,
                          """ Get: MenuItemName(self: CustomCommand) -> str
                          
                          Set: MenuItemName(self: CustomCommand) = value
                           """
                          )

  MenuPopup = None
  MenuSelectMessage: str
  
  Name: str
  

  def OnInvoked(self, arg0, arg1):
    """ OnInvoked(self: CustomCommand, args: EventArgs) """
    pass

  def OnMenuPopup(self, arg0, arg1):
    """ OnMenuPopup(self: CustomCommand, args: EventArgs) """
    pass

  Parent: CustomCommand
  

  def ReferenceEquals(objA: object, objB: object) -> bool:
    """ ReferenceEquals(objA: object, objB: object) -> bool
     """
    return None

  
class CustomDataContainer(object):
  """ A container for custom data saved with various objects in a vegas project. """

  def DeleteData(self: CustomDataContainer, dataID: Guid):
    """ DeleteData(self: CustomDataContainer, dataID: Guid) """
    import System
    return System.Void()

  def GetBytes(self: CustomDataContainer, dataID: Guid) -> Array[Byte]:
    """ GetBytes(self: CustomDataContainer, dataID: Guid) -> Array[Byte]
     """
    import System
    return System.Byte[]()

  def GetObject(self: CustomDataContainer, dataID: Guid) -> object:
    """ GetObject(self: CustomDataContainer, dataID: Guid) -> object
     """
    import System
    return System.Object()

  def GetStream(self: CustomDataContainer, dataID: Guid, dataStream: Stream) -> bool:
    """ GetStream(self: CustomDataContainer, dataID: Guid, dataStream: Stream) -> bool
     """
    import System
    return System.Boolean()

  def ReferenceEquals(objA: object, objB: object) -> bool:
    """ ReferenceEquals(objA: object, objB: object) -> bool
     """
    return None

  def SetBytes(self: CustomDataContainer, dataID: Guid, data: Array[Byte])SetBytes(self: CustomDataContainer, dataID: Guid, data: Array[Byte], index: int, count: int):
    """ SetBytes(self: CustomDataContainer, dataID: Guid, data: Array[Byte])SetBytes(self: CustomDataContainer, dataID: Guid, data: Array[Byte], index: int, count: int) """
    import System
    return System.Void()

  def SetObject(self: CustomDataContainer, dataID: Guid, obj: object):
    """ SetObject(self: CustomDataContainer, dataID: Guid, obj: object) """
    import System
    return System.Void()

  def SetStream(self: CustomDataContainer, dataID: Guid, dataStream: Stream, cbData: int):
    """ SetStream(self: CustomDataContainer, dataID: Guid, dataStream: Stream, cbData: int) """
    import System
    return System.Void()

class DockWindowStyle(Enum):
  """ 
  
  enum DockWindowStyle, values: Client (3), Detached (0), Docked (2), Floating (1)
  
   """

  Client = None
  Detached = None
  Docked = None
  Floating = None

class DockableControl(UserControl):
  """ Represents a user control that can be docked in the Vegas user interface.
  DockableControl(instanceName: str)
   """

  def AttachedToWindow(self, hwndParent):
    """ AttachedToWindow(self: DockableControl, hwndParent: IntPtr) """
    import System
    return System.Void()

  AutoLoadCommand:  CustomCommand # Get or set the custom command that loads this control.
  

  def BringToTop(self, arg0):
    """ BringToTop(self: DockableControl) """
    pass

  def Close(self: DockableControl):
    """ Close(self: DockableControl) """
    import System
    return System.Void()

  
  DefaultDockWindowStyle:   DockWindowStyle
  
  DefaultFloatingLocation:  Point
  
  DefaultFloatingSize:  Size
  
  DisplayName:  str
  
  
  DockWindow: IDockWindow
                       )

  DockWindowID:  int
  
  
  HasModalDockWindow:  bool
  
  InstanceName: str
 
  def OnAppWindowClosed(self, arg0, arg1):
    """ OnAppWindowClosed(self: DockableControl, args: EventArgs) """
    pass

  def OnAppWindowClosing(self, arg0, arg1):
    """ OnAppWindowClosing(self: DockableControl, args: CancelEventArgs) """
    pass

  def OnCaptionDoubleClick(self, arg0, arg1):
    """ OnCaptionDoubleClick(self: DockableControl, args: CaptionDoubleClickEventArgs) """
    pass

  def OnClosed(self, arg0, arg1):
    """ OnClosed(self: DockableControl, args: EventArgs) """
    pass

  def OnClosing(self, arg0, arg1):
    """ OnClosing(self: DockableControl, args: CancelEventArgs) """
    pass

  def OnHandleCreated(self, arg0, arg1):
    """ OnHandleCreated(self: DockableControl, args: EventArgs) """
    pass

  def OnHandleDestroyed(self, arg0, arg1):
    """ OnHandleDestroyed(self: DockableControl, args: EventArgs) """
    pass

  def OnLoaded(self, arg0, arg1):
    """ OnLoaded(self: DockableControl, args: EventArgs) """
    pass

  def OnParentWindowChanged(self, arg0, arg1):
    """ OnParentWindowChanged(self: DockableControl, args: EventArgs) """
    pass

  def OnWindowMove(self, arg0, arg1):
    """ OnWindowMove(self: DockableControl, args: EventArgs) """
    pass

  OwnerWindow: IWin32Window
  
  
  ParentWindow:  IWin32Window
   
  PersistDockWindowState:  bool
  
  def ResumeCloseAppWindow(self: DockableControl, args: CancelEventArgs):
    """ ResumeCloseAppWindow(self: DockableControl, args: CancelEventArgs) """
    import System
    return System.Void()

  

  def SaveFocus(self: DockableControl)SaveFocus(self: DockableControl, focusControl: Control):
    """ SaveFocus(self: DockableControl)SaveFocus(self: DockableControl, focusControl: Control) """
    import System
    return System.Void()

  def SetFocus(self: DockableControl):
    """ SetFocus(self: DockableControl) """
    import System
    return System.Void()

  def SetFocusToMainTrackView(self: DockableControl) :
    """ SetFocusToMainTrackView(self: DockableControl) """
    import System
    return System.Void()
 
  myInstanceName: str
  myVegas: Vegas



class Effect_(object):
  """ Represents an instance of an effect, transition, or generator.
  Effect(plugIn: PlugInNode)
   """

  ApplyBeforePanCrop: bool
  
  Bypass: bool
  
  CurrentPreset: EffectPreset

  Description: str
  
  def Equals(self, that):
    """ Equals(self: Effect, that: object) -> bool
     """
    import System
    return System.Boolean()

  def GetHashCode(self):
    """ GetHashCode(self: Effect) -> int
     """
    import System
    return System.int()

  Index: int int
  
  IsOFX:  bool
  
  def IsValid(self: Effect_) -> bool:
    """ IsValid(self: Effect) -> bool
     """
    import System
    return System.Boolean()

  Keyframes: Keyframes_
  
  def MembersEqual(self, arg0, arg1):
    """ MembersEqual(self: Effect, that: Effect) -> bool
     """
    return None

  OFXEffect: OFXEffect_

  PlugIn: PlugInNode
  
  Preset: Str
   
  Presets: EffectPresets
  
  def ReferenceEquals(objA: object, objB: object) -> bool:
    """ ReferenceEquals(objA: object, objB: object) -> bool
     """
    return None

  

class EffectPreset(object):
  """ Represents a set of predefined parameter values for an effect key frame. """

  Index: int
  
  Name:  str
  

class EffectPresets(BaseList[EffectPreset]):
  """ Collection of parameter presets for an effect. """

  def GetCount(self, arg0):
    """ GetCount(self: EffectPresets) -> int
     """
    return 1

  def GetItem(self, arg0, arg1):
    """ GetItem(self: EffectPresets, index: int) -> EffectPreset
     """
    return None

  IsFixedSize: bool
 

  IsReadOnly:  bool
   

  def ReferenceEquals(objA: object, objB: object) -> bool:
    """ ReferenceEquals(objA: object, objB: object) -> bool
     """
    return None

class Effects_(BaseList[Effect_]):
  """  """

  def AddEffect(self, plugIn):
    """ AddEffect(self: Effects, plugIn: PlugInNode) -> Effect
     """
    import ScriptPortal.Vegas
    return ScriptPortal.Vegas.Effect()

  def BaseAdd(self, arg0, arg1):
    """ BaseAdd(self: Effects, item: Effect) -> int
     """
    return 1

  def BaseIndex(self, arg0, arg1):
    """ BaseIndex(self: Effects, item: Effect) -> int
     """
    return 1

  def BaseRemove(self, arg0, arg1):
    """ BaseRemove(self: Effects, item: Effect) -> bool
     """
    return None

  def Clear(self):
    """ Clear(self: Effects) """
    import System
    return System.Void()

  def GetCount(self, arg0):
    """ GetCount(self: Effects) -> int
     """
    return 1

  def GetItem(self, arg0, arg1):
    """ GetItem(self: Effects, index: int) -> Effect
     """
    return None

  def Insert(self, index, item):
    """ Insert(self: Effects, index: int, item: Effect) """
    import System
    return System.Void()

  def ReferenceEquals(objA: object, objB: object) -> bool:
    """ ReferenceEquals(objA: object, objB: object) -> bool
     """
    return None

class ElastiqueStretchAttributes(Enum):
  """ 
  
  enum ElastiqueStretchAttributes, values: Efficient (1), Pro (0), Soloist_Monophonic (2), Soloist_Speech (3)
  
   """

  Efficient = None

  def Format(self, arg0, arg1, arg2):
    """ Format(enumType: Type, value: object, format: str) -> str
     """
    return ""

  def GetName(self, arg0, arg1):
    """ GetName(enumType: Type, value: object) -> str
     """
    return ""

  def GetNames(self, arg0):
    """ GetNames(enumType: Type) -> Array[str]
     """
    return ""

  def GetUnderlyingType(self, arg0):
    """ GetUnderlyingType(enumType: Type) -> Type
     """
    return None

  def GetValues(self, arg0):
    """ GetValues(enumType: Type) -> Array
     """
    return None

  def IsDefined(self, arg0, arg1):
    """ IsDefined(enumType: Type, value: object) -> bool
     """
    return None

  def Parse(self, arg0, arg1):
    """ Parse(enumType: Type, value: str) -> object
    Parse(enumType: Type, value: str, ignoreCase: bool) -> object
     """
    return None

  Pro = None

  def ReferenceEquals(objA: object, objB: object) -> bool:
    """ ReferenceEquals(objA: object, objB: object) -> bool
     """
    return None

  Soloist_Monophonic = None
  Soloist_Speech = None

  def ToObject(self, arg0, arg1):
    """ ToObject(enumType: Type, value: object) -> object
    ToObject(enumType: Type, value: SByte) -> object
    ToObject(enumType: Type, value: Int16) -> object
    ToObject(enumType: Type, value: int) -> object
    ToObject(enumType: Type, value: Byte) -> object
    ToObject(enumType: Type, value: UInt16) -> object
    ToObject(enumType: Type, value: int) -> object
    ToObject(enumType: Type, value: int) -> object
    ToObject(enumType: Type, value: int) -> object
     """
    return None

  def TryParse(self, arg0):
    """ TryParse[TEnum](value: str) -> (bool, TEnum)
    TryParse[TEnum](value: str, ignoreCase: bool) -> (bool, TEnum)
     """
    return (None, None)

  value__ = None

class Envelope(object):
  """ Represents an envelope.
  Envelope(type: EnvelopeType)
   """

  def Equals(self, that):
    """ Equals(self: Envelope, that: object) -> bool
     """
    import System
    return System.Boolean()

  def GetHashCode(self):
    """ GetHashCode(self: Envelope) -> int
     """
    import System
    return System.int()

  Index:  int
  

  def IsValid(self: Envelope) -> bool:
    """ IsValid(self: Envelope) -> bool
     """
    import System
    return System.Boolean()

  Max: float
  

  def MembersEqual(self, arg0, arg1):
    """ MembersEqual(self: Envelope, that: Envelope) -> bool
     """
    return None

  Min:  float
 

  Name:  str
  

  Neutral: float

  Points: EnvelopePoints
  

  def ReferenceEquals(objA: object, objB: object) -> bool:
    """ ReferenceEquals(objA: object, objB: object) -> bool
     """
    return None

  Type:  EnvelopeType
  


  def ValueAt(self: Envelope, position: Timecode) -> float:
    """ ValueAt(self: Envelope, position: Timecode) -> float
     """
    import System
    return System.Double()

class EnvelopePoint(x: Timecode, y: float, curveType: CurveType):
  """ Represents an envelope point.
  EnvelopePoint(x: Timecode, y: float, curveType: CurveType)
  EnvelopePoint(x: Timecode, y: float)
   """

  class AddParams(object):
    """ AddParams(x: Timecode, y: float, curveType: CurveType)
     """

    def ReferenceEquals(objA: object, objB: object) -> bool:
      """ ReferenceEquals(objA: object, objB: object) -> bool
       """
      return None

  Curve: CurveType
  
  EnvelopeType: EnvelopeType_
   
  def Equals(self, obj):
    """ Equals(self: EnvelopePoint, obj: object) -> bool
     """
    import System
    return System.Boolean()

  def GetHashCode(self):
    """ GetHashCode(self: EnvelopePoint) -> int
     """
    import System
    return System.int()

  Index: int
  

  def IsValid(self: EnvelopePoint) -> bool:
    """ IsValid(self: EnvelopePoint) -> bool
     """
    import System
    return System.Boolean()

  MaxTransitionProgress: Timecode
  


  def MembersEqual(self, arg0, arg1):
    """ MembersEqual(self: EnvelopePoint, that: EnvelopePoint) -> bool
     """
    return None

  def ReferenceEquals(objA: object, objB: object) -> bool:
    """ ReferenceEquals(objA: object, objB: object) -> bool
     """
    return None

  X: Timecode
  
  Y: float
  


class EnvelopePoints_(BaseList[EnvelopePoint]):
  """ Collection of points in an envelope. """

  def BaseAdd(self: EnvelopePoints_, item: EnvelopePoint) -> int:
    """ BaseAdd(self: EnvelopePoints, item: EnvelopePoint) -> int
     """
    return 1

  def BaseIndex(self: EnvelopePoints_, item: EnvelopePoint) -> int:
    """ BaseIndex(self: EnvelopePoints, item: EnvelopePoint) -> int
     """
     return 0 

  def BaseRemove(self, arg0, arg1):
    """ BaseRemove(self: EnvelopePoints, item: EnvelopePoint) -> bool
     """
    return None

  def  Clear(self: EnvelopePoints):
    """ Clear(self: EnvelopePoints) """
    import System
    return System.Void()

  def GetCount(self, arg0):
    """ GetCount(self: EnvelopePoints) -> int
     """
    return 1

  def GetItem(self, arg0, arg1):
    """ GetItem(self: EnvelopePoints, index: int) -> EnvelopePoint
     """
    return 1

  def GetPointAtX(self: EnvelopePoints, x: Timecode) -> EnvelopePoint:
    """ GetPointAtX(self: EnvelopePoints, x: Timecode) -> EnvelopePoint
     """
    import ScriptPortal.Vegas
    return ScriptPortal.Vegas.EnvelopePoint()

  def ReferenceEquals(objA: object, objB: object) -> bool:
    """ ReferenceEquals(objA: object, objB: object) -> bool
     """
    return None

class EnvelopeType(Enum):
  """ Enumeration of envelope types.    
  enum EnvelopeType, values: AutomationMax (400), AutomationMin (301), BusA (3), BusB (4), BusC (5), BusD (6), BusE (7), BusF (8), BusG (9), BusH (10), BusI (11), BusJ (12), BusK (13), BusL (14), BusM (15), BusN (16), BusO (17), BusP (18), BusQ (19), BusR (20), BusS (21), BusT (22), BusU (23), BusV (24), BusW (25), BusX (26), BusY (27), BusZ (28), Composite (29), Fade (201), FadeToColor (30), FX1 (64), FX10 (73), FX11 (74), FX12 (75), FX13 (76), FX14 (77), FX15 (78), FX16 (79), FX17 (80), FX18 (81), FX19 (82), FX2 (65), FX20 (83), FX21 (84), FX22 (85), FX23 (86), FX24 (87), FX25 (88), FX26 (89), FX27 (90), FX28 (91), FX29 (92), FX3 (66), FX30 (93), FX31 (94), FX32 (95), FX4 (67), FX5 (68), FX6 (69), FX7 (70), FX8 (71), FX9 (72), MotionBlurLength (32), Mute (31), Pan (1), PanCenter (101), PanSmoothness (97), PanY (96), TransitionProgress (200), Unknown (-1), Velocity (202), VideoSupersampling (33), Volume (0)
  
   """

  AutomationMax = None
  AutomationMin = None
  BusA = None
  BusB = None
  BusC = None
  BusD = None
  BusE = None
  BusF = None
  BusG = None
  BusH = None
  BusI = None
  BusJ = None
  BusK = None
  BusL = None
  BusM = None
  BusN = None
  BusO = None
  BusP = None
  BusQ = None
  BusR = None
  BusS = None
  BusT = None
  BusU = None
  BusV = None
  BusW = None
  BusX = None
  BusY = None
  BusZ = None
  Composite = None
  FX1 = None
  FX10 = None
  FX11 = None
  FX12 = None
  FX13 = None
  FX14 = None
  FX15 = None
  FX16 = None
  FX17 = None
  FX18 = None
  FX19 = None
  FX2 = None
  FX20 = None
  FX21 = None
  FX22 = None
  FX23 = None
  FX24 = None
  FX25 = None
  FX26 = None
  FX27 = None
  FX28 = None
  FX29 = None
  FX3 = None
  FX30 = None
  FX31 = None
  FX32 = None
  FX4 = None
  FX5 = None
  FX6 = None
  FX7 = None
  FX8 = None
  FX9 = None
  Fade = None
  FadeToColor = None

  def Format(self, arg0, arg1, arg2):
    """ Format(enumType: Type, value: object, format: str) -> str
     """
    return ""

  def GetName(self, arg0, arg1):
    """ GetName(enumType: Type, value: object) -> str
     """
    return ""

  def GetNames(self, arg0):
    """ GetNames(enumType: Type) -> Array[str]
     """
    return ""

  def GetUnderlyingType(self, arg0):
    """ GetUnderlyingType(enumType: Type) -> Type
     """
    return None

  def GetValues(self, arg0):
    """ GetValues(enumType: Type) -> Array
     """
    return None

  def IsDefined(self, arg0, arg1):
    """ IsDefined(enumType: Type, value: object) -> bool
     """
    return None

  MotionBlurLength = None
  Mute = None
  Pan = None
  PanCenter = None
  PanSmoothness = None
  PanY = None

  def Parse(self, arg0, arg1):
    """ Parse(enumType: Type, value: str) -> object
    Parse(enumType: Type, value: str, ignoreCase: bool) -> object
     """
    return None

  def ReferenceEquals(objA: object, objB: object) -> bool:
    """ ReferenceEquals(objA: object, objB: object) -> bool
     """
    return None

  def ToObject(self, arg0, arg1):
    """ ToObject(enumType: Type, value: object) -> object
    ToObject(enumType: Type, value: SByte) -> object
    ToObject(enumType: Type, value: Int16) -> object
    ToObject(enumType: Type, value: int) -> object
    ToObject(enumType: Type, value: Byte) -> object
    ToObject(enumType: Type, value: UInt16) -> object
    ToObject(enumType: Type, value: int) -> object
    ToObject(enumType: Type, value: int) -> object
    ToObject(enumType: Type, value: int) -> object
     """
    return None

  TransitionProgress = None

  def TryParse(self, arg0):
    """ TryParse[TEnum](value: str) -> (bool, TEnum)
    TryParse[TEnum](value: str, ignoreCase: bool) -> (bool, TEnum)
     """
    return (None, None)

  Unknown = None
  Velocity = None
  VideoSupersampling = None
  Volume = None
  value__ = None

class Envelopes_(BaseList[Envelope]):
  """ Collection of envelopes. """

  def BaseAdd(self, arg0, arg1):
    """ BaseAdd(self: Envelopes, item: Envelope) -> int
     """
    return 1

  def BaseRemove(self, arg0, arg1):
    """ BaseRemove(self: Envelopes, item: Envelope) -> bool
     """
    return None

  def FindByType(self: Envelopes_, type: EnvelopeType) -> Envelope:
    """ FindByType(self: Envelopes, type: EnvelopeType) -> Envelope
     """
    import ScriptPortal.Vegas
    return ScriptPortal.Vegas.Envelope()

  def GetCount(self, arg0):
    """ GetCount(self: Envelopes) -> int
     """
    return 1

  def GetItem(self, arg0, arg1):
    """ GetItem(self: Envelopes, index: int) -> Envelope
     """
    return None

  def HasEnvelope(self: Envelopes_, type: EnvelopeType) -> bool:
    """ HasEnvelope(self: Envelopes, type: EnvelopeType) -> bool
     """
    import System
    return System.Boolean()

  def ReferenceEquals(objA: object, objB: object) -> bool:
    """ ReferenceEquals(objA: object, objB: object) -> bool
     """
    return None

class Fade(object):
  """ Represents the fade (in or out) of an event. """

  def CanAddEnvelope(self, type):
    """ CanAddEnvelope(self: Fade, type: EnvelopeType) -> bool
     """
    import System
    return System.Boolean()

  Curve: CurveType
  
  Envelopes: Envelopes_


  def Equals(self, that):
    """ Equals(self: Fade, that: object) -> bool
     """
    import System
    return System.Boolean()

  Gain:  Single
   
  def GetHashCode(self):
    """ GetHashCode(self: Fade) -> int
     """
    import System
    return System.int()

  Length:  Timecode
  
  def MembersEqual(self, arg0, arg1):
    """ MembersEqual(self: Fade, that: Fade) -> bool
     """
    return None

  Project: Project_
  
  ReciprocalCurve:  CurveType

  def ReferenceEquals(objA: object, objB: object) -> bool:
    """ ReferenceEquals(objA: object, objB: object) -> bool
     """
    return None

  def RemoveTransition(self):
    """ RemoveTransition(self: Fade) -> bool
     """
    import System
    return System.Boolean()

  Transition:  object
  


class GeneratedMedia(Media):
  """  """

  def CreateInstance(self, arg0, arg1):
    """ CreateInstance(project: Project, path: str) -> Media
    CreateInstance(project: Project, generator: PlugInNode, presetName: str) -> Media
    CreateInstance(project: Project, generator: PlugInNode) -> Media
     """
    return None

  class GeneratorEffectOwner(object):
    """ GeneratorEffectOwner(project: Project, com: IEffectCOM)
    GeneratorEffectOwner(com: IEffectCOM)
     """

    def ReferenceEquals(objA: object, objB: object) -> bool:
      """ ReferenceEquals(objA: object, objB: object) -> bool
       """
      return None

  MEDIA_FLAG_CUSTOM_OFFSET = None

  def ReferenceEquals(objA: object, objB: object) -> bool:
    """ ReferenceEquals(objA: object, objB: object) -> bool
     """
    return None

  SourceUMIDCustomDataID = None
  myCOM = None
  myCustomDataContainer = None
  myEffectCOM = None
  myEffects = None
  myGenerator = None
  myMediaID = None
  myMetaPathType = None
  myProject = None

class GuidListSetting(ListSetting[Guid]):
  """ GuidListSetting(name: str)
   """

  def ItemFromString(self, arg0, arg1):
    """ ItemFromString(self: GuidListSetting, s: str) -> Guid
     """
    return None

  def ItemToString(self, arg0, arg1):
    """ ItemToString(self: GuidListSetting, item: Guid) -> str
     """
    return ""

  Name = None

  def ReferenceEquals(objA: object, objB: object) -> bool:
    """ ReferenceEquals(objA: object, objB: object) -> bool
     """
    return None

  Value = None

class GuidSetting(XmlSetting):
  """ GuidSetting(name: str, val: Guid)
   """

  def FromString(self, value):
    """ FromString(self: GuidSetting, value: str) """
    import System
    return System.Void()

  Name = None

  def ReferenceEquals(objA: object, objB: object) -> bool:
    """ ReferenceEquals(objA: object, objB: object) -> bool
     """
    return None

  def ToString(self):
    """ ToString(self: GuidSetting) -> str
     """
    import System
    return System.String()

  Value = None

class IBurgerMenuConfig:
  """  """

  def AddItem(self, isOn, name):
    """ AddItem(self: IBurgerMenuConfig, isOn: bool, name: str) """
    import System
    return System.Void()

  CancelDlg = property(None, None, None,
                       """ Get: CancelDlg(self: IBurgerMenuConfig) -> bool
                       
                       Set: CancelDlg(self: IBurgerMenuConfig) = value
                        """
                       )


  def ClearItems(self):
    """ ClearItems(self: IBurgerMenuConfig) """
    import System
    return System.Void()

  Description = property(None, None, None,
                         """ Get: Description(self: IBurgerMenuConfig) -> str
                         
                         Set: Description(self: IBurgerMenuConfig) = value
                          """
                         )


  def GetCount(self, count):
    """ GetCount(self: IBurgerMenuConfig) -> int
     """
    import System
    return System.Void()

  def GetItem(self, name, isOn):
    """ GetItem(self: IBurgerMenuConfig, name: str) -> bool
     """
    import System
    return System.Void()

  def GetItemByIndex(self, index, name, isOn):
    """ GetItemByIndex(self: IBurgerMenuConfig, index: int) -> (str, bool)
     """
    import System
    return System.Void()

  Title = property(None, None, None,
                   """ Get: Title(self: IBurgerMenuConfig) -> str
                   
                   Set: Title(self: IBurgerMenuConfig) = value
                    """
                   )


class IBusTrackCOM:
  """  """

  def GetBusTrackFadeBottomColor(self, busID, value):
    """ GetBusTrackFadeBottomColor(self: IBusTrackCOM, busID: int) -> SFDIBPIXEL
     """
    import System
    return System.Void()

  def GetBusTrackFadeTopColor(self, busID, value):
    """ GetBusTrackFadeTopColor(self: IBusTrackCOM, busID: int) -> SFDIBPIXEL
     """
    import System
    return System.Void()

  def GetBusTrackIndex(self, busID, value):
    """ GetBusTrackIndex(self: IBusTrackCOM, busID: int) -> int
     """
    import System
    return System.Void()

  def GetBypass(self, busID, bypass):
    """ GetBypass(self: IBusTrackCOM, busID: int) -> bool
     """
    import System
    return System.Void()

  def GetDescription(self, busID, description):
    """ GetDescription(self: IBusTrackCOM, busID: int) -> str
     """
    import System
    return System.Void()

  def GetEffectCOM(self, busID, context):
    """ GetEffectCOM(self: IBusTrackCOM, busID: int) -> IEffectCOM
     """
    import System
    return System.Void()

  def GetEnvelopeCOM(self, busID, context):
    """ GetEnvelopeCOM(self: IBusTrackCOM, busID: int) -> IEnvelopeCOM
     """
    import System
    return System.Void()

  def GetMute(self, busID, mute):
    """ GetMute(self: IBusTrackCOM, busID: int) -> bool
     """
    import System
    return System.Void()

  def GetName(self, busID, name):
    """ GetName(self: IBusTrackCOM, busID: int) -> str
     """
    import System
    return System.Void()

  def GetPanType(self, busID, panType):
    """ GetPanType(self: IBusTrackCOM, busID: int) -> int
     """
    import System
    return System.Void()

  def GetRenderEnabled(self, busID, mix, value):
    """ GetRenderEnabled(self: IBusTrackCOM, busID: int, mix: int) -> bool
     """
    import System
    return System.Void()

  def GetRenderOrder(self, busID, mix, value):
    """ GetRenderOrder(self: IBusTrackCOM, busID: int, mix: int) -> int
     """
    import System
    return System.Void()

  def GetSolo(self, busID, solo):
    """ GetSolo(self: IBusTrackCOM, busID: int) -> bool
     """
    import System
    return System.Void()

  def SetBusTrackFadeBottomColor(self, busID, value):
    """ SetBusTrackFadeBottomColor(self: IBusTrackCOM, busID: int, value: SFDIBPIXEL) """
    import System
    return System.Void()

  def SetBusTrackFadeTopColor(self, busID, value):
    """ SetBusTrackFadeTopColor(self: IBusTrackCOM, busID: int, value: SFDIBPIXEL) """
    import System
    return System.Void()

  def SetBypass(self, busID, bypass):
    """ SetBypass(self: IBusTrackCOM, busID: int, bypass: bool) """
    import System
    return System.Void()

  def SetDescription(self, busID, description):
    """ SetDescription(self: IBusTrackCOM, busID: int, description: str) """
    import System
    return System.Void()

  def SetMute(self, busID, mute):
    """ SetMute(self: IBusTrackCOM, busID: int, mute: bool) """
    import System
    return System.Void()

  def SetPanType(self, busID, panType):
    """ SetPanType(self: IBusTrackCOM, busID: int, panType: int) """
    import System
    return System.Void()

  def SetRenderEnabled(self, busID, mix, value):
    """ SetRenderEnabled(self: IBusTrackCOM, busID: int, mix: int, value: bool) """
    import System
    return System.Void()

  def SetRenderOrder(self, busID, mix, value):
    """ SetRenderOrder(self: IBusTrackCOM, busID: int, mix: int, value: int) """
    import System
    return System.Void()

  def SetSolo(self, busID, solo):
    """ SetSolo(self: IBusTrackCOM, busID: int, solo: bool) """
    import System
    return System.Void()

class ICustomCommandModule:
  """ Defines initialization routines for hosting a set of custom commands. """

  def GetCustomCommands(self: ICustomCommandModule) -> ICollection:
    """ GetCustomCommands(self: ICustomCommandModule) -> ICollection
     """
    import System.Collections
    return System.Collections.ICollection()

  def InitializeModule(self: ICustomCommandModule, vegas: Vegas):
    """ InitializeModule(self: ICustomCommandModule, vegas: Vegas) """
    import System
    return System.Void()

class IDockView:
  """  """

  def AttachedToWindow(self, hwnd):
    """ AttachedToWindow(self: IDockView, hwnd: IntPtr) """
    import System
    return System.Void()

  DisplayName:  str
                      
  DockWindow: IDockWindow

  DockWindowID:  int
  
  HasModalDockWindow: bool

  InstanceName: > str
  
  def InvokeAppWindowClosed(self):
    """ InvokeAppWindowClosed(self: IDockView) """
    import System
    return System.Void()

  def InvokeAppWindowClosing(self, hwndApp):
    """ InvokeAppWindowClosing(self: IDockView, hwndApp: IntPtr) -> int
     """
    import System
    return System.int()

  def InvokeCaptionDoubleClick(self, newWidth, newHeight):
    """ InvokeCaptionDoubleClick(self: IDockView) -> (int, int, int)
     """
    import System
    return System.int()

  def InvokeClosed(self):
    """ InvokeClosed(self: IDockView) """
    import System
    return System.Void()

  def InvokeClosing(self):
    """ InvokeClosing(self: IDockView) -> int
     """
    import System
    return System.int()

  def InvokeCreateControl(self):
    """ InvokeCreateControl(self: IDockView) """
    import System
    return System.Void()

  def InvokeLoaded(self):
    """ InvokeLoaded(self: IDockView) """
    import System
    return System.Void()

  def InvokeWindowMove(self):
    """ InvokeWindowMove(self: IDockView) """
    import System
    return System.Void()

  def KillFocus(self):
    """ KillFocus(self: IDockView) """
    import System
    return System.Void()

  PersistDockWindowState:  bool
 
  def SetFocus(self: IDockView):
    """ SetFocus(self: IDockView) """
    import System
    return System.Void()

class IDockWindow:
  """  """

  def BringToTop(self):
    """ BringToTop(self: IDockWindow) """
    import System
    return System.Void()

  def DockViewHandleCreated(self, hwndDockView):
    """ DockViewHandleCreated(self: IDockWindow, hwndDockView: IntPtr) """
    import System
    return System.Void()

  def DockViewHandleDestroyed(self):
    """ DockViewHandleDestroyed(self: IDockWindow) """
    import System
    return System.Void()

  def SaveFocus(self, hwndFocus):
    """ SaveFocus(self: IDockWindow, hwndFocus: IntPtr) """
    import System
    return System.Void()

  def SetFocusToMainTrackView(self):
    """ SetFocusToMainTrackView(self: IDockWindow) """
    import System
    return System.Void()

class IDomainManager:
  """  """

  def ActivateDockView(self, instanceName):
    """ ActivateDockView(self: IDomainManager, instanceName: str) -> bool
     """
    import System
    return System.Boolean()

  def AddExtraCommandModule(self, modulePath):
    """ AddExtraCommandModule(self: IDomainManager, modulePath: str) """
    import System
    return System.Void()

  def AppInitialized(self, hwndVegas, hwndExternNotify):
    """ AppInitialized(self: IDomainManager, hwndVegas: IntPtr, hwndExternNotify: IntPtr) """
    import System
    return System.Void()

  def AppWindowClosed(self):
    """ AppWindowClosed(self: IDomainManager) """
    import System
    return System.Void()

  def AppWindowClosing(self, hwndApp):
    """ AppWindowClosing(self: IDomainManager, hwndApp: IntPtr) -> int
     """
    import System
    return System.int()

  def BeginPersistToolbarCmds(self):
    """ BeginPersistToolbarCmds(self: IDomainManager) """
    import System
    return System.Void()

  def CanTutorProceed(self, callbackName):
    """ CanTutorProceed(self: IDomainManager, callbackName: str) -> int
     """
    import System
    return System.int()

  def CreateDefaultDockViews(self):
    """ CreateDefaultDockViews(self: IDomainManager) """
    import System
    return System.Void()

  def EndPersistToolbarCmds(self):
    """ EndPersistToolbarCmds(self: IDomainManager) """
    import System
    return System.Void()

  def FindDockView(self, instanceName, dockview):
    """ FindDockView(self: IDomainManager, instanceName: str) -> (bool, IDockView)
     """
    import System
    return System.Boolean()

  def FireEvent(self, id, comArgs):
    """ FireEvent(self: IDomainManager, id: VegasEventID, comArgs: object) """
    import System
    return System.Void()

  def FreeDockView(self, dockView):
    """ FreeDockView(self: IDomainManager, dockView: IDockView) """
    import System
    return System.Void()

  def GetAutoLoadCommandName(self, commandName, dockView):
    """ GetAutoLoadCommandName(self: IDomainManager, dockView: IDockView) -> (bool, str)
     """
    import System
    return System.Boolean()

  def GetCustomCmdByPersistID(self, persistID, currentID):
    """ GetCustomCmdByPersistID(self: IDomainManager, persistID: int) -> (int, int)
     """
    import System
    return System.int()

  def GetCustomCmdByToolbarIndex(self, ndex, category, cmdID, glyphIndex, cmdName):
    """ GetCustomCmdByToolbarIndex(self: IDomainManager, ndex: int) -> (int, CommandCategory, int, int, str)
     """
    import System
    return System.int()

  def GetCustomCmdGlyphIndex(self, cmdID, category, value):
    """ GetCustomCmdGlyphIndex(self: IDomainManager, cmdID: int) -> (int, CommandCategory, int)
     """
    import System
    return System.int()

  def GetCustomCmdInfo(self, cmdID, category, name, scriptFile):
    """ GetCustomCmdInfo(self: IDomainManager, cmdID: int) -> (int, CommandCategory, str, str)
     """
    import System
    return System.int()

  def GetCustomCmdMenuSelectMsg(self, cmdID, msg):
    """ GetCustomCmdMenuSelectMsg(self: IDomainManager, cmdID: int) -> (int, str)
     """
    import System
    return System.int()

  def GetDefaultDockWindowState(self, dockView, dockWindowStyle, floatingLeft, floatingTop, floatingWidth, floatingHeight):
    """ GetDefaultDockWindowState(self: IDomainManager, dockView: IDockView) -> (DockWindowStyle, int, int, int, int)
     """
    import System
    return System.Void()

  def GetDockWindowState(self, dockView, dockStyle, dockInfo, floatingWidth, floatingHeight, normalLeft, normalTop, normalRight, normalBottom):
    """ GetDockWindowState(self: IDomainManager, dockView: IDockView, dockStyle: int, dockInfo: int, floatingWidth: int, floatingHeight: int, normalLeft: int, normalTop: int, normalRight: int, normalBottom: int) -> (int, int, int, int, int, int, int, int, int)
     """
    import System
    return System.int()

  def GetFirstDockView(self, dockview):
    """ GetFirstDockView(self: IDomainManager) -> (bool, IDockView)
     """
    import System
    return System.Boolean()

  def GetNextDockView(self, current, dockview):
    """ GetNextDockView(self: IDomainManager, current: IDockView) -> (bool, IDockView)
     """
    import System
    return System.Boolean()

  def GetTutorRect(self, callbackName, rect):
    """ GetTutorRect(self: IDomainManager, callbackName: str) -> (int, RECT)
     """
    import System
    return System.int()

  def InitCustomCommands(self, idScriptMin, idScriptMax, noUI, idScriptMinEx, idScriptMaxEx):
    """ InitCustomCommands(self: IDomainManager, idScriptMin: int, idScriptMax: int, noUI: bool, idScriptMinEx: int, idScriptMaxEx: int) """
    import System
    return System.Void()

  def Initialize(self, objVegasCOM):
    """ Initialize(self: IDomainManager, objVegasCOM: object) """
    import System
    return System.Void()

  def InvokeCustomCmd(self, cmdID):
    """ InvokeCustomCmd(self: IDomainManager, cmdID: int) """
    import System
    return System.Void()

  def InvokeCustomCmdByName(self, cmdName):
    """ InvokeCustomCmdByName(self: IDomainManager, cmdName: str) """
    import System
    return System.Void()

  def IsVideoDeviceModuleAllowed(self, moduleID):
    """ IsVideoDeviceModuleAllowed(self: IDomainManager, moduleID: Guid) -> int
     """
    import System
    return System.int()

  def LoadDockView(self, className):
    """ LoadDockView(self: IDomainManager, className: str) """
    import System
    return System.Void()

  def OnCustomCmdMenuPopup(self, category, hmenu):
    """ OnCustomCmdMenuPopup(self: IDomainManager, category: CommandCategory, hmenu: UIntPtr) """
    import System
    return System.Void()

  def PersistToolbarCmd(self, cmdID):
    """ PersistToolbarCmd(self: IDomainManager, cmdID: int) """
    import System
    return System.Void()

  def SavePrefs(self):
    """ SavePrefs(self: IDomainManager) """
    import System
    return System.Void()

  def SetDockWindowState(self, dockView, dockStyle, dockInfo, floatingWidth, floatingHeight, normalLeft, normalTop, normalRight, normalBottom):
    """ SetDockWindowState(self: IDomainManager, dockView: IDockView, dockStyle: int, dockInfo: int, floatingWidth: int, floatingHeight: int, normalLeft: int, normalTop: int, normalRight: int, normalBottom: int) -> int
     """
    import System
    return System.int()


class IMediaBinNode:
  """  """

  def IsValid(self):
    """ IsValid(self: IMediaBinNode) -> bool
     """
    import System
    return System.Boolean()

  NodeID: int
  

  NodeType:  MediaBinNodeType
                      
  


class INetRenderDialogArgs:
  """  """

  FinalRendererGuid = property(None, None, None,
                               """ Get: FinalRendererGuid(self: INetRenderDialogArgs) -> Guid
                               
                                """
                               )


  def GetTemplateData(self, templateDataStream, cbData):
    """ GetTemplateData(self: INetRenderDialogArgs) -> (IStream, int)
     """
    import System
    return System.Void()

  IncludeMarkers = property(None, None, None,
                            """ Get: IncludeMarkers(self: INetRenderDialogArgs) -> bool
                            
                             """
                            )

  LengthNanos = property(None, None, None,
                         """ Get: LengthNanos(self: INetRenderDialogArgs) -> int
                         
                          """
                         )

  OutputFile = property(None, None, None,
                        """ Get: OutputFile(self: INetRenderDialogArgs) -> str
                        
                         """
                        )

  SaveType = property(None, None, None,
                      """ Get: SaveType(self: INetRenderDialogArgs) -> StreamType
                      
                       """
                      )

  SegmentRendererGuid = property(None, None, None,
                                 """ Get: SegmentRendererGuid(self: INetRenderDialogArgs) -> Guid
                                 
                                  """
                                 )

  StartNanos = property(None, None, None,
                        """ Get: StartNanos(self: INetRenderDialogArgs) -> int
                        
                         """
                        )

  UseChannelMapping = property(None, None, None,
                               """ Get: UseChannelMapping(self: INetRenderDialogArgs) -> bool
                               
                                """
                               )


class IOFXPlugCOM:
  """  """

  def DeleteKeyframe(self, paramIndex, keyframeID):
    """ DeleteKeyframe(self: IOFXPlugCOM, paramIndex: int, keyframeID: int) -> int
     """
    import System
    return System.int()

  def EnumParameterChoices(self, paramIndex, choiceIndex, val):
    """ EnumParameterChoices(self: IOFXPlugCOM, paramIndex: int, choiceIndex: int) -> (int, str)
     """
    import System
    return System.int()

  def FindParameterByName(self, val, index):
    """ FindParameterByName(self: IOFXPlugCOM, val: str) -> (int, int)
     """
    import System
    return System.int()

  def GetBool(self, index, val):
    """ GetBool(self: IOFXPlugCOM, index: int) -> bool
     """
    import System
    return System.Void()

  def GetBoolAt(self, index, when, val):
    """ GetBoolAt(self: IOFXPlugCOM, index: int, when: int) -> bool
     """
    import System
    return System.Void()

  def GetBoolKf(self, paramIndex, kfID, val):
    """ GetBoolKf(self: IOFXPlugCOM, paramIndex: int, kfID: int) -> bool
     """
    import System
    return System.Void()

  def GetChoice(self, index, val):
    """ GetChoice(self: IOFXPlugCOM, index: int) -> int
     """
    import System
    return System.Void()

  def GetChoiceAt(self, index, when, val):
    """ GetChoiceAt(self: IOFXPlugCOM, index: int, when: int) -> int
     """
    import System
    return System.Void()

  def GetChoiceKf(self, index, kfID, val):
    """ GetChoiceKf(self: IOFXPlugCOM, index: int, kfID: int) -> int
     """
    import System
    return System.Void()

  def GetControlPoint(self, paramIndex, keyframeID, cpType, cpIndex, nanos, val):
    """ GetControlPoint(self: IOFXPlugCOM, paramIndex: int, keyframeID: int, cpType: OFXControlPointType, cpIndex: int) -> (int, float)
     """
    import System
    return System.Void()

  def GetCustom(self, index, val):
    """ GetCustom(self: IOFXPlugCOM, index: int) -> str
     """
    import System
    return System.Void()

  def GetCustomAt(self, index, when, val):
    """ GetCustomAt(self: IOFXPlugCOM, index: int, when: int) -> str
     """
    import System
    return System.Void()

  def GetCustomKf(self, index, kfID, val):
    """ GetCustomKf(self: IOFXPlugCOM, index: int, kfID: int) -> str
     """
    import System
    return System.Void()

  def GetDescription(self, val):
    """ GetDescription(self: IOFXPlugCOM) -> str
     """
    import System
    return System.Void()

  def GetDouble(self, index, val):
    """ GetDouble(self: IOFXPlugCOM, index: int) -> float
     """
    import System
    return System.Void()

  def GetDouble2D(self, index, x, y):
    """ GetDouble2D(self: IOFXPlugCOM, index: int) -> (float, float)
     """
    import System
    return System.Void()

  def GetDouble2DAt(self, index, when, x, y):
    """ GetDouble2DAt(self: IOFXPlugCOM, index: int, when: int) -> (float, float)
     """
    import System
    return System.Void()

  def GetDouble2DKf(self, index, kfID, x, y):
    """ GetDouble2DKf(self: IOFXPlugCOM, index: int, kfID: int) -> (float, float)
     """
    import System
    return System.Void()

  def GetDouble3D(self, index, x, z, y):
    """ GetDouble3D(self: IOFXPlugCOM, index: int) -> (float, float, float)
     """
    import System
    return System.Void()

  def GetDouble3DAt(self, index, when, x, y, z):
    """ GetDouble3DAt(self: IOFXPlugCOM, index: int, when: int) -> (float, float, float)
     """
    import System
    return System.Void()

  def GetDouble3DKf(self, index, kfID, x, y, z):
    """ GetDouble3DKf(self: IOFXPlugCOM, index: int, kfID: int) -> (float, float, float)
     """
    import System
    return System.Void()

  def GetDoubleAt(self, index, when, val):
    """ GetDoubleAt(self: IOFXPlugCOM, index: int, when: int) -> float
     """
    import System
    return System.Void()

  def GetDoubleKf(self, index, kfID, val):
    """ GetDoubleKf(self: IOFXPlugCOM, index: int, kfID: int) -> float
     """
    import System
    return System.Void()

  def GetEffectType(self, val):
    """ GetEffectType(self: IOFXPlugCOM) -> OFXEffectType
     """
    import System
    return System.Void()

  def GetGrouping(self, val):
    """ GetGrouping(self: IOFXPlugCOM) -> str
     """
    import System
    return System.Void()

  def GetInteger(self, index, val):
    """ GetInteger(self: IOFXPlugCOM, index: int) -> int
     """
    import System
    return System.Void()

  def GetInteger2D(self, index, x, y):
    """ GetInteger2D(self: IOFXPlugCOM, index: int) -> (int, int)
     """
    import System
    return System.Void()

  def GetInteger2DAt(self, index, when, x, y):
    """ GetInteger2DAt(self: IOFXPlugCOM, index: int, when: int) -> (int, int)
     """
    import System
    return System.Void()

  def GetInteger2DKf(self, index, kfID, x, y):
    """ GetInteger2DKf(self: IOFXPlugCOM, index: int, kfID: int) -> (int, int)
     """
    import System
    return System.Void()

  def GetInteger3D(self, index, x, z, y):
    """ GetInteger3D(self: IOFXPlugCOM, index: int) -> (int, int, int)
     """
    import System
    return System.Void()

  def GetInteger3DAt(self, index, when, x, y, z):
    """ GetInteger3DAt(self: IOFXPlugCOM, index: int, when: int) -> (int, int, int)
     """
    import System
    return System.Void()

  def GetInteger3DKf(self, index, kfID, x, y, z):
    """ GetInteger3DKf(self: IOFXPlugCOM, index: int, kfID: int) -> (int, int, int)
     """
    import System
    return System.Void()

  def GetIntegerAt(self, index, when, val):
    """ GetIntegerAt(self: IOFXPlugCOM, index: int, when: int) -> int
     """
    import System
    return System.Void()

  def GetIntegerKf(self, index, kfID, val):
    """ GetIntegerKf(self: IOFXPlugCOM, index: int, kfID: int) -> int
     """
    import System
    return System.Void()

  def GetKeyframeCount(self, paramIndex, val):
    """ GetKeyframeCount(self: IOFXPlugCOM, paramIndex: int) -> int
     """
    import System
    return System.Void()

  def GetKeyframeID(self, paramIndex, keyframeIndex, val):
    """ GetKeyframeID(self: IOFXPlugCOM, paramIndex: int, keyframeIndex: int) -> int
     """
    import System
    return System.Void()

  def GetKeyframeIndex(self, paramIndex, keyframeID, val):
    """ GetKeyframeIndex(self: IOFXPlugCOM, paramIndex: int, keyframeID: int) -> int
     """
    import System
    return System.Void()

  def GetKeyframeInterp(self, paramIndex, keyframeID, val):
    """ GetKeyframeInterp(self: IOFXPlugCOM, paramIndex: int, keyframeID: int) -> OFXInterpolationType
     """
    import System
    return System.Void()

  def GetKeyframeTime(self, paramIndex, keyframeID, val):
    """ GetKeyframeTime(self: IOFXPlugCOM, paramIndex: int, keyframeID: int) -> int
     """
    import System
    return System.Void()

  def GetLabel(self, val):
    """ GetLabel(self: IOFXPlugCOM) -> str
     """
    import System
    return System.Void()

  def GetParamPropDouble(self, paramIndex, property, propIndex, value):
    """ GetParamPropDouble(self: IOFXPlugCOM, paramIndex: int, property: str, propIndex: int) -> float
     """
    import System
    return System.Void()

  def GetParamPropInteger(self, paramIndex, property, propIndex, value):
    """ GetParamPropInteger(self: IOFXPlugCOM, paramIndex: int, property: str, propIndex: int) -> int
     """
    import System
    return System.Void()

  def GetParamPropString(self, paramIndex, property, propIndex, value):
    """ GetParamPropString(self: IOFXPlugCOM, paramIndex: int, property: str, propIndex: int) -> str
     """
    import System
    return System.Void()

  def GetParameterAnimated(self, index, val):
    """ GetParameterAnimated(self: IOFXPlugCOM, index: int) -> bool
     """
    import System
    return System.Void()

  def GetParameterCanAnimate(self, index, val):
    """ GetParameterCanAnimate(self: IOFXPlugCOM, index: int) -> bool
     """
    import System
    return System.Void()

  def GetParameterCount(self, val):
    """ GetParameterCount(self: IOFXPlugCOM) -> int
     """
    import System
    return System.Void()

  def GetParameterDefinition(self, index, val):
    """ GetParameterDefinition(self: IOFXPlugCOM, index: int) -> str
     """
    import System
    return System.Void()

  def GetParameterEnabled(self, index, val):
    """ GetParameterEnabled(self: IOFXPlugCOM, index: int) -> bool
     """
    import System
    return System.Void()

  def GetParameterHint(self, index, val):
    """ GetParameterHint(self: IOFXPlugCOM, index: int) -> str
     """
    import System
    return System.Void()

  def GetParameterLabel(self, index, val):
    """ GetParameterLabel(self: IOFXPlugCOM, index: int) -> str
     """
    import System
    return System.Void()

  def GetParameterName(self, index, val):
    """ GetParameterName(self: IOFXPlugCOM, index: int) -> str
     """
    import System
    return System.Void()

  def GetParameterParentName(self, index, val):
    """ GetParameterParentName(self: IOFXPlugCOM, index: int) -> str
     """
    import System
    return System.Void()

  def GetParameterPersist(self, index, val):
    """ GetParameterPersist(self: IOFXPlugCOM, index: int) -> bool
     """
    import System
    return System.Void()

  def GetParameterSecret(self, index, val):
    """ GetParameterSecret(self: IOFXPlugCOM, index: int) -> bool
     """
    import System
    return System.Void()

  def GetParameterSubservient(self, index, val):
    """ GetParameterSubservient(self: IOFXPlugCOM, index: int) -> bool
     """
    import System
    return System.Void()

  def GetParameterType(self, index, val):
    """ GetParameterType(self: IOFXPlugCOM, index: int) -> OFXParameterType
     """
    import System
    return System.Void()

  def GetPluginPath(self, val):
    """ GetPluginPath(self: IOFXPlugCOM) -> str
     """
    import System
    return System.Void()

  def GetPluginTime(self, val):
    """ GetPluginTime(self: IOFXPlugCOM) -> int
     """
    import System
    return System.Void()

  def GetRGB(self, index, r, g, b):
    """ GetRGB(self: IOFXPlugCOM, index: int) -> (float, float, float)
     """
    import System
    return System.Void()

  def GetRGBA(self, index, r, g, b, a):
    """ GetRGBA(self: IOFXPlugCOM, index: int) -> (float, float, float, float)
     """
    import System
    return System.Void()

  def GetRGBAAt(self, index, when, r, g, b, a):
    """ GetRGBAAt(self: IOFXPlugCOM, index: int, when: int) -> (float, float, float, float)
     """
    import System
    return System.Void()

  def GetRGBAKf(self, index, kfID, r, g, b, a):
    """ GetRGBAKf(self: IOFXPlugCOM, index: int, kfID: int) -> (float, float, float, float)
     """
    import System
    return System.Void()

  def GetRGBAt(self, index, when, r, g, b):
    """ GetRGBAt(self: IOFXPlugCOM, index: int, when: int) -> (float, float, float)
     """
    import System
    return System.Void()

  def GetRGBKf(self, index, kfID, r, g, b):
    """ GetRGBKf(self: IOFXPlugCOM, index: int, kfID: int) -> (float, float, float)
     """
    import System
    return System.Void()

  def GetString(self, index, val):
    """ GetString(self: IOFXPlugCOM, index: int) -> str
     """
    import System
    return System.Void()

  def GetStringAt(self, index, when, val):
    """ GetStringAt(self: IOFXPlugCOM, index: int, when: int) -> str
     """
    import System
    return System.Void()

  def GetStringKf(self, index, kfID, val):
    """ GetStringKf(self: IOFXPlugCOM, index: int, kfID: int) -> str
     """
    import System
    return System.Void()

  def GetUniqueID(self, val):
    """ GetUniqueID(self: IOFXPlugCOM) -> str
     """
    import System
    return System.Void()

  def GetVersion(self, major, minor):
    """ GetVersion(self: IOFXPlugCOM) -> (int, int)
     """
    import System
    return System.Void()

  def MoveControlPoint(self, paramIndex, keyframeID, cpType, cpIndex, nanos, val):
    """ MoveControlPoint(self: IOFXPlugCOM, paramIndex: int, keyframeID: int, cpType: OFXControlPointType, cpIndex: int, nanos: int, val: float) """
    import System
    return System.Void()

  def NotifyPluginOfAllParametersChanged(self):
    """ NotifyPluginOfAllParametersChanged(self: IOFXPlugCOM) """
    import System
    return System.Void()

  def NotifyPluginOfUserChange(self, index):
    """ NotifyPluginOfUserChange(self: IOFXPlugCOM, index: int) """
    import System
    return System.Void()

  def SetBool(self, index, val):
    """ SetBool(self: IOFXPlugCOM, index: int, val: bool) """
    import System
    return System.Void()

  def SetBoolAt(self, index, when, val):
    """ SetBoolAt(self: IOFXPlugCOM, index: int, when: int, val: bool) """
    import System
    return System.Void()

  def SetBoolKf(self, paramIndex, kfID, val):
    """ SetBoolKf(self: IOFXPlugCOM, paramIndex: int, kfID: int, val: bool) """
    import System
    return System.Void()

  def SetChoice(self, index, val):
    """ SetChoice(self: IOFXPlugCOM, index: int, val: int) """
    import System
    return System.Void()

  def SetChoiceAt(self, index, when, val):
    """ SetChoiceAt(self: IOFXPlugCOM, index: int, when: int, val: int) """
    import System
    return System.Void()

  def SetChoiceKf(self, index, kfID, val):
    """ SetChoiceKf(self: IOFXPlugCOM, index: int, kfID: int, val: int) """
    import System
    return System.Void()

  def SetCustom(self, index, val):
    """ SetCustom(self: IOFXPlugCOM, index: int, val: str) """
    import System
    return System.Void()

  def SetCustomAt(self, index, when, val):
    """ SetCustomAt(self: IOFXPlugCOM, index: int, when: int, val: str) """
    import System
    return System.Void()

  def SetCustomKf(self, index, kfID, val):
    """ SetCustomKf(self: IOFXPlugCOM, index: int, kfID: int, val: str) """
    import System
    return System.Void()

  def SetDouble(self, index, val):
    """ SetDouble(self: IOFXPlugCOM, index: int, val: float) """
    import System
    return System.Void()

  def SetDouble2D(self, index, x, y):
    """ SetDouble2D(self: IOFXPlugCOM, index: int, x: float, y: float) """
    import System
    return System.Void()

  def SetDouble2DAt(self, index, when, x, y):
    """ SetDouble2DAt(self: IOFXPlugCOM, index: int, when: int, x: float, y: float) """
    import System
    return System.Void()

  def SetDouble2DKf(self, index, kfID, x, y):
    """ SetDouble2DKf(self: IOFXPlugCOM, index: int, kfID: int, x: float, y: float) """
    import System
    return System.Void()

  def SetDouble3D(self, index, x, y, z):
    """ SetDouble3D(self: IOFXPlugCOM, index: int, x: float, y: float, z: float) """
    import System
    return System.Void()

  def SetDouble3DAt(self, index, when, x, y, z):
    """ SetDouble3DAt(self: IOFXPlugCOM, index: int, when: int, x: float, y: float, z: float) """
    import System
    return System.Void()

  def SetDouble3DKf(self, index, kfID, x, y, z):
    """ SetDouble3DKf(self: IOFXPlugCOM, index: int, kfID: int, x: float, y: float, z: float) """
    import System
    return System.Void()

  def SetDoubleAt(self, index, when, val):
    """ SetDoubleAt(self: IOFXPlugCOM, index: int, when: int, val: float) """
    import System
    return System.Void()

  def SetDoubleKf(self, index, kfID, val):
    """ SetDoubleKf(self: IOFXPlugCOM, index: int, kfID: int, val: float) """
    import System
    return System.Void()

  def SetInteger(self, index, val):
    """ SetInteger(self: IOFXPlugCOM, index: int, val: int) """
    import System
    return System.Void()

  def SetInteger2D(self, index, x, y):
    """ SetInteger2D(self: IOFXPlugCOM, index: int, x: int, y: int) """
    import System
    return System.Void()

  def SetInteger2DAt(self, index, when, x, y):
    """ SetInteger2DAt(self: IOFXPlugCOM, index: int, when: int, x: int, y: int) """
    import System
    return System.Void()

  def SetInteger2DKf(self, index, kfID, x, y):
    """ SetInteger2DKf(self: IOFXPlugCOM, index: int, kfID: int, x: int, y: int) """
    import System
    return System.Void()

  def SetInteger3D(self, index, x, y, z):
    """ SetInteger3D(self: IOFXPlugCOM, index: int, x: int, y: int, z: int) """
    import System
    return System.Void()

  def SetInteger3DAt(self, index, when, x, y, z):
    """ SetInteger3DAt(self: IOFXPlugCOM, index: int, when: int, x: int, y: int, z: int) """
    import System
    return System.Void()

  def SetInteger3DKf(self, index, kfID, x, y, z):
    """ SetInteger3DKf(self: IOFXPlugCOM, index: int, kfID: int, x: int, y: int, z: int) """
    import System
    return System.Void()

  def SetIntegerAt(self, index, when, val):
    """ SetIntegerAt(self: IOFXPlugCOM, index: int, when: int, val: int) """
    import System
    return System.Void()

  def SetIntegerKf(self, index, kfID, val):
    """ SetIntegerKf(self: IOFXPlugCOM, index: int, kfID: int, val: int) """
    import System
    return System.Void()

  def SetKeyframeInterp(self, paramIndex, keyframeID, val):
    """ SetKeyframeInterp(self: IOFXPlugCOM, paramIndex: int, keyframeID: int, val: OFXInterpolationType) """
    import System
    return System.Void()

  def SetKeyframeTime(self, paramIndex, keyframeID, val):
    """ SetKeyframeTime(self: IOFXPlugCOM, paramIndex: int, keyframeID: int, val: int) """
    import System
    return System.Void()

  def SetParameterAnimated(self, index, val):
    """ SetParameterAnimated(self: IOFXPlugCOM, index: int, val: bool) """
    import System
    return System.Void()

  def SetPluginTime(self, val):
    """ SetPluginTime(self: IOFXPlugCOM, val: int) """
    import System
    return System.Void()

  def SetRGB(self, index, r, g, b):
    """ SetRGB(self: IOFXPlugCOM, index: int, r: float, g: float, b: float) """
    import System
    return System.Void()

  def SetRGBA(self, index, r, g, b, a):
    """ SetRGBA(self: IOFXPlugCOM, index: int, r: float, g: float, b: float, a: float) """
    import System
    return System.Void()

  def SetRGBAAt(self, index, when, r, g, b, a):
    """ SetRGBAAt(self: IOFXPlugCOM, index: int, when: int, r: float, g: float, b: float, a: float) """
    import System
    return System.Void()

  def SetRGBAKf(self, index, kfID, r, g, b, a):
    """ SetRGBAKf(self: IOFXPlugCOM, index: int, kfID: int, r: float, g: float, b: float, a: float) """
    import System
    return System.Void()

  def SetRGBAt(self, index, when, r, g, b):
    """ SetRGBAt(self: IOFXPlugCOM, index: int, when: int, r: float, g: float, b: float) """
    import System
    return System.Void()

  def SetRGBKf(self, index, kfID, r, g, b):
    """ SetRGBKf(self: IOFXPlugCOM, index: int, kfID: int, r: float, g: float, b: float) """
    import System
    return System.Void()

  def SetString(self, index, val):
    """ SetString(self: IOFXPlugCOM, index: int, val: str) """
    import System
    return System.Void()

  def SetStringAt(self, index, when, val):
    """ SetStringAt(self: IOFXPlugCOM, index: int, when: int, val: str) """
    import System
    return System.Void()

  def SetStringKf(self, index, kfID, val):
    """ SetStringKf(self: IOFXPlugCOM, index: int, kfID: int, val: str) """
    import System
    return System.Void()

class IPlugInNodeCOM:
  """  """

  def GetCategory(self, val):
    """ GetCategory(self: IPlugInNodeCOM) -> int
     """
    import System
    return System.Void()

  def GetChildByClassID(self, classID, childCOM):
    """ GetChildByClassID(self: IPlugInNodeCOM, classID: Guid) -> IPlugInNodeCOM
     """
    import System
    return System.Void()

  def GetChildByIndex(self, index, childCOM):
    """ GetChildByIndex(self: IPlugInNodeCOM, index: int) -> IPlugInNodeCOM
     """
    import System
    return System.Void()

  def GetChildByName(self, name, childCOM):
    """ GetChildByName(self: IPlugInNodeCOM, name: str) -> IPlugInNodeCOM
     """
    import System
    return System.Void()

  def GetChildByUniqueID(self, uniqueID, childCOM):
    """ GetChildByUniqueID(self: IPlugInNodeCOM, uniqueID: str) -> IPlugInNodeCOM
     """
    import System
    return System.Void()

  def GetClassID(self, asGuid, asString):
    """ GetClassID(self: IPlugInNodeCOM) -> (Guid, str)
     """
    import System
    return System.Void()

  def GetCount(self, count):
    """ GetCount(self: IPlugInNodeCOM) -> int
     """
    import System
    return System.Void()

  def GetFlags(self, flags):
    """ GetFlags(self: IPlugInNodeCOM) -> int
     """
    import System
    return System.Void()

  def GetMetaPath(self, metaPath):
    """ GetMetaPath(self: IPlugInNodeCOM) -> str
     """
    import System
    return System.Void()

  def GetName(self, name):
    """ GetName(self: IPlugInNodeCOM) -> str
     """
    import System
    return System.Void()

  def GetPresetCount(self, count):
    """ GetPresetCount(self: IPlugInNodeCOM) -> int
     """
    import System
    return System.Void()

  def GetPresetName(self, index, name):
    """ GetPresetName(self: IPlugInNodeCOM, index: int) -> str
     """
    import System
    return System.Void()

class IProgressCallback:
  """  """

  def UpdatePercentComplete(self, percentComplete):
    """ UpdatePercentComplete(self: IProgressCallback, percentComplete: int) """
    import System
    return System.Void()

class IProjectCOM:
  """  """

  def ActivateBusTracks(self, wasAlreadyActive):
    """ ActivateBusTracks(self: IProjectCOM) -> bool
     """
    import System
    return System.Void()

  def AddBusTrack(self, busType, fxClassID, busID, busIndex):
    """ AddBusTrack(self: IProjectCOM, busType: BusType, fxClassID: Guid) -> (int, int, int)
     """
    import System
    return System.int()

  def AddTrack(self, type, index, trackID):
    """ AddTrack(self: IProjectCOM, type: MediaType, index: int) -> (int, int)
     """
    import System
    return System.Void()

  def ArchiveProject(self, path, flags, wasSaved):
    """ ArchiveProject(self: IProjectCOM, path: str, flags: int) -> bool
     """
    import System
    return System.Void()

  def BeginWrite(self, backupFile, saveType, wasSaveStarted):
    """ BeginWrite(self: IProjectCOM, backupFile: str, saveType: int) -> bool
     """
    import System
    return System.Void()

  def CloneProject(self, path, callback, com):
    """ CloneProject(self: IProjectCOM, path: str, callback: IProjectProgressUpdateCOM) -> IProjectCOM
     """
    import System
    return System.Void()

  def CreateBusTrackCOM(self, com):
    """ CreateBusTrackCOM(self: IProjectCOM) -> IBusTrackCOM
     """
    import System
    return System.Void()

  def CreateEmptyProject(self, callback, com):
    """ CreateEmptyProject(self: IProjectCOM, callback: IProjectProgressUpdateCOM) -> IProjectCOM
     """
    import System
    return System.Void()

  def CreateEventCOM(self, com):
    """ CreateEventCOM(self: IProjectCOM) -> IEventCOM
     """
    import System
    return System.Void()

  def CreateFileOpenCOM(self, fileOpener):
    """ CreateFileOpenCOM(self: IProjectCOM) -> IFileOpenCOM
     """
    import System
    return System.Void()

  def CreateGroupCOM(self, com):
    """ CreateGroupCOM(self: IProjectCOM) -> IGroupCOM
     """
    import System
    return System.Void()

  def CreateMediaBinCOM(self, com):
    """ CreateMediaBinCOM(self: IProjectCOM) -> IMediaBinCOM
     """
    import System
    return System.Void()

  def CreateMediaCOM(self, com):
    """ CreateMediaCOM(self: IProjectCOM) -> IMediaCOM
     """
    import System
    return System.Void()

  def CreateRendererCOM(self, rendererID, com):
    """ CreateRendererCOM(self: IProjectCOM, rendererID: int) -> IRendererCOM
     """
    import System
    return System.Void()

  def CreateTakeCOM(self, com):
    """ CreateTakeCOM(self: IProjectCOM) -> ITakeCOM
     """
    import System
    return System.Void()

  def CreateTrackCOM(self, com):
    """ CreateTrackCOM(self: IProjectCOM) -> ITrackCOM
     """
    import System
    return System.Void()

  def CreateVideoMotionCOM(self, com):
    """ CreateVideoMotionCOM(self: IProjectCOM) -> IVideoMotionCOM
     """
    import System
    return System.Void()

  def DeactivateBusTracks(self):
    """ DeactivateBusTracks(self: IProjectCOM) """
    import System
    return System.Void()

  FilePath = property(None, None, None,
                      """ Get: FilePath(self: IProjectCOM) -> str
                      
                       """
                      )


  def FindPlugInNode(self, plugType, uniqueID, classID, com):
    """ FindPlugInNode(self: IProjectCOM, plugType: int, uniqueID: str, classID: Guid) -> (Guid, IPlugInNodeCOM)
     """
    import System
    return System.Void()

  def FinishUndoBlock(self, cancelUndo):
    """ FinishUndoBlock(self: IProjectCOM, cancelUndo: bool) """
    import System
    return System.Void()

  def FrameCountToNano(self, frameCount, nanos):
    """ FrameCountToNano(self: IProjectCOM, frameCount: int) -> int
     """
    import System
    return System.Void()

  def FreeClonedProject(self):
    """ FreeClonedProject(self: IProjectCOM) """
    import System
    return System.Void()

  def GetAudioCDFirstTrack(self, index):
    """ GetAudioCDFirstTrack(self: IProjectCOM) -> int
     """
    import System
    return System.Void()

  def GetAudioCDUPC(self, upc):
    """ GetAudioCDUPC(self: IProjectCOM) -> str
     """
    import System
    return System.Void()

  def GetAudioResampleQuality(self, quality):
    """ GetAudioResampleQuality(self: IProjectCOM) -> int
     """
    import System
    return System.Void()

  def GetBusTrackCount(self, busType, count):
    """ GetBusTrackCount(self: IProjectCOM, busType: BusType) -> int
     """
    import System
    return System.Void()

  def GetBusTrackID(self, index, busType, busID):
    """ GetBusTrackID(self: IProjectCOM, index: int) -> (BusType, int)
     """
    import System
    return System.Void()

  def GetDefaultProjectPath(self, pathID, createIfNeeded, path):
    """ GetDefaultProjectPath(self: IProjectCOM, pathID: ProjectPathID, createIfNeeded: bool) -> str
     """
    import System
    return System.Void()

  def GetEventGroupCount(self, count):
    """ GetEventGroupCount(self: IProjectCOM) -> int
     """
    import System
    return System.Void()

  def GetEventGroupID(self, index, groupID):
    """ GetEventGroupID(self: IProjectCOM, index: int) -> int
     """
    import System
    return System.Void()

  def GetGenericMetadata(self, dataID, dataStream):
    """ GetGenericMetadata(self: IProjectCOM, dataID: Guid, dataStream: IStream) -> int
     """
    import System
    return System.int()

  def GetGroupIDOfTrack(self, index, groupID):
    """ GetGroupIDOfTrack(self: IProjectCOM, index: int) -> int
     """
    import System
    return System.Void()

  def GetLFELowpassCutoff(self, cutoff):
    """ GetLFELowpassCutoff(self: IProjectCOM) -> int
     """
    import System
    return System.Void()

  def GetLFELowpassEnable(self, enabled):
    """ GetLFELowpassEnable(self: IProjectCOM) -> bool
     """
    import System
    return System.Void()

  def GetLFELowpassQuality(self, quality):
    """ GetLFELowpassQuality(self: IProjectCOM) -> int
     """
    import System
    return System.Void()

  def GetLength(self, length):
    """ GetLength(self: IProjectCOM) -> int
     """
    import System
    return System.Void()

  def GetMarkerCOM(self, markerType, context):
    """ GetMarkerCOM(self: IProjectCOM, markerType: MarkerType) -> IMarkerCOM
     """
    import System
    return System.Void()

  def GetMasterBusMode(self, mode):
    """ GetMasterBusMode(self: IProjectCOM) -> int
     """
    import System
    return System.Void()

  def GetMixerInfo(self, rate, bitDepth):
    """ GetMixerInfo(self: IProjectCOM) -> (int, int)
     """
    import System
    return System.Void()

  def GetMotionBlurType(self, type):
    """ GetMotionBlurType(self: IProjectCOM) -> int
     """
    import System
    return System.Void()

  def GetNumberOfMappedAudioChannels(self, val):
    """ GetNumberOfMappedAudioChannels(self: IProjectCOM) -> int
     """
    import System
    return System.Void()

  def GetPlugInRoot(self, type, rootNode):
    """ GetPlugInRoot(self: IProjectCOM, type: int) -> IPlugInNodeCOM
     """
    import System
    return System.Void()

  def GetPreviewPath(self, path):
    """ GetPreviewPath(self: IProjectCOM) -> str
     """
    import System
    return System.Void()

  def GetProject3DCrosstalk(self, mode, value):
    """ GetProject3DCrosstalk(self: IProjectCOM, mode: Stereo3DOutputMode) -> Single
     """
    import System
    return System.Void()

  def GetProject3DCrosstalkRender(self, mode, value):
    """ GetProject3DCrosstalkRender(self: IProjectCOM, mode: Stereo3DOutputMode) -> bool
     """
    import System
    return System.Void()

  def GetProject3DMode(self, value):
    """ GetProject3DMode(self: IProjectCOM) -> Stereo3DOutputMode
     """
    import System
    return System.Void()

  def GetProject3DSwap(self, mode, value):
    """ GetProject3DSwap(self: IProjectCOM, mode: Stereo3DOutputMode) -> bool
     """
    import System
    return System.Void()

  def GetProjectPath(self, pathID, createIfNeeded, path):
    """ GetProjectPath(self: IProjectCOM, pathID: ProjectPathID, createIfNeeded: bool) -> str
     """
    import System
    return System.Void()

  def GetRecordedFilesFolder(self, path):
    """ GetRecordedFilesFolder(self: IProjectCOM) -> str
     """
    import System
    return System.Void()

  def GetRulerInfo(self, fmt, offset, bpMin, bpMsr, beatVal):
    """ GetRulerInfo(self: IProjectCOM) -> (RulerFormat, int, float, int, int)
     """
    import System
    return System.Void()

  def GetSummaryItem(self, code, item):
    """ GetSummaryItem(self: IProjectCOM, code: int) -> str
     """
    import System
    return System.Void()

  def GetTrackCount(self, count):
    """ GetTrackCount(self: IProjectCOM) -> int
     """
    import System
    return System.Void()

  def GetTrackGroupID(self, index, groupID):
    """ GetTrackGroupID(self: IProjectCOM, index: int) -> int
     """
    import System
    return System.Void()

  def GetTrackGroupsCount(self, count):
    """ GetTrackGroupsCount(self: IProjectCOM) -> int
     """
    import System
    return System.Void()

  def GetTrackID(self, index, trackID, mediaType):
    """ GetTrackID(self: IProjectCOM, index: int) -> (int, int)
     """
    import System
    return System.Void()

  def GetVideoDeinterlaceMethod(self, method):
    """ GetVideoDeinterlaceMethod(self: IProjectCOM) -> int
     """
    import System
    return System.Void()

  def GetVideoPreviewSize(self, eSize):
    """ GetVideoPreviewSize(self: IProjectCOM) -> VideoPreviewSize
     """
    import System
    return System.Void()

  def GetVideoRenderQuality(self, propType, quality):
    """ GetVideoRenderQuality(self: IProjectCOM, propType: VideoPropertiesType) -> int
     """
    import System
    return System.Void()

  def GroupSelectedTracks(self, groupID):
    """ GroupSelectedTracks(self: IProjectCOM) -> int
     """
    import System
    return System.Void()

  def HasMarkers(self):
    """ HasMarkers(self: IProjectCOM) -> int
     """
    import System
    return System.int()

  def InsertTime(self, start, length, ignoreSelection):
    """ InsertTime(self: IProjectCOM, start: int, length: int, ignoreSelection: bool) """
    import System
    return System.Void()

  def IsInScript(self):
    """ IsInScript(self: IProjectCOM) -> int
     """
    import System
    return System.int()

  def IsInUndoBlock(self):
    """ IsInUndoBlock(self: IProjectCOM) -> int
     """
    import System
    return System.int()

  def IsModified(self):
    """ IsModified(self: IProjectCOM) -> int
     """
    import System
    return System.int()

  IsUntitled = property(None, None, None,
                        """ Get: IsUntitled(self: IProjectCOM) -> bool
                        
                         """
                        )


  def MatchVideoSettings(self, filePath, succeeded):
    """ MatchVideoSettings(self: IProjectCOM, filePath: str) -> bool
     """
    import System
    return System.Void()

  def MatchVideoSettingsToMedia(self, mediaID, succeeded):
    """ MatchVideoSettingsToMedia(self: IProjectCOM, mediaID: int) -> bool
     """
    import System
    return System.Void()

  def Modified(self):
    """ Modified(self: IProjectCOM) -> int
     """
    import System
    return System.int()

  def NanoToFrameCount(self, nanos, frameCount):
    """ NanoToFrameCount(self: IProjectCOM, nanos: int) -> int
     """
    import System
    return System.Void()

  def NanoToString(self, nanos, rulerFormat, isPosition, stamp):
    """ NanoToString(self: IProjectCOM, nanos: int, rulerFormat: RulerFormat, isPosition: bool) -> str
     """
    import System
    return System.Void()

  def NewProject(self, promptSave, showDialog, wasCreated):
    """ NewProject(self: IProjectCOM, promptSave: bool, showDialog: bool) -> bool
     """
    import System
    return System.Void()

  PreviewVideoFrameRate = property(None, None, None,
                                   """ Get: PreviewVideoFrameRate(self: IProjectCOM) -> float
                                   
                                    """
                                   )

  PreviewVideoHeight = property(None, None, None,
                                """ Get: PreviewVideoHeight(self: IProjectCOM) -> int
                                
                                 """
                                )

  PreviewVideoInterlace = property(None, None, None,
                                   """ Get: PreviewVideoInterlace(self: IProjectCOM) -> VideoFieldOrder
                                   
                                    """
                                   )

  PreviewVideoPixelAspect = property(None, None, None,
                                     """ Get: PreviewVideoPixelAspect(self: IProjectCOM) -> float
                                     
                                      """
                                     )

  PreviewVideoWidth = property(None, None, None,
                               """ Get: PreviewVideoWidth(self: IProjectCOM) -> int
                               
                                """
                               )

  ProjectVideoFrameRate = property(None, None, None,
                                   """ Get: ProjectVideoFrameRate(self: IProjectCOM) -> float
                                   
                                   Set: ProjectVideoFrameRate(self: IProjectCOM) = value
                                    """
                                   )

  ProjectVideoHeight = property(None, None, None,
                                """ Get: ProjectVideoHeight(self: IProjectCOM) -> int
                                
                                Set: ProjectVideoHeight(self: IProjectCOM) = value
                                 """
                                )

  ProjectVideoInterlace = property(None, None, None,
                                   """ Get: ProjectVideoInterlace(self: IProjectCOM) -> VideoFieldOrder
                                   
                                   Set: ProjectVideoInterlace(self: IProjectCOM) = value
                                    """
                                   )

  ProjectVideoPixelAspect = property(None, None, None,
                                     """ Get: ProjectVideoPixelAspect(self: IProjectCOM) -> float
                                     
                                     Set: ProjectVideoPixelAspect(self: IProjectCOM) = value
                                      """
                                     )

  ProjectVideoPixelFormat = property(None, None, None,
                                     """ Get: ProjectVideoPixelFormat(self: IProjectCOM) -> PixelFormat
                                     
                                     Set: ProjectVideoPixelFormat(self: IProjectCOM) = value
                                      """
                                     )

  ProjectVideoRotation = property(None, None, None,
                                  """ Get: ProjectVideoRotation(self: IProjectCOM) -> VideoOutputRotation
                                  
                                  Set: ProjectVideoRotation(self: IProjectCOM) = value
                                   """
                                  )

  ProjectVideoWidth = property(None, None, None,
                               """ Get: ProjectVideoWidth(self: IProjectCOM) -> int
                               
                               Set: ProjectVideoWidth(self: IProjectCOM) = value
                                """
                               )


  def ReadProject(self, path, callback, com):
    """ ReadProject(self: IProjectCOM, path: str, callback: IProjectProgressUpdateCOM) -> IProjectCOM
     """
    import System
    return System.Void()

  def RemoveBusTrack(self, busID):
    """ RemoveBusTrack(self: IProjectCOM, busID: int) """
    import System
    return System.Void()

  def RemoveTrack(self, trackID):
    """ RemoveTrack(self: IProjectCOM, trackID: int) """
    import System
    return System.Void()

  def Render(self, punkArgs, status):
    """ Render(self: IProjectCOM, punkArgs: object) -> int
     """
    import System
    return System.Void()

  def SaveProject(self, path, showDialog, closeApp, waitForIdle, wasSaved):
    """ SaveProject(self: IProjectCOM, path: str, showDialog: ShowDialogOption, closeApp: bool, waitForIdle: bool) -> bool
     """
    import System
    return System.Void()

  def SetAudioCDFirstTrack(self, index):
    """ SetAudioCDFirstTrack(self: IProjectCOM, index: int) """
    import System
    return System.Void()

  def SetAudioCDUPC(self, upc):
    """ SetAudioCDUPC(self: IProjectCOM, upc: str) """
    import System
    return System.Void()

  def SetAudioResampleQuality(self, quality):
    """ SetAudioResampleQuality(self: IProjectCOM, quality: int) """
    import System
    return System.Void()

  def SetGenericMetadata(self, dataID, cbData, dataStream):
    """ SetGenericMetadata(self: IProjectCOM, dataID: Guid, cbData: UIntPtr, dataStream: IStream) """
    import System
    return System.Void()

  def SetLFELowpassCutoff(self, cutoff):
    """ SetLFELowpassCutoff(self: IProjectCOM, cutoff: int) """
    import System
    return System.Void()

  def SetLFELowpassEnable(self, enabled):
    """ SetLFELowpassEnable(self: IProjectCOM, enabled: bool) """
    import System
    return System.Void()

  def SetLFELowpassQuality(self, quality):
    """ SetLFELowpassQuality(self: IProjectCOM, quality: int) """
    import System
    return System.Void()

  def SetMasterBusMode(self, mode):
    """ SetMasterBusMode(self: IProjectCOM, mode: int) """
    import System
    return System.Void()

  def SetMixerInfo(self, rate, bitDepth):
    """ SetMixerInfo(self: IProjectCOM, rate: int, bitDepth: int) """
    import System
    return System.Void()

  def SetMotionBlurType(self, type):
    """ SetMotionBlurType(self: IProjectCOM, type: int) """
    import System
    return System.Void()

  def SetPreviewPath(self, path):
    """ SetPreviewPath(self: IProjectCOM, path: str) """
    import System
    return System.Void()

  def SetProject3DCrosstalk(self, mode, value):
    """ SetProject3DCrosstalk(self: IProjectCOM, mode: Stereo3DOutputMode, value: Single) """
    import System
    return System.Void()

  def SetProject3DCrosstalkRender(self, mode, value):
    """ SetProject3DCrosstalkRender(self: IProjectCOM, mode: Stereo3DOutputMode, value: bool) """
    import System
    return System.Void()

  def SetProject3DMode(self, value):
    """ SetProject3DMode(self: IProjectCOM, value: Stereo3DOutputMode) """
    import System
    return System.Void()

  def SetProject3DSwap(self, mode, value):
    """ SetProject3DSwap(self: IProjectCOM, mode: Stereo3DOutputMode, value: bool) """
    import System
    return System.Void()

  def SetRecordedFilesFolder(self, path):
    """ SetRecordedFilesFolder(self: IProjectCOM, path: str) """
    import System
    return System.Void()

  def SetRulerInfo(self, fmt, offset, bpMin, bpMsr, beatVal):
    """ SetRulerInfo(self: IProjectCOM, fmt: RulerFormat, offset: int, bpMin: float, bpMsr: int, beatVal: int) """
    import System
    return System.Void()

  def SetSummaryItem(self, code, item):
    """ SetSummaryItem(self: IProjectCOM, code: int, item: str) """
    import System
    return System.Void()

  def SetUntitledFlag(self):
    """ SetUntitledFlag(self: IProjectCOM) """
    import System
    return System.Void()

  def SetVideoDeinterlaceMethod(self, method):
    """ SetVideoDeinterlaceMethod(self: IProjectCOM, method: int) """
    import System
    return System.Void()

  def SetVideoPreviewSize(self, eSize):
    """ SetVideoPreviewSize(self: IProjectCOM, eSize: VideoPreviewSize) """
    import System
    return System.Void()

  def SetVideoRenderQuality(self, propType, quality):
    """ SetVideoRenderQuality(self: IProjectCOM, propType: VideoPropertiesType, quality: int) """
    import System
    return System.Void()

  def ShowMultichannelMappingDialog(self, hwndParent):
    """ ShowMultichannelMappingDialog(self: IProjectCOM, hwndParent: IntPtr) -> int
     """
    import System
    return System.int()

  def ShowRenderTemplateEditDialog(self, hwndParent, rendererID, includeDefaultTemplate, multichannelEnabled, currentTemplate, editedTemplate):
    """ ShowRenderTemplateEditDialog(self: IProjectCOM, hwndParent: IntPtr, rendererID: int, includeDefaultTemplate: bool, multichannelEnabled: bool, currentTemplate: IRenderTemplateCOM) -> (int, IRenderTemplateCOM)
     """
    import System
    return System.int()

  def StartUndoBlock(self, undoDescription):
    """ StartUndoBlock(self: IProjectCOM, undoDescription: str) -> int
     """
    import System
    return System.int()

  def StringToNano(self, stamp, rulerFormat, isPosition, nanos):
    """ StringToNano(self: IProjectCOM, stamp: str, rulerFormat: RulerFormat, isPosition: bool) -> int
     """
    import System
    return System.Void()

  def UngroupSelectedTracks(self):
    """ UngroupSelectedTracks(self: IProjectCOM) """
    import System
    return System.Void()

  def UpdateProjectPath(self, pathID, path):
    """ UpdateProjectPath(self: IProjectCOM, pathID: ProjectPathID, path: str) """
    import System
    return System.Void()

class IProjectProgressUpdateCOM:
  """  """

  def AnnouncePercentComplete(self, percentComplete):
    """ AnnouncePercentComplete(self: IProjectProgressUpdateCOM, percentComplete: int) """
    import System
    return System.Void()

class IRenderArgs:
  """  """

  CancelRender = property(None, None, None,
                          """ Get: CancelRender(self: IRenderArgs) -> bool
                          
                          Set: CancelRender(self: IRenderArgs) = value
                           """
                          )

  GenerateLoudnessLog = property(None, None, None,
                                 """ Get: GenerateLoudnessLog(self: IRenderArgs) -> bool
                                 
                                 Set: GenerateLoudnessLog(self: IRenderArgs) = value
                                  """
                                 )


  def GetTemplateCOM(self, templateCOM):
    """ GetTemplateCOM(self: IRenderArgs) -> IRenderTemplateCOM
     """
    import System
    return System.Void()

  IncludeMarkers = property(None, None, None,
                            """ Get: IncludeMarkers(self: IRenderArgs) -> bool
                            
                            Set: IncludeMarkers(self: IRenderArgs) = value
                             """
                            )

  LengthNanos = property(None, None, None,
                         """ Get: LengthNanos(self: IRenderArgs) -> int
                         
                         Set: LengthNanos(self: IRenderArgs) = value
                          """
                         )

  OutputFile = property(None, None, None,
                        """ Get: OutputFile(self: IRenderArgs) -> str
                        
                        Set: OutputFile(self: IRenderArgs) = value
                         """
                        )

  RendererID = property(None, None, None,
                        """ Get: RendererID(self: IRenderArgs) -> int
                        
                         """
                        )

  SaveAsMono = property(None, None, None,
                        """ Get: SaveAsMono(self: IRenderArgs) -> bool
                        
                        Set: SaveAsMono(self: IRenderArgs) = value
                         """
                        )

  SaveAsMonoStreams = property(None, None, None,
                               """ Get: SaveAsMonoStreams(self: IRenderArgs) -> bool
                               
                               Set: SaveAsMonoStreams(self: IRenderArgs) = value
                                """
                               )

  SaveProjectPathLink = property(None, None, None,
                                 """ Get: SaveProjectPathLink(self: IRenderArgs) -> bool
                                 
                                 Set: SaveProjectPathLink(self: IRenderArgs) = value
                                  """
                                 )

  ShowOpenButtonsOnComplete = property(None, None, None,
                                       """ Get: ShowOpenButtonsOnComplete(self: IRenderArgs) -> bool
                                       
                                       Set: ShowOpenButtonsOnComplete(self: IRenderArgs) = value
                                        """
                                       )

  StartNanos = property(None, None, None,
                        """ Get: StartNanos(self: IRenderArgs) -> int
                        
                        Set: StartNanos(self: IRenderArgs) = value
                         """
                        )

  Stereo3DModeOverride = property(None, None, None,
                                  """ Get: Stereo3DModeOverride(self: IRenderArgs) -> Stereo3DOutputMode
                                  
                                  Set: Stereo3DModeOverride(self: IRenderArgs) = value
                                   """
                                  )

  StretchToFill = property(None, None, None,
                           """ Get: StretchToFill(self: IRenderArgs) -> bool
                           
                           Set: StretchToFill(self: IRenderArgs) = value
                            """
                           )

  TemplateID = property(None, None, None,
                        """ Get: TemplateID(self: IRenderArgs) -> int
                        
                         """
                        )

  UseChannelMapping = property(None, None, None,
                               """ Get: UseChannelMapping(self: IRenderArgs) -> bool
                               
                               Set: UseChannelMapping(self: IRenderArgs) = value
                                """
                               )

  UseProjectRotation = property(None, None, None,
                                """ Get: UseProjectRotation(self: IRenderArgs) -> bool
                                
                                Set: UseProjectRotation(self: IRenderArgs) = value
                                 """
                                )

  UseSelection = property(None, None, None,
                          """ Get: UseSelection(self: IRenderArgs) -> bool
                          
                          Set: UseSelection(self: IRenderArgs) = value
                           """
                          )

  WaitForIdle = property(None, None, None,
                         """ Get: WaitForIdle(self: IRenderArgs) -> bool
                         
                         Set: WaitForIdle(self: IRenderArgs) = value
                          """
                         )


class IRenderStatusEventArgs:
  """  """

  ErrorMessage = property(None, None, None,
                          """ Get: ErrorMessage(self: IRenderStatusEventArgs) -> str
                          
                           """
                          )

  PercentComplete = property(None, None, None,
                             """ Get: PercentComplete(self: IRenderStatusEventArgs) -> int
                             
                              """
                             )

  Result = property(None, None, None,
                    """ Get: Result(self: IRenderStatusEventArgs) -> int
                    
                     """
                    )

  Status = property(None, None, None,
                    """ Get: Status(self: IRenderStatusEventArgs) -> RenderStatus
                    
                     """
                    )


  pass

class IRenderTemplateCOM:
  """  """

  def CopyTemplate(self, ppTemplate):
    """ CopyTemplate(self: IRenderTemplateCOM) -> IntPtr
     """
    import System
    return System.Void()

  def GetAVInfo(self, punkFormatInfoList):
    """ GetAVInfo(self: IRenderTemplateCOM, punkFormatInfoList: object) -> int
     """
    import System
    return System.int()

  def GetAudioBitsPerSample(self, value):
    """ GetAudioBitsPerSample(self: IRenderTemplateCOM) -> int
     """
    import System
    return System.Void()

  def GetAudioChannelCount(self, value):
    """ GetAudioChannelCount(self: IRenderTemplateCOM) -> int
     """
    import System
    return System.Void()

  def GetAudioChannelMask(self, value):
    """ GetAudioChannelMask(self: IRenderTemplateCOM) -> int
     """
    import System
    return System.Void()

  def GetAudioSampleRate(self, value):
    """ GetAudioSampleRate(self: IRenderTemplateCOM) -> int
     """
    import System
    return System.Void()

  def GetAudioStreamCount(self, value):
    """ GetAudioStreamCount(self: IRenderTemplateCOM) -> int
     """
    import System
    return System.Void()

  def GetBitrate(self, streamTypes, value):
    """ GetBitrate(self: IRenderTemplateCOM, streamTypes: int) -> (int, int)
     """
    import System
    return System.int()

  def GetDescription(self, description):
    """ GetDescription(self: IRenderTemplateCOM) -> str
     """
    import System
    return System.Void()

  def GetFileExtensions(self, rendererID, ext):
    """ GetFileExtensions(self: IRenderTemplateCOM, rendererID: int) -> str
     """
    import System
    return System.Void()

  def GetGuid(self, guid):
    """ GetGuid(self: IRenderTemplateCOM) -> Guid
     """
    import System
    return System.Void()

  def GetName(self, name):
    """ GetName(self: IRenderTemplateCOM) -> str
     """
    import System
    return System.Void()

  def GetNotes(self, notes):
    """ GetNotes(self: IRenderTemplateCOM) -> str
     """
    import System
    return System.Void()

  def GetStatusForContext(self, videoStreams, surroundEnabled, allowMultiFile, mappingEnabled, mappedChannels, status):
    """ GetStatusForContext(self: IRenderTemplateCOM, videoStreams: int, surroundEnabled: bool, allowMultiFile: bool, mappingEnabled: bool, mappedChannels: int) -> int
     """
    import System
    return System.Void()

  def GetTemplateData(self, templateDataStream, cbData):
    """ GetTemplateData(self: IRenderTemplateCOM) -> (IStream, int)
     """
    import System
    return System.Void()

  def GetVideoDataRate(self, value):
    """ GetVideoDataRate(self: IRenderTemplateCOM) -> int
     """
    import System
    return System.Void()

  def GetVideoFPS(self, value):
    """ GetVideoFPS(self: IRenderTemplateCOM) -> float
     """
    import System
    return System.Void()

  def GetVideoFieldOrder(self, value):
    """ GetVideoFieldOrder(self: IRenderTemplateCOM) -> VideoFieldOrder
     """
    import System
    return System.Void()

  def GetVideoHeight(self, value):
    """ GetVideoHeight(self: IRenderTemplateCOM) -> int
     """
    import System
    return System.Void()

  def GetVideoPAR(self, value):
    """ GetVideoPAR(self: IRenderTemplateCOM) -> float
     """
    import System
    return System.Void()

  def GetVideoStreamCount(self, value):
    """ GetVideoStreamCount(self: IRenderTemplateCOM) -> int
     """
    import System
    return System.Void()

  def GetVideoWidth(self, value):
    """ GetVideoWidth(self: IRenderTemplateCOM) -> int
     """
    import System
    return System.Void()

  def ReportInvalidTemplate(self, statusCode, hwndOwner):
    """ ReportInvalidTemplate(self: IRenderTemplateCOM, statusCode: int, hwndOwner: IntPtr) """
    import System
    return System.Void()

class IRendererCOM:
  """  """

  def CanEditTemplates(self, rendererID, value):
    """ CanEditTemplates(self: IRendererCOM, rendererID: int) -> bool
     """
    import System
    return System.Void()

  def CreateTemplateCOM(self, templateDataStream, templateDataSize, com):
    """ CreateTemplateCOM(self: IRendererCOM, templateDataStream: IStream, templateDataSize: int) -> IRenderTemplateCOM
     """
    import System
    return System.Void()

  def GetCapCommands(self, rendererID, value):
    """ GetCapCommands(self: IRendererCOM, rendererID: int) -> bool
     """
    import System
    return System.Void()

  def GetCapLinkedProject(self, rendererID, value):
    """ GetCapLinkedProject(self: IRendererCOM, rendererID: int) -> bool
     """
    import System
    return System.Void()

  def GetCapMarkers(self, rendererID, value):
    """ GetCapMarkers(self: IRendererCOM, rendererID: int) -> bool
     """
    import System
    return System.Void()

  def GetCapMultichannel(self, rendererID, value):
    """ GetCapMultichannel(self: IRendererCOM, rendererID: int) -> bool
     """
    import System
    return System.Void()

  def GetCapMultistream(self, rendererID, value):
    """ GetCapMultistream(self: IRendererCOM, rendererID: int) -> bool
     """
    import System
    return System.Void()

  def GetCount(self, count):
    """ GetCount(self: IRendererCOM) -> int
     """
    import System
    return System.Void()

  def GetInfo(self, rendererID, guid, name, ext):
    """ GetInfo(self: IRendererCOM, rendererID: int) -> (Guid, str, str)
     """
    import System
    return System.Void()

  def GetInfoByClassID(self, classID, rendererID, name, ext):
    """ GetInfoByClassID(self: IRendererCOM, classID: Guid) -> (int, int, str, str)
     """
    import System
    return System.int()

  def GetTemplateCOM(self, rendererID, templateID, com):
    """ GetTemplateCOM(self: IRendererCOM, rendererID: int, templateID: int) -> IRenderTemplateCOM
     """
    import System
    return System.Void()

  def GetTemplateCount(self, rendererID, count):
    """ GetTemplateCount(self: IRendererCOM, rendererID: int) -> int
     """
    import System
    return System.Void()

  def HasAboutBox(self, rendererID, value):
    """ HasAboutBox(self: IRendererCOM, rendererID: int) -> bool
     """
    import System
    return System.Void()

  def HasReader(self, rendererID, value):
    """ HasReader(self: IRendererCOM, rendererID: int) -> bool
     """
    import System
    return System.Void()

  def IsActive(self, guid, value):
    """ IsActive(self: IRendererCOM, guid: Guid) -> bool
     """
    import System
    return System.Void()

  def RefreshTemplateList(self):
    """ RefreshTemplateList(self: IRendererCOM) """
    import System
    return System.Void()

  def ShowAboutBox(self, rendererID, hwndOwner):
    """ ShowAboutBox(self: IRendererCOM, rendererID: int, hwndOwner: IntPtr) -> int
     """
    import System
    return System.int()

class IRendererEnumCOM:
  """  """

  def Detach(self):
    """ Detach(self: IRendererEnumCOM) """
    import System
    return System.Void()

  def GetNextInfo(self, index, rendererID, guid, name, ext, streamTypes):
    """ GetNextInfo(self: IRendererEnumCOM, index: int) -> (int, int, Guid, str, str, int)
     """
    import System
    return System.int()

class IRendererLoadCOM:
  """  """

  def LoadRenderer(self, guid):
    """ LoadRenderer(self: IRendererLoadCOM, guid: Guid) -> int
     """
    import System
    return System.int()

class IRunRenderDialog:
  """  """

  def RunRenderDialog(self, args):
    """ RunRenderDialog(self: IRunRenderDialog, args: IRenderArgs) -> int
     """
    import System
    return System.int()

class IScriptHost:
  """  """

  def FireEvent(self, id, comArgs):
    """ FireEvent(self: IScriptHost, id: VegasEventID, comArgs: object) """
    import System
    return System.Void()

  def Initialize(self, vegasCOM, hwndVegas, hwndExternNotify):
    """ Initialize(self: IScriptHost, vegasCOM: object, hwndVegas: IntPtr, hwndExternNotify: IntPtr) """
    import System
    return System.Void()

  def RunScriptFile(self, scriptFileName, scriptArgs):
    """ RunScriptFile(self: IScriptHost, scriptFileName: str, scriptArgs: str) """
    import System
    return System.Void()

  def RunScriptText(self, scriptText, engineType, compileOnly, scriptArgs):
    """ RunScriptText(self: IScriptHost, scriptText: str, engineType: ScriptEngineType, compileOnly: bool, scriptArgs: str) """
    import System
    return System.Void()

class ISelPastAttrConfig:
  """  """

  def AddItem(self, isOn, index, name):
    """ AddItem(self: ISelPastAttrConfig, isOn: bool, index: int, name: str) """
    import System
    return System.Void()

  CancelDlg = property(None, None, None,
                       """ Get: CancelDlg(self: ISelPastAttrConfig) -> bool
                       
                       Set: CancelDlg(self: ISelPastAttrConfig) = value
                        """
                       )


  def ClearItems(self):
    """ ClearItems(self: ISelPastAttrConfig) """
    import System
    return System.Void()

  Description = property(None, None, None,
                         """ Get: Description(self: ISelPastAttrConfig) -> str
                         
                         Set: Description(self: ISelPastAttrConfig) = value
                          """
                         )


  def GetCount(self, count):
    """ GetCount(self: ISelPastAttrConfig) -> int
     """
    import System
    return System.Void()

  def GetItem(self, index, isOn):
    """ GetItem(self: ISelPastAttrConfig, index: int) -> bool
     """
    import System
    return System.Void()

  def GetItemByIndex(self, index, isOn):
    """ GetItemByIndex(self: ISelPastAttrConfig, index: int) -> bool
     """
    import System
    return System.Void()

  def SetItem(self, index, isOn):
    """ SetItem(self: ISelPastAttrConfig, index: int, isOn: bool) """
    import System
    return System.Void()

  Title = property(None, None, None,
                   """ Get: Title(self: ISelPastAttrConfig) -> str
                   
                   Set: Title(self: ISelPastAttrConfig) = value
                    """
                   )


class IShellLinkW:
  """  """

  def GetArguments(self, pszArgs, cch):
    """ GetArguments(self: IShellLinkW, pszArgs: StringBuilder, cch: int) """
    import System
    return System.Void()

  def GetDescription(self, pszName, cch):
    """ GetDescription(self: IShellLinkW, pszName: StringBuilder, cch: int) """
    import System
    return System.Void()

  def GetHotkey(self, pwHotkey):
    """ GetHotkey(self: IShellLinkW) -> UInt16
     """
    import System
    return System.Void()

  def GetIDList(self, ppidl):
    """ GetIDList(self: IShellLinkW) -> IntPtr
     """
    import System
    return System.Void()

  def GetIconLocation(self, pszIconPath, cch, piIcon):
    """ GetIconLocation(self: IShellLinkW, pszIconPath: StringBuilder, cch: int) -> int
     """
    import System
    return System.Void()

  def GetPath(self, file, cch, pfd, fFlags):
    """ GetPath(self: IShellLinkW, file: StringBuilder, cch: int, fFlags: int) -> IntPtr
     """
    import System
    return System.Void()

  def GetShowCmd(self, piShowCmd):
    """ GetShowCmd(self: IShellLinkW) -> int
     """
    import System
    return System.Void()

  def GetWorkingDirectory(self, pszDir, cch):
    """ GetWorkingDirectory(self: IShellLinkW, pszDir: StringBuilder, cch: int) """
    import System
    return System.Void()

  def Resolve(self, hwnd, fFlags):
    """ Resolve(self: IShellLinkW, hwnd: IntPtr, fFlags: int) """
    import System
    return System.Void()

  def SetArguments(self, pszArgs):
    """ SetArguments(self: IShellLinkW, pszArgs: str) """
    import System
    return System.Void()

  def SetDescription(self, pszName):
    """ SetDescription(self: IShellLinkW, pszName: str) """
    import System
    return System.Void()

  def SetHotkey(self, wHotkey):
    """ SetHotkey(self: IShellLinkW, wHotkey: Int16) """
    import System
    return System.Void()

  def SetIDList(self, pidl):
    """ SetIDList(self: IShellLinkW, pidl: IntPtr) """
    import System
    return System.Void()

  def SetIconLocation(self, pszIconPath, iIcon):
    """ SetIconLocation(self: IShellLinkW, pszIconPath: str, iIcon: int) """
    import System
    return System.Void()

  def SetPath(self, pszFile):
    """ SetPath(self: IShellLinkW, pszFile: str) """
    import System
    return System.Void()

  def SetRelativePath(self, pszPathRel, dwReserved):
    """ SetRelativePath(self: IShellLinkW, pszPathRel: str, dwReserved: int) """
    import System
    return System.Void()

  def SetShowCmd(self, iShowCmd):
    """ SetShowCmd(self: IShellLinkW, iShowCmd: int) """
    import System
    return System.Void()

  def SetWorkingDirectory(self, pszDir):
    """ SetWorkingDirectory(self: IShellLinkW, pszDir: str) """
    import System
    return System.Void()

class ITakeCOM:
  """  """

  def GetAvailableLength(self, trackID, eventID, takeID, length):
    """ GetAvailableLength(self: ITakeCOM, trackID: int, eventID: int, takeID: int) -> int
     """
    import System
    return System.Void()

  def GetLength(self, trackID, eventID, takeID, length):
    """ GetLength(self: ITakeCOM, trackID: int, eventID: int, takeID: int) -> int
     """
    import System
    return System.Void()

  def GetMediaInfo(self, trackID, eventID, takeID, mediaID, metaType, mediaType, streamID, streamIndex):
    """ GetMediaInfo(self: ITakeCOM, trackID: int, eventID: int, takeID: int) -> (int, int, MetaPathType, MediaType, int, int)
     """
    import System
    return System.int()

  def GetMultichannelAudioInfo(self, trackID, eventID, takeID, streamChannelCount, index, count):
    """ GetMultichannelAudioInfo(self: ITakeCOM, trackID: int, eventID: int, takeID: int) -> (int, int, int, int)
     """
    import System
    return System.int()

  def GetName(self, trackID, eventID, takeID, name):
    """ GetName(self: ITakeCOM, trackID: int, eventID: int, takeID: int) -> str
     """
    import System
    return System.Void()

  def GetOffset(self, trackID, eventID, takeID, offset):
    """ GetOffset(self: ITakeCOM, trackID: int, eventID: int, takeID: int) -> int
     """
    import System
    return System.Void()

  def GetStreamIndex(self, trackID, eventID, takeID, index):
    """ GetStreamIndex(self: ITakeCOM, trackID: int, eventID: int, takeID: int) -> int
     """
    import System
    return System.Void()

  def IsActive(self, trackID, eventID, takeID, active):
    """ IsActive(self: ITakeCOM, trackID: int, eventID: int, takeID: int) -> bool
     """
    import System
    return System.Void()

  def SetMultichannelAudioInfo(self, trackID, eventID, takeID, index, count):
    """ SetMultichannelAudioInfo(self: ITakeCOM, trackID: int, eventID: int, takeID: int, index: int, count: int) """
    import System
    return System.Void()

  def SetName(self, trackID, eventID, takeID, name):
    """ SetName(self: ITakeCOM, trackID: int, eventID: int, takeID: int, name: str) """
    import System
    return System.Void()

  def SetOffset(self, trackID, eventID, takeID, offset):
    """ SetOffset(self: ITakeCOM, trackID: int, eventID: int, takeID: int, offset: int) """
    import System
    return System.Void()

class ITrackCOM:
  """  """

  def AddEvent(self, trackID, start, length, eventID, index):
    """ AddEvent(self: ITrackCOM, trackID: int, start: int, length: int) -> (int, int)
     """
    import System
    return System.Void()

  def AddTrackMotionKeyframe(self, trackID, type, position, sessionID):
    """ AddTrackMotionKeyframe(self: ITrackCOM, trackID: int, type: TrackMotionType, position: int) -> int
     """
    import System
    return System.Void()

  def CollapseTrackGroup(self, groupID):
    """ CollapseTrackGroup(self: ITrackCOM, groupID: int) """
    import System
    return System.Void()

  def ExpandTrackGroup(self, groupID):
    """ ExpandTrackGroup(self: ITrackCOM, groupID: int) """
    import System
    return System.Void()

  def GetArmRecord(self, trackID, value):
    """ GetArmRecord(self: ITrackCOM, trackID: int) -> bool
     """
    import System
    return System.Void()

  def GetAudioPanCenterTrim(self, trackID, value):
    """ GetAudioPanCenterTrim(self: ITrackCOM, trackID: int) -> Single
     """
    import System
    return System.Void()

  def GetAudioPanX(self, trackID, value):
    """ GetAudioPanX(self: ITrackCOM, trackID: int) -> Single
     """
    import System
    return System.Void()

  def GetAudioPanXTrim(self, trackID, value):
    """ GetAudioPanXTrim(self: ITrackCOM, trackID: int) -> Single
     """
    import System
    return System.Void()

  def GetAudioPanYTrim(self, trackID, value):
    """ GetAudioPanYTrim(self: ITrackCOM, trackID: int) -> Single
     """
    import System
    return System.Void()

  def GetAudioVolumeTrim(self, trackID, value):
    """ GetAudioVolumeTrim(self: ITrackCOM, trackID: int) -> Single
     """
    import System
    return System.Void()

  def GetBusTrack(self, trackID, busTrackID):
    """ GetBusTrack(self: ITrackCOM, trackID: int) -> int
     """
    import System
    return System.Void()

  def GetBypassMotionBlur(self, trackID, value):
    """ GetBypassMotionBlur(self: ITrackCOM, trackID: int) -> bool
     """
    import System
    return System.Void()

  def GetCompositeMode(self, trackID, parentMode, mode):
    """ GetCompositeMode(self: ITrackCOM, trackID: int, parentMode: bool) -> CompositeMode
     """
    import System
    return System.Void()

  def GetCompositeModeEffectCOM(self, trackID, context):
    """ GetCompositeModeEffectCOM(self: ITrackCOM, trackID: int) -> IEffectCOM
     """
    import System
    return System.Void()

  def GetCompositeNestingLevel(self, trackID, nestingLevel):
    """ GetCompositeNestingLevel(self: ITrackCOM, trackID: int) -> int
     """
    import System
    return System.Void()

  def GetDisplayIndex(self, trackID, index):
    """ GetDisplayIndex(self: ITrackCOM, trackID: int) -> int
     """
    import System
    return System.Void()

  def GetEffectCOM(self, trackID, context):
    """ GetEffectCOM(self: ITrackCOM, trackID: int) -> IEffectCOM
     """
    import System
    return System.Void()

  def GetEnvelopeCOM(self, trackID, context):
    """ GetEnvelopeCOM(self: ITrackCOM, trackID: int) -> IEnvelopeCOM
     """
    import System
    return System.Void()

  def GetEventCount(self, trackID, count):
    """ GetEventCount(self: ITrackCOM, trackID: int) -> int
     """
    import System
    return System.Void()

  def GetEventID(self, trackID, index, eventID):
    """ GetEventID(self: ITrackCOM, trackID: int, index: int) -> int
     """
    import System
    return System.Void()

  def GetGenericMetadata(self, trackID, dataID, dataStream):
    """ GetGenericMetadata(self: ITrackCOM, trackID: int, dataID: Guid, dataStream: IStream) -> int
     """
    import System
    return System.int()

  def GetIndex(self, trackID, index):
    """ GetIndex(self: ITrackCOM, trackID: int) -> int
     """
    import System
    return System.Void()

  def GetInvertPhase(self, trackID, value):
    """ GetInvertPhase(self: ITrackCOM, trackID: int) -> bool
     """
    import System
    return System.Void()

  def GetLength(self, trackID, length):
    """ GetLength(self: ITrackCOM, trackID: int) -> int
     """
    import System
    return System.Void()

  def GetMediaType(self, trackID, mediaType):
    """ GetMediaType(self: ITrackCOM, trackID: int) -> MediaType
     """
    import System
    return System.Void()

  def GetMute(self, trackID, value):
    """ GetMute(self: ITrackCOM, trackID: int) -> bool
     """
    import System
    return System.Void()

  def GetName(self, trackID, name):
    """ GetName(self: ITrackCOM, trackID: int) -> str
     """
    import System
    return System.Void()

  def GetPanXAutomationState(self, trackID, value):
    """ GetPanXAutomationState(self: ITrackCOM, trackID: int) -> AutomationControlAutomationState
     """
    import System
    return System.Void()

  def GetParentCompositeModeEffectCOM(self, trackID, context):
    """ GetParentCompositeModeEffectCOM(self: ITrackCOM, trackID: int) -> IEffectCOM
     """
    import System
    return System.Void()

  def GetSelected(self, trackID, value):
    """ GetSelected(self: ITrackCOM, trackID: int) -> bool
     """
    import System
    return System.Void()

  def GetSolo(self, trackID, value):
    """ GetSolo(self: ITrackCOM, trackID: int) -> bool
     """
    import System
    return System.Void()

  def GetTrackFadeBottomColor(self, trackID, value):
    """ GetTrackFadeBottomColor(self: ITrackCOM, trackID: int) -> SFDIBPIXEL
     """
    import System
    return System.Void()

  def GetTrackFadeTopColor(self, trackID, value):
    """ GetTrackFadeTopColor(self: ITrackCOM, trackID: int) -> SFDIBPIXEL
     """
    import System
    return System.Void()

  def GetTrackGroupCount(self, groupID, count):
    """ GetTrackGroupCount(self: ITrackCOM, groupID: int) -> int
     """
    import System
    return System.Void()

  def GetTrackGroupItem(self, groupID, index, trackID, mediaType):
    """ GetTrackGroupItem(self: ITrackCOM, groupID: int, index: int) -> (int, int)
     """
    import System
    return System.Void()

  def GetTrackGroupMute(self, groupID, value):
    """ GetTrackGroupMute(self: ITrackCOM, groupID: int) -> bool
     """
    import System
    return System.Void()

  def GetTrackGroupName(self, groupID, value):
    """ GetTrackGroupName(self: ITrackCOM, groupID: int) -> str
     """
    import System
    return System.Void()

  def GetTrackGroupSolo(self, groupID, value):
    """ GetTrackGroupSolo(self: ITrackCOM, groupID: int) -> bool
     """
    import System
    return System.Void()

  def GetTrackMotion3DCameraDepthAdjust(self, trackID, type, val):
    """ GetTrackMotion3DCameraDepthAdjust(self: ITrackCOM, trackID: int, type: TrackMotionType) -> float
     """
    import System
    return System.Void()

  def GetTrackMotion3DCameraLensSeparation(self, trackID, type, val):
    """ GetTrackMotion3DCameraLensSeparation(self: ITrackCOM, trackID: int, type: TrackMotionType) -> float
     """
    import System
    return System.Void()

  def GetTrackMotionBlur(self, trackID, type, sessionID, val):
    """ GetTrackMotionBlur(self: ITrackCOM, trackID: int, type: TrackMotionType, sessionID: int) -> float
     """
    import System
    return System.Void()

  def GetTrackMotionColor(self, trackID, type, sessionID, val):
    """ GetTrackMotionColor(self: ITrackCOM, trackID: int, type: TrackMotionType, sessionID: int) -> SFDIBPIXEL
     """
    import System
    return System.Void()

  def GetTrackMotionEnabled(self, trackID, type, value):
    """ GetTrackMotionEnabled(self: ITrackCOM, trackID: int, type: TrackMotionType) -> bool
     """
    import System
    return System.Void()

  def GetTrackMotionIntensity(self, trackID, type, sessionID, val):
    """ GetTrackMotionIntensity(self: ITrackCOM, trackID: int, type: TrackMotionType, sessionID: int) -> float
     """
    import System
    return System.Void()

  def GetTrackMotionKeyframeCount(self, trackID, type, count):
    """ GetTrackMotionKeyframeCount(self: ITrackCOM, trackID: int, type: TrackMotionType) -> int
     """
    import System
    return System.Void()

  def GetTrackMotionKeyframeIndex(self, trackID, type, sessionID, value):
    """ GetTrackMotionKeyframeIndex(self: ITrackCOM, trackID: int, type: TrackMotionType, sessionID: int) -> (int, int)
     """
    import System
    return System.int()

  def GetTrackMotionKeyframeNanos(self, trackID, type, sessionID, value):
    """ GetTrackMotionKeyframeNanos(self: ITrackCOM, trackID: int, type: TrackMotionType, sessionID: int) -> int
     """
    import System
    return System.Void()

  def GetTrackMotionKeyframeSelected(self, trackID, type, sessionID, value):
    """ GetTrackMotionKeyframeSelected(self: ITrackCOM, trackID: int, type: TrackMotionType, sessionID: int) -> bool
     """
    import System
    return System.Void()

  def GetTrackMotionKeyframeSessionID(self, trackID, type, ixKeyframe, sessionID):
    """ GetTrackMotionKeyframeSessionID(self: ITrackCOM, trackID: int, type: TrackMotionType, ixKeyframe: int) -> int
     """
    import System
    return System.Void()

  def GetTrackMotionKeyframeSmoothness(self, trackID, type, sessionID, value):
    """ GetTrackMotionKeyframeSmoothness(self: ITrackCOM, trackID: int, type: TrackMotionType, sessionID: int) -> float
     """
    import System
    return System.Void()

  def GetTrackMotionKeyframeType(self, trackID, type, sessionID, value):
    """ GetTrackMotionKeyframeType(self: ITrackCOM, trackID: int, type: TrackMotionType, sessionID: int) -> VideoKeyframeType
     """
    import System
    return System.Void()

  def GetTrackMotionOrgX(self, trackID, type, sessionID, val):
    """ GetTrackMotionOrgX(self: ITrackCOM, trackID: int, type: TrackMotionType, sessionID: int) -> float
     """
    import System
    return System.Void()

  def GetTrackMotionOrgY(self, trackID, type, sessionID, val):
    """ GetTrackMotionOrgY(self: ITrackCOM, trackID: int, type: TrackMotionType, sessionID: int) -> float
     """
    import System
    return System.Void()

  def GetTrackMotionOrgZ(self, trackID, type, sessionID, val):
    """ GetTrackMotionOrgZ(self: ITrackCOM, trackID: int, type: TrackMotionType, sessionID: int) -> float
     """
    import System
    return System.Void()

  def GetTrackMotionOriX(self, trackID, type, sessionID, val):
    """ GetTrackMotionOriX(self: ITrackCOM, trackID: int, type: TrackMotionType, sessionID: int) -> float
     """
    import System
    return System.Void()

  def GetTrackMotionOriY(self, trackID, type, sessionID, val):
    """ GetTrackMotionOriY(self: ITrackCOM, trackID: int, type: TrackMotionType, sessionID: int) -> float
     """
    import System
    return System.Void()

  def GetTrackMotionOriZ(self, trackID, type, sessionID, val):
    """ GetTrackMotionOriZ(self: ITrackCOM, trackID: int, type: TrackMotionType, sessionID: int) -> float
     """
    import System
    return System.Void()

  def GetTrackMotionPosX(self, trackID, type, sessionID, val):
    """ GetTrackMotionPosX(self: ITrackCOM, trackID: int, type: TrackMotionType, sessionID: int) -> float
     """
    import System
    return System.Void()

  def GetTrackMotionPosY(self, trackID, type, sessionID, val):
    """ GetTrackMotionPosY(self: ITrackCOM, trackID: int, type: TrackMotionType, sessionID: int) -> float
     """
    import System
    return System.Void()

  def GetTrackMotionPosZ(self, trackID, type, sessionID, val):
    """ GetTrackMotionPosZ(self: ITrackCOM, trackID: int, type: TrackMotionType, sessionID: int) -> float
     """
    import System
    return System.Void()

  def GetTrackMotionRotX(self, trackID, type, sessionID, val):
    """ GetTrackMotionRotX(self: ITrackCOM, trackID: int, type: TrackMotionType, sessionID: int) -> float
     """
    import System
    return System.Void()

  def GetTrackMotionRotY(self, trackID, type, sessionID, val):
    """ GetTrackMotionRotY(self: ITrackCOM, trackID: int, type: TrackMotionType, sessionID: int) -> float
     """
    import System
    return System.Void()

  def GetTrackMotionRotZ(self, trackID, type, sessionID, val):
    """ GetTrackMotionRotZ(self: ITrackCOM, trackID: int, type: TrackMotionType, sessionID: int) -> float
     """
    import System
    return System.Void()

  def GetTrackMotionSclX(self, trackID, type, sessionID, val):
    """ GetTrackMotionSclX(self: ITrackCOM, trackID: int, type: TrackMotionType, sessionID: int) -> float
     """
    import System
    return System.Void()

  def GetTrackMotionSclY(self, trackID, type, sessionID, val):
    """ GetTrackMotionSclY(self: ITrackCOM, trackID: int, type: TrackMotionType, sessionID: int) -> float
     """
    import System
    return System.Void()

  def GetTrackMotionSclZ(self, trackID, type, sessionID, val):
    """ GetTrackMotionSclZ(self: ITrackCOM, trackID: int, type: TrackMotionType, sessionID: int) -> float
     """
    import System
    return System.Void()

  def GetVideoCompositeLevel(self, trackID, value):
    """ GetVideoCompositeLevel(self: ITrackCOM, trackID: int) -> Single
     """
    import System
    return System.Void()

  def InsertTrackIntoGroup(self, groupID, trackID, ixWhereToInsert):
    """ InsertTrackIntoGroup(self: ITrackCOM, groupID: int, trackID: int, ixWhereToInsert: int) -> int
     """
    import System
    return System.int()

  def IsCompositingChild(self, trackID, isChild):
    """ IsCompositingChild(self: ITrackCOM, trackID: int) -> bool
     """
    import System
    return System.Void()

  def IsCompositingParent(self, trackID, isParent):
    """ IsCompositingParent(self: ITrackCOM, trackID: int) -> bool
     """
    import System
    return System.Void()

  def RemoveEvent(self, trackID, eventID):
    """ RemoveEvent(self: ITrackCOM, trackID: int, eventID: int) """
    import System
    return System.Void()

  def RemoveTrackMotionKeyframe(self, trackID, type, sessionID):
    """ RemoveTrackMotionKeyframe(self: ITrackCOM, trackID: int, type: TrackMotionType, sessionID: int) -> int
     """
    import System
    return System.int()

  def SetAudioPanCenterTrim(self, trackID, value):
    """ SetAudioPanCenterTrim(self: ITrackCOM, trackID: int, value: Single) """
    import System
    return System.Void()

  def SetAudioPanX(self, trackID, value):
    """ SetAudioPanX(self: ITrackCOM, trackID: int, value: Single) """
    import System
    return System.Void()

  def SetAudioPanXTrim(self, trackID, value):
    """ SetAudioPanXTrim(self: ITrackCOM, trackID: int, value: Single) """
    import System
    return System.Void()

  def SetAudioPanYTrim(self, trackID, value):
    """ SetAudioPanYTrim(self: ITrackCOM, trackID: int, value: Single) """
    import System
    return System.Void()

  def SetAudioVolumeTrim(self, trackID, value):
    """ SetAudioVolumeTrim(self: ITrackCOM, trackID: int, value: Single) """
    import System
    return System.Void()

  def SetAutomationState(self, trackID, value):
    """ SetAutomationState(self: ITrackCOM, trackID: int, value: AutomationReadWriteState) """
    import System
    return System.Void()

  def SetAutomationWritingMode(self, trackID, value):
    """ SetAutomationWritingMode(self: ITrackCOM, trackID: int, value: AutomationWritingMode) """
    import System
    return System.Void()

  def SetBusTrack(self, trackID, busTrackID):
    """ SetBusTrack(self: ITrackCOM, trackID: int, busTrackID: int) """
    import System
    return System.Void()

  def SetBypassMotionBlur(self, trackID, value):
    """ SetBypassMotionBlur(self: ITrackCOM, trackID: int, value: bool) """
    import System
    return System.Void()

  def SetCompositeMode(self, trackID, mode, warnAboutCompositeModeSwitch, parentMode):
    """ SetCompositeMode(self: ITrackCOM, trackID: int, mode: CompositeMode, warnAboutCompositeModeSwitch: bool, parentMode: bool) -> int
     """
    import System
    return System.int()

  def SetCompositeNestingLevel(self, trackID, nestingLevel, newLevel):
    """ SetCompositeNestingLevel(self: ITrackCOM, trackID: int, nestingLevel: int) -> int
     """
    import System
    return System.Void()

  def SetGenericMetadata(self, trackID, dataID, cbData, dataStream):
    """ SetGenericMetadata(self: ITrackCOM, trackID: int, dataID: Guid, cbData: UIntPtr, dataStream: IStream) """
    import System
    return System.Void()

  def SetInvertPhase(self, trackID, value):
    """ SetInvertPhase(self: ITrackCOM, trackID: int, value: bool) """
    import System
    return System.Void()

  def SetMute(self, trackID, value):
    """ SetMute(self: ITrackCOM, trackID: int, value: bool) """
    import System
    return System.Void()

  def SetName(self, trackID, name):
    """ SetName(self: ITrackCOM, trackID: int, name: str) """
    import System
    return System.Void()

  def SetPanXTouch(self, trackID, value):
    """ SetPanXTouch(self: ITrackCOM, trackID: int, value: bool) """
    import System
    return System.Void()

  def SetSelected(self, trackID, value):
    """ SetSelected(self: ITrackCOM, trackID: int, value: bool) """
    import System
    return System.Void()

  def SetSolo(self, trackID, value):
    """ SetSolo(self: ITrackCOM, trackID: int, value: bool) """
    import System
    return System.Void()

  def SetTrackFadeBottomColor(self, trackID, value):
    """ SetTrackFadeBottomColor(self: ITrackCOM, trackID: int, value: SFDIBPIXEL) """
    import System
    return System.Void()

  def SetTrackFadeTopColor(self, trackID, value):
    """ SetTrackFadeTopColor(self: ITrackCOM, trackID: int, value: SFDIBPIXEL) """
    import System
    return System.Void()

  def SetTrackGroupMute(self, groupID, value):
    """ SetTrackGroupMute(self: ITrackCOM, groupID: int, value: bool) """
    import System
    return System.Void()

  def SetTrackGroupName(self, groupID, value):
    """ SetTrackGroupName(self: ITrackCOM, groupID: int, value: str) """
    import System
    return System.Void()

  def SetTrackGroupSolo(self, groupID, value):
    """ SetTrackGroupSolo(self: ITrackCOM, groupID: int, value: bool) """
    import System
    return System.Void()

  def SetTrackMotion3DCameraDepthAdjust(self, trackID, type, val):
    """ SetTrackMotion3DCameraDepthAdjust(self: ITrackCOM, trackID: int, type: TrackMotionType, val: float) -> int
     """
    import System
    return System.int()

  def SetTrackMotion3DCameraLensSeparation(self, trackID, type, val):
    """ SetTrackMotion3DCameraLensSeparation(self: ITrackCOM, trackID: int, type: TrackMotionType, val: float) -> int
     """
    import System
    return System.int()

  def SetTrackMotionBlur(self, trackID, type, sessionID, val):
    """ SetTrackMotionBlur(self: ITrackCOM, trackID: int, type: TrackMotionType, sessionID: int, val: float) -> int
     """
    import System
    return System.int()

  def SetTrackMotionColor(self, trackID, type, sessionID, val):
    """ SetTrackMotionColor(self: ITrackCOM, trackID: int, type: TrackMotionType, sessionID: int, val: SFDIBPIXEL) -> int
     """
    import System
    return System.int()

  def SetTrackMotionEnabled(self, trackID, type, value):
    """ SetTrackMotionEnabled(self: ITrackCOM, trackID: int, type: TrackMotionType, value: bool) -> int
     """
    import System
    return System.int()

  def SetTrackMotionIntensity(self, trackID, type, sessionID, val):
    """ SetTrackMotionIntensity(self: ITrackCOM, trackID: int, type: TrackMotionType, sessionID: int, val: float) -> int
     """
    import System
    return System.int()

  def SetTrackMotionKeyframeNanos(self, trackID, type, sessionID, value):
    """ SetTrackMotionKeyframeNanos(self: ITrackCOM, trackID: int, type: TrackMotionType, sessionID: int, value: int) """
    import System
    return System.Void()

  def SetTrackMotionKeyframeSelected(self, trackID, type, sessionID, value):
    """ SetTrackMotionKeyframeSelected(self: ITrackCOM, trackID: int, type: TrackMotionType, sessionID: int, value: bool) """
    import System
    return System.Void()

  def SetTrackMotionKeyframeSmoothness(self, trackID, type, sessionID, value):
    """ SetTrackMotionKeyframeSmoothness(self: ITrackCOM, trackID: int, type: TrackMotionType, sessionID: int, value: float) """
    import System
    return System.Void()

  def SetTrackMotionKeyframeType(self, trackID, type, sessionID, value):
    """ SetTrackMotionKeyframeType(self: ITrackCOM, trackID: int, type: TrackMotionType, sessionID: int, value: VideoKeyframeType) """
    import System
    return System.Void()

  def SetTrackMotionOrgX(self, trackID, type, sessionID, val):
    """ SetTrackMotionOrgX(self: ITrackCOM, trackID: int, type: TrackMotionType, sessionID: int, val: float) -> int
     """
    import System
    return System.int()

  def SetTrackMotionOrgY(self, trackID, type, sessionID, val):
    """ SetTrackMotionOrgY(self: ITrackCOM, trackID: int, type: TrackMotionType, sessionID: int, val: float) -> int
     """
    import System
    return System.int()

  def SetTrackMotionOrgZ(self, trackID, type, sessionID, val):
    """ SetTrackMotionOrgZ(self: ITrackCOM, trackID: int, type: TrackMotionType, sessionID: int, val: float) -> int
     """
    import System
    return System.int()

  def SetTrackMotionOriX(self, trackID, type, sessionID, val):
    """ SetTrackMotionOriX(self: ITrackCOM, trackID: int, type: TrackMotionType, sessionID: int, val: float) -> int
     """
    import System
    return System.int()

  def SetTrackMotionOriY(self, trackID, type, sessionID, val):
    """ SetTrackMotionOriY(self: ITrackCOM, trackID: int, type: TrackMotionType, sessionID: int, val: float) -> int
     """
    import System
    return System.int()

  def SetTrackMotionOriZ(self, trackID, type, sessionID, val):
    """ SetTrackMotionOriZ(self: ITrackCOM, trackID: int, type: TrackMotionType, sessionID: int, val: float) -> int
     """
    import System
    return System.int()

  def SetTrackMotionPosX(self, trackID, type, sessionID, val):
    """ SetTrackMotionPosX(self: ITrackCOM, trackID: int, type: TrackMotionType, sessionID: int, val: float) -> int
     """
    import System
    return System.int()

  def SetTrackMotionPosY(self, trackID, type, sessionID, val):
    """ SetTrackMotionPosY(self: ITrackCOM, trackID: int, type: TrackMotionType, sessionID: int, val: float) -> int
     """
    import System
    return System.int()

  def SetTrackMotionPosZ(self, trackID, type, sessionID, val):
    """ SetTrackMotionPosZ(self: ITrackCOM, trackID: int, type: TrackMotionType, sessionID: int, val: float) -> int
     """
    import System
    return System.int()

  def SetTrackMotionRotX(self, trackID, type, sessionID, val):
    """ SetTrackMotionRotX(self: ITrackCOM, trackID: int, type: TrackMotionType, sessionID: int, val: float) -> int
     """
    import System
    return System.int()

  def SetTrackMotionRotY(self, trackID, type, sessionID, val):
    """ SetTrackMotionRotY(self: ITrackCOM, trackID: int, type: TrackMotionType, sessionID: int, val: float) -> int
     """
    import System
    return System.int()

  def SetTrackMotionRotZ(self, trackID, type, sessionID, val):
    """ SetTrackMotionRotZ(self: ITrackCOM, trackID: int, type: TrackMotionType, sessionID: int, val: float) -> int
     """
    import System
    return System.int()

  def SetTrackMotionSclX(self, trackID, type, sessionID, val):
    """ SetTrackMotionSclX(self: ITrackCOM, trackID: int, type: TrackMotionType, sessionID: int, val: float) -> int
     """
    import System
    return System.int()

  def SetTrackMotionSclY(self, trackID, type, sessionID, val):
    """ SetTrackMotionSclY(self: ITrackCOM, trackID: int, type: TrackMotionType, sessionID: int, val: float) -> int
     """
    import System
    return System.int()

  def SetTrackMotionSclZ(self, trackID, type, sessionID, val):
    """ SetTrackMotionSclZ(self: ITrackCOM, trackID: int, type: TrackMotionType, sessionID: int, val: float) -> int
     """
    import System
    return System.int()

  def SetVideoCompositeLevel(self, trackID, value):
    """ SetVideoCompositeLevel(self: ITrackCOM, trackID: int, value: Single) """
    import System
    return System.Void()

  def TrackMotionHasData(self, trackID, type, value):
    """ TrackMotionHasData(self: ITrackCOM, trackID: int, type: TrackMotionType) -> bool
     """
    import System
    return System.Void()

  def TrackMotionInitialize(self, trackID, type):
    """ TrackMotionInitialize(self: ITrackCOM, trackID: int, type: TrackMotionType) """
    import System
    return System.Void()

class IVegasCOM:
  """  """

  def AddContextHelpWindowButton(self, hwnd):
    """ AddContextHelpWindowButton(self: IVegasCOM, hwnd: IntPtr) """
    import System
    return System.Void()

  def AddCustomCommand(self, category, cmdName, cmdID, glyphIndex, displayName):
    """ AddCustomCommand(self: IVegasCOM, category: CommandCategory, cmdName: str, cmdID: int, glyphIndex: int, displayName: str) """
    import System
    return System.Void()

  def AddScriptToolbarGlyph(self, glyphFile, glyphIndex):
    """ AddScriptToolbarGlyph(self: IVegasCOM, glyphFile: str) -> (int, int)
     """
    import System
    return System.int()

  def CancelProgMan(self):
    """ CancelProgMan(self: IVegasCOM) """
    import System
    return System.Void()

  def CancelUpload(self):
    """ CancelUpload(self: IVegasCOM) """
    import System
    return System.Void()

  def ChangeAttachedMetaFilename(self, metadataFilename, mediaFilename):
    """ ChangeAttachedMetaFilename(self: IVegasCOM, metadataFilename: str, mediaFilename: str) """
    import System
    return System.Void()

  def CompilerError(self, errorNumber, isWarning, fileName, line, colStart, colEnd, errorText, preFomrattedMsg):
    """ CompilerError(self: IVegasCOM, errorNumber: str, isWarning: bool, fileName: str, line: int, colStart: int, colEnd: int, errorText: str, preFomrattedMsg: str) """
    import System
    return System.Void()

  def CreateDockWindow(self, dockView, windowCaption, windowID, isModal, isClient):
    """ CreateDockWindow(self: IVegasCOM, dockView: IDockView, windowCaption: str, windowID: int, isModal: bool, isClient: bool) """
    import System
    return System.Void()

  def CreatePlexiglass(self, useDefaultCursor):
    """ CreatePlexiglass(self: IVegasCOM, useDefaultCursor: bool) """
    import System
    return System.Void()

  def CreateProjectCOM(self, com):
    """ CreateProjectCOM(self: IVegasCOM) -> IProjectCOM
     """
    import System
    return System.Void()

  def CreateRendererEnumCOM(self, com):
    """ CreateRendererEnumCOM(self: IVegasCOM) -> IRendererEnumCOM
     """
    import System
    return System.Void()

  def CreateRendererLoadCOM(self, com):
    """ CreateRendererLoadCOM(self: IVegasCOM) -> IRendererLoadCOM
     """
    import System
    return System.Void()

  CursorPosition = property(None, None, None,
                            """ Get: CursorPosition(self: IVegasCOM) -> int
                            
                            Set: CursorPosition(self: IVegasCOM) = value
                             """
                            )


  def DebugClear(self):
    """ DebugClear(self: IVegasCOM) """
    import System
    return System.Void()

  def DebugOut(self, msg):
    """ DebugOut(self: IVegasCOM, msg: str) """
    import System
    return System.Void()

  def DestroyPlexiglass(self):
    """ DestroyPlexiglass(self: IVegasCOM) """
    import System
    return System.Void()

  def ErrMsg(self, errMsg):
    """ ErrMsg(self: IVegasCOM, errMsg: str) """
    import System
    return System.Void()

  def Exit(self):
    """ Exit(self: IVegasCOM) """
    import System
    return System.Void()

  def GetAppDataPath(self, baseFolder, appDataPath):
    """ GetAppDataPath(self: IVegasCOM, baseFolder: SpecialFolder) -> str
     """
    import System
    return System.Void()

  def GetAppSkinColor(self, colorID):
    """ GetAppSkinColor(self: IVegasCOM, colorID: AppSkinColorID) -> int
     """
    import System
    return System.int()

  def GetBestThumbForFile(self, filename, scan0, cx, cy, realHR):
    """ GetBestThumbForFile(self: IVegasCOM, filename: str, scan0: IntPtr, cx: int, cy: int) -> int
     """
    import System
    return System.Void()

  def GetBurgerMenuConfig(self, config):
    """ GetBurgerMenuConfig(self: IVegasCOM) -> IBurgerMenuConfig
     """
    import System
    return System.Void()

  def GetBypassAllAudioFX(self, bypass):
    """ GetBypassAllAudioFX(self: IVegasCOM) -> bool
     """
    import System
    return System.Void()

  def GetDefaultRenderClassID(self, eRenderType, streamTypes, val):
    """ GetDefaultRenderClassID(self: IVegasCOM, eRenderType: int, streamTypes: int) -> Guid
     """
    import System
    return System.Void()

  def GetInfoDialogArgs(self, infoDlgArgs):
    """ GetInfoDialogArgs(self: IVegasCOM) -> IInfoDialogArgs
     """
    import System
    return System.Void()

  def GetInterfaceScale(self, scale):
    """ GetInterfaceScale(self: IVegasCOM) -> int
     """
    import System
    return System.Void()

  def GetInterfaceType(self, type):
    """ GetInterfaceType(self: IVegasCOM) -> InterfaceType
     """
    import System
    return System.Void()

  def GetLanguageID(self):
    """ GetLanguageID(self: IVegasCOM) -> int
     """
    import System
    return System.int()

  def GetLastAddPicturesDirectory(self, path):
    """ GetLastAddPicturesDirectory(self: IVegasCOM) -> str
     """
    import System
    return System.Void()

  def GetLicenseInfo(self, userSpecifiedLicense, license, maxHostsPerLicense, maxUnrestrictedRenderers):
    """ GetLicenseInfo(self: IVegasCOM, userSpecifiedLicense: str) -> (str, int, int)
     """
    import System
    return System.Void()

  def GetLongAppName(self, longName):
    """ GetLongAppName(self: IVegasCOM) -> str
     """
    import System
    return System.Void()

  def GetMainToolBarHIL(self, hilStd, hilHot, hilDis):
    """ GetMainToolBarHIL(self: IVegasCOM) -> (IntPtr, IntPtr, IntPtr)
     """
    import System
    return System.Void()

  def GetMaxUndoDescriptionLength(self, maxlength):
    """ GetMaxUndoDescriptionLength(self: IVegasCOM) -> int
     """
    import System
    return System.Void()

  def GetMemStream(self, memStream):
    """ GetMemStream(self: IVegasCOM) -> IStream
     """
    import System
    return System.Void()

  def GetModuleName(self, moduleName):
    """ GetModuleName(self: IVegasCOM) -> str
     """
    import System
    return System.Void()

  def GetNewStillImageLength(self, nanos):
    """ GetNewStillImageLength(self: IVegasCOM) -> int
     """
    import System
    return System.Void()

  def GetPlayLoop(self, start, length):
    """ GetPlayLoop(self: IVegasCOM) -> (int, int)
     """
    import System
    return System.Void()

  def GetPreferenceFlag(self, type, flag):
    """ GetPreferenceFlag(self: IVegasCOM, type: PreferenceFlag) -> bool
     """
    import System
    return System.Void()

  def GetPreferenceintSetting(self, type, setting):
    """ GetPreferenceintSetting(self: IVegasCOM, type: intPreference) -> int
     """
    import System
    return System.Void()

  def GetPreferenceString(self, type, str):
    """ GetPreferenceString(self: IVegasCOM, type: PreferenceString) -> str
     """
    import System
    return System.Void()

  def GetProductID(self, productID):
    """ GetProductID(self: IVegasCOM) -> int
     """
    import System
    return System.Void()

  def GetReduceInterlaceSlideshowEvents(self, value):
    """ GetReduceInterlaceSlideshowEvents(self: IVegasCOM) -> bool
     """
    import System
    return System.Void()

  def GetRenderArgs(self, renderArgs):
    """ GetRenderArgs(self: IVegasCOM) -> IRenderArgs
     """
    import System
    return System.Void()

  def GetScaleFactor(self, scale):
    """ GetScaleFactor(self: IVegasCOM) -> float
     """
    import System
    return System.Void()

  def GetScriptExitFlags(self, flags):
    """ GetScriptExitFlags(self: IVegasCOM) -> ScriptExitFlags
     """
    import System
    return System.Void()

  def GetSelPastAttrConfig(self, config):
    """ GetSelPastAttrConfig(self: IVegasCOM) -> ISelPastAttrConfig
     """
    import System
    return System.Void()

  def GetSelection(self, start, length):
    """ GetSelection(self: IVegasCOM) -> (int, int)
     """
    import System
    return System.Void()

  def GetSettingsPath(self, pathID, settingsPath):
    """ GetSettingsPath(self: IVegasCOM, pathID: SettingsPathID) -> str
     """
    import System
    return System.Void()

  def GetShellLink(self, shellLink):
    """ GetShellLink(self: IVegasCOM) -> object
     """
    import System
    return System.Void()

  def GetShortAppName(self, shortName):
    """ GetShortAppName(self: IVegasCOM) -> str
     """
    import System
    return System.Void()

  def GetSlideshowToolBarHIL(self, hilStd, hilHot, hilDis, pImgX, pImgY):
    """ GetSlideshowToolBarHIL(self: IVegasCOM) -> (IntPtr, IntPtr, IntPtr, IntPtr, IntPtr)
     """
    import System
    return System.Void()

  def GetSpecialPrefsPath(self, pathID, path):
    """ GetSpecialPrefsPath(self: IVegasCOM, pathID: SpecialPrefsPathID) -> str
     """
    import System
    return System.Void()

  def GetTempFilesPath(self, tempFilesPath):
    """ GetTempFilesPath(self: IVegasCOM) -> str
     """
    import System
    return System.Void()

  def GetUsingCustomAppColors(self, value):
    """ GetUsingCustomAppColors(self: IVegasCOM) -> bool
     """
    import System
    return System.Void()

  def GetVersionString(self, versionString):
    """ GetVersionString(self: IVegasCOM) -> str
     """
    import System
    return System.Void()

  def GetVideoDeviceController(self, controller):
    """ GetVideoDeviceController(self: IVegasCOM) -> object
     """
    import System
    return System.Void()

  def HasCompilerErrors(self):
    """ HasCompilerErrors(self: IVegasCOM) -> int
     """
    import System
    return System.int()

  def InvokeCommand(self, section, name):
    """ InvokeCommand(self: IVegasCOM, section: str, name: str) """
    import System
    return System.Void()

  def IsEventSubscribed(self, id):
    """ IsEventSubscribed(self: IVegasCOM, id: VegasEventID) -> int
     """
    import System
    return System.int()

  def IsInScript(self):
    """ IsInScript(self: IVegasCOM) -> int
     """
    import System
    return System.int()

  def IsRestrictedRenderFileClass(self, rendererClassID, isRestricted):
    """ IsRestrictedRenderFileClass(self: IVegasCOM, rendererClassID: Guid) -> (Guid, bool)
     """
    import System
    return System.Void()

  def LaunchCreatorApp(self, fileName):
    """ LaunchCreatorApp(self: IVegasCOM, fileName: str) """
    import System
    return System.Void()

  def LoadWindowLayoutFile(self, layoutFileName):
    """ LoadWindowLayoutFile(self: IVegasCOM, layoutFileName: str) """
    import System
    return System.Void()

  def OnEnterScript(self):
    """ OnEnterScript(self: IVegasCOM) """
    import System
    return System.Void()

  def OnExitScript(self):
    """ OnExitScript(self: IVegasCOM) """
    import System
    return System.Void()

  PlayCursorPosition = property(None, None, None,
                                """ Get: PlayCursorPosition(self: IVegasCOM) -> int
                                
                                 """
                                )


  def PostFrameCommand(self, cmdID):
    """ PostFrameCommand(self: IVegasCOM, cmdID: int) """
    import System
    return System.Void()

  def PurgeAllAutoSaveFiles(self, projectOnly):
    """ PurgeAllAutoSaveFiles(self: IVegasCOM, projectOnly: bool) """
    import System
    return System.Void()

  def QueueProgmanEvent(self, punkWorker):
    """ QueueProgmanEvent(self: IVegasCOM, punkWorker: object) """
    import System
    return System.Void()

  def QueueSerialProgmanEvent(self, workerFunction):
    """ QueueSerialProgmanEvent(self: IVegasCOM, workerFunction: IntPtr) """
    import System
    return System.Void()

  def RemoveMinMaxWindowButtons(self, hwnd):
    """ RemoveMinMaxWindowButtons(self: IVegasCOM, hwnd: IntPtr) """
    import System
    return System.Void()

  def ResetFPU(self):
    """ ResetFPU(self: IVegasCOM) """
    import System
    return System.Void()

  def RunScriptFile(self, scriptFile, scriptArgs):
    """ RunScriptFile(self: IVegasCOM, scriptFile: str, scriptArgs: str) """
    import System
    return System.Void()

  def RunScriptText(self, scriptText, scriptType, compileOnly, scriptArgs):
    """ RunScriptText(self: IVegasCOM, scriptText: str, scriptType: ScriptEngineType, compileOnly: bool, scriptArgs: str) """
    import System
    return System.Void()

  def SaveSnapshot(self, path, imageFormat, seekTime, status):
    """ SaveSnapshot(self: IVegasCOM, path: str, imageFormat: int, seekTime: int) -> int
     """
    import System
    return System.Void()

  def SetBypassAllAudioFX(self, bypass):
    """ SetBypassAllAudioFX(self: IVegasCOM, bypass: bool) """
    import System
    return System.Void()

  def SetFocus(self):
    """ SetFocus(self: IVegasCOM) """
    import System
    return System.Void()

  def SetLastAddPicturesDirectory(self, path):
    """ SetLastAddPicturesDirectory(self: IVegasCOM, path: str) """
    import System
    return System.Void()

  def SetPlayLoop(self, start, length, fieldFlags):
    """ SetPlayLoop(self: IVegasCOM, start: int, length: int, fieldFlags: int) """
    import System
    return System.Void()

  def SetPreferenceFlag(self, type, flag):
    """ SetPreferenceFlag(self: IVegasCOM, type: PreferenceFlag, flag: bool) """
    import System
    return System.Void()

  def SetPreferenceintSetting(self, type, setting):
    """ SetPreferenceintSetting(self: IVegasCOM, type: intPreference, setting: int) """
    import System
    return System.Void()

  def SetPreferenceString(self, type, str):
    """ SetPreferenceString(self: IVegasCOM, type: PreferenceString, str: str) """
    import System
    return System.Void()

  def SetScriptExitFlags(self, flags, value):
    """ SetScriptExitFlags(self: IVegasCOM, flags: ScriptExitFlags, value: bool) """
    import System
    return System.Void()

  def SetSelection(self, start, length, fialdFlags):
    """ SetSelection(self: IVegasCOM, start: int, length: int, fialdFlags: int) """
    import System
    return System.Void()

  def SetSettingsPath(self, pathID, settingsPath):
    """ SetSettingsPath(self: IVegasCOM, pathID: SettingsPathID, settingsPath: str) """
    import System
    return System.Void()

  def SetSpecialPrefsPath(self, pathID, path):
    """ SetSpecialPrefsPath(self: IVegasCOM, pathID: SpecialPrefsPathID, path: str) """
    import System
    return System.Void()

  def SetTileSize(self, cxTileWidth, cyTileHeight):
    """ SetTileSize(self: IVegasCOM, cxTileWidth: int, cyTileHeight: int) """
    import System
    return System.Void()

  def ShowError(self, summary, details):
    """ ShowError(self: IVegasCOM, summary: str, details: str) """
    import System
    return System.Void()

  def ShowHelp(self, hwndCaller, helpID):
    """ ShowHelp(self: IVegasCOM, hwndCaller: IntPtr, helpID: int) -> int
     """
    import System
    return System.int()

  def SignalNewListOfSyncFiles(self):
    """ SignalNewListOfSyncFiles(self: IVegasCOM) """
    import System
    return System.Void()

  def SubscribeEvent(self, id):
    """ SubscribeEvent(self: IVegasCOM, id: VegasEventID) """
    import System
    return System.Void()

  def SuppressUndoBlockCheck(self, createIfNeeded):
    """ SuppressUndoBlockCheck(self: IVegasCOM, createIfNeeded: bool) """
    import System
    return System.Void()

  TransportIsPlaying = property(None, None, None,
                                """ Get: TransportIsPlaying(self: IVegasCOM) -> bool
                                
                                 """
                                )

  TransportIsRecMonitoring = property(None, None, None,
                                      """ Get: TransportIsRecMonitoring(self: IVegasCOM) -> bool
                                      
                                       """
                                      )

  TransportIsRecording = property(None, None, None,
                                  """ Get: TransportIsRecording(self: IVegasCOM) -> bool
                                  
                                   """
                                  )

  TransportLoopMode = property(None, None, None,
                               """ Get: TransportLoopMode(self: IVegasCOM) -> bool
                               
                               Set: TransportLoopMode(self: IVegasCOM) = value
                                """
                               )


  def TransportPause(self):
    """ TransportPause(self: IVegasCOM) """
    import System
    return System.Void()

  def TransportPlay(self):
    """ TransportPlay(self: IVegasCOM) """
    import System
    return System.Void()

  def TransportPlayFromStart(self):
    """ TransportPlayFromStart(self: IVegasCOM) """
    import System
    return System.Void()

  def TransportProfileAtTimeStamp(self, startTime, endTime, duration, framerate):
    """ TransportProfileAtTimeStamp(self: IVegasCOM, startTime: int, endTime: int) -> (float, float)
     """
    import System
    return System.Void()

  def TransportProfileForMarker(self, startMarkerId, endMarkerId, duration, framerate):
    """ TransportProfileForMarker(self: IVegasCOM, startMarkerId: int, endMarkerId: int) -> (float, float)
     """
    import System
    return System.Void()

  def TransportProfileForRegion(self, index, duration, framerate):
    """ TransportProfileForRegion(self: IVegasCOM, index: int) -> (float, float)
     """
    import System
    return System.Void()

  def TransportProfileSelection(self, duration, framerate):
    """ TransportProfileSelection(self: IVegasCOM) -> (float, float)
     """
    import System
    return System.Void()

  def TransportResume(self, forFX):
    """ TransportResume(self: IVegasCOM, forFX: bool) -> int
     """
    import System
    return System.int()

  def TransportStop(self):
    """ TransportStop(self: IVegasCOM) """
    import System
    return System.Void()

  def TransportSuspend(self, forFX):
    """ TransportSuspend(self: IVegasCOM, forFX: bool) -> int
     """
    import System
    return System.int()

  def TutorNotify(self, NotifyID):
    """ TutorNotify(self: IVegasCOM, NotifyID: int) """
    import System
    return System.Void()

  def UnsubscribeEvent(self, id):
    """ UnsubscribeEvent(self: IVegasCOM, id: VegasEventID) """
    import System
    return System.Void()

  def UpdateUI(self):
    """ UpdateUI(self: IVegasCOM) """
    import System
    return System.Void()

  def UploadToOFACommunity(self, communityID, filePath, title, description, tags, privateBroadcast, value):
    """ UploadToOFACommunity(self: IVegasCOM, communityID: int, filePath: str, title: str, description: str, tags: str, privateBroadcast: bool) -> bool
     """
    import System
    return System.Void()

  def ViewCursor(self, centered):
    """ ViewCursor(self: IVegasCOM, centered: bool) """
    import System
    return System.Void()

  def WaitForIdle(self):
    """ WaitForIdle(self: IVegasCOM) """
    import System
    return System.Void()

  def ZoomSelection(self):
    """ ZoomSelection(self: IVegasCOM) """
    import System
    return System.Void()

class IVideoMotionCOM:
  """  """

  def AddKeyframe(self, trackID, eventID, listType, pos, index):
    """ AddKeyframe(self: IVideoMotionCOM, trackID: int, eventID: int, listType: VMKeyframeType, pos: int) -> int
     """
    import System
    return System.Void()

  def GetFlags(self, trackID, eventID, flags):
    """ GetFlags(self: IVideoMotionCOM, trackID: int, eventID: int) -> int
     """
    import System
    return System.Void()

  def GetKeyframeAngle(self, trackID, eventID, listType, keyframeID, angle):
    """ GetKeyframeAngle(self: IVideoMotionCOM, trackID: int, eventID: int, listType: VMKeyframeType, keyframeID: int) -> float
     """
    import System
    return System.Void()

  def GetKeyframeBounds(self, trackID, eventID, listType, keyframeID, tlX, tlY, trX, trY, blX, blY, brX, brY):
    """ GetKeyframeBounds(self: IVideoMotionCOM, trackID: int, eventID: int, listType: VMKeyframeType, keyframeID: int) -> (Single, Single, Single, Single, Single, Single, Single, Single)
     """
    import System
    return System.Void()

  def GetKeyframeCount(self, trackID, eventID, listType, count):
    """ GetKeyframeCount(self: IVideoMotionCOM, trackID: int, eventID: int, listType: VMKeyframeType) -> int
     """
    import System
    return System.Void()

  def GetKeyframePosition(self, trackID, eventID, listType, keyframeID, pos):
    """ GetKeyframePosition(self: IVideoMotionCOM, trackID: int, eventID: int, listType: VMKeyframeType, keyframeID: int) -> int
     """
    import System
    return System.Void()

  def GetKeyframeTension(self, trackID, eventID, listType, keyframeID, tension):
    """ GetKeyframeTension(self: IVideoMotionCOM, trackID: int, eventID: int, listType: VMKeyframeType, keyframeID: int) -> Single
     """
    import System
    return System.Void()

  def GetKeyframeType(self, trackID, eventID, listType, keyframeID, curveType):
    """ GetKeyframeType(self: IVideoMotionCOM, trackID: int, eventID: int, listType: VMKeyframeType, keyframeID: int) -> VideoKeyframeType
     """
    import System
    return System.Void()

  def GetKeyframeVertex(self, trackID, eventID, listType, keyframeID, vertexID, x, y):
    """ GetKeyframeVertex(self: IVideoMotionCOM, trackID: int, eventID: int, listType: VMKeyframeType, keyframeID: int, vertexID: int) -> (Single, Single)
     """
    import System
    return System.Void()

  def RemoveKeyframe(self, trackID, eventID, listType, keyframeID):
    """ RemoveKeyframe(self: IVideoMotionCOM, trackID: int, eventID: int, listType: VMKeyframeType, keyframeID: int) """
    import System
    return System.Void()

  def RotateKeyframe(self, trackID, eventID, listType, keyframeID, angle):
    """ RotateKeyframe(self: IVideoMotionCOM, trackID: int, eventID: int, listType: VMKeyframeType, keyframeID: int, angle: float) """
    import System
    return System.Void()

  def ScaleKeyframe(self, trackID, eventID, listType, keyframeID, x, y):
    """ ScaleKeyframe(self: IVideoMotionCOM, trackID: int, eventID: int, listType: VMKeyframeType, keyframeID: int, x: Single, y: Single) """
    import System
    return System.Void()

  def SetKeyframeAngle(self, trackID, eventID, listType, keyframeID, angle):
    """ SetKeyframeAngle(self: IVideoMotionCOM, trackID: int, eventID: int, listType: VMKeyframeType, keyframeID: int, angle: float) """
    import System
    return System.Void()

  def SetKeyframeBounds(self, trackID, eventID, listType, keyframeID, tlX, tlY, trX, trY, blX, blY, brX, brY):
    """ SetKeyframeBounds(self: IVideoMotionCOM, trackID: int, eventID: int, listType: VMKeyframeType, keyframeID: int, tlX: Single, tlY: Single, trX: Single, trY: Single, blX: Single, blY: Single, brX: Single, brY: Single) -> int
     """
    import System
    return System.int()

  def SetKeyframePosition(self, trackID, eventID, listType, keyframeID, pos, newID):
    """ SetKeyframePosition(self: IVideoMotionCOM, trackID: int, eventID: int, listType: VMKeyframeType, keyframeID: int, pos: int) -> int
     """
    import System
    return System.Void()

  def SetKeyframeTension(self, trackID, eventID, listType, keyframeID, tension):
    """ SetKeyframeTension(self: IVideoMotionCOM, trackID: int, eventID: int, listType: VMKeyframeType, keyframeID: int, tension: Single) """
    import System
    return System.Void()

  def SetKeyframeType(self, trackID, eventID, listType, keyframeID, curveType):
    """ SetKeyframeType(self: IVideoMotionCOM, trackID: int, eventID: int, listType: VMKeyframeType, keyframeID: int, curveType: VideoKeyframeType) """
    import System
    return System.Void()

  def SetKeyframeVertex(self, trackID, eventID, listType, keyframeID, vertexID, x, y):
    """ SetKeyframeVertex(self: IVideoMotionCOM, trackID: int, eventID: int, listType: VMKeyframeType, keyframeID: int, vertexID: int, x: Single, y: Single) """
    import System
    return System.Void()

  def SetScaleToFit(self, trackID, eventID, scale):
    """ SetScaleToFit(self: IVideoMotionCOM, trackID: int, eventID: int, scale: bool) """
    import System
    return System.Void()

  def TranslateKeyframe(self, trackID, eventID, listType, keyframeID, x, y):
    """ TranslateKeyframe(self: IVideoMotionCOM, trackID: int, eventID: int, listType: VMKeyframeType, keyframeID: int, x: Single, y: Single) """
    import System
    return System.Void()

class ImageFileFormat(Enum):
  """ 
  
  enum ImageFileFormat, values: JPEG (2), PNG (1), Unknown (0)
  
   """

  def Format(self, arg0, arg1, arg2):
    """ Format(enumType: Type, value: object, format: str) -> str
     """
    return ""

  def GetName(self, arg0, arg1):
    """ GetName(enumType: Type, value: object) -> str
     """
    return ""

  def GetNames(self, arg0):
    """ GetNames(enumType: Type) -> Array[str]
     """
    return ""

  def GetUnderlyingType(self, arg0):
    """ GetUnderlyingType(enumType: Type) -> Type
     """
    return None

  def GetValues(self, arg0):
    """ GetValues(enumType: Type) -> Array
     """
    return None

  def IsDefined(self, arg0, arg1):
    """ IsDefined(enumType: Type, value: object) -> bool
     """
    return None

  JPEG = None
  PNG = None

  def Parse(self, arg0, arg1):
    """ Parse(enumType: Type, value: str) -> object
    Parse(enumType: Type, value: str, ignoreCase: bool) -> object
     """
    return None

  def ReferenceEquals(objA: object, objB: object) -> bool:
    """ ReferenceEquals(objA: object, objB: object) -> bool
     """
    return None

  def ToObject(self, arg0, arg1):
    """ ToObject(enumType: Type, value: object) -> object
    ToObject(enumType: Type, value: SByte) -> object
    ToObject(enumType: Type, value: Int16) -> object
    ToObject(enumType: Type, value: int) -> object
    ToObject(enumType: Type, value: Byte) -> object
    ToObject(enumType: Type, value: UInt16) -> object
    ToObject(enumType: Type, value: int) -> object
    ToObject(enumType: Type, value: int) -> object
    ToObject(enumType: Type, value: int) -> object
     """
    return None

  def TryParse(self, arg0):
    """ TryParse[TEnum](value: str) -> (bool, TEnum)
    TryParse[TEnum](value: str, ignoreCase: bool) -> (bool, TEnum)
     """
    return (None, None)

  Unknown = None
  value__ = None

class ImageSequence(Media):
  """  """

  def CreateInstance(self, arg0, arg1):
    """ CreateInstance(project: Project, path: str) -> Media
    CreateInstance(project: Project, generator: PlugInNode, presetName: str) -> Media
    CreateInstance(project: Project, generator: PlugInNode) -> Media
     """
    return None

  ImageBaseName = property(None, None, None,
                           """ Get: ImageBaseName(self: ImageSequence) -> str
                           
                            """
                           )

  ImageFilePaths = property(None, None, None,
                            """ Get: ImageFilePaths(self: ImageSequence) -> Array[str]
                            
                             """
                            )


  def ImagePathWithNewBaseName(self, baseName, index):
    """ ImagePathWithNewBaseName(self: ImageSequence, baseName: str, index: int) -> str
     """
    import System
    return System.String()

  MEDIA_FLAG_CUSTOM_OFFSET = None

  def ReferenceEquals(objA: object, objB: object) -> bool:
    """ ReferenceEquals(objA: object, objB: object) -> bool
     """
    return None

  SourceUMIDCustomDataID = None
  myCOM = None
  myCustomDataContainer = None
  myEffectCOM = None
  myEffects = None
  myGenerator = None
  myMediaID = None
  myMetaPathType = None
  myProject = None

class ImproperProjectSettingException(ArgumentException):
  """ ImproperProjectSettingException()
   """

  def ReferenceEquals(objA: object, objB: object) -> bool:
    """ ReferenceEquals(objA: object, objB: object) -> bool
     """
    return None

  SerializeObjectState = None

class IneligableMediaException(ArgumentException):
  """ IneligableMediaException()
   """

  def ReferenceEquals(objA: object, objB: object) -> bool:
    """ ReferenceEquals(objA: object, objB: object) -> bool
     """
    return None

  SerializeObjectState = None

class InfoDialogArgs(object):
  """ InfoDialogArgs()
   """

  Description = property(None, None, None,
                         """ Get: Description(self: InfoDialogArgs) -> str
                         
                         Set: Description(self: InfoDialogArgs) = value
                          """
                         )


  def ReferenceEquals(objA: object, objB: object) -> bool:
    """ ReferenceEquals(objA: object, objB: object) -> bool
     """
    return None

  Title = property(None, None, None,
                   """ Get: Title(self: InfoDialogArgs) -> str
                   
                   Set: Title(self: InfoDialogArgs) = value
                    """
                   )

  m_description = None
  m_title = None

class intListSetting(ListSetting[int]):
  """ intListSetting(name: str)
   """

  def ItemFromString(self, arg0, arg1):
    """ ItemFromString(self: intListSetting, s: str) -> int
     """
    return 1

  def ItemToString(self, arg0, arg1):
    """ ItemToString(self: intListSetting, item: int) -> str
     """
    return ""

  Name = None

  def ReferenceEquals(objA: object, objB: object) -> bool:
    """ ReferenceEquals(objA: object, objB: object) -> bool
     """
    return None

  Value = None

class intPreference(Enum):
  """ 
  
  enum intPreference, values: AutoSaveDailyMaxSaves (2), AutoSaveHourlyInterval (1), AutoSaveMinuteInterval (0), AutoSaveRealTimeMaxSaves (3), InsertSubtitlesDefaultIndex (4), InsertSubtitlesFromRegionsDefaultIndex (5)
  
   """

  AutoSaveDailyMaxSaves = None
  AutoSaveHourlyInterval = None
  AutoSaveMinuteInterval = None
  AutoSaveRealTimeMaxSaves = None

  def Format(self, arg0, arg1, arg2):
    """ Format(enumType: Type, value: object, format: str) -> str
     """
    return ""

  def GetName(self, arg0, arg1):
    """ GetName(enumType: Type, value: object) -> str
     """
    return ""

  def GetNames(self, arg0):
    """ GetNames(enumType: Type) -> Array[str]
     """
    return ""

  def GetUnderlyingType(self, arg0):
    """ GetUnderlyingType(enumType: Type) -> Type
     """
    return None

  def GetValues(self, arg0):
    """ GetValues(enumType: Type) -> Array
     """
    return None

  InsertSubtitlesDefaultIndex = None
  InsertSubtitlesFromRegionsDefaultIndex = None

  def IsDefined(self, arg0, arg1):
    """ IsDefined(enumType: Type, value: object) -> bool
     """
    return None

  def Parse(self, arg0, arg1):
    """ Parse(enumType: Type, value: str) -> object
    Parse(enumType: Type, value: str, ignoreCase: bool) -> object
     """
    return None

  def ReferenceEquals(objA: object, objB: object) -> bool:
    """ ReferenceEquals(objA: object, objB: object) -> bool
     """
    return None

  def ToObject(self, arg0, arg1):
    """ ToObject(enumType: Type, value: object) -> object
    ToObject(enumType: Type, value: SByte) -> object
    ToObject(enumType: Type, value: Int16) -> object
    ToObject(enumType: Type, value: int) -> object
    ToObject(enumType: Type, value: Byte) -> object
    ToObject(enumType: Type, value: UInt16) -> object
    ToObject(enumType: Type, value: int) -> object
    ToObject(enumType: Type, value: int) -> object
    ToObject(enumType: Type, value: int) -> object
     """
    return None

  def TryParse(self, arg0):
    """ TryParse[TEnum](value: str) -> (bool, TEnum)
    TryParse[TEnum](value: str, ignoreCase: bool) -> (bool, TEnum)
     """
    return (None, None)

  value__ = None

class intSetting(XmlSetting):
  """ intSetting(name: str, val: int)
   """

  def FromString(self, value):
    """ FromString(self: intSetting, value: str) """
    import System
    return System.Void()

  Name = None

  def ReferenceEquals(objA: object, objB: object) -> bool:
    """ ReferenceEquals(objA: object, objB: object) -> bool
     """
    return None

  def ToString(self):
    """ ToString(self: intSetting) -> str
     """
    import System
    return System.String()

  Value = None

class intListSetting(ListSetting[int]):
  """ intListSetting(name: str)
   """

  def ItemFromString(self, arg0, arg1):
    """ ItemFromString(self: intListSetting, s: str) -> int
     """
    return None

  def ItemToString(self, arg0, arg1):
    """ ItemToString(self: intListSetting, item: int) -> str
     """
    return ""

  Name = None

  def ReferenceEquals(objA: object, objB: object) -> bool:
    """ ReferenceEquals(objA: object, objB: object) -> bool
     """
    return None

  Value = None

class intSetting(XmlSetting):
  """ intSetting(name: str, val: int)
   """

  def FromString(self, value):
    """ FromString(self: intSetting, value: str) """
    import System
    return System.Void()

  Name = None

  def ReferenceEquals(objA: object, objB: object) -> bool:
    """ ReferenceEquals(objA: object, objB: object) -> bool
     """
    return None

  def ToString(self):
    """ ToString(self: intSetting) -> str
     """
    import System
    return System.String()

  Value = None

class InterfaceType(Enum):
  """ 
  
  enum InterfaceType, values: Dark (0), Light (2), Medium (1), White (3)
  
   """

  Dark = None

  def Format(self, arg0, arg1, arg2):
    """ Format(enumType: Type, value: object, format: str) -> str
     """
    return ""

  def GetName(self, arg0, arg1):
    """ GetName(enumType: Type, value: object) -> str
     """
    return ""

  def GetNames(self, arg0):
    """ GetNames(enumType: Type) -> Array[str]
     """
    return ""

  def GetUnderlyingType(self, arg0):
    """ GetUnderlyingType(enumType: Type) -> Type
     """
    return None

  def GetValues(self, arg0):
    """ GetValues(enumType: Type) -> Array
     """
    return None

  def IsDefined(self, arg0, arg1):
    """ IsDefined(enumType: Type, value: object) -> bool
     """
    return None

  Light = None
  Medium = None

  def Parse(self, arg0, arg1):
    """ Parse(enumType: Type, value: str) -> object
    Parse(enumType: Type, value: str, ignoreCase: bool) -> object
     """
    return None

  def ReferenceEquals(objA: object, objB: object) -> bool:
    """ ReferenceEquals(objA: object, objB: object) -> bool
     """
    return None

  def ToObject(self, arg0, arg1):
    """ ToObject(enumType: Type, value: object) -> object
    ToObject(enumType: Type, value: SByte) -> object
    ToObject(enumType: Type, value: Int16) -> object
    ToObject(enumType: Type, value: int) -> object
    ToObject(enumType: Type, value: Byte) -> object
    ToObject(enumType: Type, value: UInt16) -> object
    ToObject(enumType: Type, value: int) -> object
    ToObject(enumType: Type, value: int) -> object
    ToObject(enumType: Type, value: int) -> object
     """
    return None

  def TryParse(self, arg0):
    """ TryParse[TEnum](value: str) -> (bool, TEnum)
    TryParse[TEnum](value: str, ignoreCase: bool) -> (bool, TEnum)
     """
    return (None, None)

  White = None
  value__ = None

class Keyframe(object):
  """ Represents a video effect key frame.
  Keyframe(position: Timecode)
   """

  Effect: Effect_
                    
  

  Index:  int
   
  def IsValid(self: Keyframe) -> bool:
    """ IsValid(self: Keyframe) -> bool
     """
    import System
    return System.Boolean()

  Position:  Timecode
  

  Preset: str
  

  Type: VideoKeyframeType
  

class Keyframes(BaseList[Keyframe]):
  """ Collection of effect key frames. """

  def BaseAdd(self, arg0, arg1):
    """ BaseAdd(self: Keyframes, item: Keyframe) -> int
     """
    return 1

  def BaseIndex(self, arg0, arg1):
    """ BaseIndex(self: Keyframes, item: Keyframe) -> int
     """
    return 1

  def BaseRemove(self, arg0, arg1):
    """ BaseRemove(self: Keyframes, item: Keyframe) -> bool
     """
    return None

  def GetCount(self, arg0):
    """ GetCount(self: Keyframes) -> int
     """
    return 1

  def GetItem(self, arg0, arg1):
    """ GetItem(self: Keyframes, index: int) -> Keyframe
     """
    return None

  def ReferenceEquals(objA: object, objB: object) -> bool:
    """ ReferenceEquals(objA: object, objB: object) -> bool
     """
    return None

  
class ListSetting(XmlSetting):
  """ ListSetting[T](name: str)
   """

  def FromString(self, s):
    """ FromString(self: ListSetting[T], s: str) """
    import System
    return System.Void()

  def FromXml(self, elt):
    """ FromXml(self: ListSetting[T], elt: XmlElement) """
    import System
    return System.Void()

  def ItemFromString(self, arg0=None, arg1=None):
    """ ItemFromString(self: ListSetting[T], s: str) -> T
     """
    return None

  def ItemToString(self, arg0=None, arg1=None):
    """ ItemToString(self: ListSetting[T], item: T) -> str
     """
    return ""

  Name = None

  def ReferenceEquals(objA: object, objB: object) -> bool:
    """ ReferenceEquals(objA: object, objB: object) -> bool
     """
    return None

  def ToXml(self, elt):
    """ ToXml(self: ListSetting[T], elt: XmlElement) """
    import System
    return System.Void()

  Value = None

class LogCallback(MulticastDelegate):
  """ This delegate matches the signature of AddLogEntry(string) 
  LogCallback(object: object, method: IntPtr)
   """

  def BeginInvoke(self, log, callback, object):
    """ BeginInvoke(self: LogCallback, log: str, callback: AsyncCallback, object: object) -> IAsyncResult
     """
    import System
    return System.IAsyncResult()

  def Combine(self, arg0, arg1):
    """ Combine(a: Delegate, b: Delegate) -> Delegate
    Combine(*delegates: Array[Delegate]) -> Delegate
     """
    return None

  def CreateDelegate(self, arg0, arg1, arg2):
    """ CreateDelegate(type: Type, target: object, method: str) -> Delegate
    CreateDelegate(type: Type, target: object, method: str, ignoreCase: bool) -> Delegate
    CreateDelegate(type: Type, target: object, method: str, ignoreCase: bool, throwOnBindFailure: bool) -> Delegate
    CreateDelegate(type: Type, target: Type, method: str) -> Delegate
    CreateDelegate(type: Type, target: Type, method: str, ignoreCase: bool) -> Delegate
    CreateDelegate(type: Type, target: Type, method: str, ignoreCase: bool, throwOnBindFailure: bool) -> Delegate
    CreateDelegate(type: Type, method: MethodInfo, throwOnBindFailure: bool) -> Delegate
    CreateDelegate(type: Type, firstArgument: object, method: MethodInfo) -> Delegate
    CreateDelegate(type: Type, firstArgument: object, method: MethodInfo, throwOnBindFailure: bool) -> Delegate
    CreateDelegate(type: Type, method: MethodInfo) -> Delegate
     """
    return None

  def EndInvoke(self, result):
    """ EndInvoke(self: LogCallback, result: IAsyncResult) """
    import System
    return System.Void()

  def Invoke(self, log):
    """ Invoke(self: LogCallback, log: str) """
    import System
    return System.Void()

  def ReferenceEquals(objA: object, objB: object) -> bool:
    """ ReferenceEquals(objA: object, objB: object) -> bool
     """
    return None

  def Remove(self, arg0, arg1):
    """ Remove(source: Delegate, value: Delegate) -> Delegate
     """
    return None

  def RemoveAll(self, arg0, arg1):
    """ RemoveAll(source: Delegate, value: Delegate) -> Delegate
     """
    return None

class LogFile(object):
  """ This is a very simple implementation of a file-based logger. 
  LogFile()
  LogFile(vegas: Vegas, logFilePath: str)
   """

  def AddLogEntry(self, entry):
    """ AddLogEntry(self: LogFile, entry: str) """
    import System
    return System.Void()

  AutoFlush:  bool
  

  def Close(self: LogFile):
    """ Close(self: LogFile) """
    import System
    return System.Void()

  def Dispose(self):
    """ Dispose(self: LogFile) """
    import System
    return System.Void()

  def ReferenceEquals(objA: object, objB: object) -> bool:
    """ ReferenceEquals(objA: object, objB: object) -> bool
     """
    return None

  def ShowLogAsDialog(self, title):
    """ ShowLogAsDialog(self: LogFile, title: str) """
    import System
    return System.Void()

class LowPassFilterQuality(Enum):
  """ 
  Enumeration of low-pass filter qualities
Syntax:
  enum LowPassFilterQuality, values: Best (2), Good (1), Preview (0)
  
   """

  Best = None
  Good = None
  Preview = None


class MS(object):
  """ MS()
   """

  def AppendMenu(self, hmenu, uFlags, uIDNewItem, lpNewItem):
    """ AppendMenu(hmenu: UIntPtr, uFlags: MenuFlags, uIDNewItem: UIntPtr, lpNewItem: str) -> bool
     """
    import System
    return System.Boolean()

  class COPYDATASTRUCT(object):
    """  """

    def ReferenceEquals(objA: object, objB: object) -> bool:
      """ ReferenceEquals(objA: object, objB: object) -> bool
       """
      return None

    cbData = None
    dwData = None
    lpData = None

  def ClientToScreen(self, hWnd, lpPoint):
    """ ClientToScreen(hWnd: IntPtr) -> (bool, POINT)
     """
    import System
    return System.Boolean()

  def CreatePopupMenu(self):
    """ CreatePopupMenu() -> UIntPtr
     """
    import System
    return System.UIntPtr()

  def DeleteMenu(self, hMenu, uPosition, uFlags):
    """ DeleteMenu(hMenu: UIntPtr, uPosition: int, uFlags: MenuFlags) -> bool
     """
    import System
    return System.Boolean()

  E_ABORT = -2147467260
  E_ACCESSDENIED = -2147024891
  E_FAIL = -2147467259
  E_HANDLE = -2147024890
  E_INVALIDARG = -2147024809
  E_NOINTERFACE = -2147467262
  E_NOTIMPL = -2147467263
  E_OUTOFMEMORY = -2147024882
  E_POINTER = -2147467261
  E_UNEXPECTED = -2147418113

  def Failed(self, hr):
    """ Failed(hr: int) -> bool
     """
    import System
    return System.Boolean()

  def GetClientRect(self, hWnd, lpRect):
    """ GetClientRect(hWnd: IntPtr) -> (bool, RECT)
     """
    import System
    return System.Boolean()

  def GetMenuItemCount(self, hMenu):
    """ GetMenuItemCount(hMenu: UIntPtr) -> int
     """
    import System
    return System.int()

  def GetWindowRect(self, hWnd, lpRect):
    """ GetWindowRect(hWnd: IntPtr) -> (bool, RECT)
     """
    import System
    return System.Boolean()

  IDABORT = 3
  IDCANCEL = 2
  IDIGNORE = 5
  IDNO = 7
  IDOK = 1
  IDRETRY = 4
  IDYES = 6

  def IsWin2K(self):
    """ IsWin2K() -> bool
     """
    import System
    return System.Boolean()

  def IsWinNT(self):
    """ IsWinNT() -> bool
     """
    import System
    return System.Boolean()

  MAX_PATH = 260

  class MenuFlags(Enum):
    """ 
    
    enum (flags) MenuFlags, values: MF_BYCOMMAND (0), MF_BYPOSITION (1024), MF_CHECKED (8), MF_DISABLED (2), MF_ENABLED (0), MF_GRAYED (1), MF_POPUP (16), MF_REMOVE (4096), MF_SEPARATOR (2048), MF_STRING (0), MF_UNCHECKED (0)
    
     """

    def Format(self, arg0, arg1, arg2):
      """ Format(enumType: Type, value: object, format: str) -> str
       """
      return ""

    def GetName(self, arg0, arg1):
      """ GetName(enumType: Type, value: object) -> str
       """
      return ""

    def GetNames(self, arg0):
      """ GetNames(enumType: Type) -> Array[str]
       """
      return ""

    def GetUnderlyingType(self, arg0):
      """ GetUnderlyingType(enumType: Type) -> Type
       """
      return None

    def GetValues(self, arg0):
      """ GetValues(enumType: Type) -> Array
       """
      return None

    def IsDefined(self, arg0, arg1):
      """ IsDefined(enumType: Type, value: object) -> bool
       """
      return None

    MF_BYCOMMAND = None
    MF_BYPOSITION = None
    MF_CHECKED = None
    MF_DISABLED = None
    MF_ENABLED = None
    MF_GRAYED = None
    MF_POPUP = None
    MF_REMOVE = None
    MF_SEPARATOR = None
    MF_STRING = None
    MF_UNCHECKED = None

    def Parse(self, arg0, arg1):
      """ Parse(enumType: Type, value: str) -> object
      Parse(enumType: Type, value: str, ignoreCase: bool) -> object
       """
      return None

    def ReferenceEquals(objA: object, objB: object) -> bool:
      """ ReferenceEquals(objA: object, objB: object) -> bool
       """
      return None

    def ToObject(self, arg0, arg1):
      """ ToObject(enumType: Type, value: object) -> object
      ToObject(enumType: Type, value: SByte) -> object
      ToObject(enumType: Type, value: Int16) -> object
      ToObject(enumType: Type, value: int) -> object
      ToObject(enumType: Type, value: Byte) -> object
      ToObject(enumType: Type, value: UInt16) -> object
      ToObject(enumType: Type, value: int) -> object
      ToObject(enumType: Type, value: int) -> object
      ToObject(enumType: Type, value: int) -> object
       """
      return None

    def TryParse(self, arg0):
      """ TryParse[TEnum](value: str) -> (bool, TEnum)
      TryParse[TEnum](value: str, ignoreCase: bool) -> (bool, TEnum)
       """
      return (None, None)

    value__ = None

  NIF_ICON = 2
  NIF_INFO = 16
  NIF_MESSAGE = 1
  NIF_STATE = 8
  NIF_TIP = 4
  NIIF_ERROR = 3
  NIIF_INFO = 1
  NIIF_NONE = 0
  NIIF_WARNING = 2
  NIM_ADD = 0
  NIM_DELETE = 2
  NIM_MODIFY = 1
  NIM_SETFOCUS = 3
  NIM_SETVERSION = 4
  NIS_HIDDEN = 1
  NIS_SHAREDICON = 2

  class NOTIFYICONDATA(object):
    """  """

    def ReferenceEquals(objA: object, objB: object) -> bool:
      """ ReferenceEquals(objA: object, objB: object) -> bool
       """
      return None

    cbSize = None
    dwInfoFlags = None
    dwState = None
    dwStateMask = None
    hIcon = None
    hwnd = None
    szInfo = None
    szInfoTitle = None
    szTip = None
    uCallbackMessage = None
    uFlags = None
    uID = None
    uTimeoutAndVersion = None

  NOTIFYICON_OLDVERSION = 0
  NOTIFYICON_VERSION = 3

  def NormalizeDirString(self, dir):
    """ NormalizeDirString(dir: str) -> str
     """
    import System
    return System.String()

  def OpenIcon(self, hwnd):
    """ OpenIcon(hwnd: IntPtr) -> bool
     """
    import System
    return System.Boolean()

  class POINT(object):
    """  """

    def ReferenceEquals(objA: object, objB: object) -> bool:
      """ ReferenceEquals(objA: object, objB: object) -> bool
       """
      return None

    x = None
    y = None

  def PostMessage(self, hWnd, msg, wParam, lParam):
    """ PostMessage(hWnd: IntPtr, msg: int, wParam: IntPtr, lParam: IntPtr) -> bool
     """
    import System
    return System.Boolean()

  class RECT(object):
    """  """

    Bottom = None
    Left = None

    def ReferenceEquals(objA: object, objB: object) -> bool:
      """ ReferenceEquals(objA: object, objB: object) -> bool
       """
      return None

    Right = None
    Top = None

  def ReferenceEquals(objA: object, objB: object) -> bool:
    """ ReferenceEquals(objA: object, objB: object) -> bool
     """
    return None

  SF_E_CANCEL = -2147164148
  SF_E_SPIKE_FAILURE = -2147163860
  SF_E_SPIKE_NOLICENSE = -2147163859
  SLGP_RAWPATH = None
  SLR_NO_UI = None
  SS_ETCHEDHORZ = 16
  STGM_READ = 0
  S_FALSE = 1
  S_OK = 0

  def SendCopyDataMessage(self, hwnd, wMsg, wParam, lParam):
    """ SendCopyDataMessage(hwnd: IntPtr, wMsg: int, wParam: IntPtr, lParam: COPYDATASTRUCT) -> (IntPtr, COPYDATASTRUCT)
     """
    import System
    return System.IntPtr()

  def SendCopyDataTextMessage(self, hwnd, wParam, msgWhat, msgText):
    """ SendCopyDataTextMessage(hwnd: IntPtr, wParam: IntPtr, msgWhat: int, msgText: str) -> IntPtr
     """
    import System
    return System.IntPtr()

  def SendMessage(self, hWnd, msg, wParam, lParam):
    """ SendMessage(hWnd: IntPtr, msg: int, wParam: IntPtr, lParam: IntPtr) -> IntPtr
     """
    import System
    return System.IntPtr()

  def SetForegroundWindow(self, hWnd):
    """ SetForegroundWindow(hWnd: IntPtr) -> bool
     """
    import System
    return System.Boolean()

  def SetWindowPos(self, hWnd, hWndInsertAfter, X, Y, cx, cy, uFlags):
    """ SetWindowPos(hWnd: IntPtr, hWndInsertAfter: IntPtr, X: int, Y: int, cx: int, cy: int, uFlags: int) -> bool
     """
    import System
    return System.Boolean()

  def Shell_NotifyIcon(self, dwMessage, lpData):
    """ Shell_NotifyIcon(dwMessage: int, lpData: NOTIFYICONDATA) -> (bool, NOTIFYICONDATA)
     """
    import System
    return System.Boolean()

  TB_SETDISABLEDIMAGELIST = 1078
  TB_SETHOTIMAGELIST = 1076
  TB_SETIMAGELIST = 1072
  TPM_BOTTOMALIGN = 32
  TPM_CENTERALIGN = 4
  TPM_HORIZONTAL = 0
  TPM_HORNEGANIMATION = 2048
  TPM_HORPOSANIMATION = 1024
  TPM_LAYOUTRTL = 32768
  TPM_LEFTALIGN = 0
  TPM_LEFTBUTTON = 0
  TPM_NOANIMATION = 16384
  TPM_NONOTIFY = 128
  TPM_RECURSE = 1
  TPM_RETURNCMD = 256
  TPM_RIGHTALIGN = 8
  TPM_RIGHTBUTTON = 2
  TPM_TOPALIGN = 0
  TPM_VCENTERALIGN = 16
  TPM_VERNEGANIMATION = 8192
  TPM_VERPOSANIMATION = 4096
  TPM_VERTICAL = 64

  def TrackPopupMenu(self, hMenu, wFlags, x, y, nReserved, hwnd, prcRect):
    """ TrackPopupMenu(hMenu: IntPtr, wFlags: int, x: int, y: int, nReserved: int, hwnd: IntPtr, prcRect: IntPtr) -> int
     """
    import System
    return System.int()

  WM_CLOSE = 16
  WM_COMMAND = 273
  WM_COPYDATA = 74
  WM_LBUTTONDBLCLK = 515
  WM_LBUTTONDOWN = 513
  WM_LBUTTONUP = 514
  WM_MOUSEMOVE = 512
  WM_NULL = 0
  WM_RBUTTONDBLCLK = 518
  WM_RBUTTONDOWN = 516
  WM_RBUTTONUP = 517
  WM_USER = 1024
  WM_USER_SAFE_BASE = 1536
  WS_CAPTION = 12582912
  WS_CHILD = 1073741824
  WS_EX_APPWINDOW = 262144
  WS_EX_CONTROLPARENT = 65536
  WS_EX_DLGMODALFRAME = 1
  WS_EX_TOOLWINDOW = 128
  WS_EX_WINDOWEDGE = 256
  WS_VISIBLE = 268435456

class Marker(object):
  """ Represents a marker on the project's time line.
  Marker()
  Marker(position: Timecode)
  Marker(position: Timecode, label: str)
   """

  def Equals(self, obj):
    """ Equals(self: Marker, obj: object) -> bool
     """
    import System
    return System.Boolean()

  def GetHashCode(self):
    """ GetHashCode(self: Marker) -> int
     """
    import System
    return System.int()

  def GetLabel(self, arg0):
    """ GetLabel(self: Marker) -> str
     """
    return ""

  Index: int

  def IsValid(self: Marker) -> bool:
    """ IsValid(self: Marker) -> bool
     """
    import System
    return System.Boolean()

  Label: str
  

  def MembersEqual(self, arg0, arg1):
    """ MembersEqual(self: Marker, o: Marker) -> bool
     """
    return None

  Position: Timecode
 
  def ReferenceEquals(objA: object, objB: object) -> bool:
    """ ReferenceEquals(objA: object, objB: object) -> bool
     """
    return None

  def SetLabel(self: Marker, value: str):
    """ SetLabel(self: Marker, value: str) """
    pass

  def SetPosition(self: Marker, value: Timecode):
    """ SetPosition(self: Marker, value: Timecode) """
    pass

  
class MarkerCommandType(object):
  """ Command marker types
  MarkerCommandType(cmd: str)
   """

  Author: MarkerCommandType
  CEA608CC1 : MarkerCommandType
  CEA608CC2 : MarkerCommandType
  CEA608CC3 : MarkerCommandType
  CEA608CC4 : MarkerCommandType
  Copyright : MarkerCommandType
  HotSpotBrowse : MarkerCommandType
  HotSpotPlay : MarkerCommandType
  HotSpotSeek : MarkerCommandType
  ScottCueIn : MarkerCommandType
  ScottEOM : MarkerCommandType
  Text : MarkerCommandType
  Title : MarkerCommandType
  URL : MarkerCommandType
  WMClosedCaption : MarkerCommandType
  WMTextHeadline : MarkerCommandType
  WMWMTextBodytext : MarkerCommandType

class MarkerList(BaseMarkerList[Marker]):
  """ List of Marker objects.
  MarkerList()
   """

  def ReferenceEquals(objA: object, objB: object) -> bool:
    """ ReferenceEquals(objA: object, objB: object) -> bool
     """
    return None

  
class MarkerType(Enum):
  """ 
  
  enum MarkerType, values: CDMarker (3), CDRegion (4), CommandMarker (5), Marker (1), MediaCommandMarker (8), MediaMarker (6), MediaRegion (7), Region (2), Unknown (0)
  
   """

  CDMarker = None
  CDRegion = None
  CommandMarker = None
  Marker = None
  MediaCommandMarker = None
  MediaMarker = None
  MediaRegion = None
  Region = None
  Unknown = None

class Media_(object):
  """ Represents a media file referenced by a Vegas project.
  Media(path: str)
  Media(generator: PlugInNode)
  Media(generator: PlugInNode, presetName: str)
   """

  AverageDataRate: int
  
  def CanRecapture(self: Media) -> bool:
    """ CanRecapture(self: Media) -> bool
     """
    import System
    return System.Boolean()

  CommandMarkers: MediaCommandMarkerList
  
  Comment: str 
  
  def CreateInstance(project: Project, path: str) -> Media_:
    """ CreateInstance(project: Project, path: str) -> Media
    CreateInstance(project: Project, generator: PlugInNode, presetName: str) -> Media
    CreateInstance(project: Project, generator: PlugInNode) -> Media
     """
    import ScriptPortal.Vegas
    return ScriptPortal.Vegas.Media()

  def CreateOfflineStream(self: Media_, type: MediaType) -> MediaStream:
    """ CreateOfflineStream(self: Media, type: MediaType) -> MediaStream
     """
    import ScriptPortal.Vegas
    return ScriptPortal.Vegas.MediaStream()

  CustomData: CustomDataContainer
  
  Effects: Effects_
    

  def Equals(self: Media, that: object) -> bool:
    """ Equals(self: Media, that: object) -> bool
     """
    import System
    return System.Boolean()

  FilePath: str
  
  Generator:  Effect_
   

  def GetAudioStreamByIndex(self, index):
    """ GetAudioStreamByIndex(self: Media, index: int) -> AudioStream
     """
    import ScriptPortal.Vegas
    return ScriptPortal.Vegas.AudioStream()

  def GetHashCode(self):
    """ GetHashCode(self: Media) -> int
     """
    import System
    return System.int()

  def GetUMID(self):
    """ GetUMID(self: Media) -> UMID
     """
    import ScriptPortal.MediaSoftware.Tools
    return ScriptPortal.MediaSoftware.Tools.UMID()

  def GetVideoStreamByIndex(self: Media_, index: int) -> VideoStream:
    """ GetVideoStreamByIndex(self: Media, index: int) -> VideoStream
     """
    import ScriptPortal.Vegas
    return ScriptPortal.Vegas.VideoStream()

  def HasAudio(self):
    """ HasAudio(self: Media) -> bool
     """
    import System
    return System.Boolean()

  def HasVideo(self):
    """ HasVideo(self: Media) -> bool
     """
    import System
    return System.Boolean()

  def IsGenerated(self):
    """ IsGenerated(self: Media) -> bool
     """
    import System
    return System.Boolean()

  def IsImageSequence(self):
    """ IsImageSequence(self: Media) -> bool
     """
    import System
    return System.Boolean()

  def IsOffline(self):
    """ IsOffline(self: Media) -> bool
     """
    import System
    return System.Boolean()

  def IsSubclip(self):
    """ IsSubclip(self: Media) -> bool
     """
    import System
    return System.Boolean()

  def IsValid(self):
    """ IsValid(self: Media) -> bool
     """
    import System
    return System.Boolean()

  KeyString: str
  
  Length: Timecode
  
  MEDIA_FLAG_CUSTOM_OFFSET = None
  Markers: MediaMarkerList
  
  MediaFiles:  MediaFiles_
  
  MediaID: int

  def MembersEqual(self, arg0, arg1):
    """ MembersEqual(self: Media, that: Media) -> bool
     """
    return None

  NodeID: int
  
  NodeType: MediaBinNodeType
  

  Project: Project_
  
  Rating: str
  
  RecordedDateTime: DateTime
  
  def ReferenceEquals(objA: object, objB: object) -> bool:
    """ ReferenceEquals(objA: object, objB: object) -> bool
     """
    return None

  Regions: MediaRegionList
  
  def ReplaceWith(self: Media, other: Media):
    """ ReplaceWith(self: Media, other: Media) """
    import System
    return System.Void()

  RulerFormat: RulerFormat_
  
  SourceUMIDCustomDataID = None

  def StreamCount(self: Media, type: MediaType) -> int:
    """ StreamCount(self: Media, type: MediaType) -> int
     """
    import System
    return System.int()

  Streams: MediaStreams
    
  TapeName: str
  
  TimecodeIn:  Timecode
  
  TimecodeOut: Timecode
   
  Title: str
  
  UseCount:  int
  
  UseCustomTimecode:  bool
  
  VideoCaptureComment:  str
  
  
class MediaBin(BaseList[IMediaBinNode]):
  """ MediaBin(project: Project, name: str)
  MediaBin(name: str)
   """

  def BaseAdd(self, arg0, arg1):
    """ BaseAdd(self: MediaBin, item: IMediaBinNode) -> int
     """
    return 1

  def BaseIndex(self, arg0, arg1):
    """ BaseIndex(self: MediaBin, item: IMediaBinNode) -> int
     """
    return 1

  def BaseRemove(self, arg0, arg1):
    """ BaseRemove(self: MediaBin, item: IMediaBinNode) -> bool
     """
    return None

  def GetCount(self, arg0):
    """ GetCount(self: MediaBin) -> int
     """
    return 1

  def GetItem(self, arg0, arg1):
    """ GetItem(self: MediaBin, index: int) -> IMediaBinNode
     """
    return None

  def IsRoot(self):
    """ IsRoot(self: MediaBin) -> bool
     """
    import System
    return System.Boolean()

  def IsValid(self):
    """ IsValid(self: MediaBin) -> bool
     """
    import System
    return System.Boolean()

  Name: str
  
  NodeID: int
  
  NodeType:  MediaBinNodeType
  
  Parent:  MediaBin
  
  def ReferenceEquals(objA: object, objB: object) -> bool:
    """ ReferenceEquals(objA: object, objB: object) -> bool
     """
    return None

class MediaBinNodeType(Enum):
  """ 
  Enumeration of media bin object types.
  enum MediaBinNodeType, values: Bin (1), MediaRef (2), Unknown (0)
  
   """

  Bin = None
  MediaRef = None
  Unknown = None
  

class MediaCommandMarker(CommandMarker):
  """ Represents a media command marker.
  MediaCommandMarker()
   """

  def Equals(self, obj):
    """ Equals(self: MediaCommandMarker, obj: object) -> bool
     """
    import System
    return System.Boolean()

  def GetHashCode(self):
    """ GetHashCode(self: MediaCommandMarker) -> int
     """
    import System
    return System.int()

  def Initialize(self, project, com, id, mediaID):
    """ Initialize(self: MediaCommandMarker, project: Project, com: IMarkerCOM, id: int, mediaID: int)Initialize(self: MediaCommandMarker, com: IMarkerCOM, id: int, mediaID: int) """
    import System
    return System.Void()

  def IsOwner(self, mediaID):
    """ IsOwner(self: MediaCommandMarker, mediaID: int) -> bool
     """
    import System
    return System.Boolean()

  def ReferenceEquals(objA: object, objB: object) -> bool:
    """ ReferenceEquals(objA: object, objB: object) -> bool
     """
    return None

  def SetLabel(self, arg0, arg1):
    """ SetLabel(self: MediaCommandMarker, label: str) """
    pass

  def SetPosition(self, arg0, arg1):
    """ SetPosition(self: MediaCommandMarker, value: Timecode) """
    pass

 

class MediaCommandMarkerList(BaseMediaMarkerList[MediaCommandMarker]):
  """ List of MediaCommandMarker objects.
  MediaCommandMarkerList()
   """

  def ReferenceEquals(objA: object, objB: object) -> bool:
    """ ReferenceEquals(objA: object, objB: object) -> bool
     """
    return None

 
class MediaFile(object):
  """ A file asset associated with a project Media object. 
  Many Media assets have just one file (e.g. Movie.mp4) but in some cases there 
  can be many associated files. For example, Panasonic P2 has separate essence 
  files for video and each audio channel. Most formats support proxy files, 
  and all audio formats have cached peaks files. Some media files 
  store metadata in external sidecar files rather than inside the media file. 
  MediaFile()
   """

  FilePath: str

  def FixMetadataFile(metadataFilename: str, mediaFilename: str):
    """ FixMetadataFile(metadataFilename: str, mediaFilename: str) """
    import System
    return System.Void()

  def FormatPath(self: MediaFile, mediaPath: str) -> str:
    """ FormatPath(self: MediaFile, mediaPath: str) -> str
     """
    import System
    return System.String()

  IsEssence:  bool
   
  IsMetadata: bool
  
  IsProxy: bool
  
  PathPattern: str
  
  def ReferenceEquals(objA: object, objB: object) -> bool:
    """ ReferenceEquals(objA: object, objB: object) -> bool
     """
    return None

  Type: MediaFileType
  
class MediaFileType(Enum):
  """ 
  
  enum MediaFileType, values: AudioEssence (3), AudioProxy (5), MixedEssence (1), OtherMetadata (7), Unknown (0), VegasMetadata (6), VideoEssence (2), VideoProxy (4)
  
   """

  AudioEssence = None
  AudioProxy = None
  MixedEssence = None
  OtherMetadata = None
  Unknown = None
  VegasMetadata = None
  VideoEssence = None
  VideoProxy = None
  

class MediaFiles(BaseList[MediaFile]):
  """ A immutable collection of the MediaFile assets for a given Media instance. 
  Although this collection is immutable from the scripting API, 
  it is possible that the media may change without warning from the engine side
  -- for example, if a video proxy is created for the asset that will add a 
  new entry to this collection automatically. 
  This list will not reflect that change until Media.
  MediaFiles is invoked again.  """

  def BaseIndex(self, arg0, arg1):
    """ BaseIndex(self: MediaFiles, item: MediaFile) -> int
     """
    return 1

  def GetCount(self: MediaFiles) -> int:
    """ GetCount(self: MediaFiles) -> int
     """
    return 1

  def GetItem(self: MediaFiles, index: int) -> MediaFile:
    """ GetItem(self: MediaFiles, index: int) -> MediaFile
     """
    return None

  IsReadOnly:  bool

  def ReferenceEquals(objA: object, objB: object) -> bool:
    """ ReferenceEquals(objA: object, objB: object) -> bool
     """
    return None

class MediaMarker(Marker):
  """ Represents a media marker.
  MediaMarker()
   """

  def Equals(self, obj):
    """ Equals(self: MediaMarker, obj: object) -> bool
     """
    import System
    return System.Boolean()

  def GetHashCode(self):
    """ GetHashCode(self: MediaMarker) -> int
     """
    import System
    return System.int()

  def Initialize(self, project, com, id, mediaID):
    """ Initialize(self: MediaMarker, project: Project, com: IMarkerCOM, id: int, mediaID: int)Initialize(self: MediaMarker, com: IMarkerCOM, id: int, mediaID: int) """
    import System
    return System.Void()

  def IsOwner(self, mediaID):
    """ IsOwner(self: MediaMarker, mediaID: int) -> bool
     """
    import System
    return System.Boolean()

  def IsValid(self):
    """ IsValid(self: MediaMarker) -> bool
     """
    import System
    return System.Boolean()

  def ReferenceEquals(objA: object, objB: object) -> bool:
    """ ReferenceEquals(objA: object, objB: object) -> bool
     """
    return None

  def SetLabel(self, arg0, arg1):
    """ SetLabel(self: MediaMarker, label: str) """
    pass

  def SetPosition(self, arg0, arg1):
    """ SetPosition(self: MediaMarker, value: Timecode) """
    pass

  
class MediaMarkerList(BaseMediaMarkerList[MediaMarker]):
  """ List of MediaMarker objects.
  MediaMarkerList()
   """

  def ReferenceEquals(objA: object, objB: object) -> bool:
    """ ReferenceEquals(objA: object, objB: object) -> bool
     """
    return None

 

class MediaPool_(object):
  """ Collection of media used in a project. 
  This pool is represented as an immutable IDictionary, 
  but please note that the IDictionary implementation is incomplete 
  and has flaws that cannot be corrected without breaking backward compatibility. 
  Most significantly: 
  1) CopyTo, Keys and Values are not implemented, 
  2) GetEnumerator() iterates over Media items rather than DictionaryEntry 
  items like it's supposed to. 
  If you try to code "foreach (DictionaryEntry de in pool)" you will get an 
  InvalidCastException. Instead, you need to code as "foreach (Media m in pool)" 
  and the key will be "m.KeyString".  """

  def Add(self: MediaPool, key: object, value: object):
    """ Add(self: MediaPool, key: object, value: object) """
    import System
    return System.Void()

  def AddImageSequence(self: MediaPool, path: str, imageCount: int, fps: float) -> Media:
    """ AddImageSequence(self: MediaPool, path: str, imageCount: int, fps: float) -> Media
    AddImageSequence(self: MediaPool, path: str, imageCount: int, fps: float, addToSelectedBin: bool) -> Media
     """
    import ScriptPortal.Vegas
    return ScriptPortal.Vegas.Media()

  def AddMedia(self: MediaPool, path: str) -> Media:
    """ AddMedia(self: MediaPool, path: str) -> Media
    AddMedia(self: MediaPool, path: str, addToSelectedBin: bool) -> Media
     """
    import ScriptPortal.Vegas
    return ScriptPortal.Vegas.Media()
  
  def AddMedia(self: MediaPool, path: str, addToSelectedBin: bool) -> Media:
    """ AddMedia(self: MediaPool, path: str) -> Media
    AddMedia(self: MediaPool, path: str, addToSelectedBin: bool) -> Media
     """
    import ScriptPortal.Vegas
    return ScriptPortal.Vegas.Media()
  
  def CanCreateStereo3DSubclip(self: MediaPool, left: Media, right: Media) -> bool:
    """ CanCreateStereo3DSubclip(self: MediaPool, left: Media, right: Media) -> bool
     """
    import System
    return System.Boolean()

  def Clear(self):
    """ Clear(self: MediaPool) """
    import System
    return System.Void()

  def Contains(self, key):
    """ Contains(self: MediaPool, key: object) -> bool
     """
    import System
    return System.Boolean()

  def CopyTo(self, array, index):
    """ CopyTo(self: MediaPool, array: Array, index: int) """
    import System
    return System.Void()

  Count: int


  def CreateStereo3DSubclip(self: MediaPool, left: Media, right: Media) -> Subclip:
    """ CreateStereo3DSubclip(self: MediaPool, left: Media, right: Media) -> Subclip
     """
    import ScriptPortal.Vegas
    return ScriptPortal.Vegas.Subclip()

  def Find(self: MediaPool, path: str) -> Media:
    """ Find(self: MediaPool, path: str) -> Media
     """
    import ScriptPortal.Vegas
    return ScriptPortal.Vegas.Media()

  def GetEnumerator(self: MediaPool) -> IDictionaryEnumerator:
    """ GetEnumerator(self: MediaPool) -> IDictionaryEnumerator
     """
    import System.Collections
    return System.Collections.IDictionaryEnumerator()

  def GetSelectedMedia(self: MediaPool) -> Array[Media_]:
    """ GetSelectedMedia(self: MediaPool) -> Array[Media]
     """
    import ScriptPortal.Vegas
    return ScriptPortal.Vegas.Media[]()

  IsFixedSize: bool

  IsReadOnly: bool
  

  IsSynchronized: bool
  
  Item:ICollection
  
  def OpenAllMedia(self: MediaPool):
    """ OpenAllMedia(self: MediaPool) """
    import System
    return System.Void()

  def ReferenceEquals(objA: object, objB: object) -> bool:
    """ ReferenceEquals(objA: object, objB: object) -> bool
     """
    return None

  def Remove(self: MediaPool, key: object):
    """ Remove(self: MediaPool, key: object) """
    import System
    return System.Void()

  def RemoveUnusedMedia(self: MediaPool):
    """ RemoveUnusedMedia(self: MediaPool) """
    import System
    return System.Void()

  RootMediaBin: MediaBin

  SyncRoot: object

  Values: ICollection


class MediaPoolEnumerator(object):
  """ Enumerator of media referenced by a project. """

  Current: object
                  
  Entry:  DictionaryEntry

  Key: object

  def MoveNext(self: MediaPoolEnumerator) -> bool:
    """ MoveNext(self: MediaPoolEnumerator) -> bool
     """
    import System
    return System.Boolean()

  def ReferenceEquals(objA: object, objB: object) -> bool:
    """ ReferenceEquals(objA: object, objB: object) -> bool
     """
    return None

  def Reset(self: MediaPoolEnumerator):
    """ Reset(self: MediaPoolEnumerator) """
    import System
    return System.Void()

  Value: object

  def next(self, arg0):
    """ next(self: object) -> object
     """
    return None

class MediaRegion(Region):
  """ Represents a media region.
  MediaRegion()
   """

  def Equals(self: MediaRegion, obj: object) -> bool:
    """ Equals(self: MediaRegion, obj: object) -> bool
     """
    import System
    return System.Boolean()

  def GetHashCode(self: MediaRegion) -> int:
    """ GetHashCode(self: MediaRegion) -> int
     """
    import System
    return System.int()

  def Initialize(self: MediaRegion, project: Project, com: IMarkerCOM, id: int, mediaID: int)Initialize(self: MediaRegion, com: IMarkerCOM, id: int, mediaID: int):
    """ Initialize(self: MediaRegion, project: Project, com: IMarkerCOM, id: int, mediaID: int)Initialize(self: MediaRegion, com: IMarkerCOM, id: int, mediaID: int) """
    import System
    return System.Void()

  def IsOwner(self: MediaRegion, mediaID: int) -> bool:
    """ IsOwner(self: MediaRegion, mediaID: int) -> bool
     """
    import System
    return System.Boolean()

  def ReferenceEquals(objA: object, objB: object) -> bool:
    """ ReferenceEquals(objA: object, objB: object) -> bool
     """
    return None

  def SetLabel(self: MediaRegion, label: str):
    """ SetLabel(self: MediaRegion, label: str) """
    pass

  def SetLength(self: MediaRegion, value: Timecode):
    """ SetLength(self: MediaRegion, value: Timecode) """
    pass

  def SetPosition(self: MediaRegion, value: Timecode) :
    """ SetPosition(self: MediaRegion, value: Timecode) """
    pass

  

class MediaRegionList(BaseMediaMarkerList[MediaRegion]):
  """ List of MediaRegion objects.
  MediaRegionList()
   """

  def ReferenceEquals(objA: object, objB: object) -> bool:
    """ ReferenceEquals(objA: object, objB: object) -> bool
     """
    return None

  

class MediaStream_(object):
  """ Represents a media stream. """

  def Equals(self: MediaStream_, that: object) -> bool:
    """ Equals(self: MediaStream, that: object) -> bool
     """
    import System
    return System.Boolean()

  FormatFourCCString: str

  def GetHashCode(self: MediaStream_) -> int:
    """ GetHashCode(self: MediaStream) -> int """
    import System
    return System.int()

  Index: int

  IsOffline: bool

  Length: Timecode

  MediaType: MediaType
 
  def MembersEqual(self: MediaStream, that: MediaStream_) -> bool:
    """ MembersEqual(self: MediaStream, that: MediaStream) -> bool
     """
    return None

  Offset: Timecode

  Parent: Media

  def ReferenceEquals(objA: object, objB: object) -> bool:
    """ ReferenceEquals(objA: object, objB: object) -> bool
     """
    return None

  StreamInfoText: str

 

class MediaStreams(BaseList[MediaStream_]):
  """ Collection of media streams. """

  def BaseIndex(self: MediaStreams, stream: MediaStream_) -> int:
    """ BaseIndex(self: MediaStreams, stream: MediaStream) -> int
     """
    return 1

  def GetCount(self: MediaStreams) -> int:
    """ GetCount(self: MediaStreams) -> int
     """
    return 1

  def GetItem(self: MediaStreams, index: int) -> MediaStream_:
    """ GetItem(self: MediaStreams, index: int) -> MediaStream
     """
    return None

  def GetItemByMediaType(self: MediaStreams, type: MediaType, index: int) -> MediaStream_:
    """ GetItemByMediaType(self: MediaStreams, type: MediaType, index: int) -> MediaStream
     """
    import ScriptPortal.Vegas
    return ScriptPortal.Vegas.MediaStream()

  IsFixedSize: bool

  IsReadOnly: bool
 
  def ReferenceEquals(objA: object, objB: object) -> bool:
    """ ReferenceEquals(objA: object, objB: object) -> bool
     """
    return None

  myCOM = None
  myMedia = None
  myMediaID = None
  myProject = None

class MediaType(Enum):
  """ 
  
  enum MediaType, values: Audio (2), Max (6), Midi (4), Stream (1), Text (5), Unknown (0), Video (3)
  
   """

  Audio = None
  Max = None
  Midi = None
  Stream = None
  Text = None
  Unknown = None
  Video = None

class MetaPathType(Enum):
  """ 
  
  enum MetaPathType, values: Generator (1), Invalid (0), Sequence (2), Subclip (3)
  
   """

  Generator = None
  Invalid = None
  Sequence = None
  Subclip = None


class MissingMediaEventArgs(EventArgs):
  """ Arguments provided to MissingMedia event handlers. """

  Empty = None
  IgnoreMissingMedia: value

  MissingMedia:  str
 
  def ReferenceEquals(objA: object, objB: object) -> bool:
    """ ReferenceEquals(objA: object, objB: object) -> bool
     """
    return None

class MissingMediaEventHandler(MulticastDelegate):
  """ Represents the method that handles a MissingMedia event.
  MissingMediaEventHandler(object: object, method: IntPtr)
   """

  def BeginInvoke(self: MissingMediaEventHandler, sender: object, args: MissingMediaEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult:
    """ BeginInvoke(self: MissingMediaEventHandler, sender: object, args: MissingMediaEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult
     """
    import System
    return System.IAsyncResult()

  def Combine(*delegates: Array[Delegate]) -> Delegate:
    """ Combine(a: Delegate, b: Delegate) -> Delegate
    Combine(*delegates: Array[Delegate]) -> Delegate
     """
    return None

  def CreateDelegate(type: Type, target: object, method: str) -> Delegate:
    """ CreateDelegate(type: Type, target: object, method: str) -> Delegate
    CreateDelegate(type: Type, target: object, method: str, ignoreCase: bool) -> Delegate
    CreateDelegate(type: Type, target: object, method: str, ignoreCase: bool, throwOnBindFailure: bool) -> Delegate
    CreateDelegate(type: Type, target: Type, method: str) -> Delegate
    CreateDelegate(type: Type, target: Type, method: str, ignoreCase: bool) -> Delegate
    CreateDelegate(type: Type, target: Type, method: str, ignoreCase: bool, throwOnBindFailure: bool) -> Delegate
    CreateDelegate(type: Type, method: MethodInfo, throwOnBindFailure: bool) -> Delegate
    CreateDelegate(type: Type, firstArgument: object, method: MethodInfo) -> Delegate
    CreateDelegate(type: Type, firstArgument: object, method: MethodInfo, throwOnBindFailure: bool) -> Delegate
    CreateDelegate(type: Type, method: MethodInfo) -> Delegate
     """
    return None

  def EndInvoke(self: MissingMediaEventHandler, result: IAsyncResult):
    """ EndInvoke(self: MissingMediaEventHandler, result: IAsyncResult) """
    import System
    return System.Void()

  def Invoke(self: MissingMediaEventHandler, sender: object, args: MissingMediaEventArgs):
    """ Invoke(self: MissingMediaEventHandler, sender: object, args: MissingMediaEventArgs) """
    import System
    return System.Void()

  def ReferenceEquals(objA: object, objB: object) -> bool:
    """ ReferenceEquals(objA: object, objB: object) -> bool
     """
    return None

  def RRemove(source: Delegate, value: Delegate) -> Delegate:
    """ Remove(source: Delegate, value: Delegate) -> Delegate
     """
    return None

  def RemoveAll(source: Delegate, value: Delegate) -> Delegate:
    """ RemoveAll(source: Delegate, value: Delegate) -> Delegate
     """
    return None

class MotionBlurType(Enum):
  """ Enumeration of motion blur types.
  
  enum MotionBlurType, values: AsymmetricBox (5), AsymmetricGaussian (3), AsymmetricPyramid (4), Box (2), Gaussian (0), Pyramid (1), Unknown (-1)
  
   """

  AsymmetricBox = None
  AsymmetricGaussian = None
  AsymmetricPyramid = None
  Box = None
  Gaussian = None
  Unknown = None

class NestedProject(Media):
  """  """

  def CreateInstance(self, arg0, arg1):
    """ CreateInstance(project: Project, path: str) -> Media
    CreateInstance(project: Project, generator: PlugInNode, presetName: str) -> Media
    CreateInstance(project: Project, generator: PlugInNode) -> Media
     """
    return None

  MEDIA_FLAG_CUSTOM_OFFSET = None

  def ReadProject(self):
    """ ReadProject(self: NestedProject) -> Project
    ReadProject(self: NestedProject, callback: IProgressCallback) -> Project
     """
    import ScriptPortal.Vegas
    return ScriptPortal.Vegas.Project()

  def ReferenceEquals(objA: object, objB: object) -> bool:
    """ ReferenceEquals(objA: object, objB: object) -> bool
     """
    return None

  SourceUMIDCustomDataID = None
  myCOM = None
  myCustomDataContainer = None
  myEffectCOM = None
  myEffects = None
  myGenerator = None
  myMediaID = None
  myMetaPathType = None
  myProject = None

class NormalizeFlags(Enum):
  """ 
  
  enum (flags) NormalizeFlags, values: Gain (2), None (0), Norm (1)
  
   """

  def Format(self, arg0, arg1, arg2):
    """ Format(enumType: Type, value: object, format: str) -> str
     """
    return ""

  Gain = None

  def GetName(self, arg0, arg1):
    """ GetName(enumType: Type, value: object) -> str
     """
    return ""

  def GetNames(self, arg0):
    """ GetNames(enumType: Type) -> Array[str]
     """
    return ""

  def GetUnderlyingType(self, arg0):
    """ GetUnderlyingType(enumType: Type) -> Type
     """
    return None

  def GetValues(self, arg0):
    """ GetValues(enumType: Type) -> Array
     """
    return None

  def IsDefined(self, arg0, arg1):
    """ IsDefined(enumType: Type, value: object) -> bool
     """
    return None

  None_ = None
  Norm = None

  def Parse(self, arg0, arg1):
    """ Parse(enumType: Type, value: str) -> object
    Parse(enumType: Type, value: str, ignoreCase: bool) -> object
     """
    return None

  def ReferenceEquals(objA: object, objB: object) -> bool:
    """ ReferenceEquals(objA: object, objB: object) -> bool
     """
    return None

  def ToObject(self, arg0, arg1):
    """ ToObject(enumType: Type, value: object) -> object
    ToObject(enumType: Type, value: SByte) -> object
    ToObject(enumType: Type, value: Int16) -> object
    ToObject(enumType: Type, value: int) -> object
    ToObject(enumType: Type, value: Byte) -> object
    ToObject(enumType: Type, value: UInt16) -> object
    ToObject(enumType: Type, value: int) -> object
    ToObject(enumType: Type, value: int) -> object
    ToObject(enumType: Type, value: int) -> object
     """
    return None

  def TryParse(self, arg0):
    """ TryParse[TEnum](value: str) -> (bool, TEnum)
    TryParse[TEnum](value: str, ignoreCase: bool) -> (bool, TEnum)
     """
    return (None, None)

  value__ = None

class OFXBase(object):
  """ Represents a base class for Open FX video plug-ins and effects. """

  EffectType: OFXEffectType
   
  def Equals(self, that):
    """ Equals(self: OFXBase, that: OFXBase) -> bool
     """
    import System
    return System.Boolean()

  Grouping: str
  
  Label: str
   
  PlugInPath: str
   

  def ReferenceEquals(objA: object, objB: object) -> bool:
    """ ReferenceEquals(objA: object, objB: object) -> bool
     """
    return None

  Version: Version_
   
 
class OFXBooleanKeyframe(OFXKeyframe[bool]):
  """  """

  def ReferenceEquals(objA: object, objB: object) -> bool:
    """ ReferenceEquals(objA: object, objB: object) -> bool
     """
    return None

  Value = property(None, None, None,
                   """ Get: Value(self: OFXBooleanKeyframe) -> bool
                   
                   Set: Value(self: OFXBooleanKeyframe) = value
                    """
                   )

  myCOM = None
  myOwner = None
  myParamID = None

class OFXBooleanParameter(OFXParameter[bool, OFXBooleanKeyframe]):
  """  """

  def GetProp(self, arg0, arg1):
    """ GetProp(self: OFXBooleanParameter, propName: str) -> bool
     """
    return None

  def GetValueAtTime(self, time):
    """ GetValueAtTime(self: OFXBooleanParameter, time: Timecode) -> bool
     """
    import System
    return System.Boolean()

  def ReferenceEquals(objA: object, objB: object) -> bool:
    """ ReferenceEquals(objA: object, objB: object) -> bool
     """
    return None

  def SetValueAtTime(self: OFXBooleanParameter, time: Timecode, value: bool):
    """ SetValueAtTime(self: OFXBooleanParameter, time: Timecode, value: bool) """
    import System
    return System.Void()

  Value:  bool
  

  myCOM = None
  myIndex = None
  myKeyframes = None
  myOwner = None

class OFXChoice(object):
  """  """

  Index = None
  Name = None

  def ReferenceEquals(objA: object, objB: object) -> bool:
    """ ReferenceEquals(objA: object, objB: object) -> bool
     """
    return None

  def ToString(self):
    """ ToString(self: OFXChoice) -> str
     """
    import System
    return System.String()

class OFXChoiceKeyframe(OFXKeyframe[OFXChoice]):
  """  """

  def ReferenceEquals(objA: object, objB: object) -> bool:
    """ ReferenceEquals(objA: object, objB: object) -> bool
     """
    return None

  Value: OFXChoice
  
  myCOM = None
  myOwner = None
  myParamID = None

class OFXChoiceParameter(OFXParameter[OFXChoice, OFXChoiceKeyframe]):
  """  """

  Choices: Array[OFXChoice]
  
  def GetProp(self, arg0, arg1):
    """ GetProp(self: OFXChoiceParameter, propName: str) -> OFXChoice
     """
    return None

  def GetValueAtTime(self, time):
    """ GetValueAtTime(self: OFXChoiceParameter, time: Timecode) -> OFXChoice
     """
    import ScriptPortal.Vegas
    return ScriptPortal.Vegas.OFXChoice()

  def ReferenceEquals(objA: object, objB: object) -> bool:
    """ ReferenceEquals(objA: object, objB: object) -> bool
     """
    return None

  def SetValueAtTime(self, time, value):
    """ SetValueAtTime(self: OFXChoiceParameter, time: Timecode, value: OFXChoice) """
    import System
    return System.Void()

  Value = property(None, None, None,
                   """ Get: Value(self: OFXChoiceParameter) -> OFXChoice
                   
                   Set: Value(self: OFXChoiceParameter) = value
                    """
                   )

  myCOM = None
  myIndex = None
  myKeyframes = None
  myOwner = None

class OFXColor(object):
  """ OFXColor(r: float, g: float, b: float)
  OFXColor(r: float, g: float, b: float, a: float)
   """

  A = None
  B = None

  def Equals(self, that):
    """ Equals(self: OFXColor, that: OFXColor) -> bool
    Equals(self: OFXColor, that: object) -> bool
     """
    import System
    return System.Boolean()

  G = None

  def GetHashCode(self):
    """ GetHashCode(self: OFXColor) -> int
     """
    import System
    return System.int()

  R = None

  def ReferenceEquals(objA: object, objB: object) -> bool:
    """ ReferenceEquals(objA: object, objB: object) -> bool
     """
    return None

class OFXControlPoint(object):
  """ OFXControlPoint(time: Timecode, val: float)
   """

  def ReferenceEquals(objA: object, objB: object) -> bool:
    """ ReferenceEquals(objA: object, objB: object) -> bool
     """
    return None

  Time = None
  Value = None

class OFXControlPointType(Enum):
  """ 
  
  enum OFXControlPointType, values: Next (2), Prev (1), Unknown (0)
  
   """

  def Format(self, arg0, arg1, arg2):
    """ Format(enumType: Type, value: object, format: str) -> str
     """
    return ""

  def GetName(self, arg0, arg1):
    """ GetName(enumType: Type, value: object) -> str
     """
    return ""

  def GetNames(self, arg0):
    """ GetNames(enumType: Type) -> Array[str]
     """
    return ""

  def GetUnderlyingType(self, arg0):
    """ GetUnderlyingType(enumType: Type) -> Type
     """
    return None

  def GetValues(self, arg0):
    """ GetValues(enumType: Type) -> Array
     """
    return None

  def IsDefined(self, arg0, arg1):
    """ IsDefined(enumType: Type, value: object) -> bool
     """
    return None

  Next = None

  def Parse(self, arg0, arg1):
    """ Parse(enumType: Type, value: str) -> object
    Parse(enumType: Type, value: str, ignoreCase: bool) -> object
     """
    return None

  Prev = None

  def ReferenceEquals(objA: object, objB: object) -> bool:
    """ ReferenceEquals(objA: object, objB: object) -> bool
     """
    return None

  def ToObject(self, arg0, arg1):
    """ ToObject(enumType: Type, value: object) -> object
    ToObject(enumType: Type, value: SByte) -> object
    ToObject(enumType: Type, value: Int16) -> object
    ToObject(enumType: Type, value: int) -> object
    ToObject(enumType: Type, value: Byte) -> object
    ToObject(enumType: Type, value: UInt16) -> object
    ToObject(enumType: Type, value: int) -> object
    ToObject(enumType: Type, value: int) -> object
    ToObject(enumType: Type, value: int) -> object
     """
    return None

  def TryParse(self, arg0):
    """ TryParse[TEnum](value: str) -> (bool, TEnum)
    TryParse[TEnum](value: str, ignoreCase: bool) -> (bool, TEnum)
     """
    return (None, None)

  Unknown = None
  value__ = None

class OFXCustomKeyframe(OFXKeyframe[str]):
  """  """

  def ReferenceEquals(objA: object, objB: object) -> bool:
    """ ReferenceEquals(objA: object, objB: object) -> bool
     """
    return None

  Value = property(None, None, None,
                   """ Get: Value(self: OFXCustomKeyframe) -> str
                   
                   Set: Value(self: OFXCustomKeyframe) = value
                    """
                   )

  myCOM = None
  myOwner = None
  myParamID = None

class OFXCustomParameter(OFXParameter[str, OFXCustomKeyframe]):
  """  """

  def GetProp(self, arg0, arg1):
    """ GetProp(self: OFXCustomParameter, propName: str) -> str
     """
    return ""

  def GetValueAtTime(self, time):
    """ GetValueAtTime(self: OFXCustomParameter, time: Timecode) -> str
     """
    import System
    return System.String()

  def ReferenceEquals(objA: object, objB: object) -> bool:
    """ ReferenceEquals(objA: object, objB: object) -> bool
     """
    return None

  def SetValueAtTime(self, time, value):
    """ SetValueAtTime(self: OFXCustomParameter, time: Timecode, value: str) """
    import System
    return System.Void()

  Value = property(None, None, None,
                   """ Get: Value(self: OFXCustomParameter) -> str
                   
                   Set: Value(self: OFXCustomParameter) = value
                    """
                   )

  myCOM = None
  myIndex = None
  myKeyframes = None
  myOwner = None

class OFXDouble2D(object):
  """  """

  def ReferenceEquals(objA: object, objB: object) -> bool:
    """ ReferenceEquals(objA: object, objB: object) -> bool
     """
    return None

  X = None
  Y = None

class OFXDouble2DKeyframe(OFXKeyframe[OFXDouble2D]):
  """  """

  NextControlPointX = property(None, None, None,
                               """ Get: NextControlPointX(self: OFXDouble2DKeyframe) -> OFXControlPoint
                               
                               Set: NextControlPointX(self: OFXDouble2DKeyframe) = value
                                """
                               )

  NextControlPointY = property(None, None, None,
                               """ Get: NextControlPointY(self: OFXDouble2DKeyframe) -> OFXControlPoint
                               
                               Set: NextControlPointY(self: OFXDouble2DKeyframe) = value
                                """
                               )

  PrevControlPointX = property(None, None, None,
                               """ Get: PrevControlPointX(self: OFXDouble2DKeyframe) -> OFXControlPoint
                               
                               Set: PrevControlPointX(self: OFXDouble2DKeyframe) = value
                                """
                               )

  PrevControlPointY = property(None, None, None,
                               """ Get: PrevControlPointY(self: OFXDouble2DKeyframe) -> OFXControlPoint
                               
                               Set: PrevControlPointY(self: OFXDouble2DKeyframe) = value
                                """
                               )


  def ReferenceEquals(objA: object, objB: object) -> bool:
    """ ReferenceEquals(objA: object, objB: object) -> bool
     """
    return None

  Value = property(None, None, None,
                   """ Get: Value(self: OFXDouble2DKeyframe) -> OFXDouble2D
                   
                   Set: Value(self: OFXDouble2DKeyframe) = value
                    """
                   )

  myCOM = None
  myOwner = None
  myParamID = None

class OFXDouble2DParameter(OFXRangeParameter[OFXDouble2D, OFXDouble2DKeyframe]):
  """  """

  def GetProp(self, arg0, arg1):
    """ GetProp(self: OFXDouble2DParameter, propName: str) -> OFXDouble2D
     """
    return None

  def GetValueAtTime(self, time):
    """ GetValueAtTime(self: OFXDouble2DParameter, time: Timecode) -> OFXDouble2D
     """
    import ScriptPortal.Vegas
    return ScriptPortal.Vegas.OFXDouble2D()

  def ReferenceEquals(objA: object, objB: object) -> bool:
    """ ReferenceEquals(objA: object, objB: object) -> bool
     """
    return None

  def SetValueAtTime(self, time, value):
    """ SetValueAtTime(self: OFXDouble2DParameter, time: Timecode, value: OFXDouble2D) """
    import System
    return System.Void()

  Value = property(None, None, None,
                   """ Get: Value(self: OFXDouble2DParameter) -> OFXDouble2D
                   
                   Set: Value(self: OFXDouble2DParameter) = value
                    """
                   )

  myCOM = None
  myIndex = None
  myKeyframes = None
  myOwner = None

class OFXDouble3D(object):
  """  """

  def ReferenceEquals(objA: object, objB: object) -> bool:
    """ ReferenceEquals(objA: object, objB: object) -> bool
     """
    return None

  X = None
  Y = None
  Z = None

class OFXDouble3DKeyframe(OFXKeyframe[OFXDouble3D]):
  """  """

  NextControlPointX = property(None, None, None,
                               """ Get: NextControlPointX(self: OFXDouble3DKeyframe) -> OFXControlPoint
                               
                               Set: NextControlPointX(self: OFXDouble3DKeyframe) = value
                                """
                               )

  NextControlPointY = property(None, None, None,
                               """ Get: NextControlPointY(self: OFXDouble3DKeyframe) -> OFXControlPoint
                               
                               Set: NextControlPointY(self: OFXDouble3DKeyframe) = value
                                """
                               )

  NextControlPointZ = property(None, None, None,
                               """ Get: NextControlPointZ(self: OFXDouble3DKeyframe) -> OFXControlPoint
                               
                               Set: NextControlPointZ(self: OFXDouble3DKeyframe) = value
                                """
                               )

  PrevControlPointX = property(None, None, None,
                               """ Get: PrevControlPointX(self: OFXDouble3DKeyframe) -> OFXControlPoint
                               
                               Set: PrevControlPointX(self: OFXDouble3DKeyframe) = value
                                """
                               )

  PrevControlPointY = property(None, None, None,
                               """ Get: PrevControlPointY(self: OFXDouble3DKeyframe) -> OFXControlPoint
                               
                               Set: PrevControlPointY(self: OFXDouble3DKeyframe) = value
                                """
                               )

  PrevControlPointZ = property(None, None, None,
                               """ Get: PrevControlPointZ(self: OFXDouble3DKeyframe) -> OFXControlPoint
                               
                               Set: PrevControlPointZ(self: OFXDouble3DKeyframe) = value
                                """
                               )


  def ReferenceEquals(objA: object, objB: object) -> bool:
    """ ReferenceEquals(objA: object, objB: object) -> bool
     """
    return None

  Value = property(None, None, None,
                   """ Get: Value(self: OFXDouble3DKeyframe) -> OFXDouble3D
                   
                   Set: Value(self: OFXDouble3DKeyframe) = value
                    """
                   )

  myCOM = None
  myOwner = None
  myParamID = None

class OFXDouble3DParameter(OFXRangeParameter[OFXDouble3D, OFXDouble3DKeyframe]):
  """  """

  def GetProp(self, arg0, arg1):
    """ GetProp(self: OFXDouble3DParameter, propName: str) -> OFXDouble3D
     """
    return None

  def GetValueAtTime(self, time):
    """ GetValueAtTime(self: OFXDouble3DParameter, time: Timecode) -> OFXDouble3D
     """
    import ScriptPortal.Vegas
    return ScriptPortal.Vegas.OFXDouble3D()

  def ReferenceEquals(objA: object, objB: object) -> bool:
    """ ReferenceEquals(objA: object, objB: object) -> bool
     """
    return None

  def SetValueAtTime(self, time, value):
    """ SetValueAtTime(self: OFXDouble3DParameter, time: Timecode, value: OFXDouble3D) """
    import System
    return System.Void()

  Value = property(None, None, None,
                   """ Get: Value(self: OFXDouble3DParameter) -> OFXDouble3D
                   
                   Set: Value(self: OFXDouble3DParameter) = value
                    """
                   )

  myCOM = None
  myIndex = None
  myKeyframes = None
  myOwner = None

class OFXDoubleKeyframe(OFXKeyframe[float]):
  """  """

  NextControlPoint = property(None, None, None,
                              """ Get: NextControlPoint(self: OFXDoubleKeyframe) -> OFXControlPoint
                              
                              Set: NextControlPoint(self: OFXDoubleKeyframe) = value
                               """
                              )

  PrevControlPoint = property(None, None, None,
                              """ Get: PrevControlPoint(self: OFXDoubleKeyframe) -> OFXControlPoint
                              
                              Set: PrevControlPoint(self: OFXDoubleKeyframe) = value
                               """
                              )


  def ReferenceEquals(objA: object, objB: object) -> bool:
    """ ReferenceEquals(objA: object, objB: object) -> bool
     """
    return None

  Value = property(None, None, None,
                   """ Get: Value(self: OFXDoubleKeyframe) -> float
                   
                   Set: Value(self: OFXDoubleKeyframe) = value
                    """
                   )

  myCOM = None
  myOwner = None
  myParamID = None

class OFXDoubleParameter(OFXRangeParameter[float, OFXDoubleKeyframe]):
  """  """

  def GetProp(self, arg0, arg1):
    """ GetProp(self: OFXDoubleParameter, propName: str) -> float
     """
    return 1.0

  def GetValueAtTime(self, time):
    """ GetValueAtTime(self: OFXDoubleParameter, time: Timecode) -> float
     """
    import System
    return System.Double()

  def ReferenceEquals(objA: object, objB: object) -> bool:
    """ ReferenceEquals(objA: object, objB: object) -> bool
     """
    return None

  def SetValueAtTime(self, time, value):
    """ SetValueAtTime(self: OFXDoubleParameter, time: Timecode, value: float) """
    import System
    return System.Void()

  Value = property(None, None, None,
                   """ Get: Value(self: OFXDoubleParameter) -> float
                   
                   Set: Value(self: OFXDoubleParameter) = value
                    """
                   )

  myCOM = None
  myIndex = None
  myKeyframes = None
  myOwner = None

class OFXEffect(OFXBase):
  """  """

  def AllParametersChanged(self):
    """ AllParametersChanged(self: OFXEffect) """
    import System
    return System.Void()

  CurrentTime = property(None, None, None,
                         """ Get: CurrentTime(self: OFXEffect) -> Timecode
                         
                         Set: CurrentTime(self: OFXEffect) = value
                          """
                         )


  def Equals(self, that):
    """ Equals(self: OFXEffect, that: OFXEffect) -> bool
    Equals(self: OFXEffect, that: object) -> bool
     """
    import System
    return System.Boolean()

  def FindParameterByName(self, name):
    """ FindParameterByName(self: OFXEffect, name: str) -> OFXParameter
     """
    import ScriptPortal.Vegas
    return ScriptPortal.Vegas.OFXParameter()

  def GetHashCode(self):
    """ GetHashCode(self: OFXEffect) -> int
     """
    import System
    return System.int()

  Item = None
  Parameters = property(None, None, None,
                        """ Get: Parameters(self: OFXEffect) -> OFXParameters
                        
                         """
                        )


  def ReferenceEquals(objA: object, objB: object) -> bool:
    """ ReferenceEquals(objA: object, objB: object) -> bool
     """
    return None

  myCOM = None
  myUniqueID = None

class OFXEffectType(Enum):
  """ 
  
  enum OFXEffectType, values: Compositor (1), Filter (3), General (2), Generator (4), Paint (7), Retimer (6), Transition (5), Unknown (0)
  
   """

  Compositor = None
  Filter = None

  def Format(self, arg0, arg1, arg2):
    """ Format(enumType: Type, value: object, format: str) -> str
     """
    return ""

  General = None
  Generator = None

  def GetName(self, arg0, arg1):
    """ GetName(enumType: Type, value: object) -> str
     """
    return ""

  def GetNames(self, arg0):
    """ GetNames(enumType: Type) -> Array[str]
     """
    return ""

  def GetUnderlyingType(self, arg0):
    """ GetUnderlyingType(enumType: Type) -> Type
     """
    return None

  def GetValues(self, arg0):
    """ GetValues(enumType: Type) -> Array
     """
    return None

  def IsDefined(self, arg0, arg1):
    """ IsDefined(enumType: Type, value: object) -> bool
     """
    return None

  Paint = None

  def Parse(self, arg0, arg1):
    """ Parse(enumType: Type, value: str) -> object
    Parse(enumType: Type, value: str, ignoreCase: bool) -> object
     """
    return None

  def ReferenceEquals(objA: object, objB: object) -> bool:
    """ ReferenceEquals(objA: object, objB: object) -> bool
     """
    return None

  Retimer = None

  def ToObject(self, arg0, arg1):
    """ ToObject(enumType: Type, value: object) -> object
    ToObject(enumType: Type, value: SByte) -> object
    ToObject(enumType: Type, value: Int16) -> object
    ToObject(enumType: Type, value: int) -> object
    ToObject(enumType: Type, value: Byte) -> object
    ToObject(enumType: Type, value: UInt16) -> object
    ToObject(enumType: Type, value: int) -> object
    ToObject(enumType: Type, value: int) -> object
    ToObject(enumType: Type, value: int) -> object
     """
    return None

  Transition = None

  def TryParse(self, arg0):
    """ TryParse[TEnum](value: str) -> (bool, TEnum)
    TryParse[TEnum](value: str, ignoreCase: bool) -> (bool, TEnum)
     """
    return (None, None)

  Unknown = None
  value__ = None

class OFXInteger2D(object):
  """  """

  def ReferenceEquals(objA: object, objB: object) -> bool:
    """ ReferenceEquals(objA: object, objB: object) -> bool
     """
    return None

  X = None
  Y = None

class OFXInteger2DKeyframe(OFXKeyframe[OFXInteger2D]):
  """  """

  def ReferenceEquals(objA: object, objB: object) -> bool:
    """ ReferenceEquals(objA: object, objB: object) -> bool
     """
    return None

  Value = property(None, None, None,
                   """ Get: Value(self: OFXInteger2DKeyframe) -> OFXInteger2D
                   
                   Set: Value(self: OFXInteger2DKeyframe) = value
                    """
                   )

  myCOM = None
  myOwner = None
  myParamID = None

class OFXInteger2DParameter(OFXRangeParameter[OFXInteger2D, OFXInteger2DKeyframe]):
  """  """

  def GetProp(self, arg0, arg1):
    """ GetProp(self: OFXInteger2DParameter, propName: str) -> OFXInteger2D
     """
    return None

  def GetValueAtTime(self, time):
    """ GetValueAtTime(self: OFXInteger2DParameter, time: Timecode) -> OFXInteger2D
     """
    import ScriptPortal.Vegas
    return ScriptPortal.Vegas.OFXInteger2D()

  def ReferenceEquals(objA: object, objB: object) -> bool:
    """ ReferenceEquals(objA: object, objB: object) -> bool
     """
    return None

  def SetValueAtTime(self, time, value):
    """ SetValueAtTime(self: OFXInteger2DParameter, time: Timecode, value: OFXInteger2D) """
    import System
    return System.Void()

  Value = property(None, None, None,
                   """ Get: Value(self: OFXInteger2DParameter) -> OFXInteger2D
                   
                   Set: Value(self: OFXInteger2DParameter) = value
                    """
                   )

  myCOM = None
  myIndex = None
  myKeyframes = None
  myOwner = None

class OFXInteger3D(object):
  """  """

  def ReferenceEquals(objA: object, objB: object) -> bool:
    """ ReferenceEquals(objA: object, objB: object) -> bool
     """
    return None

  X = None
  Y = None
  Z = None

class OFXInteger3DKeyframe(OFXKeyframe[OFXInteger3D]):
  """  """

  def ReferenceEquals(objA: object, objB: object) -> bool:
    """ ReferenceEquals(objA: object, objB: object) -> bool
     """
    return None

  Value = property(None, None, None,
                   """ Get: Value(self: OFXInteger3DKeyframe) -> OFXInteger3D
                   
                   Set: Value(self: OFXInteger3DKeyframe) = value
                    """
                   )

  myCOM = None
  myOwner = None
  myParamID = None

class OFXInteger3DParameter(OFXRangeParameter[OFXInteger3D, OFXInteger3DKeyframe]):
  """  """

  def GetProp(self, arg0, arg1):
    """ GetProp(self: OFXInteger3DParameter, propName: str) -> OFXInteger3D
     """
    return None

  def GetValueAtTime(self, time):
    """ GetValueAtTime(self: OFXInteger3DParameter, time: Timecode) -> OFXInteger3D
     """
    import ScriptPortal.Vegas
    return ScriptPortal.Vegas.OFXInteger3D()

  def ReferenceEquals(objA: object, objB: object) -> bool:
    """ ReferenceEquals(objA: object, objB: object) -> bool
     """
    return None

  def SetValueAtTime(self, time, value):
    """ SetValueAtTime(self: OFXInteger3DParameter, time: Timecode, value: OFXInteger3D) """
    import System
    return System.Void()

  Value = property(None, None, None,
                   """ Get: Value(self: OFXInteger3DParameter) -> OFXInteger3D
                   
                   Set: Value(self: OFXInteger3DParameter) = value
                    """
                   )

  myCOM = None
  myIndex = None
  myKeyframes = None
  myOwner = None

class OFXIntegerKeyframe(OFXKeyframe[int]):
  """  """

  def ReferenceEquals(objA: object, objB: object) -> bool:
    """ ReferenceEquals(objA: object, objB: object) -> bool
     """
    return None

  Value = property(None, None, None,
                   """ Get: Value(self: OFXIntegerKeyframe) -> int
                   
                   Set: Value(self: OFXIntegerKeyframe) = value
                    """
                   )

  myCOM = None
  myOwner = None
  myParamID = None

class OFXIntegerParameter(OFXRangeParameter[int, OFXIntegerKeyframe]):
  """  """

  def GetProp(self, arg0, arg1):
    """ GetProp(self: OFXIntegerParameter, propName: str) -> int
     """
    return 1

  def GetValueAtTime(self, time):
    """ GetValueAtTime(self: OFXIntegerParameter, time: Timecode) -> int
     """
    import System
    return System.int()

  def ReferenceEquals(objA: object, objB: object) -> bool:
    """ ReferenceEquals(objA: object, objB: object) -> bool
     """
    return None

  def SetValueAtTime(self, time, value):
    """ SetValueAtTime(self: OFXIntegerParameter, time: Timecode, value: int) """
    import System
    return System.Void()

  Value = property(None, None, None,
                   """ Get: Value(self: OFXIntegerParameter) -> int
                   
                   Set: Value(self: OFXIntegerParameter) = value
                    """
                   )

  myCOM = None
  myIndex = None
  myKeyframes = None
  myOwner = None

class OFXInterpolationType(Enum):
  """ 
  
  enum OFXInterpolationType, values: Fast (2), Hold (6), Linear (1), Manual (7), Sharp (5), Slow (3), Smooth (4), Split (8), Unknown (0)
  
   """

  Fast = None

  def Format(self, arg0, arg1, arg2):
    """ Format(enumType: Type, value: object, format: str) -> str
     """
    return ""

  def GetName(self, arg0, arg1):
    """ GetName(enumType: Type, value: object) -> str
     """
    return ""

  def GetNames(self, arg0):
    """ GetNames(enumType: Type) -> Array[str]
     """
    return ""

  def GetUnderlyingType(self, arg0):
    """ GetUnderlyingType(enumType: Type) -> Type
     """
    return None

  def GetValues(self, arg0):
    """ GetValues(enumType: Type) -> Array
     """
    return None

  Hold = None

  def IsDefined(self, arg0, arg1):
    """ IsDefined(enumType: Type, value: object) -> bool
     """
    return None

  Linear = None
  Manual = None

  def Parse(self, arg0, arg1):
    """ Parse(enumType: Type, value: str) -> object
    Parse(enumType: Type, value: str, ignoreCase: bool) -> object
     """
    return None

  def ReferenceEquals(objA: object, objB: object) -> bool:
    """ ReferenceEquals(objA: object, objB: object) -> bool
     """
    return None

  Sharp = None
  Slow = None
  Smooth = None
  Split = None

  def ToObject(self, arg0, arg1):
    """ ToObject(enumType: Type, value: object) -> object
    ToObject(enumType: Type, value: SByte) -> object
    ToObject(enumType: Type, value: Int16) -> object
    ToObject(enumType: Type, value: int) -> object
    ToObject(enumType: Type, value: Byte) -> object
    ToObject(enumType: Type, value: UInt16) -> object
    ToObject(enumType: Type, value: int) -> object
    ToObject(enumType: Type, value: int) -> object
    ToObject(enumType: Type, value: int) -> object
     """
    return None

  def TryParse(self, arg0):
    """ TryParse[TEnum](value: str) -> (bool, TEnum)
    TryParse[TEnum](value: str, ignoreCase: bool) -> (bool, TEnum)
     """
    return (None, None)

  Unknown = None
  value__ = None

def OFXKeyframe():
  """  """
  pass

class OFXKeyframes(BaseList[TKeyframe]):
  """  """

  def BaseIndex(self, arg0=None, TKeyframe=None, arg1=None):
    """ BaseIndex(self: OFXKeyframes[TValue, TKeyframe], item: TKeyframe) -> int
     """
    return 1

  def BaseRemove(self, arg0=None, TKeyframe=None, arg1=None):
    """ BaseRemove(self: OFXKeyframes[TValue, TKeyframe], item: TKeyframe) -> bool
     """
    return None

  def GetCount(self, arg0=None, TKeyframe=None):
    """ GetCount(self: OFXKeyframes[TValue, TKeyframe]) -> int
     """
    return 1

  def GetItem(self, arg0=None, TKeyframe=None, arg1=None):
    """ GetItem(self: OFXKeyframes[TValue, TKeyframe], index: int) -> TKeyframe
     """
    return None

  def ReferenceEquals(objA: object, objB: object) -> bool:
    """ ReferenceEquals(objA: object, objB: object) -> bool
     """
    return None

  myCOM = None
  myOwner = None
  myParamID = None

def OFXParameter():
  """  """
  pass

class OFXParameterType(Enum):
  """ 
  
  enum OFXParameterType, values: Boolean (4), Choice (5), Custom (15), Double (11), Double2D (12), Double3D (13), Group (2), Integer (8), Integer2D (9), Integer3D (10), Page (1), PushButton (3), RGB (6), RGBA (7), String (14), Unknown (0)
  
   """

  Boolean = None
  Choice = None
  Custom = None
  Double = None
  Double2D = None
  Double3D = None

  def Format(self, arg0, arg1, arg2):
    """ Format(enumType: Type, value: object, format: str) -> str
     """
    return ""

  def GetName(self, arg0, arg1):
    """ GetName(enumType: Type, value: object) -> str
     """
    return ""

  def GetNames(self, arg0):
    """ GetNames(enumType: Type) -> Array[str]
     """
    return ""

  def GetUnderlyingType(self, arg0):
    """ GetUnderlyingType(enumType: Type) -> Type
     """
    return None

  def GetValues(self, arg0):
    """ GetValues(enumType: Type) -> Array
     """
    return None

  Group = None
  Integer = None
  Integer2D = None
  Integer3D = None

  def IsDefined(self, arg0, arg1):
    """ IsDefined(enumType: Type, value: object) -> bool
     """
    return None

  Page = None

  def Parse(self, arg0, arg1):
    """ Parse(enumType: Type, value: str) -> object
    Parse(enumType: Type, value: str, ignoreCase: bool) -> object
     """
    return None

  PushButton = None
  RGB = None
  RGBA = None

  def ReferenceEquals(objA: object, objB: object) -> bool:
    """ ReferenceEquals(objA: object, objB: object) -> bool
     """
    return None

  String = None

  def ToObject(self, arg0, arg1):
    """ ToObject(enumType: Type, value: object) -> object
    ToObject(enumType: Type, value: SByte) -> object
    ToObject(enumType: Type, value: Int16) -> object
    ToObject(enumType: Type, value: int) -> object
    ToObject(enumType: Type, value: Byte) -> object
    ToObject(enumType: Type, value: UInt16) -> object
    ToObject(enumType: Type, value: int) -> object
    ToObject(enumType: Type, value: int) -> object
    ToObject(enumType: Type, value: int) -> object
     """
    return None

  def TryParse(self, arg0):
    """ TryParse[TEnum](value: str) -> (bool, TEnum)
    TryParse[TEnum](value: str, ignoreCase: bool) -> (bool, TEnum)
     """
    return (None, None)

  Unknown = None
  value__ = None

class OFXParameters(BaseList[OFXParameter]):
  """  """

  def BaseIndex(self, arg0, arg1):
    """ BaseIndex(self: OFXParameters, item: OFXParameter) -> int
     """
    return 1

  def GetCount(self, arg0):
    """ GetCount(self: OFXParameters) -> int
     """
    return 1

  def GetItem(self, arg0, arg1):
    """ GetItem(self: OFXParameters, index: int) -> OFXParameter
     """
    return None

  def ReferenceEquals(objA: object, objB: object) -> bool:
    """ ReferenceEquals(objA: object, objB: object) -> bool
     """
    return None

  myCOM = None
  myOwner = None

class OFXPlugIn(OFXBase):
  """  """

  def Equals(self, that):
    """ Equals(self: OFXPlugIn, that: OFXPlugIn) -> bool
    Equals(self: OFXPlugIn, that: object) -> bool
     """
    import System
    return System.Boolean()

  def GetHashCode(self):
    """ GetHashCode(self: OFXPlugIn) -> int
     """
    import System
    return System.int()

  def ReferenceEquals(objA: object, objB: object) -> bool:
    """ ReferenceEquals(objA: object, objB: object) -> bool
     """
    return None

  myCOM = None
  myUniqueID = None

class OFXRGBAKeyframe(OFXKeyframe[OFXColor]):
  """  """

  def ReferenceEquals(objA: object, objB: object) -> bool:
    """ ReferenceEquals(objA: object, objB: object) -> bool
     """
    return None

  Value = property(None, None, None,
                   """ Get: Value(self: OFXRGBAKeyframe) -> OFXColor
                   
                   Set: Value(self: OFXRGBAKeyframe) = value
                    """
                   )

  myCOM = None
  myOwner = None
  myParamID = None

class OFXRGBAParameter(OFXParameter[OFXColor, OFXRGBAKeyframe]):
  """  """

  def GetProp(self, arg0, arg1):
    """ GetProp(self: OFXRGBAParameter, propName: str) -> OFXColor
     """
    return None

  def GetValueAtTime(self, time):
    """ GetValueAtTime(self: OFXRGBAParameter, time: Timecode) -> OFXColor
     """
    import ScriptPortal.Vegas
    return ScriptPortal.Vegas.OFXColor()

  def ReferenceEquals(objA: object, objB: object) -> bool:
    """ ReferenceEquals(objA: object, objB: object) -> bool
     """
    return None

  def SetValueAtTime(self, time, value):
    """ SetValueAtTime(self: OFXRGBAParameter, time: Timecode, value: OFXColor) """
    import System
    return System.Void()

  Value = property(None, None, None,
                   """ Get: Value(self: OFXRGBAParameter) -> OFXColor
                   
                   Set: Value(self: OFXRGBAParameter) = value
                    """
                   )

  myCOM = None
  myIndex = None
  myKeyframes = None
  myOwner = None

class OFXRGBKeyframe(OFXKeyframe[OFXColor]):
  """  """

  def ReferenceEquals(objA: object, objB: object) -> bool:
    """ ReferenceEquals(objA: object, objB: object) -> bool
     """
    return None

  Value = property(None, None, None,
                   """ Get: Value(self: OFXRGBKeyframe) -> OFXColor
                   
                   Set: Value(self: OFXRGBKeyframe) = value
                    """
                   )

  myCOM = None
  myOwner = None
  myParamID = None

class OFXRGBParameter(OFXParameter[OFXColor, OFXRGBKeyframe]):
  """  """

  def GetProp(self, arg0, arg1):
    """ GetProp(self: OFXRGBParameter, propName: str) -> OFXColor
     """
    return None

  def GetValueAtTime(self, time):
    """ GetValueAtTime(self: OFXRGBParameter, time: Timecode) -> OFXColor
     """
    import ScriptPortal.Vegas
    return ScriptPortal.Vegas.OFXColor()

  def ReferenceEquals(objA: object, objB: object) -> bool:
    """ ReferenceEquals(objA: object, objB: object) -> bool
     """
    return None

  def SetValueAtTime(self, time, value):
    """ SetValueAtTime(self: OFXRGBParameter, time: Timecode, value: OFXColor) """
    import System
    return System.Void()

  Value = property(None, None, None,
                   """ Get: Value(self: OFXRGBParameter) -> OFXColor
                   
                   Set: Value(self: OFXRGBParameter) = value
                    """
                   )

  myCOM = None
  myIndex = None
  myKeyframes = None
  myOwner = None

class OFXRangeParameter(OFXParameter[TValue, TKeyframe]):
  """  """

  DisplayMax = property(None, None, None,
                        """ Get: DisplayMax(self: OFXRangeParameter[TValue, TKeyframe]) -> TValue
                        
                         """
                        )

  DisplayMin = property(None, None, None,
                        """ Get: DisplayMin(self: OFXRangeParameter[TValue, TKeyframe]) -> TValue
                        
                         """
                        )

  Max = property(None, None, None,
                 """ Get: Max(self: OFXRangeParameter[TValue, TKeyframe]) -> TValue
                 
                  """
                 )

  Min = property(None, None, None,
                 """ Get: Min(self: OFXRangeParameter[TValue, TKeyframe]) -> TValue
                 
                  """
                 )


  def ReferenceEquals(objA: object, objB: object) -> bool:
    """ ReferenceEquals(objA: object, objB: object) -> bool
     """
    return None

  myCOM = None
  myIndex = None
  myKeyframes = None
  myOwner = None

class OFXStringKeyframe(OFXKeyframe[str]):
  """  """

  def ReferenceEquals(objA: object, objB: object) -> bool:
    """ ReferenceEquals(objA: object, objB: object) -> bool
     """
    return None

  Value = property(None, None, None,
                   """ Get: Value(self: OFXStringKeyframe) -> str
                   
                   Set: Value(self: OFXStringKeyframe) = value
                    """
                   )

  myCOM = None
  myOwner = None
  myParamID = None

class OFXStringParameter(OFXParameter[str, OFXStringKeyframe]):
  """  """

  def GetProp(self, arg0, arg1):
    """ GetProp(self: OFXStringParameter, propName: str) -> str
     """
    return ""

  def GetValueAtTime(self, time):
    """ GetValueAtTime(self: OFXStringParameter, time: Timecode) -> str
     """
    import System
    return System.String()

  def ReferenceEquals(objA: object, objB: object) -> bool:
    """ ReferenceEquals(objA: object, objB: object) -> bool
     """
    return None

  def SetValueAtTime(self, time, value):
    """ SetValueAtTime(self: OFXStringParameter, time: Timecode, value: str) """
    import System
    return System.Void()

  Value = property(None, None, None,
                   """ Get: Value(self: OFXStringParameter) -> str
                   
                   Set: Value(self: OFXStringParameter) = value
                    """
                   )

  myCOM = None
  myIndex = None
  myKeyframes = None
  myOwner = None

class OwnerType(Enum):
  """ 
  
  enum OwnerType, values: Event (1), EventFadeIn (7), EventFadeOut (8), Media (6), None (0), ParentTrack (10), ParentTrack2To1 (11), Project (4), Surface (5), Track (2), Track2To1 (9), TrackMask (3)
  
   """

  Event = None
  EventFadeIn = None
  EventFadeOut = None
  Media = None
  None_ = None
  ParentTrack = None
  ParentTrack2To1 = None
  Project = None
  Surface = None
  Track = None
  Track2To1 = None
  TrackMask = None

class PanType(Enum):
  """ 
  Enumeration of audio pan settings.
  enum PanType, values: Add (0), Balance (2), ConstantPower (1), Film (5), Notch3Db (3), Notch6Db (4), Unknown (666)
  
   """

  Add = None
  Balance = None
  ConstantPower = None
  Film = None
  Notch3Db = None
  Notch6Db = None
  Unknown = None
  value__ = None

class PixelFormat(Enum):
  """ 
  Enumeration of video pixel formats.
  enum PixelFormat, values: Float32Bit (1), Float32BitFullRange (2), Int8Bit (0)
  
   """

  Float32Bit = None
  Float32BitFullRange = None
  Int8Bit = None


class PlugInNode(BaseList[PlugInNode]):
  """ Represents a node in the hierarchy of plug-in effects, transitions, and generators. """

  CanCreateSubnodes: bool


  ClassID: Guid
 
  def Equals(self, obj):
    """ Equals(self: PlugInNode, obj: object) -> bool
     """
    import System
    return System.Boolean()

  def FindChildByClassID(self, classID):
    """ FindChildByClassID(self: PlugInNode, classID: Guid) -> PlugInNode
     """
    import ScriptPortal.Vegas
    return ScriptPortal.Vegas.PlugInNode()

  def FindChildByName(self, name):
    """ FindChildByName(self: PlugInNode, name: str) -> PlugInNode
     """
    import ScriptPortal.Vegas
    return ScriptPortal.Vegas.PlugInNode()

  def FindChildByUniqueID(self, uniqueID):
    """ FindChildByUniqueID(self: PlugInNode, uniqueID: str) -> PlugInNode
     """
    import ScriptPortal.Vegas
    return ScriptPortal.Vegas.PlugInNode()

  def GetChild(self, index):
    """ GetChild(self: PlugInNode, index: int) -> PlugInNode
     """
    import ScriptPortal.Vegas
    return ScriptPortal.Vegas.PlugInNode()

  def GetChildByClassID(self, val):
    """ GetChildByClassID(self: PlugInNode, val: Guid) -> PlugInNode
     """
    import ScriptPortal.Vegas
    return ScriptPortal.Vegas.PlugInNode()

  def GetChildByName(self, val):
    """ GetChildByName(self: PlugInNode, val: str) -> PlugInNode
     """
    import ScriptPortal.Vegas
    return ScriptPortal.Vegas.PlugInNode()

  def GetChildByUniqueID(self, val):
    """ GetChildByUniqueID(self: PlugInNode, val: str) -> PlugInNode
     """
    import ScriptPortal.Vegas
    return ScriptPortal.Vegas.PlugInNode()

  def GetCount(self, arg0):
    """ GetCount(self: PlugInNode) -> int
     """
    return 1

  def GetHashCode(self):
    """ GetHashCode(self: PlugInNode) -> int
     """
    import System
    return System.int()

  def GetItem(self, arg0, arg1):
    """ GetItem(self: PlugInNode, index: int) -> PlugInNode
     """
    return None

  IsAudio: bool

  IsAutomatable: bool

  IsContainer: bool

  IsDisabled:  bool

  IsFixedSize: bool

  IsOFX: bool

  IsPackage: bool

  IsReadOnly: bool 

  IsVideo: bool 

  def MembersEqual(self, arg0, arg1):
    """ MembersEqual(self: PlugInNode, other: PlugInNode) -> bool
     """
    return None

  Name: str

  OFXPlugIn: OFXPlugIn
 
  Presets:  EffectPresets

  def ReferenceEquals(objA: object, objB: object) -> bool:
    """ ReferenceEquals(objA: object, objB: object) -> bool
     """
    return None

  UniqueID:  str

class PlugInType(Enum):
  """ 
  
  enum PlugInType, values: Audio3rdParty (4), AudioAll (2), AudioAutomatable (5), AudioPackage (7), AudioSf (3), AudioTrackOptimized (6), None (0), Root (1), Video2to1 (15), VideoFilter (9), VideoFilterPackage (10), VideoGenerator (13), VideoGeneratorPackage (14), VideoRoot (8), VideoTransition (11), VideoTransitionPackage (12)
  
   """

  Audio3rdParty = None
  AudioAll = None
  AudioAutomatable = None
  AudioPackage = None
  AudioSf = None
  AudioTrackOptimized = None
  None_ = None
  Root = None
  Video2to1 = None
  VideoFilter = None
  VideoFilterPackage = None
  VideoGenerator = None
  VideoGeneratorPackage = None
  VideoRoot = None
  VideoTransition = None
  VideoTransitionPackage = None
  
class PreferenceFlag(Enum):
  """ 
  
  enum PreferenceFlag, values: AutoSaveEnableAdvanced (0), AutoSaveEnableDaily (3), AutoSaveEnableHourly (2), AutoSaveEnableMinute (1), AutoSaveEnableRealTime (4), AutoSaveUseProjDir (7), AutoSaveUseTempDir (5), InsertSubtitlesEnableDefault (8), InsertSubtitlesFromRegionsEnableDefault (9), LiveSaveEnable (6)
  
   """

  AutoSaveEnableAdvanced = None
  AutoSaveEnableDaily = None
  AutoSaveEnableHourly = None
  AutoSaveEnableMinute = None
  AutoSaveEnableRealTime = None
  AutoSaveUseProjDir = None
  AutoSaveUseTempDir = None
  InsertSubtitlesEnableDefault = None
  InsertSubtitlesFromRegionsEnableDefault = None
  LiveSaveEnable = None


class PreferenceString(Enum):
  """ 
  
  enum PreferenceString, values: AutoSaveDirectory (1), TempDirectory (0)
  
   """

  AutoSaveDirectory = None
  TempDirectory = None


  value__ = None

class PreviewVideoProperties(VideoProperties):
  """  Represents a project's preview video properties."""

  FieldOrder: VideoFieldOrder

  FrameRate: float

  FullSize:  bool

  Height: int

  PixelAspectRatio:  float

  PreviewSize:  VideoPreviewSize
  
  def ReferenceEquals(objA: object, objB: object) -> bool:
    """ ReferenceEquals(objA: object, objB: object) -> bool
     """
    return None

  RenderQuality: VideoRenderQuality
  
  Width: int
  
  myProject = None
  myType = None

class PrintWizard(PrintWizard):
  """ PrintWizard()
   """

  Activated = None
  ActiveForm = None
  ActivePage = None

  def AllowMultichannelMapping(self, arg0):
    """ AllowMultichannelMapping(self: PrintWizard) -> bool
     """
    return None

  AutoSizeChanged = None
  AutoValidateChanged = None
  BackColorChanged = None
  BackgroundImageChanged = None
  BackgroundImageLayoutChanged = None
  BindingContextChanged = None
  CausesValidationChanged = None
  ChangeUICues = None

  class ChannelPickerItem(object):
    """ ChannelPickerItem(label: str, flags: AutoEditPresetFlags)
     """

    def ReferenceEquals(objA: object, objB: object) -> bool:
      """ ReferenceEquals(objA: object, objB: object) -> bool
       """
      return None

  CheckForIllegalCrossThreadCalls = False
  Click = None
  ClientSizeChanged = None
  Closed = None
  Closing = None
  ContextMenuChanged = None
  ContextMenuStripChanged = None
  ControlAdded = None

  class ControlCollection(ControlCollection):
    """ ControlCollection(owner: Form)
     """

    def Add(self, value):
      """ Add(self: ControlCollection, value: Control) """
      import System
      return System.Void()

    def ReferenceEquals(objA: object, objB: object) -> bool:
      """ ReferenceEquals(objA: object, objB: object) -> bool
       """
      return None

    def Remove(self, value):
      """ Remove(self: ControlCollection, value: Control) """
      import System
      return System.Void()

  ControlRemoved = None
  CursorChanged = None
  Deactivate = None
  DefaultBackColor = None
  DefaultFont = None
  DefaultForeColor = None
  Disposed = None
  DockChanged = None
  DoubleClick = None
  DpiChanged = None
  DpiChangedAfterParent = None
  DpiChangedBeforeParent = None
  DragDrop = None
  DragEnter = None
  DragLeave = None
  DragOver = None
  EnabledChanged = None
  Enter = None
  FontChanged = None
  ForeColorChanged = None
  FormClosed = None
  FormClosing = None

  def FromChildHandle(self, arg0):
    """ FromChildHandle(handle: IntPtr) -> Control
     """
    return None

  def FromHandle(self, arg0):
    """ FromHandle(handle: IntPtr) -> Control
     """
    return None

  def GetAutoScaleSize(self, arg0):
    """ GetAutoScaleSize(font: Font) -> SizeF
     """
    return None

  def GetCurrentAppSmpteType(self, arg0):
    """ GetCurrentAppSmpteType(self: PrintWizard) -> SMPTEType
     """
    return None

  def GetOwnerWindow(self, arg0):
    """ GetOwnerWindow(self: PrintWizard) -> IWin32Window
     """
    return None

  def GetProjectTime(self, arg0):
    """ GetProjectTime(self: PrintWizard) -> int
     """
    return None

  def GetSelectionTime(self, arg0):
    """ GetSelectionTime(self: PrintWizard) -> int
     """
    return None

  def GetShortAppName(self, arg0):
    """ GetShortAppName(self: PrintWizard) -> str
     """
    return ""

  GiveFeedback = None
  GotFocus = None
  HandleCreated = None
  HandleDestroyed = None
  HelpButtonClicked = None
  HelpRequested = None
  ImeModeChanged = None

  def InitTestPatternOptions(self, arg0):
    """ InitTestPatternOptions(self: PrintWizard) """
    pass

  InputLanguageChanged = None
  InputLanguageChanging = None
  Invalidated = None

  def IsKeyLocked(self, arg0):
    """ IsKeyLocked(keyVal: Keys) -> bool
     """
    return None

  def IsMnemonic(self, arg0, arg1):
    """ IsMnemonic(charCode: Char, text: str) -> bool
     """
    return None

  KeyDown = None
  KeyPress = None
  KeyUp = None
  Layout = None
  Leave = None
  Load = None
  LocationChanged = None
  LostFocus = None
  MarginChanged = None
  MaximizedBoundsChanged = None
  MaximumSizeChanged = None
  MdiChildActivate = None
  MenuComplete = None
  MenuStart = None
  MinimumSizeChanged = None
  ModifierKeys = None
  MouseButtons = None
  MouseCaptureChanged = None
  MouseClick = None
  MouseDoubleClick = None
  MouseDown = None
  MouseEnter = None
  MouseHover = None
  MouseLeave = None
  MouseMove = None
  MousePosition = None
  MouseUp = None
  MouseWheel = None
  Move = None
  PaddingChanged = None
  PageMarginX = None
  PageMarginY = None
  Pages = None
  Paint = None
  ParentChanged = None
  PreferredStartTime: Timecode

  PreviewKeyDown = None
  QueryAccessibilityHelp = None
  QueryContinueDrag = None

  def ReferenceEquals(objA: object, objB: object) -> bool:
    """ ReferenceEquals(objA: object, objB: object) -> bool
     """
    return None

  def ReflectMessage(self, arg0, arg1):
    """ ReflectMessage(hWnd: IntPtr, m: Message) -> (bool, Message)
     """
    return (None, None)

  RegionChanged = None
  Resize = None
  ResizeBegin = None
  ResizeEnd = None
  RightToLeftChanged = None
  RightToLeftLayoutChanged = None
  Scroll = None
  ScrollStateAutoScrolling = 1
  ScrollStateFullDrag = 16
  ScrollStateHScrollVisible = 2
  ScrollStateUserHasScrolled = 8
  ScrollStateVScrollVisible = 4

  def ShowMultichannelMappingDialog(self, arg0, arg1):
    """ ShowMultichannelMappingDialog(self: PrintWizard, parentWindow: IWin32Window) -> DialogResult
     """
    return None

  def ShowSelectDirectoryDlg(self, arg0, arg1, arg2, arg3, arg4):
    """ ShowSelectDirectoryDlg(self: PrintWizard, hwndOwn: IntPtr, title: str, defaultDir: str, useNet: bool) -> str
     """
    return ""

  Shown = None
  SizeChanged = None
  StyleChanged = None
  SystemColorsChanged = None
  TabIndexChanged = None
  TabStopChanged = None
  TextChanged = None
  ThePreferredStartTime = None
  Validated = None
  Validating = None
  VisibleChanged = None
  myAllowTestPattern = None
  myAutoButton = None
  myAutoEditPresets = None
  myBackButton = None
  myButtonPacker = None
  myCancelButton = None
  myChannelMappingsButton = None
  myChannelPicker = None
  myController = None
  myCrashButton = None
  myCreateSMPTETimecode = None
  myDeviceSelector = None
  myDeviceTimecodeBox = None
  myDeviceTimecodeLabel = None
  myEnableMultichannelButton = None
  myEnableMultichannelMapping = None
  myEndTimeBox = None
  myEndTimeLabel = None
  myFormatLabel = None
  myGenerateToneCheckBox = None
  myHRule = None
  myIgnorePrintModeChange = None
  myInitChannelPage = None
  myInitControlPage = None
  myInitDevicePage = None
  myInitFormatPage = None
  myInitLeaderPage = None
  myLeaderBCD = None
  myLeaderCheckBox = None
  myLeaderTime = None
  myLeaderTimeBox = None
  myLeaderTimeLabel = None
  myLoadedAudioFormat = None
  myLoadedVideoFormat = None
  myManualButton = None
  myNextButton = None
  myPatternBCD = None
  myPatternCheckBox = None
  myPatternGeneratorID = None
  myPatternPresetID = None
  myPatternTime = None
  myPrerenderedFilesBox = None
  myPrerenderedFilesButton = None
  myPrerenderedFilesLabel = None
  myPreviewCheckBox = None
  myProxyRendererID = None
  myRefreshTimer = None
  myReloadOnNextRefresh = None
  myRenderAudioRealtimeCheckBox = None
  myRenderLoopRegionCheckBox = None
  mySMPTE = None
  mySelectAllButton = None
  mySelectSomeButton = None
  mySelectedDeviceID = None
  myStartTimeBox = None
  myStartTimeLabel = None
  myTestPatternCombo = None
  myTestPatternComboLabel = None
  myTestPatternTimeBox = None
  myTestPatternTimeLabel = None
  myTimelineTime = None
  myTrailerBCD = None
  myTrailerCheckBox = None
  myTrailerTime = None
  myTrailerTimeBox = None
  myTrailerTimeLabel = None
  myUseRenderRotationButton = None
  myVegas = None

class ProgressEventArgs(EventArgs):
  """ Represents the arguments passed to a progress worker event.
  ProgressEventArgs()
   """

  Cancel = None
  Empty = None
  NeedUserInput = None

  def ReferenceEquals(objA: object, objB: object) -> bool:
    """ ReferenceEquals(objA: object, objB: object) -> bool
     """
    return None

class ProgressEventHandler(MulticastDelegate):
  """ Represents a method that handles a progress worker event.
  ProgressEventHandler(object: object, method: IntPtr)
   """

  def BeginInvoke(self, worker, args, callback, object):
    """ BeginInvoke(self: ProgressEventHandler, worker: ProgressWorker, args: ProgressEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult
     """
    import System
    return System.IAsyncResult()

  def Combine(self, arg0, arg1):
    """ Combine(a: Delegate, b: Delegate) -> Delegate
    Combine(*delegates: Array[Delegate]) -> Delegate
     """
    return None

  def CreateDelegate(self, arg0, arg1, arg2):
    """ CreateDelegate(type: Type, target: object, method: str) -> Delegate
    CreateDelegate(type: Type, target: object, method: str, ignoreCase: bool) -> Delegate
    CreateDelegate(type: Type, target: object, method: str, ignoreCase: bool, throwOnBindFailure: bool) -> Delegate
    CreateDelegate(type: Type, target: Type, method: str) -> Delegate
    CreateDelegate(type: Type, target: Type, method: str, ignoreCase: bool) -> Delegate
    CreateDelegate(type: Type, target: Type, method: str, ignoreCase: bool, throwOnBindFailure: bool) -> Delegate
    CreateDelegate(type: Type, method: MethodInfo, throwOnBindFailure: bool) -> Delegate
    CreateDelegate(type: Type, firstArgument: object, method: MethodInfo) -> Delegate
    CreateDelegate(type: Type, firstArgument: object, method: MethodInfo, throwOnBindFailure: bool) -> Delegate
    CreateDelegate(type: Type, method: MethodInfo) -> Delegate
     """
    return None

  def EndInvoke(self, result):
    """ EndInvoke(self: ProgressEventHandler, result: IAsyncResult) """
    import System
    return System.Void()

  def Invoke(self, worker, args):
    """ Invoke(self: ProgressEventHandler, worker: ProgressWorker, args: ProgressEventArgs) """
    import System
    return System.Void()

  def ReferenceEquals(objA: object, objB: object) -> bool:
    """ ReferenceEquals(objA: object, objB: object) -> bool
     """
    return None

  def Remove(self, arg0, arg1):
    """ Remove(source: Delegate, value: Delegate) -> Delegate
     """
    return None

  def RemoveAll(self, arg0, arg1):
    """ RemoveAll(source: Delegate, value: Delegate) -> Delegate
     """
    return None

class ProgressWorker(object):
  """ Represents an object that performs work on Vegas' asynchronous task manager.
  ProgressWorker()
   """

  BlockUserInput: bool
  
  Canceled:       bool
  
  CompleteWork = None
  Dequeued = None
  DoWork = None
  KeepStatusDialog: bool
  
  def OnCompleteWork(self, arg0, arg1):
    """ OnCompleteWork(self: ProgressWorker, args: ProgressEventArgs) """
    pass

  def OnDequeued(self, arg0, arg1):
    """ OnDequeued(self: ProgressWorker, args: EventArgs) """
    pass

  def OnDoWork(self, arg0, arg1):
    """ OnDoWork(self: ProgressWorker, args: ProgressEventArgs) """
    pass

  def OnStatusBegin(self, arg0, arg1):
    """ OnStatusBegin(self: ProgressWorker, args: EventArgs) """
    pass

  def OnStatusEnd(self, arg0, arg1):
    """ OnStatusEnd(self: ProgressWorker, args: EventArgs) """
    pass

  def OnStatusUpdate(self, arg0, arg1):
    """ OnStatusUpdate(self: ProgressWorker, args: EventArgs) """
    pass

  PercentComplete: int
  
  Progress: float
  
  ProgressMax: float
   
  ProgressMin: float
  
  ProgressText: str
  
  def ReferenceEquals(objA: object, objB: object) -> bool:
    """ ReferenceEquals(objA: object, objB: object) -> bool
     """
    return None

  SerializeWork: bool
  
  StatusBegin = None
  StatusDialog: Form
  
  StatusEnd = None
  StatusUpdate = None

  def WaitForStatusDialog(self):
    """ WaitForStatusDialog(self: ProgressWorker) """
    import System
    return System.Void()

class Project_(object):
  """ Represents the currently opened project.
  Project class """

  ActiveProject: Project_
  
  def AddAudioBusTrack(self: Project_) -> AudioBusTrack:
    """ AddAudioBusTrack(self: Project) -> AudioBusTrack
     """
    import ScriptPortal.Vegas
    return ScriptPortal.Vegas.AudioBusTrack()

  def AddAudioFXBusTrack(self: Project_, plugin: PlugInNode) -> AudioFXBusTrack:
    """ AddAudioFXBusTrack(self: Project, plugin: PlugInNode) -> AudioFXBusTrack
     """
    import ScriptPortal.Vegas
    return ScriptPortal.Vegas.AudioFXBusTrack()

  def AddAudioTrack(self: Project_) -> AudioTrack:
    """ AddAudioTrack(self: Project) -> AudioTrack
     """
    import ScriptPortal.Vegas
    return ScriptPortal.Vegas.AudioTrack()

  def AddVideoTrack(self: Project_) -> VideoTrack:
    """ AddVideoTrack(self: Project) -> VideoTrack
     """
    import ScriptPortal.Vegas
    return ScriptPortal.Vegas.VideoTrack()

  def ArchiveProject(self: Project_, fileName: str) -> bool:
    """ ArchiveProject(self: Project, fileName: str) -> bool
    ArchiveProject(self: Project, fileName: str, flags: ArchiveProjectFlags) -> bool
     """
    import System
    return System.Boolean()

  Audio: ProjectAudioProperties
  
  AudioCD: AudioCDProperties
  
  def BeginWrite(self: Project_, fileName: str, saveType: ProjectSaveType) -> bool:
    """ BeginWrite(self: Project, fileName: str, saveType: ProjectSaveType) -> bool
     """
    import System
    return System.Boolean()

  BusTracks: BusTracks
  
  CDIndices: CDMarkerList
   
  CDTracks:  CDRegionList
  
  COM:  IProjectCOM
  
  CapturePath: str
  
  def CloneProject(self: Project_, newPath: str) -> Project_:
    """ CloneProject(self: Project, newPath: str) -> Project
    CloneProject(self: Project, newPath: str, callback: IProgressCallback) -> Project
     """
    import ScriptPortal.Vegas
    return ScriptPortal.Vegas.Project()

  CommandMarkers: CommandMarkerList
  
  def CreateBackgroundProjectActiveState(self: Project_) -> BackgroundProjectActiveState:
    """ CreateBackgroundProjectActiveState(self: Project) -> BackgroundProjectActiveState
     """
    import ScriptPortal.Vegas
    return ScriptPortal.Vegas.BackgroundProjectActiveState()

  CustomData: CustomDataContainer
  
  DefaultCapturePath: str

  DefaultRenderPath:  str
  
  def Dispose(self: Project_):
    """ Dispose(self: Project) """
    import System
    return System.Void()

  FilePath: str
  
  def GetNumberOfMappedAudioChannels(self: Project_) -> int:
    """ GetNumberOfMappedAudioChannels(self: Project) -> int
     """
    import System
    return System.int()

  def GetTrackGroupOfTrack(self: Project_, indexOfTrack: int) -> TrackGroup:
    """ GetTrackGroupOfTrack(self: Project, indexOfTrack: int) -> TrackGroup
     """
    import ScriptPortal.Vegas
    return ScriptPortal.Vegas.TrackGroup()

  def GroupSelectedTracks(self: Project_) -> TrackGroup:
    """ GroupSelectedTracks(self: Project) -> TrackGroup
     """
    import ScriptPortal.Vegas
    return ScriptPortal.Vegas.TrackGroup()

  Groups:  TrackEventGroups
  
  def InsertTime(self: Project_, start: Timecode, length: Timecode, ignoreSelection: bool):
    """ InsertTime(self: Project)
    InsertTime(self: Project, start: Timecode, length: Timecode)
    InsertTime(self: Project, start: Timecode, length: Timecode, ignoreSelection: bool) """
    import System
    return System.Void()

  IsModified: bool
   
  IsUntitled:  bool
  
  Length: Timecode
  
  Markers:  MarkerList
  
  MasterBus:  AudioBusTrack

  def MatchProjectSettingsWithMedia(self: Project_, media: Media_) -> bool:
    """ MatchProjectSettingsWithMedia(self: Project, media: Media) -> bool
     """
    import System
    return System.Boolean()

  MediaPool: MediaPool_
  
  Preview: PreviewVideoProperties
  
  def ReferenceEquals(objA: object, objB: object) -> bool:
    """ ReferenceEquals(objA: object, objB: object) -> bool
     """
    return None

  Regions: RegionList
  
  def Render(self: Project_, outputFile: str, renderTemplate: RenderTemplate, start: Timecode, length: Timecode) -> RenderStatus:
    """ Render(self: Project, args: RenderArgs) -> RenderStatus
    Render(self: Project, outputFile: str, renderTemplate: RenderTemplate, start: Timecode, length: Timecode) -> RenderStatus
    Render(self: Project, outputFile: str, renderTemplate: RenderTemplate) -> RenderStatus
     """
    import ScriptPortal.Vegas
    return ScriptPortal.Vegas.RenderStatus()

  RenderPath: str
  
  Ruler: RulerProperties
  
  def SaveProject(self: Project_, fileName: str) -> bool:
    """ SaveProject(self: Project, fileName: str) -> bool
     """
    import System
    return System.Boolean()

  def SetUntitledFlag(self: Project_):
    """ SetUntitledFlag(self: Project) """
    import System
    return System.Void()

  def ShowMultichannelMappingDialog(self: Project_) -> DialogResult:
    """ ShowMultichannelMappingDialog(self: Project) -> DialogResult
    ShowMultichannelMappingDialog(self: Project, parentWindow: IWin32Window) -> DialogResult
     """
    import System.Windows.Forms
    return System.Windows.Forms.DialogResult()

  Summary: SummaryProperties
  
  TheActiveProject = None
  TheProjectCOM = None
  TrackEventGroups: TrackEventGroups
  
  TrackGroups: TrackGroups
  
  Tracks: Tracks_ = None # type: Tracks_

  def UngroupSelectedTracks(self: Project_) :
    """ UngroupSelectedTracks(self: Project) """
    import System
    return System.Void()

  Video: ProjectVideoProperties
  
  VideoBus: VideoBusTrack
  
  myCustomDataContainer = None

class ProjectAudioProperties(AudioProperties):
  """ Represents a project's audio properties. """

  BitDepth: int
  
  LFELowpassFilterCutoffFrequency: int
  
  LFELowpassFilterEnabled: bool
  
  LFELowpassFilterQuality: LowPassFilterQuality
  
  MasterBusMode:  AudioBusMode
  
  def MatchProjectSettingsWithMedia(self: ProjectAudioProperties, media: Media_) -> bool:
    """ MatchProjectSettingsWithMedia(self: ProjectAudioProperties, media: Media) -> bool
     """
    import System
    return System.Boolean()

  RecordedFilesFolder: str
  
  def ReferenceEquals(objA: object, objB: object) -> bool:
    """ ReferenceEquals(objA: object, objB: object) -> bool
     """
    return None

  ResampleQuality: AudioResampleQuality
  
  SampleRate: int
  
  myProject: Project_ = None

class ProjectChangeFlag(Enum):
  """ Enumeration of project change flags
  
  enum (flags) ProjectChangeFlag, values: Bin (1), EndEventDrag (2), EventCount (4), EventData (8), EventGroup (16), EventOrder (32), EventState (64), EventTime (128), FxAutomation (67108864), Markers (256), MediaFx (134217728), MediaReOpen (1024), MediaReplaced (512), MixerFx (2048), MixerGraph (4096), MixerProps (8192), MuteSolo (16384), None (0), PendingDelete (32768), PlaylistDirty (65536), PreviewsDirty (131072), ProjectProps (262144), RulerEvent (524288), SurroundPan (1048576), TimeRange (2097152), TrackCount (4194304), TrackHeight (16777216), TrackState (8388608), VideoQuality (33554432)
  
   """

  Bin = None
  EndEventDrag = None
  EventCount = None
  EventData = None
  EventGroup = None
  EventOrder = None
  EventState = None
  EventTime = None
  FxAutomation = None
  Markers = None
  MediaFx = None
  MediaReOpen = None
  MediaReplaced = None
  MixerFx = None
  MixerGraph = None
  MixerProps = None
  MuteSolo = None
  None_ = None
  PendingDelete = None
  PlaylistDirty = None
  PreviewsDirty = None
  ProjectProps = None
  RulerEvent = None
  SurroundPan = None
  TimeRange = None
  TrackCount = None
  TrackHeight = None
  TrackState = None
  VideoQuality = None


class ProjectOpeningEventArgs(EventArgs):
  """ Represents the method that handles a ProjectOpening event. """

  Empty = None
  ProjectFile = None

  def ReferenceEquals(objA: object, objB: object) -> bool:
    """ ReferenceEquals(objA: object, objB: object) -> bool
     """
    return None

class ProjectOpeningEventHandler(MulticastDelegate):
  """ ProjectOpeningEventHandler(object: object, method: IntPtr)
   """

  def BeginInvoke(self, sender, args, callback, object):
    """ BeginInvoke(self: ProjectOpeningEventHandler, sender: object, args: ProjectOpeningEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult
     """
    import System
    return System.IAsyncResult()

  def Combine(self, arg0, arg1):
    """ Combine(a: Delegate, b: Delegate) -> Delegate
    Combine(*delegates: Array[Delegate]) -> Delegate
     """
    return None

  def CreateDelegate(self, arg0, arg1, arg2):
    """ CreateDelegate(type: Type, target: object, method: str) -> Delegate
    CreateDelegate(type: Type, target: object, method: str, ignoreCase: bool) -> Delegate
    CreateDelegate(type: Type, target: object, method: str, ignoreCase: bool, throwOnBindFailure: bool) -> Delegate
    CreateDelegate(type: Type, target: Type, method: str) -> Delegate
    CreateDelegate(type: Type, target: Type, method: str, ignoreCase: bool) -> Delegate
    CreateDelegate(type: Type, target: Type, method: str, ignoreCase: bool, throwOnBindFailure: bool) -> Delegate
    CreateDelegate(type: Type, method: MethodInfo, throwOnBindFailure: bool) -> Delegate
    CreateDelegate(type: Type, firstArgument: object, method: MethodInfo) -> Delegate
    CreateDelegate(type: Type, firstArgument: object, method: MethodInfo, throwOnBindFailure: bool) -> Delegate
    CreateDelegate(type: Type, method: MethodInfo) -> Delegate
     """
    return None

  def EndInvoke(self, result):
    """ EndInvoke(self: ProjectOpeningEventHandler, result: IAsyncResult) """
    import System
    return System.Void()

  def Invoke(self, sender, args):
    """ Invoke(self: ProjectOpeningEventHandler, sender: object, args: ProjectOpeningEventArgs) """
    import System
    return System.Void()

  def ReferenceEquals(objA: object, objB: object) -> bool:
    """ ReferenceEquals(objA: object, objB: object) -> bool
     """
    return None

  def Remove(self, arg0, arg1):
    """ Remove(source: Delegate, value: Delegate) -> Delegate
     """
    return None

  def RemoveAll(self, arg0, arg1):
    """ RemoveAll(source: Delegate, value: Delegate) -> Delegate
     """
    return None

class ProjectPathID(Enum):
  """ 
  
  enum ProjectPathID, values: Capture (0), Render (1)
  
   """

  Capture = None
  Render = None


class ProjectSaveType(Enum):
  """ 
  
  enum ProjectSaveType, values: Project_AAF (2), Project_Archive (4), Project_AvidAAF (3), Project_Default (0), Project_Reference (1), Render_Vfw (6), Render_Wave (5), Unknown (-1)
  
   """

  Project_AAF = None
  Project_Archive = None
  Project_AvidAAF = None
  Project_Default = None
  Project_Reference = None
  Render_Vfw = None
  Render_Wave = None
  Unknown = None


class ProjectTimecode(Timecode):
  """ ProjectTimecode()
   """

  def FromFrames(project: Project, frames: int) -> Timecode:
    """ FromFrames(project: Project, frames: int) -> Timecode
     """
    import ScriptPortal.Vegas
    return ScriptPortal.Vegas.Timecode()

  def FromMilliseconds(project: Project, milliseconds: float) -> Timecode:
    """ FromMilliseconds(project: Project, milliseconds: float) -> Timecode
     """
    import ScriptPortal.Vegas
    return ScriptPortal.Vegas.Timecode()

  def FromNanos(project: Project, nanos: int) -> Timecode:
    """ FromNanos(project: Project, nanos: int) -> Timecode
     """
    import ScriptPortal.Vegas
    return ScriptPortal.Vegas.Timecode()

  def FromPositionNanos(project: Project, nanos: int) -> Timecode:
    """ FromPositionNanos(project: Project, nanos: int) -> Timecode
     """
    import ScriptPortal.Vegas
    return ScriptPortal.Vegas.Timecode()

  def FromPositionString(project: Project, timestamp: str) -> Timecode:
    """ FromPositionString(project: Project, timestamp: str) -> Timecode
    FromPositionString(project: Project, timestamp: str, format: RulerFormat) -> Timecode
     """
    import ScriptPortal.Vegas
    return ScriptPortal.Vegas.Timecode()

  def FromSeconds(project: Project, seconds: float) -> Timecode:
    """ FromSeconds(project: Project, seconds: float) -> Timecode
     """
    import ScriptPortal.Vegas
    return ScriptPortal.Vegas.Timecode()

  def FromString(project: Project, timestamp: str) -> Timecode:
    """ FromString(project: Project, timestamp: str) -> Timecode
    FromString(project: Project, timestamp: str, format: RulerFormat) -> Timecode
    FromString(project: Project, timestamp: str, format: RulerFormat, isPosition: bool) -> Timecode
     """
    import ScriptPortal.Vegas
    return ScriptPortal.Vegas.Timecode()

  def ReferenceEquals(objA: object, objB: object) -> bool:
    """ ReferenceEquals(objA: object, objB: object) -> bool
     """
    return None

class ProjectVideoProperties(VideoProperties):
  """ Represents a project's video properties. """

  DeinterlaceMethod:  VideoDeinterlaceMethod
  
  FieldOrder: VideoFieldOrder
  
  FrameRate: float
  

  def GetIncludeCrosstalkCancelationInRenders(self, mode):
    """ GetIncludeCrosstalkCancelationInRenders(self: ProjectVideoProperties, mode: Stereo3DOutputMode) -> bool
     """
    import System
    return System.Boolean()

  def GetStereo3DCrosstalkCancelation(self, mode):
    """ GetStereo3DCrosstalkCancelation(self: ProjectVideoProperties, mode: Stereo3DOutputMode) -> Single
     """
    import System
    return System.Single()

  def GetStereo3DSwap(self, mode):
    """ GetStereo3DSwap(self: ProjectVideoProperties, mode: Stereo3DOutputMode) -> bool
     """
    import System
    return System.Boolean()

  Height: int
  
  def MatchProjectSettingsWithFile(self, filePath):
    """ MatchProjectSettingsWithFile(self: ProjectVideoProperties, filePath: str) -> bool
     """
    import System
    return System.Boolean()

  def MatchProjectSettingsWithMedia(self, media):
    """ MatchProjectSettingsWithMedia(self: ProjectVideoProperties, media: Media) -> bool
     """
    import System
    return System.Boolean()

  MotionBlurType: MotionBlurType
  
  OutputRotation: VideoOutputRotation
  
  PixelAspectRatio: float
  
  PixelFormat: PixelFormat
  
  PrerenderedFilesFolder: str
  
  def ReferenceEquals(objA: object, objB: object) -> bool:
    """ ReferenceEquals(objA: object, objB: object) -> bool
     """
    return None

  RenderQuality: VideoRenderQuality
  
  def SetIncludeCrosstalkCancelationInRenders(self, mode, value):
    """ SetIncludeCrosstalkCancelationInRenders(self: ProjectVideoProperties, mode: Stereo3DOutputMode, value: bool) """
    import System
    return System.Void()

  def SetStereo3DCrosstalkCancelation(self, mode, value):
    """ SetStereo3DCrosstalkCancelation(self: ProjectVideoProperties, mode: Stereo3DOutputMode, value: Single) """
    import System
    return System.Void()

  def SetStereo3DSwap(self, mode, value):
    """ SetStereo3DSwap(self: ProjectVideoProperties, mode: Stereo3DOutputMode, value: bool) """
    import System
    return System.Void()

  Stereo3DMode: Stereo3DOutputMode
  
  Width: int
  
  myProject = None
  myType = None

class RectangleSetting(XmlSetting):
  """ RectangleSetting(name: str)
  RectangleSetting(name: str, val: Rectangle)
   """

  def FromString(self, value):
    """ FromString(self: RectangleSetting, value: str) """
    import System
    return System.Void()

  Name = None

  def ReferenceEquals(objA: object, objB: object) -> bool:
    """ ReferenceEquals(objA: object, objB: object) -> bool
     """
    return None

  def ToString(self):
    """ ToString(self: RectangleSetting) -> str
     """
    import System
    return System.String()

  Value = None

class Region(Marker):
  """ Represents a region marker on the project time line.
  Region()
  Region(position: Timecode, length: Timecode)
  Region(position: Timecode, length: Timecode, label: str)
   """

  End: Timecode
  
  def Equals(self: Region, obj: object) -> bool:
    """ Equals(self: Region, obj: object) -> bool
     """
    import System
    return System.Boolean()

  def GetHashCode(self):
    """ GetHashCode(self: Region) -> int
     """
    import System
    return System.int()

  Length: Timecode
  
  def ReferenceEquals(objA: object, objB: object) -> bool:
    """ ReferenceEquals(objA: object, objB: object) -> bool
     """
    return None

  def SetLength(self: Region, value: Timecode):
    """ SetLength(self: Region, value: Timecode) """
    pass

  

class RegionList(BaseMarkerList[Region]):
  """ List of Region objects.
  RegionList()
   """

  def ReferenceEquals(objA: object, objB: object) -> bool:
    """ ReferenceEquals(objA: object, objB: object) -> bool
     """
    return None

 

class RenderArgs(object):
  """ Arguments for a render operation
  RenderArgs(project: Project)
  RenderArgs()
   """

  CancelRender:  bool
  
  GenerateLoudnessLog:  bool
  
  def GetTemplateCOM(self, templateCOM):
    """ GetTemplateCOM(self: RenderArgs) -> IRenderTemplateCOM
     """
    import System
    return System.Void()

  IncludeMarkers: bool
  
  Length: Timecode
  
  LengthNanos:  int
  
  OutputFile: str
  
  OutputFileName:  str
  
  def ReferenceEquals(objA: object, objB: object) -> bool:
    """ ReferenceEquals(objA: object, objB: object) -> bool
     """
    return None

  RenderTemplate:  RenderTemplate
  
  RendererID: int
  
  SaveAsMono:  bool
   
  SaveAsMonoStreams:   bool
   
  SaveProjectPathLink:  bool
  
  ShowOpenButtonsOnComplete:  bool
  
  Start: Timecode
  
  StartNanos: int
   
  Stereo3DModeOverride:  Stereo3DOutputMode
  
  StretchToFill:  bool
  
  TemplateID: int
  
  UseChannelMapping:  bool
  
  UseProjectRotation:   bool
  
  UseSelection: bool
  
  WaitForIdle: bool
  
  
class RenderStatus(Enum):
  """ 
  Enumeration of return values for render commands.
  enum RenderStatus, values: Canceled (5), Complete (4), Failed (6), NothingToDo (1), Queued (0), Quit (7), Rendering (2), Stitching (3), Unknown (-1)
  
   """

  Canceled = None
  Complete = None
  Failed = None
  NothingToDo = None
  Queued = None
  Quit = None
  Rendering = None
  Stitching = None
  Unknown = None

class RenderStatusEventArgs(EventArgs):
  """ Arguments provided to RenderFinished and RenderProgress event handlers.
  RenderStatusEventArgs(status: RenderStatus)
   """

  Empty = None
  ErrorMessage = None
  PercentComplete = None

  def ReferenceEquals(objA: object, objB: object) -> bool:
    """ ReferenceEquals(objA: object, objB: object) -> bool
     """
    return None

  Result = None

  def ResultDescription(self):
    """ ResultDescription(self: RenderStatusEventArgs) -> str
     """
    import System
    return System.String()

  Status = None

class RenderStatusEventHandler(MulticastDelegate):
  """ RenderStatusEventHandler(object: object, method: IntPtr)
   """

  def BeginInvoke(self, sender, args, callback, object):
    """ BeginInvoke(self: RenderStatusEventHandler, sender: object, args: RenderStatusEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult
     """
    import System
    return System.IAsyncResult()

  def Combine(self, arg0, arg1):
    """ Combine(a: Delegate, b: Delegate) -> Delegate
    Combine(*delegates: Array[Delegate]) -> Delegate
     """
    return None

  def CreateDelegate(self, arg0, arg1, arg2):
    """ CreateDelegate(type: Type, target: object, method: str) -> Delegate
    CreateDelegate(type: Type, target: object, method: str, ignoreCase: bool) -> Delegate
    CreateDelegate(type: Type, target: object, method: str, ignoreCase: bool, throwOnBindFailure: bool) -> Delegate
    CreateDelegate(type: Type, target: Type, method: str) -> Delegate
    CreateDelegate(type: Type, target: Type, method: str, ignoreCase: bool) -> Delegate
    CreateDelegate(type: Type, target: Type, method: str, ignoreCase: bool, throwOnBindFailure: bool) -> Delegate
    CreateDelegate(type: Type, method: MethodInfo, throwOnBindFailure: bool) -> Delegate
    CreateDelegate(type: Type, firstArgument: object, method: MethodInfo) -> Delegate
    CreateDelegate(type: Type, firstArgument: object, method: MethodInfo, throwOnBindFailure: bool) -> Delegate
    CreateDelegate(type: Type, method: MethodInfo) -> Delegate
     """
    return None

  def EndInvoke(self, result):
    """ EndInvoke(self: RenderStatusEventHandler, result: IAsyncResult) """
    import System
    return System.Void()

  def Invoke(self, sender, args):
    """ Invoke(self: RenderStatusEventHandler, sender: object, args: RenderStatusEventArgs) """
    import System
    return System.Void()

  def ReferenceEquals(objA: object, objB: object) -> bool:
    """ ReferenceEquals(objA: object, objB: object) -> bool
     """
    return None

  def Remove(self, arg0, arg1):
    """ Remove(source: Delegate, value: Delegate) -> Delegate
     """
    return None

  def RemoveAll(self, arg0, arg1):
    """ RemoveAll(source: Delegate, value: Delegate) -> Delegate
     """
    return None

class RenderTemplate(object):
  """ Represents a render template.
  
  RenderTemplate(rCOM: IRendererCOM, rendererID: int, templateID: int)
  RenderTemplate(rCOM: IRendererCOM, rendererID: int, templateData: Array[Byte])
   """

  AudioBitrate:  int
  
  AudioBitsPerSample: int
  
  AudioChannelCount: int
  
  AudioChannelFlags: AudioChannelFlags_
 
  AudioSampleRate: int
   
  AudioStreamCount:  int
   
  Description: str
   
  FileExtensions: Array[str]
  
  def GetAVInfo(self: RenderTemplate, infoList: FormatInfoList) -> int:
    """ GetAVInfo(self: RenderTemplate, infoList: FormatInfoList) -> int
     """
    import System
    return System.int()

  def GetStatusForContext(self: RenderTemplate, videoStreams: int, surroundEnabled: bool, allowMultiFile: bool, mappingEnabled: bool, mappedChannels: int) -> RenderTemplateStatus:
    """ GetStatusForContext(self: RenderTemplate, videoStreams: int, surroundEnabled: bool, allowMultiFile: bool, mappingEnabled: bool, mappedChannels: int) -> RenderTemplateStatus
     """
    import ScriptPortal.Vegas
    return ScriptPortal.Vegas.RenderTemplateStatus()

  def GetTemplateData(self: RenderTemplate) -> Array[Byte]:
    """ GetTemplateData(self: RenderTemplate) -> Array[Byte] """
    import System
    return System.Byte[]()

  Index:  int
 

  def IsValid(self: RenderTemplate) -> bool:
    """ IsValid(self: RenderTemplate) -> bool
     """
    import System
    return System.Boolean()

  Name: str
  

  Notes: str
   

  TemplateGuid:   Guid
  
  
  TotalBitrate:  int
   

  VideoBitrate: int
   

  VideoDataRate:  int
  

  VideoFieldOrder: VideoFieldOrder_
   
  VideoFrameRate:  float
  

  VideoHeight: int
  

  VideoPixelAspectRatio: float
  
  VideoStreamCount:  int
   
  VideoWidth:  int
  
class RenderTemplateStatus(Enum):
  """ 
  
  enum RenderTemplateStatus, values: INVALID (2147483647), INVALID_24P (1), INVALID_AUDIO_RATE (4), INVALID_FRAME_SIZE (3), INVALID_IN_SURROUND_MODE (10), INVALID_MULTICHANNEL (9), INVALID_MULTISTREAM_MONO (6), INVALID_MULTISTREAM_TAKE (5), INVALID_NO_VIDEO (7), INVALID_NON_STEREO_IN_STEREO_MODE (8), INVALID_S3D (12), INVALID_SURROUND (2), INVALID_VERSION (11), OK (0)
  
   """

  INVALID = None
  INVALID_24P = None
  INVALID_AUDIO_RATE = None
  INVALID_FRAME_SIZE = None
  INVALID_IN_SURROUND_MODE = None
  INVALID_MULTICHANNEL = None
  INVALID_MULTISTREAM_MONO = None
  INVALID_MULTISTREAM_TAKE = None
  INVALID_NON_STEREO_IN_STEREO_MODE = None
  INVALID_NO_VIDEO = None
  INVALID_S3D = None
  INVALID_SURROUND = None
  INVALID_VERSION = None
  OK = None


class RenderTemplates(BaseList[RenderTemplate]):
  """ Collection of templates for a render plug-in.  """

  def BaseIndex(self, arg0, arg1):
    """ BaseIndex(self: RenderTemplates, item: RenderTemplate) -> int
     """
    return 1

  def FindByGuid(self, presetGUID):
    """ FindByGuid(self: RenderTemplates, presetGUID: Guid) -> RenderTemplate
     """
    import ScriptPortal.Vegas
    return ScriptPortal.Vegas.RenderTemplate()

  def FindByName(self, templateName):
    """ FindByName(self: RenderTemplates, templateName: str) -> RenderTemplate
     """
    import ScriptPortal.Vegas
    return ScriptPortal.Vegas.RenderTemplate()

  def FindProjectMatches(self, project):
    """ FindProjectMatches(self: RenderTemplates, project: Project) -> Array[RenderTemplate]
     """
    import ScriptPortal.Vegas
    return ScriptPortal.Vegas.RenderTemplate[]()

  def GetCount(self, arg0):
    """ GetCount(self: RenderTemplates) -> int
     """
    return 1

  def GetItem(self, arg0, arg1):
    """ GetItem(self: RenderTemplates, index: int) -> RenderTemplate
     """
    return None

  IsFixedSize:  bool
  
  IsReadOnly:  bool
  
  def ReferenceEquals(objA: object, objB: object) -> bool:
    """ ReferenceEquals(objA: object, objB: object) -> bool
     """
    return None

  def Refresh(self):
    """ Refresh(self: RenderTemplates) """
    import System
    return System.Void()

class Renderer(object):
  """ Represents a render plug-in. """

  CLSID_CSfAC3RenderFileClass = None
  CLSID_CSfAC3StudioRenderFileClass = None
  CLSID_CSfAIFRenderFileClass = None
  CLSID_CSfAVIRenderFileClass = None
  CLSID_CSfFLACRenderFileClass = None
  CLSID_CSfMCMP4RenderFileClass = None
  CLSID_CSfMCMP4RenderFileClass_2 = None
  CLSID_CSfMCMP4RenderFileClass_XAVCS = None
  CLSID_CSfMCMPEG1RenderFileClass = None
  CLSID_CSfMCMPEG4RenderFileClass = None
  CLSID_CSfMP4v2RenderFileClass = None
  CLSID_CSfMP4v3RenderFileClass = None
  CLSID_CSfMXFDVRenderFileClass = None
  CLSID_CSfMXFHDCAMSRRenderFileClass = None
  CLSID_CSfMXFRenderFileClass_P2 = None
  CLSID_CSfMXFRenderFileClass_XAVC = None
  CLSID_CSfMxHEVCAACMP4RenderFileClass = None
  CLSID_CSfPCARenderFileClass = None
  CLSID_CSfQT4RenderFileClass = None
  CLSID_CSfQT5RenderFileClass = None
  CLSID_CSfQT6RenderFileClass = None
  CLSID_CSfQT7RenderFileClass = None
  CLSID_CSfRM9RenderFileClass = None
  CLSID_CSfScottRenderFileClass = None
  CLSID_CSfWICRenderFileClass = None
  CLSID_CSfWMFRenderFileClassWMV = None
  CLSID_CSfWMFRenderFileClassWMV_V11 = None
  CLSID_CSfWMFRenderFileClassWMV_V9 = None
  CLSID_SfW64ReaderClass = None
  CLSID_SfWaveRenderClass = None
  CanEditTemplates: bool
  ClassID: = Guid
  

  def CreateInstance(self, project, classID):
    """ CreateInstance(project: Project, classID: Guid) -> Renderer
    CreateInstance(classID: Guid) -> Renderer
     """
    import ScriptPortal.Vegas
    return ScriptPortal.Vegas.Renderer()

  def CreateRenderTemplate(self, templateData):
    """ CreateRenderTemplate(self: Renderer, templateData: Array[Byte]) -> RenderTemplate
    CreateRenderTemplate(self: Renderer, templateID: int) -> RenderTemplate
     """
    import ScriptPortal.Vegas
    return ScriptPortal.Vegas.RenderTemplate()

  FileExtension: str
  
  FileExtensions:Array[str]
   
  FileTypeName:  str
  

  def GetDefaultRenderClassID(templateMRU: int, hasVideo: bool) -> Guid:
    """ GetDefaultRenderClassID(templateMRU: int, hasVideo: bool) -> Guid
     """
    import System
    return System.Guid()

  HasAboutBox:  bool

  HasReader: bool
  
  IsActive: bool
  
  Name:  str
   
  def ReferenceEquals(objA: object, objB: object) -> bool:
    """ ReferenceEquals(objA: object, objB: object) -> bool
     """
    return None

  def ShowAboutBox(self, hwndOwner):
    """ ShowAboutBox(self: Renderer, hwndOwner: IntPtr) """
    import System
    return System.Void()

  SupportsAudio:  bool
  
  SupportsCommands: bool


  SupportsLinkedProject:  bool
  
  SupportsMarkers: bool
   
  SupportsMultichannel:   bool
  
  SupportsMultistream:   bool
  
  SupportsVideo:  bool
 
  TEMPLATE_MRU_BDBurnAudio = 8
  TEMPLATE_MRU_BDBurnVideo = 9
  TEMPLATE_MRU_DAOBurn = 12
  TEMPLATE_MRU_MultimediaCD = 11
  TEMPLATE_MRU_NRTFX = 5
  TEMPLATE_MRU_PreRenderVideo = 4
  TEMPLATE_MRU_PrintToTape = 10
  TEMPLATE_MRU_RenderAs = 1
  TEMPLATE_MRU_RenderToNewTrack = 2

  def TemplateCount(self):
    """ TemplateCount(self: Renderer) -> int
     """
    import System
    return System.int()

  Templates:  RenderTemplates
  

  def ToString(self):
    """ ToString(self: Renderer) -> str
     """
    import System
    return System.String()

class Renderers(BaseList[Renderer]):
  """ Collection of render plug-ins. """

  def FindByClassID(self, classID):
    """ FindByClassID(self: Renderers, classID: Guid) -> Renderer
     """
    import ScriptPortal.Vegas
    return ScriptPortal.Vegas.Renderer()

  def FindByName(self, rendererName):
    """ FindByName(self: Renderers, rendererName: str) -> Renderer
     """
    import ScriptPortal.Vegas
    return ScriptPortal.Vegas.Renderer()

  def FindByRendererID(self, rendererID):
    """ FindByRendererID(self: Renderers, rendererID: int) -> Renderer
     """
    import ScriptPortal.Vegas
    return ScriptPortal.Vegas.Renderer()

  def GetCount(self, arg0):
    """ GetCount(self: Renderers) -> int
     """
    return 1

  def GetItem(self, arg0, arg1):
    """ GetItem(self: Renderers, index: int) -> Renderer
     """
    return None

  IsFixedSize:   bool
   

  IsReadOnly:  bool
  

  def ReferenceEquals(objA: object, objB: object) -> bool:
    """ ReferenceEquals(objA: object, objB: object) -> bool
     """
    return None

class RulerFormat(Enum):
  """ 
  Enumeration of ruler formats.
  enum RulerFormat, values: AbsoluteFrames (5), AudioCDTime (15), FeetAndFrames16mm (7), FeetAndFrames35mm (8), MeasuresAndBeats (6), Microseconds (17), Nanoseconds (16), Samples (1), Seconds (3), Smpte30 (14), SmpteDrop (13), SmpteEBU (11), SmpteFilmSync (10), SmpteFilmSyncIVTC (9), SmpteNonDrop (12), Time (2), TimeAndFrames (4), Unknown (0)
  
   """

  AbsoluteFrames = None
  AudioCDTime = None
  FeetAndFrames16mm = None
  FeetAndFrames35mm = None
  MeasuresAndBeats = None
  Microseconds = None
  Nanoseconds = None
  Samples = None
  Seconds = None
  Smpte30 = None
  SmpteDrop = None
  SmpteEBU = None
  SmpteFilmSync = None
  SmpteFilmSyncIVTC = None
  SmpteNonDrop = None
  Time = None
  TimeAndFrames = None
  Unknown = None

class RulerProperties(object):
  """ Represents a project's ruler properties. """

  BeatValue: BeatValue_
  

  BeatsPerMeasure: int
  

  BeatsPerMinute:  float
  

  Format: RulerFormat
                    
                    

  def ReferenceEquals(objA: object, objB: object) -> bool:
    """ ReferenceEquals(objA: object, objB: object) -> bool
     """
    return None

  StartTime:   Timecode
   


class Script(object):
  """ Script()
   """

  Application: Vegas
  
  Args: ScriptArgs
  
  Directory: str
  
  File: str
  
  Name: str
  
  RawArgs: str
  
  def ReferenceEquals(objA: object, objB: object) -> bool:
    """ ReferenceEquals(objA: object, objB: object) -> bool
     """
    return None

  Settings:  XmlDocument
  
  
class ScriptArg(object):
  """ ScriptArg()
  ScriptArg(szArg: str)
   """

  InvalidCharacters = None

  def IsValidNameString(self, val):
    """ IsValidNameString(val: str) -> bool
     """
    import System
    return System.Boolean()

  def IsValidValueString(self, val):
    """ IsValidValueString(val: str) -> bool
     """
    import System
    return System.Boolean()

  Name = None

  def ReferenceEquals(objA: object, objB: object) -> bool:
    """ ReferenceEquals(objA: object, objB: object) -> bool
     """
    return None

  SeparatorCharacters = None

  def ToString(self):
    """ ToString(self: ScriptArg) -> str
     """
    import System
    return System.String()

  Value = None

class ScriptArgs(CollectionBase):
  """ ScriptArgs()
   """

  def Add(self: ScriptArgs, aArg: ScriptArg):
    """ Add(self: ScriptArgs, aArg: ScriptArg) """
    import System
    return System.Void()

  def AsBool(self: ScriptArgs, sKey: str) -> bool:
    """ AsBool(self: ScriptArgs, sKey: str) -> bool
     """
    import System
    return System.Boolean()

  def AsInt(self: ScriptArgs, sKey: str, iDefault: int) -> int:
    """ AsInt(self: ScriptArgs, sKey: str, iDefault: int) -> int
    AsInt(self: ScriptArgs, sKey: str) -> int
     """
    import System
    return System.int()

  def Asint(self: ScriptArgs, sKey: str, llDefault: int) -> int:
    """ Asint(self: ScriptArgs, sKey: str, llDefault: int) -> int
    Asint(self: ScriptArgs, sKey: str) -> int
     """
    import System
    return System.int()

  def AsTimecode(self: ScriptArgs, sKey: str, tcDefault: Timecode, fmt: RulerFormat) -> Timecode:
    """ AsTimecode(self: ScriptArgs, sKey: str, tcDefault: Timecode, fmt: RulerFormat) -> Timecode
    AsTimecode(self: ScriptArgs, sKey: str, tcDefault: Timecode) -> Timecode
    AsTimecode(self: ScriptArgs, sKey: str) -> Timecode
     """
    import ScriptPortal.Vegas
    return ScriptPortal.Vegas.Timecode()

  def Exists(self: ScriptArgs, sKey: str) -> bool:
    """ Exists(self: ScriptArgs, sKey: str) -> bool
    Exists(self: ScriptArgs, sKey: str, fIgnoreCase: bool) -> bool
     """
    import System
    return System.Boolean()

  def InitFromXml(self: ScriptArgs, rootNode: XmlNode) :
    """ InitFromXml(self: ScriptArgs, rootNode: XmlNode) """
    import System
    return System.Void()

  Item = None

  def ReferenceEquals(objA: object, objB: object) -> bool:
    """ ReferenceEquals(objA: object, objB: object) -> bool
     """
    return None

  def Remove(self, index):
    """ Remove(self: ScriptArgs, index: int) """
    import System
    return System.Void()

  SeparatorCharacters = None

  def ToString(self):
    """ ToString(self: ScriptArgs) -> str
     """
    import System
    return System.String()

  def ValueOf(self, sKey):
    """ ValueOf(self: ScriptArgs, sKey: str) -> str
    ValueOf(self: ScriptArgs, sKey: str, fIgnoreCase: bool) -> str
     """
    import System
    return System.String()

class ScriptEngineType(Enum):
  """ 
  
  enum ScriptEngineType, values: CSharp (1), JScript (2), JScript_VSA (5), Precompiled (4), Unknown (0), VBScript (3), VBScript_VSA (6)
  
   """

  CSharp = None
  JScript = None
  JScript_VSA = None
  Precompiled = None
  Unknown = None
  VBScript = None
  VBScript_VSA = None
  

class ScriptExitFlags(Enum):
  """ 
  
  enum (flags) ScriptExitFlags, values: All (7), ExitApplication (4), None (0), ResumePlayback (2), UnloadScriptDomain (1)
  
   """

  All = None
  ExitApplication = None
  None_ = None
  ResumePlayback = None
  UnloadScriptDomain = None
  
class ScriptHost(object):
  """ ScriptHost()
   """

  class AppDirAssemblyReferenceResolver(AssemblyReferenceResolver):
    """ AppDirAssemblyReferenceResolver()
     """

    def ReferenceEquals(objA: object, objB: object) -> bool:
      """ ReferenceEquals(objA: object, objB: object) -> bool
       """
      return None

  class AssemblyReferenceResolver(object):
    """ AssemblyReferenceResolver()
     """

    def ReferenceEquals(objA: object, objB: object) -> bool:
      """ ReferenceEquals(objA: object, objB: object) -> bool
       """
      return None

  class CodeDomScriptManager(ScriptManager):
    """ CodeDomScriptManager(host: ScriptHost, hasFallback: bool)
    CodeDomScriptManager(host: ScriptHost)
     """

    DefaultMainClassName = 'EntryPoint'
    DefaultMainMethodName = 'FromVegas'

    def Dispose(self):
      """ Dispose(self: CodeDomScriptManager, disposing: bool) """
      import System
      return System.Void()

    def ReferenceEquals(objA: object, objB: object) -> bool:
      """ ReferenceEquals(objA: object, objB: object) -> bool
       """
      return None

    disposed = None
    myAssemblyReferences = None
    myHost = None

  class CompilationException(ApplicationException):
    """ CompilationException(msg: str)
     """

    def ReferenceEquals(objA: object, objB: object) -> bool:
      """ ReferenceEquals(objA: object, objB: object) -> bool
       """
      return None

    SerializeObjectState = None

  def FireEvent(self, id, comArgs):
    """ FireEvent(self: ScriptHost, id: VegasEventID, comArgs: object) """
    import System
    return System.Void()

  def FixUpLocalAsmPath(self, arg0, arg1):
    """ FixUpLocalAsmPath(self: ScriptHost, assemblyName: str) -> str
     """
    return ""

  GenerateDebugInfo = None

  def HandleAssemblyResolve(self, arg0, arg1, arg2):
    """ HandleAssemblyResolve(self: ScriptHost, sender: object, args: ResolveEventArgs) -> Assembly
     """
    return None

  def Initialize(self, vegasCOM, hwndVegas, hwndExternNotify):
    """ Initialize(self: ScriptHost, vegasCOM: object, hwndVegas: IntPtr, hwndExternNotify: IntPtr) """
    import System
    return System.Void()

  class JScriptManager(VSAManager):
    """ JScriptManager(host: ScriptHost)
     """

    def AddGlobalVariables(self, arg0):
      """ AddGlobalVariables(self: JScriptManager) """
      pass

    DefaultMainClassName = 'EntryPoint'
    DefaultMainMethodName = 'FromVegas'

    def Dispose(self):
      """ Dispose(self: JScriptManager, disposing: bool) """
      import System
      return System.Void()

    def ReferenceEquals(objA: object, objB: object) -> bool:
      """ ReferenceEquals(objA: object, objB: object) -> bool
       """
      return None

    disposed = None

  class LocalAssemblyReferenceResolver(AssemblyReferenceResolver):
    """ LocalAssemblyReferenceResolver(scriptFile: str)
     """

    def ReferenceEquals(objA: object, objB: object) -> bool:
      """ ReferenceEquals(objA: object, objB: object) -> bool
       """
      return None



  class PrecompiledScriptManager(ScriptManager):
    """ PrecompiledScriptManager(host: ScriptHost)
     """

    DefaultMainClassName = 'EntryPoint'
    DefaultMainMethodName = 'FromVegas'

    def ReferenceEquals(objA: object, objB: object) -> bool:
      """ ReferenceEquals(objA: object, objB: object) -> bool
       """
      return None

    disposed = None
 

  def ReferenceEquals(objA: object, objB: object) -> bool:
    """ ReferenceEquals(objA: object, objB: object) -> bool
     """
    return None

  def RunScriptData(self, cmdElt):
    """ RunScriptData(self: ScriptHost, cmdElt: XmlElement) """
    import System
    return System.Void()

  def RunScriptFile(self, szScriptFile, szArgs):
    """ RunScriptFile(self: ScriptHost, szScriptFile: str, szArgs: str) """
    import System
    return System.Void()

  def RunScriptText(self, szScriptText, eType, fCompileOnly, szArgs):
    """ RunScriptText(self: ScriptHost, szScriptText: str, eType: ScriptEngineType, fCompileOnly: bool, szArgs: str) """
    import System
    return System.Void()

  ScriptArgs: object =

  ScriptFile: object
  


  class ScriptManager(object):
    """ ScriptManager(host: ScriptHost)
     """

    DefaultMainClassName = 'EntryPoint'
    DefaultMainMethodName = 'FromVegas'

    def ReferenceEquals(objA: object, objB: object) -> bool:
      """ ReferenceEquals(objA: object, objB: object) -> bool
       """
      return None

    def Run(self):
      """ Run(self: ScriptManager, asm: Assembly, className: str, methodName: str) """
      import System
      return System.Void()

    disposed = None

  def SetCommonScriptOptions(self, arg0, arg1):
    """ SetCommonScriptOptions(self: ScriptHost, settings: XmlElement) """
    pass

  class SfVsaSite(BaseVsaSite):
    """  """

    def ReferenceEquals(objA: object, objB: object) -> bool:
      """ ReferenceEquals(objA: object, objB: object) -> bool
       """
      return None

  UseCodeDomCompiler = None

  class VSAManager(ScriptManager):
    """ VSAManager(host: ScriptHost)
     """

    def AddGlobalObject(self, arg0, arg1, arg2, arg3):
      """ AddGlobalObject(self: VSAManager, name: str, type: str, obj: object) """
      pass

    def AddGlobalVariables(self, arg0):
      """ AddGlobalVariables(self: VSAManager) """
      pass

    DefaultMainClassName = 'EntryPoint'
    DefaultMainMethodName = 'FromVegas'

    def Dispose(self):
      """ Dispose(self: VSAManager, disposing: bool) """
      import System
      return System.Void()

    def ReferenceEquals(objA: object, objB: object) -> bool:
      """ ReferenceEquals(objA: object, objB: object) -> bool
       """
      return None

    disposed = None
    myAssemblyReferences = None
    myHost = None
    myVsaEngine = None
    myVsaSite = None

class SelPastAttrConfig(object):
  """ SelPastAttrConfig()
   """

  def AddItem(self: SelPastAttrConfig, isOn: bool, index: int, name: str):
    """ AddItem(self: SelPastAttrConfig, isOn: bool, index: int, name: str) """
    import System
    return System.Void()

  CancelDlg: bool
  
  def ClearItems(self):
    """ ClearItems(self: SelPastAttrConfig) """
    import System
    return System.Void()

  Description:  str
  
  def GetCount(self, count):
    """ GetCount(self: SelPastAttrConfig) -> int
     """
    import System
    return System.Void()

  def GetItem(self, index, isOn):
    """ GetItem(self: SelPastAttrConfig, index: int) -> bool
     """
    import System
    return System.Void()

  def GetItemByIndex(self, index, isOn):
    """ GetItemByIndex(self: SelPastAttrConfig, index: int) -> bool
     """
    import System
    return System.Void()

  def GetItems(self):
    """ GetItems(self: SelPastAttrConfig) -> Dictionary[int, bool]
     """
    import System.Collections.Generic
    return System.Collections.Generic.Dictionary`2()

  def GetNames(self):
    """ GetNames(self: SelPastAttrConfig) -> Dictionary[int, str]
     """
    import System.Collections.Generic
    return System.Collections.Generic.Dictionary`2()

  def ReferenceEquals(objA: object, objB: object) -> bool:
    """ ReferenceEquals(objA: object, objB: object) -> bool
     """
    return None

  def SetItem(self, index, set):
    """ SetItem(self: SelPastAttrConfig, index: int, set: bool) """
    import System
    return System.Void()

  Title:   str


class SettingsPathID(Enum):
  """ 
  
  enum SettingsPathID, values: Capture (1), ProxySwap (3), RenderAs (2), Unknown (0)
  
   """

  Capture = None
  ProxySwap = None
  RenderAs = None
  Unknown = None
 
class ShowDialogOption(Enum):
  """ 
  
  enum ShowDialogOption, values: Always (1), Default (0), Never (2)
  
   """

  Always = None
  Default = None
  Never = None


class SpecialPrefsPathID(Enum):
  """ 
  
  enum SpecialPrefsPathID, values: PublishToYouTubePrefsPath (0), SlideshowCreatorPrefsPath (1)
  
   """

  PublishToYouTubePrefsPath = None
  SlideshowCreatorPrefsPath = None

class StatusLogEventArgs(EventArgs):
  """  """

  Empty = None
  Message = None

  def ReferenceEquals(objA: object, objB: object) -> bool:
    """ ReferenceEquals(objA: object, objB: object) -> bool
     """
    return None

class StatusLogEventHandler(MulticastDelegate):
  """ StatusLogEventHandler(object: object, method: IntPtr)
   """

  def BeginInvoke(self, sender, args, callback, object):
    """ BeginInvoke(self: StatusLogEventHandler, sender: object, args: StatusLogEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult
     """
    import System
    return System.IAsyncResult()

  def Combine(self, arg0, arg1):
    """ Combine(a: Delegate, b: Delegate) -> Delegate
    Combine(*delegates: Array[Delegate]) -> Delegate
     """
    return None

  def CreateDelegate(self, arg0, arg1, arg2):
    """ CreateDelegate(type: Type, target: object, method: str) -> Delegate
    CreateDelegate(type: Type, target: object, method: str, ignoreCase: bool) -> Delegate
    CreateDelegate(type: Type, target: object, method: str, ignoreCase: bool, throwOnBindFailure: bool) -> Delegate
    CreateDelegate(type: Type, target: Type, method: str) -> Delegate
    CreateDelegate(type: Type, target: Type, method: str, ignoreCase: bool) -> Delegate
    CreateDelegate(type: Type, target: Type, method: str, ignoreCase: bool, throwOnBindFailure: bool) -> Delegate
    CreateDelegate(type: Type, method: MethodInfo, throwOnBindFailure: bool) -> Delegate
    CreateDelegate(type: Type, firstArgument: object, method: MethodInfo) -> Delegate
    CreateDelegate(type: Type, firstArgument: object, method: MethodInfo, throwOnBindFailure: bool) -> Delegate
    CreateDelegate(type: Type, method: MethodInfo) -> Delegate
     """
    return None

  def EndInvoke(self, result):
    """ EndInvoke(self: StatusLogEventHandler, result: IAsyncResult) """
    import System
    return System.Void()

  def Invoke(self, sender, args):
    """ Invoke(self: StatusLogEventHandler, sender: object, args: StatusLogEventArgs) """
    import System
    return System.Void()

  def ReferenceEquals(objA: object, objB: object) -> bool:
    """ ReferenceEquals(objA: object, objB: object) -> bool
     """
    return None

  def Remove(self, arg0, arg1):
    """ Remove(source: Delegate, value: Delegate) -> Delegate
     """
    return None

  def RemoveAll(self, arg0, arg1):
    """ RemoveAll(source: Delegate, value: Delegate) -> Delegate
     """
    return None

class Stereo3DInputMode(Enum):
  """ 
  Enumeration of stereoscopic 3D input modes.
  enum Stereo3DInputMode, values: LineAlternate (6), Off (0), PairWithNextStream (1), SideBySideFull (3), SideBySideHalf (2), TopBottomFull (5), TopBottomHalf (4)
  
   """
  LineAlternate = None
  Off = None
  PairWithNextStream = None
  SideBySideFull = None
  SideBySideHalf = None
  TopBottomFull = None
  TopBottomHalf = None

class Stereo3DOutputMode(Enum):
  """ 
  Enumeration of stereoscopic 3D output modes.
  enum Stereo3DOutputMode, values: AnaglyphicAmberBlue (6), AnaglyphicGreenMagenta (7), AnaglyphicRedCyan (5), Blend (12), Checkerboard (9), Difference (13), LeftAndRight (14), LeftOnly (10), LineAlternate (8), Off (0), RightOnly (11), SideBySideFull (2), SideBySideHalf (1), TopBottomFull (4), TopBottomHalf (3)
  
   """

  AnaglyphicAmberBlue = None
  AnaglyphicGreenMagenta = None
  AnaglyphicRedCyan = None
  Blend = None
  Checkerboard = None
  Difference = None
  LeftAndRight = None
  LeftOnly = None
  LineAlternate = None
  Off = None
  RightOnly = None
  SideBySideFull = None
  SideBySideHalf = None
  TopBottomFull = None
  TopBottomHalf = None


class StreamType(Enum):
  """ 
  
  enum (flags) StreamType, values: Audio (1), DV (8), Midi (4), Text (8), Unknown (0), VegEDL (32), VegPrj (16), Video (2)
  
   """

  Audio = None
  DV = None
  Midi = None
  Text = None
  Unknown = None
  VegEDL = None
  VegPrj = None
  Video = None

class StringListSetting(ListSetting[str]):
  """ StringListSetting(name: str)
   """

  def ItemFromString(self, arg0, arg1):
    """ ItemFromString(self: StringListSetting, s: str) -> str
     """
    return ""

  def ItemToString(self, arg0, arg1):
    """ ItemToString(self: StringListSetting, item: str) -> str
     """
    return ""

  Name = None

  def ReferenceEquals(objA: object, objB: object) -> bool:
    """ ReferenceEquals(objA: object, objB: object) -> bool
     """
    return None

  Value = None

class StringSetting(XmlSetting):
  """ StringSetting(name: str, val: str)
   """

  def FromString(self, value):
    """ FromString(self: StringSetting, value: str) """
    import System
    return System.Void()

  Name = None

  def ReferenceEquals(objA: object, objB: object) -> bool:
    """ ReferenceEquals(objA: object, objB: object) -> bool
     """
    return None

  def ToString(self):
    """ ToString(self: StringSetting) -> str
     """
    import System
    return System.String()

  Value = None

class Subclip(Media_):
  """ Represents a subclip of a media file.
  Subclip(project: Project, path: str, start: Timecode, length: Timecode, reverse: bool, displayName: str)
  Subclip(path: str, start: Timecode, length: Timecode, reverse: bool, displayName: str)
   """

  def CreateInstance(self, arg0, arg1):
    """ CreateInstance(project: Project, path: str) -> Media
    CreateInstance(project: Project, generator: PlugInNode, presetName: str) -> Media
    CreateInstance(project: Project, generator: PlugInNode) -> Media
     """
    return None

  def Equals(self, obj):
    """ Equals(self: Subclip, obj: object) -> bool
     """
    import System
    return System.Boolean()

  def GetHashCode(self):
    """ GetHashCode(self: Subclip) -> int
     """
    import System
    return System.int()

  IsReversed: bool
  
  MEDIA_FLAG_CUSTOM_OFFSET = None
  ParentMedia:  Media_
  
  def ReferenceEquals(objA: object, objB: object) -> bool:
    """ ReferenceEquals(objA: object, objB: object) -> bool
     """
    return None

  SourceUMIDCustomDataID = None
  Start: Timecode


class SummaryProperties(object):
  """ Represents a project's summary properties. """

  Artist = str
   
  Comments:  str
  
  Copyright:   str
   
  Engineer:  str
  
  def FindFourCC(label: str, ignoreCase: bool) -> FourCC:
    """ FindFourCC(label: str, ignoreCase: bool) -> FourCC
    FindFourCC(strLabel: str) -> FourCC
     """
    import ScriptPortal.Vegas
    return ScriptPortal.Vegas.FourCC()

  class FourCC(Enum):
    """ 
    
    enum FourCC, values: APIC (1128878145), CMNT (1414417731), COMM (1296912195), DISP (1347635524), DTIM (1296651332), IARL (1280459081), IART (1414676809), ICMS (1397572425), ICMT (1414349641), ICOP (1347371849), ICRD (1146241865), ICRP (1347568457), IDIM (1296647241), IDIT (1414087753), IDPI (1229997129), IDVD (1146504265), IENG (1196311881), IGNR (1380861769), IKEY (1497713481), ILGT (1413958729), IMED (1145392457), INAM (1296125513), IPLT (1414287433), IPRD (1146245193), ISBJ (1245860681), ISFT (1413894985), ISFV (1447449417), ISHP (1346917193), ISMP (1347244873), ISRC (1129468745), ISRF (1179800393), ITCH (1212372041), LOCA (1094930252), MCDI (1229210445), MRAT (1413567053), MTIX (1481200717), PCNT (1414415184), POPM (1297108816), PVCR (1380144720), PVDR (1380210256), PVRT (1414682192), PVST (1414747728), RATE (1163149650), STAT (1413567571), SYLT (1414289747), TALB (1112293716), TAPE (1162887508), TBPM (1297105492), TCDO (1329873748), TCOD (1146045268), TCOM (1297040212), TCON (1313817428), TCOP (1347371860), TDEN (1313162324), TDIR (1380533332), TDLY (1498170452), TDOR (1380926548), TDRC (1129464916), TDRL (1280459860), TDTG (1196704852), TENC (1129203028), TEXT (1415071060), TFLT (1414284884), The (6645844), TIPL (1280330068), TIT1 (827607380), TIT2 (844384596), TIT3 (861161812), TKEY (1497713492), TLAN (1312902228), TLEN (1313164372), TMCL (1279479124), TMED (1145392468), TMOO (1330597204), TOAL (1279348564), TOBD (1145196372), TOFN (1313230676), TOLY (1498173268), TOPE (1162891092), TORG (1196576596), TOWN (1314344788), TPE1 (826626132), TPE2 (843403348), TPE3 (860180564), TPE4 (876957780), TPER (1380274260), TPOS (1397706836), TPRO (1330794580), TPUB (1112887380), TRCK (1262703188), TRSN (1314083412), TRSO (1330860628), TSOA (1095717716), TSOP (1347375956), TSOT (1414484820), TSRC (1129468756), TSSE (1163088724), TSST (1414746964), TTOR (1380930644), TURL (1280464212), TVCH (1212372564), TVCS (1396921940), TVER (1380275796), TVNA (1095652948), TVNM (1296979540), TXXX (1482184788), UFID (1145652821), USER (1380275029), USLT (1414288213), VCHP (1346913110), VMAJ (1245793622), VMIN (1313426774), VREA (1095062102), WCOM (1297040215), WCOP (1347371863), WOAF (1178685271), WOAR (1380011863), WOAS (1396789079), WORS (1397903191), WPAY (1497452631), WPUB (1112887383), WXXX (1482184791)
    
     """

    APIC = None
    CMNT = None
    COMM = None
    DISP = None
    DTIM = None
    IARL = None
    IART = None
    ICMS = None
    ICMT = None
    ICOP = None
    ICRD = None
    ICRP = None
    IDIM = None
    IDIT = None
    IDPI = None
    IDVD = None
    IENG = None
    IGNR = None
    IKEY = None
    ILGT = None
    IMED = None
    INAM = None
    IPLT = None
    IPRD = None
    ISBJ = None
    ISFT = None
    ISFV = None
    ISHP = None
    ISMP = None
    ISRC = None
    ISRF = None
    ITCH = None
    LOCA = None
    MCDI = None
    MRAT = None
    MTIX = None
    PCNT = None
    POPM = None
    PVCR = None
    PVDR = None
    PVRT = None
    PVST = None
    RATE = None
    STAT = None
    SYLT = None
    TALB = None
    TAPE = None
    TBPM = None
    TCDO = None
    TCOD = None
    TCOM = None
    TCON = None
    TCOP = None
    TDEN = None
    TDIR = None
    TDLY = None
    TDOR = None
    TDRC = None
    TDRL = None
    TDTG = None
    TENC = None
    TEXT = None
    TFLT = None
    TIPL = None
    TIT1 = None
    TIT2 = None
    TIT3 = None
    TKEY = None
    TLAN = None
    TLEN = None
    TMCL = None
    TMED = None
    TMOO = None
    TOAL = None
    TOBD = None
    TOFN = None
    TOLY = None
    TOPE = None
    TORG = None
    TOWN = None
    TPE1 = None
    TPE2 = None
    TPE3 = None
    TPE4 = None
    TPER = None
    TPOS = None
    TPRO = None
    TPUB = None
    TRCK = None
    TRSN = None
    TRSO = None
    TSOA = None
    TSOP = None
    TSOT = None
    TSRC = None
    TSSE = None
    TSST = None
    TTOR = None
    TURL = None
    TVCH = None
    TVCS = None
    TVER = None
    TVNA = None
    TVNM = None
    TXXX = None
    The = None
    UFID = None
    USER = None
    USLT = None
    VCHP = None
    VMAJ = None
    VMIN = None
    VREA = None
    WCOM = None
    WCOP = None
    WOAF = None
    WOAR = None
    WOAS = None
    WORS = None
    WPAY = None
    WPUB = None
    WXXX = None
    value__ = None

  class FourCCLabel(Enum):
    """ 
    
    enum FourCCLabel, values: Album (1129468745), AlbumArtist (826626132), AlbumCoverURL (1396789079), AlbumSortOrder (1095717716), AlbumTitle (1112293716), ArchivalLocation (1280459081), Artist (1414676809), ArtistSortOrder (1347375956), AudioFileURL (1178685271), AudioSourceURL (1396789079), AuthorURL (1380011863), BeatsPerMinute (1297105492), Comments (1414349641), CommercialURL (1297040215), Commissioned (1397572425), Composer (1297040212), Conductor (860180564), ContentGroupDescription (827607380), Copyright (1347371849), CopyrightURL (1347371863), Cropped (1347568457), Description (1245860681), DigitizationTime (1414087753), Dimensions (1296647241), Director (1380533332), DotsPerInch (1229997129), DVDID (1146504265), EncodedBy (1129203028), EncodingSettings (1163088724), EncodingTime (1313162324), Engineer (1196311881), Genre (1380861769), InitialKey (1497713492), InterpretedBy (876957780), ISRC (1129468756), Keywords (1497713481), Language (1312902228), Lightness (1413958729), Location (1094930252), Lyrics (1414288213), Lyrics_Synchronised (1414289747), MCDI (1229210445), MediaCredits (1279479124), MediaNetworkAffiliation (1095652948), MediaOriginalBroadcastDateTime (1145196372), MediaOriginalChannel (1212372564), MediaStationCallSign (1396921940), MediaStationName (1296979540), Medium (1145392457), MMThumbIndex (1481200717), ModifiedBy (1212372041), Mood (1330597204), Mp3Comments (1296912195), Mp3ContentType (1313817428), Mp3Copyright (1347371860), Mp3FileType (1414284884), Mp3InvolvedPeople (1280330068), Mp3MediaType (1145392468), Mp3PlayCounter (1414415184), Mp3Popularimeter (1297108816), Mp3RecordingTime (1129464916), Mp3ReleaseTime (1280459860), Mp3TaggingTime (1196704852), Mp3TermsOfUse (1380275029), Orchestra (843403348), Origin (1196576596), OriginalAlbumTitle (1279348564), OriginalArtist (1162891092), OriginalFilename (1313230676), OriginalLyricist (1498173268), OriginalReleaseTime (1380930644), OriginalReleaseYear (1380926548), Owner (1314344788), PaletteSetting (1414287433), ParentalRating (1346913110), ParentalRatingReason (1095062102), PartOfSet (1397706836), PaymentURL (1497452631), Period (1380274260), Picture (1128878145), PlaylistDelay (1498170452), Producer (1330794580), Product (1146245193), PromotionURL (1280464212), Provider (1380210256), ProviderCopyright (1380144720), ProviderRating (1414682192), ProviderStyle (1414747728), Publisher (1112887380), PublishersURL (1112887383), RadioStationName (1314083412), RadioStationOwner (1330860628), RadioStationURL (1397903191), Rating (1163149650), SetSubtitle (1414746964), SharedUserRating (1413567053), Sharpness (1346917193), SMPTETimeCode (1347244873), SoundSchemeTitle (1347635524), SourceForm (1179800393), SubTitle (844384596), SubTitleDescription (861161812), Text (1482184788), TextLength (1313164372), Title (1296125513), TitleSortOrder (1414484820), TitleThe (6645844), ToolName (1413894985), ToolVersion (1447449417), TrackNumber (1262703188), TrackVersion (1380275796), UniqueFileIdentifier (1145652821), UserWebURL (1482184791), VidcapComment (1414417731), VidcapEndTimecode (1329873748), VidcapMajorVersion (1245793622), VidcapMinorVersion (1313426774), VidcapRecordedDateTime (1296651332), VidcapStartTimecode (1146045268), VidcapStats (1413567571), VidcapTapeName (1162887508), Writer (1415071060), Year (1146241865)
    
     """

    Album = None
    AlbumArtist = None
    AlbumCoverURL = None
    AlbumSortOrder = None
    AlbumTitle = None
    ArchivalLocation = None
    Artist = None
    ArtistSortOrder = None
    AudioFileURL = None
    AudioSourceURL = None
    AuthorURL = None
    BeatsPerMinute = None
    Comments = None
    CommercialURL = None
    Commissioned = None
    Composer = None
    Conductor = None
    ContentGroupDescription = None
    Copyright = None
    CopyrightURL = None
    Cropped = None
    DVDID = None
    Description = None
    DigitizationTime = None
    Dimensions = None
    Director = None
    DotsPerInch = None
    EncodedBy = None
    EncodingSettings = None
    EncodingTime = None
    Engineer = None
    ISRC = None
    InitialKey = None
    InterpretedBy = None
    Keywords = None
    Language = None
    Lightness = None
    Location = None
    Lyrics = None
    Lyrics_Synchronised = None
    MCDI = None
    MMThumbIndex = None
    MediaCredits = None
    MediaNetworkAffiliation = None
    MediaOriginalBroadcastDateTime = None
    MediaOriginalChannel = None
    MediaStationCallSign = None
    MediaStationName = None
    Medium = None
    ModifiedBy = None
    Mood = None
    Mp3Comments = None
    Mp3ContentType = None
    Mp3Copyright = None
    Mp3FileType = None
    Mp3InvolvedPeople = None
    Mp3MediaType = None
    Mp3PlayCounter = None
    Mp3Popularimeter = None
    Mp3RecordingTime = None
    Mp3ReleaseTime = None
    Mp3TaggingTime = None
    Mp3TermsOfUse = None
    Orchestra = None
    Origin = None
    OriginalAlbumTitle = None
    OriginalArtist = None
    OriginalFilename = None
    OriginalLyricist = None
    OriginalReleaseTime = None
    OriginalReleaseYear = None
    Owner = None
    PaletteSetting = None
    ParentalRating = None
    ParentalRatingReason = None
    PartOfSet = None
    PaymentURL = None
    Period = None
    Picture = None
    PlaylistDelay = None
    Producer = None
    Product = None
    PromotionURL = None
    Provider = None
    ProviderCopyright = None
    ProviderRating = None
    ProviderStyle = None
    Publisher = None
    PublishersURL = None
    RadioStationName = None
    RadioStationOwner = None
    RadioStationURL = None
    Rating = None
    SMPTETimeCode = None
    SetSubtitle = None
    SharedUserRating = None
    Sharpness = None
    SoundSchemeTitle = None
    SourceForm = None
    SubTitle = None
    SubTitleDescription = None
    Text = None
    TextLength = None
    Title = None
    TitleSortOrder = None
    TitleThe = None
    ToolName = None
    ToolVersion = None
    TrackNumber = None
    TrackVersion = None
    UniqueFileIdentifier = None
    UserWebURL = None
    VidcapComment = None
    VidcapEndTimecode = None
    VidcapMajorVersion = None
    VidcapMinorVersion = None
    VidcapRecordedDateTime = None
    VidcapStartTimecode = None
    VidcapStats = None
    VidcapTapeName = None
    Writer = None
    Year = None


  def FourCCToString(fcc: FourCC) -> str:
    """ FourCCToString(fcc: FourCC) -> str
     """
    import System
    return System.String()

  def GetFourCCLabel(fcc: FourCC) -> str:
    """ GetFourCCLabel(fcc: FourCC) -> str
     """
    import System
    return System.String()

  def GetItem(self: SummaryProperties, fcc: FourCC) -> str:
    """ GetItem(self: SummaryProperties, fcc: FourCC) -> str
    GetItem(self: SummaryProperties, labelOrFcc: str) -> str
     """
    import System
    return System.String()

  def MakeFourCC(ch0: Char, ch1: Char, ch2: Char, ch3: Char) -> FourCC:
    """ MakeFourCC(ch0: Char, ch1: Char, ch2: Char, ch3: Char) -> FourCC
    MakeFourCC(strFCC: str) -> FourCC
     """
    import ScriptPortal.Vegas
    return ScriptPortal.Vegas.FourCC()

  def ReferenceEquals(objA: object, objB: object) -> bool:
    """ ReferenceEquals(objA: object, objB: object) -> bool
     """
    return None

  def SetItem(self: SummaryProperties, fcc: FourCC, value: str)SetItem(self: SummaryProperties, labelOrFcc: str, value: str) -> FourCC:
    """ SetItem(self: SummaryProperties, fcc: FourCC, value: str)SetItem(self: SummaryProperties, labelOrFcc: str, value: str) -> FourCC
     """
    import System
    return System.Void()

  Title: str


class Take_(object):
  """ Represents a take for an event.
  Take(mediaStream: MediaStream, makeActive: bool, name: str)
  Take(mediaStream: MediaStream, makeActive: bool)
  Take(mediaStream: MediaStream)
   """

  class AddParams(object):
    """ AddParams()
     """

    def ReferenceEquals(objA: object, objB: object) -> bool:
      """ ReferenceEquals(objA: object, objB: object) -> bool
       """
      return None

  AudioChannelCount: int
  
  AvailableLength: Timecode
   
  def CreateInstance(project: Project_, mediaStream: MediaStream_, makeActive: bool, name: str) -> Take:
    """ CreateInstance(project: Project, mediaStream: MediaStream, makeActive: bool, name: str) -> Take
    CreateInstance(project: Project, mediaStream: MediaStream, makeActive: bool) -> Take
    CreateInstance(project: Project, mediaStream: MediaStream) -> Take
     """
    import ScriptPortal.Vegas
    return ScriptPortal.Vegas.Take()

  def Equals(self, obj):
    """ Equals(self: Take, obj: object) -> bool
     """
    import System
    return System.Boolean()

  FirstAudioChannelIndex: int
  
  def GetHashCode(self):
    """ GetHashCode(self: Take) -> int
     """
    import System
    return System.int()

  Index: int

  IsActive: bool
  
  def sValid(self: Take) -> bool:
    """ IsValid(self: Take) -> bool
     """
    import System
    return System.Boolean()

  Length: Timecode
   
  Media: Media_
  
  MediaPath: str
  
  MediaStream: MediaStream_
  
  def MembersEqual(self, arg0, arg1):
    """ MembersEqual(self: Take, that: Take) -> bool
     """
    return None

  Name:  str
  
  Offset: Timecode
  
  def ReferenceEquals(objA: object, objB: object) -> bool:
    """ ReferenceEquals(objA: object, objB: object) -> bool
     """
    return None

  def SetAudioChannels(self, firstChannelIndex, channelCount):
    """ SetAudioChannels(self: Take, firstChannelIndex: int, channelCount: int) """
    import System
    return System.Void()

  StreamIndex:  int
  
  addParams = None

class Takes(BaseList[Take_]):
  """  """

  def BaseAdd(self: Takes, item: Take_) -> int:
    """ BaseAdd(self: Takes, item: Take) -> int
     """
    return 1

  def BaseIndex(self: Takes, item: Take_) -> int:
    """ BaseIndex(self: Takes, item: Take) -> int
     """
    return 1

  def BaseRemove(self: Takes, item: Take_) -> bool:
    """ BaseRemove(self: Takes, item: Take) -> bool
     """
    return None

  def GetCount(self: Takes) -> int:
    """ GetCount(self: Takes) -> int
     """
    return 1

  def GetItem(self: Takes, index: int) -> Take_:
    """ GetItem(self: Takes, index: int) -> Take
     """
    return None

  def ReferenceEquals(objA: object, objB: object) -> bool:
    """ ReferenceEquals(objA: object, objB: object) -> bool
     """
    return None

class TimeStretchPitchShift(Enum):
  """ 
  
  enum TimeStretchPitchShift, values: AcidStyle (1), Classic (0), Elastique (2), None (3)
  
   """

  AcidStyle = None
  Classic = None
  Elastique = None

  def Format(self, arg0, arg1, arg2):
    """ Format(enumType: Type, value: object, format: str) -> str
     """
    return ""

  def GetName(self, arg0, arg1):
    """ GetName(enumType: Type, value: object) -> str
     """
    return ""

  def GetNames(self, arg0):
    """ GetNames(enumType: Type) -> Array[str]
     """
    return ""

  def GetUnderlyingType(self, arg0):
    """ GetUnderlyingType(enumType: Type) -> Type
     """
    return None

  def GetValues(self, arg0):
    """ GetValues(enumType: Type) -> Array
     """
    return None

  def IsDefined(self, arg0, arg1):
    """ IsDefined(enumType: Type, value: object) -> bool
     """
    return None

  None_ = None

  def Parse(self, arg0, arg1):
    """ Parse(enumType: Type, value: str) -> object
    Parse(enumType: Type, value: str, ignoreCase: bool) -> object
     """
    return None

  def ReferenceEquals(objA: object, objB: object) -> bool:
    """ ReferenceEquals(objA: object, objB: object) -> bool
     """
    return None

  def ToObject(self, arg0, arg1):
    """ ToObject(enumType: Type, value: object) -> object
    ToObject(enumType: Type, value: SByte) -> object
    ToObject(enumType: Type, value: Int16) -> object
    ToObject(enumType: Type, value: int) -> object
    ToObject(enumType: Type, value: Byte) -> object
    ToObject(enumType: Type, value: UInt16) -> object
    ToObject(enumType: Type, value: int) -> object
    ToObject(enumType: Type, value: int) -> object
    ToObject(enumType: Type, value: int) -> object
     """
    return None

  def TryParse(self, arg0):
    """ TryParse[TEnum](value: str) -> (bool, TEnum)
    TryParse[TEnum](value: str, ignoreCase: bool) -> (bool, TEnum)
     """
    return (None, None)

  value__ = None

class Timecode(object):
  """ Represents a time duration or position in Vegas. 
  The constructors all apply to the active project. 
  We recommend using ProjectTimecode instead to be explicit about which 
  project's framerate your timecodes are evaluated against. 
  Timecode()
  Timecode(milliseconds: float)
  Timecode(timestamp: str)
   """

  def CompareTo(self: Timecode, other: object) -> int:
    """ CompareTo(self: Timecode, other: object) -> int
     """
    import System
    return System.int()

  def Equals(self: Timecode, obj: object) -> bool:
    """ Equals(self: Timecode, obj: object) -> bool
     """
    import System
    return System.Boolean()

  FrameCount: int
  
  FrameRate:  float
  
  def FromFrames(frames: int) -> Timecode:
    """ FromFrames(frames: int) -> Timecode
     """
    import ScriptPortal.Vegas
    return ScriptPortal.Vegas.Timecode()

  def romMilliseconds(milliseconds: float) -> Timecode:
    """ FromMilliseconds(milliseconds: float) -> Timecode
     """
    import ScriptPortal.Vegas
    return ScriptPortal.Vegas.Timecode()

  def FromNanos(nanos: int) -> Timecode:
    """ FromNanos(nanos: int) -> Timecode
     """
    import ScriptPortal.Vegas
    return ScriptPortal.Vegas.Timecode()

  def FromPositionString(timestamp: str) -> Timecode:
    """ FromPositionString(timestamp: str) -> Timecode
    FromPositionString(timestamp: str, format: RulerFormat) -> Timecode
     """
    import ScriptPortal.Vegas
    return ScriptPortal.Vegas.Timecode()

  def FromSeconds(seconds: float) -> Timecode:
    """ FromSeconds(seconds: float) -> Timecode
     """
    import ScriptPortal.Vegas
    return ScriptPortal.Vegas.Timecode()

  def FromString(timestamp: str) -> Timecode:
    """ FromString(timestamp: str) -> Timecode
    FromString(timestamp: str, format: RulerFormat) -> Timecode
    FromString(timestamp: str, format: RulerFormat, isPosition: bool) -> Timecode
     """
    import ScriptPortal.Vegas
    return ScriptPortal.Vegas.Timecode()

  def GetHashCode(self):
    """ GetHashCode(self: Timecode) -> int
     """
    import System
    return System.int()

  def MembersEqual(self: Timecode, o: Timecode) -> bool:
    """ MembersEqual(self: Timecode, o: Timecode) -> bool
     """
    return None

  Nanos: int
   
  def ReferenceEquals(objA: object, objB: object) -> bool:
    """ ReferenceEquals(objA: object, objB: object) -> bool
     """
    return None

  def ToMilliseconds(self: Timecode) -> float:
    """ ToMilliseconds(self: Timecode) -> float
     """
    import System
    return System.Double()

  def ToPositionString(self: Timecode) -> str:
    """ ToPositionString(self: Timecode) -> str
    ToPositionString(self: Timecode, format: RulerFormat) -> str
     """
    import System
    return System.String()

  def ToString(self: Timecode) -> str:
    """ ToString(self: Timecode) -> str
    ToString(self: Timecode, format: RulerFormat) -> str
    ToString(self: Timecode, format: RulerFormat, isPosition: bool) -> str
     """
    import System
    return System.String()

class Track_(object):
  """Represents an audio or video track.
  Track Class  """

  BusTrack: BusTrack_
  
  def CanAddEnvelope(self: Track, type: EnvelopeType) -> bool:
    """ CanAddEnvelope(self: Track, type: EnvelopeType) -> bool
     """
    import System
    return System.Boolean()

  CustomData: CustomDataContainer

  DisplayIndex: int

  EffectCOM: IEffectCOM

  Effects:  Effects_ = None

  EnvelopeCOM:  IEnvelopeCOM

  Envelopes: Envelopes
  
  def Equals(self, that):
    """ Equals(self: Track, that: object) -> bool
     """
    import System
    return System.Boolean()

  Events: TrackEvents_
  
  def GetHashCode(self):
    """ GetHashCode(self: Track) -> int
     """
    import System
    return System.int()

  Index: int
  
  def IsAudio(self: Track) -> bool:
    """ IsAudio(self: Track) -> bool
     """
    import System
    return System.Boolean()

  def IsValid(self: Track) -> bool:
    """ IsValid(self: Track) -> bool
     """
    import System
    return System.Boolean()

  def IsVideo(self: Track) -> bool:
    """ IsVideo(self: Track) -> bool
     """
    import System
    return System.Boolean()

  Length = None # type: Timecode
  MediaType: MediaType
  
  def MembersEqual(self, arg0, arg1):
    """ MembersEqual(self: Track, that: Track) -> bool
     """
    return None

  Mute: bool
  
  Name: str
  
  Project: Project_
  
  def ReferenceEquals(objA: object, objB: object) -> bool:
    """ ReferenceEquals(objA: object, objB: object) -> bool
     """
    return None

  Selected: bool
  
  Solo:  bool
  

class TrackEvent_(object):
  """  Represents an audio or video track. """

  ActiveTake: Take_
  
  def AddTake(self: TrackEvent, mediaStream: MediaStream_) -> Take_:
    """ AddTake(self: TrackEvent, mediaStream: MediaStream) -> Take
    AddTake(self: TrackEvent, mediaStream: MediaStream, makeActive: bool) -> Take
    AddTake(self: TrackEvent, mediaStream: MediaStream, makeActive: bool, name: str) -> Take
     """
    import ScriptPortal.Vegas
    return ScriptPortal.Vegas.Take()

  def AdjustPlaybackRate(self: TrackEvent_, rate: float, adjustStart: bool):
    """ AdjustPlaybackRate(self: TrackEvent, rate: float, adjustStart: bool) """
    import System
    return System.Void()

  def AdjustStartLength(self: TrackEvent_, start: Timecode, length: Timecode, adjustTakes: bool) :
    """ AdjustStartLength(self: TrackEvent, start: Timecode, length: Timecode, adjustTakes: bool) """
    import System
    return System.Void()

  def Copy(self: TrackEvent_, destination: Track_, startTime: Timecode) -> TrackEvent_:
    """ Copy(self: TrackEvent, destination: Track, startTime: Timecode) -> TrackEvent
     """
    import ScriptPortal.Vegas
    return ScriptPortal.Vegas.TrackEvent()

  CustomData: CustomDataContainer
  
  End:  Timecode
  
  def Equals(self: TrackEvent_, that: object) -> bool:
    """ Equals(self: TrackEvent, that: object) -> bool
     """
    import System
    return System.Boolean()

  FadeIn: Fade
  
  FadeOut: Fade
  
  def GetHashCode(self: TrackEvent_) -> int:
    """ GetHashCode(self: TrackEvent) -> int
     """
    import System
    return System.int()

  Group: TrackEventGroup
  
  Index: int
  
  def IsAudio(self: TrackEvent_) -> bool:
    """ IsAudio(self: TrackEvent) -> bool
     """
    import System
    return System.Boolean()

  IsGrouped: bool
   

  def IsValid(self: TrackEvent_) -> bool:
    """ IsValid(self: TrackEvent) -> bool
     """
    import System
    return System.Boolean()

  def IsVideo(self: TrackEvent_) -> bool:
    """ IsVideo(self: TrackEvent) -> bool
     """
    import System
    return System.Boolean()

  Length: Timecode

  Locked:  bool
  
  Loop:  bool
  
  MediaType: MediaType

  def MembersEqual(self, arg0, arg1):
    """ MembersEqual(self: TrackEvent, that: TrackEvent) -> bool
     """
    return None

  Mute: bool
  
  Name: str
  
  PlaybackRate:  float
  
  Project: Project_


  def ReferenceEquals(objA: object, objB: object) -> bool:
    """ ReferenceEquals(objA: object, objB: object) -> bool
     """
    return None

  Selected: bool
  
  SnapOffset: Timecode
  
  SourceFirstChannel: int
   
  SourceNumOfChannels:  int
  
  SourceStreamIndex:  int
  

  def Split(self: TrackEvent_, offset: Timecode) -> TrackEvent_:
    """ Split(self: TrackEvent, offset: Timecode) -> TrackEvent
     """
    import ScriptPortal.Vegas
    return ScriptPortal.Vegas.TrackEvent()

  Start: Timecode
  

  def SyncByMove(self: TrackEvent_, selected: bool):
    """ SyncByMove(self: TrackEvent, selected: bool) """
    import System
    return System.Void()

  def SyncBySlip(self: TrackEvent_, selected: bool):
    """ SyncBySlip(self: TrackEvent, selected: bool) """
    import System
    return System.Void()

  SyncEvent: TrackEvent_
  
  SyncOffset: Timecode

  Takes: Takes
  
  Track: Track_


class TrackEventGroup(BaseList[TrackEvent_]):
  """ Represents a group of track events.
  TrackEventGroup(project: Project)
  TrackEventGroup()
   """

  def BaseAdd(self: TrackEventGroup_, item: TrackEvent_) -> int:
    """ BaseAdd(self: TrackEventGroup, item: TrackEvent) -> int
     """
    return 1

  def BaseRemove(self: TrackEventGroup_, item: TrackEvent_) -> bool:
    """ BaseRemove(self: TrackEventGroup, item: TrackEvent) -> bool
     """
    return None

  def Equals(self: TrackEventGroup, obj: object) -> bool:
    """ Equals(self: TrackEventGroup, obj: object) -> bool
     """
    import System
    return System.Boolean()

  def GetCount(self: TrackEventGroup) -> int:
    """ GetCount(self: TrackEventGroup) -> int
     """
    return 1

  def GetHashCode(self: TrackEventGroup) -> int:
    """ GetHashCode(self: TrackEventGroup) -> int
     """
    import System
    return System.int()

  def GetItem(self: TrackEventGroup, index: int) -> TrackEvent_:
    """ GetItem(self: TrackEventGroup, index: int) -> TrackEvent
     """
    return None

  def IsValid(self: TrackEventGroup) -> bool:
    """ IsValid(self: TrackEventGroup) -> bool
     """
    import System
    return System.Boolean()

  def MembersEqual(self, arg0, arg1):
    """ MembersEqual(self: TrackEventGroup, o: TrackEventGroup) -> bool
     """
    return None

  def ReferenceEquals(objA: object, objB: object) -> bool:
    """ ReferenceEquals(objA: object, objB: object) -> bool
     """
    return None

  def Validate(self, arg0):
    """ Validate(self: TrackEventGroup) """
    pass

 
class TrackEventGroups_(BaseList[TrackEventGroup_]):
  """ Collection of track event groups. """

  def BaseAdd(self: TrackEventGroups, item: TrackEventGroup) -> int:
    """ BaseAdd(self: TrackEventGroups, item: TrackEventGroup) -> int
     """
    return 1

  def BaseRemove(self: TrackEventGroups, item: TrackEventGroup) -> bool:
    """ BaseRemove(self: TrackEventGroups, item: TrackEventGroup) -> bool
     """
    return None

  def GetCount(self: TrackEventGroups) -> int:
    """ GetCount(self: TrackEventGroups) -> int
     """
    return 1

  def GetItem(self: TrackEventGroups, index: int) -> TrackEventGroup:
    """ GetItem(self: TrackEventGroups, index: int) -> TrackEventGroup
     """
    return None

  def ReferenceEquals(objA: object, objB: object) -> bool:
    """ ReferenceEquals(objA: object, objB: object) -> bool
     """
    return None

class TrackEvents_(BaseList[TrackEvent_]):
  """ Collection of track events. """

  def BaseAdd(self: TrackEvents_, item: TrackEvent_) -> int:
    """ BaseAdd(self: TrackEvents, item: TrackEvent) -> int
     """
    return 1

  def BaseIndex(self: TrackEvents_, item: TrackEvent_) -> int:
    """ BaseIndex(self: TrackEvents, item: TrackEvent) -> int
     """
    return 1

  def BaseRemove(self: TrackEvents_, item: TrackEvent_) -> bool):
    """ BaseRemove(self: TrackEvents, item: TrackEvent) -> bool
     """
    return None

  def GetCount(self: TrackEvents_) -> int:
    """ GetCount(self: TrackEvents) -> int
     """
    return 1

  def GetItem(self: TrackEvents_, index: int) -> TrackEvent_:
    """ GetItem(self: TrackEvents, index: int) -> TrackEvent
     """
    return None

  def ReferenceEquals(objA: object, objB: object) -> bool:
    """ ReferenceEquals(objA: object, objB: object) -> bool
     """
    return None

class TrackGlowKeyframe(BaseTrackMotionKeyframe):
  """ Represents glow effect track motion keyframes.
  TrackGlowKeyframe()
   """

  Blur:  float
  
  Color:  VideoColor
  
  Intensity: float
  

  def ReferenceEquals(objA: object, objB: object) -> bool:
    """ ReferenceEquals(objA: object, objB: object) -> bool
     """
    return None

class TrackGlowKeyframeList(BaseTrackMotionKeyframeList[TrackGlowKeyframe]):
  """ TrackGlowKeyframeList()
   """

  def ReferenceEquals(objA: object, objB: object) -> bool:
    """ ReferenceEquals(objA: object, objB: object) -> bool
     """
    return None


class TrackGroup(BaseList[Track_]):
  """ Represents a group of tracks. """

  def CCollapseTrackGroup(self: TrackGroup):
    """ CollapseTrackGroup(self: TrackGroup) """
    import System
    return System.Void()

  def Equals(self, obj):
    """ Equals(self: TrackGroup, obj: object) -> bool
     """
    import System
    return System.Boolean()

  def ExpandTrackGroup(self: TrackGroup):
    """ ExpandTrackGroup(self: TrackGroup) """
    import System
    return System.Void()

  def GetCount(self: TrackGroup) -> int:
    """ GetCount(self: TrackGroup) -> int
     """
    return 1

  def GetHashCode(self):
    """ GetHashCode(self: TrackGroup) -> int
     """
    import System
    return System.int()

  def GetItem(self: TrackGroup, index: int) -> Track:
    """ GetItem(self: TrackGroup, index: int) -> Track
     """
    return None

  def InsertTrack(self: TrackGroup, track: Track, ixWhereToInsert: int) -> bool:
    """ InsertTrack(self: TrackGroup, track: Track, ixWhereToInsert: int) -> bool
     """
    import System
    return System.Boolean()

  def IsValid(self: TrackGroup) -> bool:
    """ IsValid(self: TrackGroup) -> bool
     """
    import System
    return System.Boolean()

  def MembersEqual(self, arg0, arg1):
    """ MembersEqual(self: TrackGroup, o: TrackGroup) -> bool
     """
    return None

  Mute: bool
  
  Name: str
  
  def ReferenceEquals(objA: object, objB: object) -> bool:
    """ ReferenceEquals(objA: object, objB: object) -> bool
     """
    return None

  Solo:  bool
  
  def Validate(self, arg0):
    """ Validate(self: TrackGroup) """
    pass

class TrackGroups(BaseList[TrackGroup]):
  """  """

  def CheckItemRange(self: TrackGroups, index: int):
    """ CheckItemRange(self: TrackGroups, index: int) """
    pass

  def GetCount(self: TrackGroups) -> int:
    """ GetCount(self: TrackGroups) -> int
     """
    return 1

  def GetItem(self: TrackGroups, index: int) -> TrackGroup:
    """ GetItem(self: TrackGroups, index: int) -> TrackGroup
     """
    return None

  def ReferenceEquals(objA: object, objB: object) -> bool:
    """ ReferenceEquals(objA: object, objB: object) -> bool
     """
    return None

class TrackMotion(object):
  """ Provides access to video track motion data. """

  DepthAdjust: float
  
  GlowEnabled: bool
  
  GlowKeyframes: TrackGlowKeyframeList
   
  HasGlowData: bool

  HasMotionData: bool
  
  HasShadowData: bool
  
  def InsertGlowKeyframe(self, position):
    """ InsertGlowKeyframe(self: TrackMotion, position: Timecode) -> TrackGlowKeyframe
     """
    import ScriptPortal.Vegas
    return ScriptPortal.Vegas.TrackGlowKeyframe()

  def InsertMotionKeyframe(self, position):
    """ InsertMotionKeyframe(self: TrackMotion, position: Timecode) -> TrackMotionKeyframe
     """
    import ScriptPortal.Vegas
    return ScriptPortal.Vegas.TrackMotionKeyframe()

  def InsertShadowKeyframe(self, position):
    """ InsertShadowKeyframe(self: TrackMotion, position: Timecode) -> TrackShadowKeyframe
     """
    import ScriptPortal.Vegas
    return ScriptPortal.Vegas.TrackShadowKeyframe()

  LensSeparation:  float
   
  MotionKeyframes: TrackMotionKeyframeList
  
  def ReferenceEquals(objA: object, objB: object) -> bool:
    """ ReferenceEquals(objA: object, objB: object) -> bool
     """
    return None

  ScaleFactors: TrackMotionScaleFactors
  
  def SetTrackMotionEnabled(self: TrackMotion, type: TrackMotionType, value: bool):
    """ SetTrackMotionEnabled(self: TrackMotion, type: TrackMotionType, value: bool) """
    pass

  ShadowEnabled: bool

  ShadowKeyframes: TrackShadowKeyframeList



class TrackMotionKeyframe(BaseTrackMotionKeyframe):
  """ Represents positional track motion keyframes.
  TrackMotionKeyframe()
   """

  Depth: float
  
  INVALID_SESSION_ID = None
  
  OrientationX: float
  
  OrientationY: float
  
  PositionZ: float
  
  def ReferenceEquals(objA: object, objB: object) -> bool:
    """ ReferenceEquals(objA: object, objB: object) -> bool
     """
    return None

  RotationOffsetZ: float
  
  RotationX: float
  

  RotationY: float
  

class TrackMotionKeyframeList(BaseTrackMotionKeyframeList[TrackMotionKeyframe]):
  """ Represents a list of positional track motion keyframes.
  TrackMotionKeyframeList()
   """

  def ReferenceEquals(objA: object, objB: object) -> bool:
    """ ReferenceEquals(objA: object, objB: object) -> bool
     """
    return None


class TrackMotionScaleFactors(object):
  """ Represents the scale factors used when accessing the stored track motion keyframe data.
  TrackMotionScaleFactors(project: Project)
  TrackMotionScaleFactors()
   """

  A: float

  def Clear(self):
    """ Clear(self: TrackMotionScaleFactors) """
    import System
    return System.Void()

  D : float
  H : float
  P : float

  def ReferenceEquals(objA: object, objB: object) -> bool:
    """ ReferenceEquals(objA: object, objB: object) -> bool
     """
    return None

  def Reset(self):
    """ Reset(self: TrackMotionScaleFactors) """
    import System
    return System.Void()

  W : float
  X : float
  Y : float
  Z : float

class TrackMotionType(Enum):
  """ 
  
  enum TrackMotionType, values: Glow (2), Invalid (6), Motion (0), ParentGlow (5), ParentMotion (3), ParentShadow (4), Shadow (1)
  
   """

  Glow = None
  Invalid = None
  Motion = None
  ParentGlow = None
  ParentMotion = None
  ParentShadow = None
  Shadow = None

class TrackShadowKeyframe(BaseTrackMotionKeyframe):
  """ TrackShadowKeyframe()
   """

  Blur: float
 
  Color: VideoColor
  
  INVALID_SESSION_ID = None
  Intensity: float
  
  def ReferenceEquals(objA: object, objB: object) -> bool:
    """ ReferenceEquals(objA: object, objB: object) -> bool
     """
    return None


class TrackShadowKeyframeList(BaseTrackMotionKeyframeList[TrackShadowKeyframe]):
  """ TrackShadowKeyframeList()
   """

  def ReferenceEquals(objA: object, objB: object) -> bool:
    """ ReferenceEquals(objA: object, objB: object) -> bool
     """
    return None

  myFactors = None
  myOwner = None
  myType = None

class Tracks_(BaseList[Track_]):
  """Track Class  """

  def BaseAdd(self: Tracks_, item: Track_) -> int:
    """ BaseAdd(self: Tracks, item: Track) -> int
     """
    return 1

  def BaseIndex(self: Tracks_, item: Track_) -> int:
    """ BaseIndex(self: Tracks, item: Track) -> int
     """
    return 1

  def BaseRemove(self: Tracks_, item: Track_) -> bool:
    """ BaseRemove(self: Tracks, item: Track) -> bool
     """
    return None

  def GetCount(self: Tracks_) -> int:
    """ GetCount(self: Tracks) -> int
     """
    return 1

  def GetItem(self: Tracks_, index: int) -> Track_:
    """ GetItem(self: Tracks, index: int) -> Track
     """
    return None

  def ReferenceEquals(objA: object, objB: object) -> bool:
    """ ReferenceEquals(objA: object, objB: object) -> bool
     """
    return None

class TransportControl(object):
  """ Represents transport controls in Vegas. """

  CursorPosition: Timecode
   
  IsPlaying:  bool
   
  IsRecordMonitoring: bool
   
  IsRecording:  bool
  
  LoopMode:  bool
 
  LoopRegionLength: Timecode

  LoopRegionStart:  Timecode

  def Pause(self):
    """ Pause(self: TransportControl) """
    import System
    return System.Void()

  def Play(self):
    """ Play(self: TransportControl) """
    import System
    return System.Void()

  PlayCursorPosition:  Timecode
 
  def PlayFromStart(self):
    """ PlayFromStart(self: TransportControl) """
    import System
    return System.Void()

  def ProfileAtTimestamp(self, startTime, endTime, duration, framerate):
    """ ProfileAtTimestamp(self: TransportControl, startTime: Timecode, endTime: Timecode) -> (float, float)
     """
    import System
    return System.Void()

  def ProfileForMarker(self, startMarkerId, endMarkerId, duration, framerate):
    """ ProfileForMarker(self: TransportControl, startMarkerId: int, endMarkerId: int) -> (float, float)
     """
    import System
    return System.Void()

  def ProfileForRegion(self, index, duration, framerate):
    """ ProfileForRegion(self: TransportControl, index: int) -> (float, float)
     """
    import System
    return System.Void()

  def ProfileSelection(self, duration, framerate):
    """ ProfileSelection(self: TransportControl) -> (float, float)
     """
    import System
    return System.Void()

  def ReferenceEquals(objA: object, objB: object) -> bool:
    """ ReferenceEquals(objA: object, objB: object) -> bool
     """
    return None

  SelectionLength: Timecode
  
  SelectionStart: Timecode
  
  def Stop(self):
    """ Stop(self: TransportControl) """
    import System
    return System.Void()

  def Suspend(self):
    """ Suspend(self: TransportControl) -> IDisposable
     """
    import System
    return System.IDisposable()

  def SuspendForFX(self):
    """ SuspendForFX(self: TransportControl) -> IDisposable
     """
    import System
    return System.IDisposable()

  def ViewCursor(self, centered):
    """ ViewCursor(self: TransportControl, centered: bool) """
    import System
    return System.Void()

  def ZoomSelection(self):
    """ ZoomSelection(self: TransportControl) """
    import System
    return System.Void()

class intListSetting(ListSetting[int]):
  """ intListSetting(name: str)
   """

  def ItemFromString(self, arg0, arg1):
    """ ItemFromString(self: intListSetting, s: str) -> int
     """
    return None

  def ItemToString(self, arg0, arg1):
    """ ItemToString(self: intListSetting, item: int) -> str
     """
    return ""

  Name = None

  def ReferenceEquals(objA: object, objB: object) -> bool:
    """ ReferenceEquals(objA: object, objB: object) -> bool
     """
    return None

  Value = None

class intSetting(XmlSetting):
  """ intSetting(name: str, val: int)
   """

  def FromString(self, value):
    """ FromString(self: intSetting, value: str) """
    import System
    return System.Void()

  Name = None

  def ReferenceEquals(objA: object, objB: object) -> bool:
    """ ReferenceEquals(objA: object, objB: object) -> bool
     """
    return None

  def ToString(self):
    """ ToString(self: intSetting) -> str
     """
    import System
    return System.String()

  Value = None

class UintListSetting(ListSetting[int]):
  """ UintListSetting(name: str)
   """

  def ItemFromString(self, arg0, arg1):
    """ ItemFromString(self: UintListSetting, s: str) -> int
     """
    return None

  def ItemToString(self, arg0, arg1):
    """ ItemToString(self: UintListSetting, item: int) -> str
     """
    return ""

  Name = None

  def ReferenceEquals(objA: object, objB: object) -> bool:
    """ ReferenceEquals(objA: object, objB: object) -> bool
     """
    return None

  Value = None

class UintSetting(XmlSetting):
  """ UintSetting(name: str, val: int)
   """

  def FromString(self, value):
    """ FromString(self: UintSetting, value: str) """
    import System
    return System.Void()

  Name = None

  def ReferenceEquals(objA: object, objB: object) -> bool:
    """ ReferenceEquals(objA: object, objB: object) -> bool
     """
    return None

  def ToString(self):
    """ ToString(self: UintSetting) -> str
     """
    import System
    return System.String()

  Value = None

class UMIDType(Enum):
  """ 
  
  enum UMIDType, values: BASIC (1), EXTENDED (2)
  
   """

  BASIC = None
  EXTENDED = None


class UndoBlock(project: Project, label: str:
  """ UndoBlock(project: Project, label: str)
  UndoBlock(label: str)
   """

  Cancel: bool
  

  def Dispose(self):
    """ Dispose(self: UndoBlock) """
    import System
    return System.Void()

  def ReferenceEquals(objA: object, objB: object) -> bool:
    """ ReferenceEquals(objA: object, objB: object) -> bool
     """
    return None

class VMKeyframeType(Enum):
  """ 
  
  enum VMKeyframeType, values: Count (2), Mask (1), None (1), Position (0)
  
   """

  Count = None
  Mask = None
  None_ = None
  Position = None


 
class Vegas(object):
  """Vegas base class
  
  Represents the Vegas application. You can get access to this singleton object via DomainManager.VegasDomainManager.GetVegas()
  
  """

  def ActivateDockView(self: Vegas, instanceName: str) -> bool: 
    """ Attempts to activate the dock view that has specified instance name.
    
    1. ActivateDockView(self: Vegas, instanceName: str) -> bool
         Parameters:
           - instanceName: the instance name of the dock view
           
           - Return Value: True if the dock view is activated, false otherwise.

    """
    ...
 
  AppActivated: Eventhandler
  AppCultureInfo: CultureInfo
  """ Get the CultureInfo that represents the culture used by the application."""

  AppDeactivate: Eventhandler
  AppInitialized: Eventhandler
  AppSkinChanged: Eventhandler
  AppWindowChanged: Eventhandler
  
  def ArchiveProject(self: Vegas, fileName: str) -> bool:
    """ Archives the current project along with a trimmed copy of all media.
    
     1. ArchiveProject(self: Vegas, fileName: str) -> bool
          Parameters:
            - fileName: project file (full path)
            
     2. ArchiveProject(self: Vegas, fileName: str, flags: ArchiveProjectFlags) -> bool
          Parameters:
            - fileName: project file (full path)
            - flags: any flags from the ArchiveProjectFlags enumeration
     
     """
    import System
    return System.Boolean()

  AudioFX: PlugInNode
  
  def BeginRender(self: Vegas, args: RenderArgs) -> RenderStatus:
    """ Begins rendering the project using the parameters specified by a RenderArgs object. (This simply invokes the same method on the active Project)
        
        1. BeginRender(self: Vegas, args: RenderArgs) -> RenderStatus        
             Parameters:
               - args: parameters for the render operation.
     """
    import ScriptPortal.Vegas
    return ScriptPortal.Vegas.RenderStatus()

  BypassAllAudioFX: bool
  
  def CancelAsynchronousTasks(self: Vegas):
    """ CancelAsynchronousTasks(self: Vegas) """
    import System
    return System.Void()

  def CancelUpload(self: Vegas):
    """ CancelUpload(self: Vegas) """
    import System
    return System.Void()

  def CreateEmptyProject(self: Vegas) -> Project_:
    """ Creates a new empty project. Unlike NewProject, this does not affect the active project. Instead, this is useful for scripting temporary projects, like transcoding single media files.
    
        1. CreateEmptyProject(self: Vegas) -> Project
             Parameters:
               - Return Value: a new Project instance.
             
        2. CreateEmptyProject(self: Vegas, callback: IProgressCallback) -> Project
             Parameters:
               - callback: null or an object to invoke periodically with progress updates
               - Return Value: a new Project instance.

     """
    import ScriptPortal.Vegas
    return ScriptPortal.Vegas.Project()

  Cursor:  Timecode

  def DebugClear(self):
    """ Clears the ScriptEditor output window. """
    import System
    return System.Void()

  def DebugOut(self, sz):
    """ Sends strings to the ScriptEditor output window.
        Parameters:
          sz:  """
    import System
    return System.Void()

  def Exit(self):
    """ Quits the Vegas application upon completion of the script. """
    import System
    return System.Void()

  def FindDockView(self: Vegas, instanceName: str) -> bool:
    """ Indicates whether a dock view that has the specified instance name is loaded.
    
    1. FindDockView(self: Vegas, instanceName: str) -> bool
         Parameters:
           - instanceName: the instance name of the dock view
           - Return Value: True if the dock view is loaded, false otherwise.
         
    2. FindDockView(self: Vegas, instanceName: str) -> (bool, IDockView)
         Parameters:
           - instanceName: the instance name of the dock view
           - out dockview: the dock view
           - Return Value: True if the dock view is loaded, false otherwise.

     """
    import System
    return System.Boolean()

  #def FixupFileUtilityFilterString(self: Vegas, filter: str) -> str:
  #  """ FixupFileUtilityFilterString(self: Vegas, filter: str) -> str
  #   """
  #  import System
  #  return System.String()

  Generators:  PlugInNode
  
  def GetApplicationDataPath(self: Vegas, baseFolder: SpecialFolder) -> str:
    """ Get the directory that contains Vegas' application data files.
    
        1. GetApplicationDataPath(self: Vegas, baseFolder: SpecialFolder) -> str
             Parameters:
               - baseFolder: which application data directory (ApplicationData, LocalApplicationData, or CommonApplicationData)
               - Return Value: ApplicationDataPath
     """
    import System
    return System.String()

  #def GetBestThumbForFile(self: Vegas, filename: str, scan0: IntPtr, cx: int, cy: int) -> int:
  #  """ GetBestThumbForFile(self: Vegas, filename: str, scan0: IntPtr, cx: int, cy: int) -> int
  #   """
  #  import System
  #  return System.Void()

  def GetFirstDockView(self: Vegas) -> (bool, IDockView):
    """ GetFirstDockView(self: Vegas) -> (bool, IDockView)
     """
    import System
    return System.Boolean()

  def GetInterfaceType(self: Vegas) -> InterfaceType:
    """ GetInterfaceType(self: Vegas) -> InterfaceType
     """
    import System
    return System.Void()

  def GetLicenseInfo(self: Vegas, userSpecifiedLicense: str, licenseInfo: LicenseInfo) -> LicenseInfo:
    """ GetLicenseInfo(self: Vegas, userSpecifiedLicense: str, licenseInfo: LicenseInfo) -> LicenseInfo
     """
    import System
    return System.Void()

  def GetNextDockView(self: Vegas, current: IDockView) -> (bool, IDockView):
    """ GetNextDockView(self: Vegas, current: IDockView) -> (bool, IDockView)
     """
    import System
    return System.Boolean()

  def GetPreferenceFlag(self: Vegas, flag: PreferenceFlag) -> bool:
    """ GetPreferenceFlag(self: Vegas, flag: PreferenceFlag) -> bool
     """
    import System
    return System.Boolean()

  def GetPreferenceintSetting(self: Vegas, flag: intPreference) -> int:
    """ GetPreferenceintSetting(self: Vegas, flag: intPreference) -> int
     """
    import System
    return System.int()

  def GetPreferenceString(self: Vegas, type: PreferenceString) -> str:
    """ GetPreferenceString(self: Vegas, type: PreferenceString) -> str
     """
    import System
    return System.String()

  def ImportFile(self: Vegas, fileName: str):
    """ Import a media or nested project file into the current project.
       
       1. ImportFile(self: Vegas, fileName: str)
            Parameters:
              - fileName: The full path of the file to import 
    
       2. ImportFile(self: Vegas, fileName: str, mediaPoolOnly: bool)
            Parameters:
              - fileName: The full path of the file to import
              - mediaPoolOnly: Add media files to the media pool only
       
      """
    import System
    return System.Void()

  def ImportFileDialog(self: Vegas) -> DialogResult:
    """ Import one or more files using Vegas' Import dialog box.
    
    1. ImportFileDialog(self: Vegas) -> DialogResult
    
    2. ImportFileDialog(self: Vegas, initialDir: str) -> DialogResult
         Parameters:
           - initialDir: The initial directory displayed by the dialog box
    
    3. ImportFileDialog(self: Vegas, initialDir: str, mediaPoolOnly: bool) -> DialogResult
         Parameters:
           - initialDir: The initial directory displayed by the dialog box
           - mediaPoolOnly: Add selected media files to the media pool only.
    
    4. ImportFileDialog(self: Vegas, initialDir: str, mediaPoolOnly: bool) -> (DialogResult, Array[str])
         Parameters:
           - initialDir: The initial directory displayed by the dialog box
           - mediaPoolOnly: Add selected media files to the media pool only.
           - filePaths: Array of file paths selected by the user.
     """
    import System.Windows.Forms
    return System.Windows.Forms.DialogResult()

  def ImportMediaFromProject(self: Vegas, fileName: str, importBins: bool, mergeBins: bool):
    """ Import media and optionally bins from a project file.
    
    1. ImportMediaFromProject(self: Vegas, fileName: str, importBins: bool, mergeBins: bool)
         Parameters:
           - fileName: The full path of the project file to import media from.
           - importBins: If true, import bins into project.
           - mergeBins: If true and importBins is true, merge them into project; else place them all under a new bin.
    
     """

    import System
    return System.Void()

  def ImportMediaFromProjectDialog(self: Vegas) -> DialogResult:
    """ Import media from a project file using Vegas' Import Media from Project dialog box.
    
    1. ImportMediaFromProjectDialog(self: Vegas) -> DialogResult
         Parameters:
          None
    
    2. ImportMediaFromProjectDialog(self: Vegas, initialDir: str) -> DialogResult
         Parameters:
           - initialDir: The initial directory displayed by the dialog box.
    3. ImportMediaFromProjectDialog(self: Vegas, initialDir: str) -> (DialogResult, Array[str])
         Parameters:
           - initialDir: The initial directory displayed by the dialog box
           - filePaths: Array of file paths selected by the user.
     """
    import System.Windows.Forms
    return System.Windows.Forms.DialogResult()
  
  InstallationDirectory: str = "" #: Get the directory that contains the running Vegas executable and accompanying files
  """ Get the directory that contains the running Vegas executable and accompanying files. """
   
  def InvokeCommand(self: Vegas, section: str, name: str):
    """ InvokeCommand(self: Vegas, section: str, name: str)InvokeCommand(self: Vegas, cmd: CustomCommand) """
    import System
    return System.Void()

  def IsRestrictedRenderFileClass(self: Vegas, classID: Guid) -> bool:
    """ IsRestrictedRenderFileClass(self: Vegas, classID: Guid) -> bool
     """
    import System
    return System.Boolean()

  def LRZ(rezName: str) -> str:
    """ LRZ(rezName: str) -> str
     """
    import System
    return System.String()

  def LoadDockView(self: Vegas, dockview: IDockView):
    """ LoadDockView(self: Vegas, dockview: IDockView) """
    import System
    return System.Void()

  def LoadWindowLayoutFile(self: Vegas, windowLayoutFile: str):
    """ LoadWindowLayoutFile(self: Vegas, windowLayoutFile: str) """
    import System
    return System.Void()

  LongAppName: str
  
  LoopMode: bool
  
  LoopPlayback:  bool
  
  MainWindow: IWin32Window 
  """ Get an interface that provides Vegas' main window handle."""
                        

  MarkersChanged = None
  MediaPoolChanged = None
  MissingMedia = None

  def NewProject(self: Vegas, promptSave: bool, showDialog: bool) -> bool:
    """ NewProject(self: Vegas, promptSave: bool, showDialog: bool) -> bool
    NewProject(self: Vegas) -> bool
     """
    import System
    return System.Boolean()

  def OpenFile(self: Vegas, fileName: str)OpenFile(self: Vegas, fileName: str, mediaPoolOnly: bool):
    """ OpenFile(self: Vegas, fileName: str)OpenFile(self: Vegas, fileName: str, mediaPoolOnly: bool) """
    import System
    return System.Void()

  def OpenFileDialog(self: Vegas) -> DialogResult:
    """ OpenFileDialog(self: Vegas) -> DialogResult
    OpenFileDialog(self: Vegas, initialDir: str) -> DialogResult
    OpenFileDialog(self: Vegas, initialDir: str, mediaPoolOnly: bool) -> DialogResult
    OpenFileDialog(self: Vegas, initialDir: str, mediaPoolOnly: bool) -> (DialogResult, Array[str])
     """
    import System.Windows.Forms
    return System.Windows.Forms.DialogResult()

  def OpenProject(self: Vegas) -> bool:
    """ OpenProject(self: Vegas) -> bool
    OpenProject(self: Vegas, fileName: str) -> bool
     """
    import System
    return System.Boolean()

  PlaybackStarted = None
  PlaybackStopped = None
  
  PlugIns: PlugInNode # Get the root plug-in node.

  Project: Project_ = None
  """ Get the current Project """

  ProjectClosed = None 
  ProjectOpened = None
  ProjectOpening = None
  ProjectSaved = None
  ProjectSaving = None

  def QueueProgressWorker(self: Vegas, worker: ProgressWorker):
    """ QueueProgressWorker(self: Vegas, worker: ProgressWorker) """
    import System
    return System.Void()

  def ReadProject(self: Vegas, path: str) -> Project_:
    """ ReadProject(self: Vegas, path: str) -> Project
    ReadProject(self: Vegas, path: str, callback: IProgressCallback) -> Project
     """
    import ScriptPortal.Vegas
    return ScriptPortal.Vegas.Project()

  def ReferenceEquals(objA: object, objB: object) -> bool:
    """ ReferenceEquals(objA: object, objB: object) -> bool
     """
    return None

  def Render(self: Vegas, args: RenderArgs) -> RenderStatus:
    """ Render(self: Vegas, args: RenderArgs) -> RenderStatus
    Render(self: Vegas, outputFile: str, renderTemplate: RenderTemplate, start: Timecode, length: Timecode) -> RenderStatus
    Render(self: Vegas, outputFile: str, renderTemplate: RenderTemplate) -> RenderStatus
     """
    import ScriptPortal.Vegas
    return ScriptPortal.Vegas.RenderStatus()

  RenderFinished = None
  RenderProgress = None
  RenderStarted = None
  
  Renderers: Renderers_ # Get the collection of render plug-ins.
  
  def ResetFPU(self: Vegas):
    """ ResetFPU(self: Vegas) """
    import System
    return System.Void()

  ResumePlaybackOnScriptExit: value
  
  RulerFormatChanged = None

  def RunScriptFile(self: Vegas, scriptFile: str):
    """ RunScriptFile(self: Vegas, scriptFile: str)
    RunScriptFile(self: Vegas, scriptFile: str, scriptArgs: str) """
    import System
    return System.Void()

  def RunScriptText(self: Vegas, engineType: ScriptEngineType, scriptText: str):
    """ RunScriptText(self: Vegas, engineType: ScriptEngineType, scriptText: str)
    RunScriptText(self: Vegas, engineType: ScriptEngineType, scriptText: str, scriptArgs: str) """
    import System
    return System.Void()

  def SaveProject(self: Vegas, fileName: str) -> bool:
    """ SaveProject(self: Vegas, fileName: str) -> bool
    SaveProject(self: Vegas) -> bool
     """
    import System
    return System.Boolean()

  def SaveProjectDialog(self: Vegas, fileName: str) -> bool:
    """ SaveProjectDialog(self: Vegas, fileName: str) -> bool
     """
    import System
    return System.Boolean()

  def SaveSnapshot(self: Vegas, outputFile: str, format: ImageFileFormat, seekTime: Timecode) -> RenderStatus:
    """ SaveSnapshot(self: Vegas, outputFile: str, format: ImageFileFormat, seekTime: Timecode) -> RenderStatus
    SaveSnapshot(self: Vegas, outputFile: str, format: ImageFileFormat) -> RenderStatus
    SaveSnapshot(self: Vegas, seekTime: Timecode) -> RenderStatus
    SaveSnapshot(self: Vegas) -> RenderStatus
     """
    import ScriptPortal.Vegas
    return ScriptPortal.Vegas.RenderStatus()

  SelectionLength: Timecode

  SelectionStart: Timecode
  
  def SetPreferenceFlag(self: Vegas, flag: PreferenceFlag, set: bool):
    """ SetPreferenceFlag(self: Vegas, flag: PreferenceFlag, set: bool) """
    import System
    return System.Void()

  def SetPreferenceintSetting(self: Vegas, flag: intPreference, set: int):
    """ SetPreferenceintSetting(self: Vegas, flag: intPreference, set: int) """
    import System
    return System.Void()

  def SetPreferenceString(self: Vegas, type: PreferenceString, set: str):
    """ SetPreferenceString(self: Vegas, type: PreferenceString, set: str) """
    import System
    return System.Void()

  ShortAppName: str
  
  def ShowError(self: Vegas, msg: str):
    """ ShowError(self: Vegas, msg: str)
    ShowError(self: Vegas, msg: str, details: str)
    ShowError(self: Vegas, e: Exception) """
    import System
    return System.Void()

  def ShowRenderTemplateEditDialog(self, ownerWindow, renderer, includeDefaultTemplate, multichannelEnabled, currentChoice, editedTemplate):
    """ ShowRenderTemplateEditDialog(self: Vegas, ownerWindow: IWin32Window, renderer: Renderer, includeDefaultTemplate: bool, multichannelEnabled: bool, currentChoice: RenderTemplate) -> (DialogResult, RenderTemplate)
    ShowRenderTemplateEditDialog(self: Vegas, ownerWindow: IWin32Window, renderer: Renderer, includeDefaultTemplate: bool, currentChoice: RenderTemplate) -> (DialogResult, RenderTemplate)
    ShowRenderTemplateEditDialog(self: Vegas, ownerWindow: IWin32Window, renderer: Renderer, currentChoice: RenderTemplate) -> (DialogResult, RenderTemplate)
     """
    import System.Windows.Forms
    return System.Windows.Forms.DialogResult()

  def SignalNewListOfSyncFiles(self: Vegas):
    """ SignalNewListOfSyncFiles(self: Vegas) """
    import System
    return System.Void()

  StatusLogVideoPlayback = None
  TemporaryFilesPath:  str
   
  TheVegasCOM = None
  TrackCountChanged = None
  TrackEventCountChanged = None
  TrackEventStateChanged = None
  TrackEventTimeChanged = None
  TrackStateChanged = None
  Transitions: PlugInNode
  
  Transport:  TransportControl # Get the transport control object for Vegas' main timeline.
  
  def UIScale(self: Vegas, scale: int) -> int:
    """ UIScale(self: Vegas, scale: int) -> int
     """
    import System
    return System.int()

  def UIScaleFactor(self: Vegas) -> float:
    """ UIScaleFactor(self: Vegas) -> float
     """
    import System
    return System.Double()

  UnloadScriptDomainOnScriptExit: value

  def UpdateUI(self: Vegas):
    """ UpdateUI(self: Vegas) """
    import System
    return System.Void()

  UploadFinished = None
  UploadProgress = None
  UploadStarted = None
  UploadStatus = None

  def UploadToOFACommunity(self: Vegas, communityID: int, filePath: str, title: str, description: str, tags: str, privateBroadcast: bool) -> bool:
    """ UploadToOFACommunity(self: Vegas, communityID: int, filePath: str, title: str, description: str, tags: str, privateBroadcast: bool) -> bool
     """
    import System
    return System.Boolean()

  Version: str
  """ Get the version of Vegas."""

  VideoCompositeFX:  PlugInNode
  
  VideoFX: PlugInNode # Get the root plug-in node for video effects.
  
  def WaitForIdle(self: Vegas):
    """ WaitForIdle(self: Vegas) """
    import System
    return System.Void()

  theCultureInfo = None
  theVegasResourceManager = None

class VegasCapturePanel(Capture):
  """ VegasCapturePanel(vegas: Vegas, dockWnd: CaptureDockWnd)
   """

  AVCPlayCapsFwd = None
  AVCPlayCapsRev = None
  Activated = None
  Activating = None

  def AddClipToPool(self: VegasCapturePanel, clip: Clip):
    """ AddClipToPool(self: VegasCapturePanel, clip: Clip) """
    pass

  AutoScalePreview = None
  AutoSizeChanged = None
  BackColorChanged = None
  BackgroundImageChanged = None
  BackgroundImageLayoutChanged = None
  BindingContextChanged = None

  def BringMediaOnline(self: VegasCapturePanel):
    """ BringMediaOnline(self: VegasCapturePanel) """
    pass

  CapSet = None
  CaptureBeginning = None
  CaptureComplete = None

  class CaptureDirComboBoxItem(object):
    """ CaptureDirComboBoxItem(dir: CaptureDir, isDefaultDir: bool)
     """

    def ReferenceEquals(objA: object, objB: object) -> bool:
      """ ReferenceEquals(objA: object, objB: object) -> bool
       """
      return None

  def aptureStatusToString(status: CaptureStatus) -> str:
    """ CaptureStatusToString(status: CaptureStatus) -> str
     """
    return ""

  CausesValidationChanged = None

  def ChangeAttachedMetaFilename(self: VegasCapturePanel, metadataFilename: str, mediaFilename: str):
    """ ChangeAttachedMetaFilename(self: VegasCapturePanel, metadataFilename: str, mediaFilename: str) """
    pass

  ChangeUICues = None
  CheckForIllegalCrossThreadCalls = False
  Click = None
  ClientSizeChanged = None

  class ClipListViewItem(ListViewItem):
    """ ClipListViewItem(clip: Clip)
     """

    def HandleClipStatusChanged(self: ClipListViewItem, sender: object, args: ClipEventArgs):
      """ HandleClipStatusChanged(self: ClipListViewItem, sender: object, args: ClipEventArgs) """
      pass

    class ListViewSubItem(object):
      """ ListViewSubItem()
      ListViewSubItem(owner: ListViewItem, text: str)
      ListViewSubItem(owner: ListViewItem, text: str, foreColor: Color, backColor: Color, font: Font)
       """

      BackColor: Color
      
      Bounds: Rectangle
      
      Font:  Font
      
      ForeColor: Color
      
      Name: str
      
      def ReferenceEquals(objA: object, objB: object) -> bool:
        """ ReferenceEquals(objA: object, objB: object) -> bool
         """
        return None

      def ResetStyle(self: ListViewSubItem):
        """ ResetStyle(self: ListViewSubItem) """
        import System
        return System.Void()

      Tag: object
       
      Text: str
      
      def ToString(self):
        """ ToString(self: ListViewSubItem) -> str
         """
        import System
        return System.String()

    class ListViewSubItemCollection(object):
      """ ListViewSubItemCollection(owner: ListViewItem)
       """

      def Add(self: ListViewSubItemCollection, item: ListViewSubItem) -> ListViewSubItem:
        """ Add(self: ListViewSubItemCollection, item: ListViewSubItem) -> ListViewSubItem
        Add(self: ListViewSubItemCollection, text: str) -> ListViewSubItem
        Add(self: ListViewSubItemCollection, text: str, foreColor: Color, backColor: Color, font: Font) -> ListViewSubItem
         """
        import System.Windows.Forms
        return System.Windows.Forms.ListViewSubItem()

      def AddRange(self: ListViewSubItemCollection, items: Array[ListViewSubItem]):
        """ AddRange(self: ListViewSubItemCollection, items: Array[ListViewSubItem])
        ddRange(self: ListViewSubItemCollection, items: Array[str])
        AddRange(self: ListViewSubItemCollection, items: Array[str], foreColor: Color, backColor: Color, font: Font) """
        import System
        return System.Void()

      def Clear(self: ListViewSubItemCollection):
        """ Clear(self: ListViewSubItemCollection) """
        import System
        return System.Void()

      def Contains(self: ListViewSubItemCollection, subItem: ListViewSubItem) -> bool:
        """ Contains(self: ListViewSubItemCollection, subItem: ListViewSubItem) -> bool
         """
        import System
        return System.Boolean()

      def ContainsKey(self: ListViewSubItemCollection, key: str) -> bool:
        """ ContainsKey(self: ListViewSubItemCollection, key: str) -> bool
         """
        import System
        return System.Boolean()

      Count: int

      def GetEnumerator(self: ListViewSubItemCollection) -> IEnumerator:
        """ GetEnumerator(self: ListViewSubItemCollection) -> IEnumerator
         """
        import System.Collections
        return System.Collections.IEnumerator()

      def IndexOf(self: ListViewSubItemCollection, subItem: ListViewSubItem) -> int:
        """ IndexOf(self: ListViewSubItemCollection, subItem: ListViewSubItem) -> int
         """
        import System
        return System.int()

      def IndexOfKey(self: ListViewSubItemCollection, key: str) -> int:
        """ IndexOfKey(self: ListViewSubItemCollection, key: str) -> int
         """
        import System
        return System.int()

      def Insert(self: ListViewSubItemCollection, index: int, item: ListViewSubItem):
        """ Insert(self: ListViewSubItemCollection, index: int, item: ListViewSubItem) """
        import System
        return System.Void()

      IsReadOnly: bool
      
      Item = None

      def ReferenceEquals(objA: object, objB: object) -> bool:
        """ ReferenceEquals(objA: object, objB: object) -> bool
         """
        return None

      def Remove(self: ListViewSubItemCollection, item: ListViewSubItem):
        """ Remove(self: ListViewSubItemCollection, item: ListViewSubItem) """
        import System
        return System.Void()

      def RemoveAt(self: ListViewSubItemCollection, index: int):
        """ RemoveAt(self: ListViewSubItemCollection, index: int) """
        import System
        return System.Void()

      def RemoveByKey(self: ListViewSubItemCollection, key: str):
        """ RemoveByKey(self: ListViewSubItemCollection, key: str) """
        import System
        return System.Void()

    def ReferenceEquals(objA: object, objB: object) -> bool:
      """ ReferenceEquals(objA: object, objB: object) -> bool
       """
      return None

  class ClipListViewItemComparer(object):
    """ ClipListViewItemComparer()
     """

    def ReferenceEquals(objA: object, objB: object) -> bool:
      """ ReferenceEquals(objA: object, objB: object) -> bool
       """
      return None

  def ClipStatusToString(clip: Clip) -> str:
    """ ClipStatusToString(clip: Clip) -> str
     """
    return ""

  def CloseMediaFile(self: VegasCapturePanel, path: str):
    """ CloseMediaFile(self: VegasCapturePanel, path: str) """
    pass

  ContextMenuChanged = None
  ContextMenuStripChanged = None
  ControlAdded = None
  ControlRemoved = None
  CurrentTapeName = None
  CursorChanged = None
  Deactivated = None
  Deactivating = None
  DeckCaps = None
  DefaultBackColor = None
  DefaultClipEditControlMargin = None
  DefaultFont = None
  DefaultForeColor = None

  class DeviceMenuItem(MenuItem):
    """ DeviceMenuItem(device: DeviceInfo, subdevice: SubDeviceInfo)
     """

    Click = None
    Disposed = None
    DrawItem = None
    FindHandle = 0
    FindShortcut = 1
    MeasureItem = None

    class MenuItemCollection(object):
      """ MenuItemCollection(owner: Menu)
       """

      def Add(self: MenuItemCollection, index: int, item: MenuItem) -> int:
        """ Add(self: MenuItemCollection, index: int, item: MenuItem) -> int
        Add(self: MenuItemCollection, caption: str) -> MenuItem
        Add(self: MenuItemCollection, caption: str, onClick: EventHandler) -> MenuItem
        Add(self: MenuItemCollection, caption: str, items: Array[MenuItem]) -> MenuItem
        Add(self: MenuItemCollection, item: MenuItem) -> int
         """
        import System
        return System.int()

      def AddRange(self: MenuItemCollection, items: Array[MenuItem]):
        """ AddRange(self: MenuItemCollection, items: Array[MenuItem]) """
        import System
        return System.Void()

      def Clear(self: MenuItemCollection):
        """ Clear(self: MenuItemCollection) """
        import System
        return System.Void()

      def Contains(self: MenuItemCollection, value: MenuItem) -> bool:
        """ Contains(self: MenuItemCollection, value: MenuItem) -> bool
         """
        import System
        return System.Boolean()

      def ContainsKey(self: MenuItemCollection, key: str) -> bool:
        """ ContainsKey(self: MenuItemCollection, key: str) -> bool
         """
        import System
        return System.Boolean()

      def CopyTo(self: MenuItemCollection, dest: Array, index: int):
        """ CopyTo(self: MenuItemCollection, dest: Array, index: int) """
        import System
        return System.Void()

      Count: int
      
      def Find(self: MenuItemCollection, key: str, searchAllChildren: bool) -> Array[MenuItem]:
        """ Find(self: MenuItemCollection, key: str, searchAllChildren: bool) -> Array[MenuItem]
         """
        import System.Windows.Forms
        return System.Windows.Forms.MenuItem[]()

      def GetEnumerator(self: MenuItemCollection) -> IEnumerator:
        """ GetEnumerator(self: MenuItemCollection) -> IEnumerator
         """
        import System.Collections
        return System.Collections.IEnumerator()

      def IndexOf(self: MenuItemCollection, value: MenuItem) -> int:
        """ IndexOf(self: MenuItemCollection, value: MenuItem) -> int
         """
        import System
        return System.int()

      def IndexOfKey(self: MenuItemCollection, key: str) -> int:
        """ IndexOfKey(self: MenuItemCollection, key: str) -> int
         """
        import System
        return System.int()

      IsReadOnly: bool
      
      Item = None

      def ReferenceEquals(objA: object, objB: object) -> bool:
        """ ReferenceEquals(objA: object, objB: object) -> bool
         """
        return None

      def Remove(self: MenuItemCollection, item: MenuItem):
        """ Remove(self: MenuItemCollection, item: MenuItem) """
        import System
        return System.Void()

      def RemoveAt(self: MenuItemCollection, index: int):
        """ RemoveAt(self: MenuItemCollection, index: int) """
        import System
        return System.Void()

      def RemoveByKey(self: MenuItemCollection, key: str):
        """ RemoveByKey(self: MenuItemCollection, key: str) """
        import System
        return System.Void()

    Popup = None

    def ReferenceEquals(objA: object, objB: object) -> bool:
      """ ReferenceEquals(objA: object, objB: object) -> bool
       """
      return None

    Select = None

  Disposed = None
  DockChanged = None
  DoubleClick = None
  DpiChangedAfterParent = None
  DpiChangedBeforeParent = None
  DragDrop = None
  DragEnter = None
  DragLeave = None
  DragOver = None
  EnabledChanged = None
  Enter = None

  def FileStatusToString(status: FileStatus) -> str:
    """ FileStatusToString(status: FileStatus) -> str
     """
    return ""

  FirstClipEditTabIndex = 1000
  FontChanged = None
  ForeColorChanged = None

  def FreeTutorCallbacks(self: VegasCapturePanel):
    """ FreeTutorCallbacks(self: VegasCapturePanel) """
    import System
    return System.Void()

  def FromChildHandle(handle: IntPtr) -> Control:
    """ FromChildHandle(handle: IntPtr) -> Control
     """
    return None

  def FromHandle(handle: IntPtr) -> Control:
    """ FromHandle(handle: IntPtr) -> Control
     """
    return None

  def GetDefaultProjectCaptureDir(self: VegasCapturePanel, createIfNeeded: bool) -> str:
    """ GetDefaultProjectCaptureDir(self: VegasCapturePanel, createIfNeeded: bool) -> str
     """
    import System
    return System.String()

  def GetDiskFreeSpace(self: VegasCapturePanel, path: str, divisor: int) -> int:
    """ GetDiskFreeSpace(self: VegasCapturePanel, path: str, divisor: int) -> int
     """
    import System
    return System.int()

  def GetDiskTotalSpace(self: VegasCapturePanel, path: str, divisor: int) -> int:
    """ GetDiskTotalSpace(self: VegasCapturePanel, path: str, divisor: int) -> int
     """
    import System
    return System.int()

  def GetOwnerWindow(self: VegasCapturePanel) -> IWin32Window:
    """ GetOwnerWindow(self: VegasCapturePanel) -> IWin32Window
     """
    import System.Windows.Forms
    return System.Windows.Forms.IWin32Window()

  def GetParentWindow(self: VegasCapturePanel) -> IWin32Window:
    """ GetParentWindow(self: VegasCapturePanel) -> IWin32Window
     """
    import System.Windows.Forms
    return System.Windows.Forms.IWin32Window()

  def GetProjectCaptureDir(self: VegasCapturePanel, createIfNeeded: bool) -> str:
    """ GetProjectCaptureDir(self: VegasCapturePanel, createIfNeeded: bool) -> str
     """
    import System
    return System.String()

  GiveFeedback = None
  GotFocus = None
  HandleCreated = None
  HandleDestroyed = None
  HelpRequested = None

  def ImageIndexForIconID(self: VegasCapturePanel, id: IconID) -> int:
    """ ImageIndexForIconID(self: VegasCapturePanel, id: IconID) -> int
     """
    import System
    return System.int()

  ImeModeChanged = None

  def InitToolBarImageList(self: VegasCapturePanel):
    """ InitToolBarImageList(self: VegasCapturePanel) """
    import System
    return System.Void()

  def InitTutorCallbacks(self: VegasCapturePanel):
    """ InitTutorCallbacks(self: VegasCapturePanel) """
    import System
    return System.Void()

  Invalidated = None
  IsActivating = None
  IsActive = None
  IsDeactivating = None
  IsInitialLoad = None

  def IsKeyLocked(keyVal: Keys) -> bool:
    """ IsKeyLocked(keyVal: Keys) -> bool
     """
    return None

  def IsMnemonic(charCode: Char, text: str) -> bool:
    """ IsMnemonic(charCode: Char, text: str) -> bool
     """
    return None

  JogMouseMoveSensitivity = 4
  KeyDown = None
  KeyPress = None
  KeyUp = None
  LabelFont = None
  Layout = None
  Leave = None
  LeftPanel = None
  LocationChanged = None
  LostFocus = None
  MarginChanged = None
  MinimumClipEditPaneWidth = 378
  ModifierKeys = None
  MouseButtons = None
  MouseCaptureChanged = None
  MouseClick = None
  MouseDoubleClick = None
  MouseDown = None
  MouseEnter = None
  MouseHover = None
  MouseLeave = None
  MouseMove = None
  MousePosition = None
  MouseUp = None
  MouseWheel = None
  Move = None

  def OnActivating(self: VegasCapturePanel, args: EventArgs):
    """ OnActivating(self: VegasCapturePanel, args: EventArgs) """
    pass

  PaddingChanged = None
  Paint = None
  ParentChanged = None
  PreviewKeyDown = None
  QueryAccessibilityHelp = None
  QueryContinueDrag = None

  def ReadyToClose(self: VegasCapturePanel):
    """ ReadyToClose(self: VegasCapturePanel) """
    pass

  def ReferenceEquals(objA: object, objB: object) -> bool:
    """ ReferenceEquals(objA: object, objB: object) -> bool
     """
    return None

  def ReflectMessage(hWnd: IntPtr, m: Message) -> (bool, Message):
    """ ReflectMessage(hWnd: IntPtr, m: Message) -> (bool, Message)
     """
    return (None, None)

  RegionChanged = None
  Resize = None
  RightPanel = None
  RightToLeftChanged = None

  def SaveFocus(self: VegasCapturePanel):
    """ SaveFocus(self: VegasCapturePanel) """
    import System
    return System.Void()

  def SaveSettings(self: VegasCapturePanel):
    """ SaveSettings(self: VegasCapturePanel) """
    import System
    return System.Void()

  Scroll = None
  ScrollStateAutoScrolling = 1
  ScrollStateFullDrag = 16
  ScrollStateHScrollVisible = 2
  ScrollStateUserHasScrolled = 8
  ScrollStateVScrollVisible = 4

  def SetProjectCaptureDir(self: VegasCapturePanel, dir: str):
    """ SetProjectCaptureDir(self: VegasCapturePanel, dir: str) """
    import System
    return System.Void()

  def ShowCreateFileDlg(self: VegasCapturePanel, title: str, filter: str, defaultFile: str, filterIndex: int) -> (str, int):
    """ ShowCreateFileDlg(self: VegasCapturePanel, title: str, filter: str, defaultFile: str, filterIndex: int) -> (str, int)
     """
    return ("", 1)

  def ShowSelectDirectoryDlg(self: VegasCapturePanel, hwndOwner: IntPtr, title: str, defaultDir: str, useNet: bool) -> str:
    """ ShowSelectDirectoryDlg(self: VegasCapturePanel, hwndOwner: IntPtr, title: str, defaultDir: str, useNet: bool) -> str
     """
    return ""

  def ShowSelectFileDlg(self: VegasCapturePanel, title: str, filter: str, defaultFile: str, filterIndex: int) -> (str, int):
    """ ShowSelectFileDlg(self: VegasCapturePanel, title: str, filter: str, defaultFile: str, filterIndex: int) -> (str, int)
     """
    return ("", 1)

  SizeChanged = None

  def StartUndoBlock(self: VegasCapturePanel, label: str) -> IDisposable:
    """ StartUndoBlock(self: VegasCapturePanel, label: str) -> IDisposable
     """
    return None

  StyleChanged = None
  SystemColorsChanged = None
  TabIndexChanged = None
  TabStopChanged = None
  TextChanged = None
  TimeToRefreshInterval = 250
  TimecodeDisplayFont = None

  def TimecodeIsValid(timecode: ISMPTETimecode) -> bool:
    """ TimecodeIsValid(timecode: ISMPTETimecode) -> bool
    TimecodeIsValid(timecode: IEditSMPTETimecode) -> bool
     """
    return None

  class TransportMenuItem(MenuItem):
    """ TransportMenuItem(name: str, handler: EventHandler, mode: DeckMode, cap: DeckCapabilities)
     """

    Click = None
    Disposed = None
    DrawItem = None
    FindHandle = 0
    FindShortcut = 1
    MeasureItem = None
    Popup = None
    Select = None
    Validated = None
    Validating = None

  class VideoPanel(Panel):
    """ VideoPanel()
     """

    AutoSizeChanged = None
    BackColorChanged = None
    BackgroundImageChanged = None
    BackgroundImageLayoutChanged = None
    BindingContextChanged = None
    CausesValidationChanged = None
    ChangeUICues = None
    CheckForIllegalCrossThreadCalls = False
    Click = None
    ClientSizeChanged = None
    ContextMenuChanged = None
    ContextMenuStripChanged = None
    ControlAdded = None
    ControlRemoved = None
    CursorChanged = None
    DefaultBackColor = None
    DefaultFont = None
    DefaultForeColor = None
    Disposed = None
    DockChanged = None
    DoubleClick = None
    DpiChangedAfterParent = None
    DpiChangedBeforeParent = None
    DragDrop = None
    DragEnter = None
    DragLeave = None
    DragOver = None
    EnabledChanged = None
    Enter = None
    FontChanged = None
    ForeColorChanged = None

    def FromChildHandle(handle: IntPtr) -> Control:
      """ FromChildHandle(handle: IntPtr) -> Control
       """
      return None

    def FromHandle(handle: IntPtr) -> Control:
      """ FromHandle(handle: IntPtr) -> Control
       """
      return None

    GiveFeedback = None
    GotFocus = None
    HandleCreated = None
    HandleDestroyed = None
    HelpRequested = None
    ImeModeChanged = None
    Invalidated = None

    def IsKeyLocked(keyVal: Keys) -> bool:
      """ IsKeyLocked(keyVal: Keys) -> bool
       """
      return None

    def IsMnemonic(charCode: Char, text: str) -> bool:
      """ IsMnemonic(charCode: Char, text: str) -> bool
       """
      return None

    KeyDown = None
    KeyPress = None
    KeyUp = None
    Layout = None
    Leave = None
    LocationChanged = None
    LostFocus = None
    MarginChanged = None
    ModifierKeys = None
    MouseButtons = None
    MouseCaptureChanged = None
    MouseClick = None
    MouseDoubleClick = None
    MouseDown = None
    MouseEnter = None
    MouseHover = None
    MouseLeave = None
    MouseMove = None
    MousePosition = None
    MouseUp = None
    MouseWheel = None
    Move = None
    PaddingChanged = None
    Paint = None
    ParentChanged = None
    PreviewKeyDown = None
    QueryAccessibilityHelp = None
    QueryContinueDrag = None

    def ReferenceEquals(objA: object, objB: object) -> bool:
      """ ReferenceEquals(objA: object, objB: object) -> bool
       """
      return None

    def ReflectMessage(hWnd: IntPtr, m: Message) -> (bool, Message):
      """ ReflectMessage(hWnd: IntPtr, m: Message) -> (bool, Message)
       """
      return (None, None)

    RegionChanged = None
    Resize = None
    RightToLeftChanged = None
    Scroll = None
    ScrollStateAutoScrolling = 1
    ScrollStateFullDrag = 16
    ScrollStateHScrollVisible = 2
    ScrollStateUserHasScrolled = 8
    ScrollStateVScrollVisible = 4
    SizeChanged = None
    StyleChanged = None
    SystemColorsChanged = None
    TabIndexChanged = None
    TabStopChanged = None
    TextChanged = None
    Validated = None
    Validating = None
    VisibleChanged = None
    VideoPreviewScaleFactor = None
    VisibleChanged = None
 

class VegasEventID(Enum):
  """ 
  
  enum VegasEventID, values: AppActivated (2), AppDeactivate (3), AppInitialized (1), AppSkinChanged (4), AppWindowChanged (24), First (0), Last (30), MarkersChanged (19), MediaPoolChanged (20), MissingMedia (10), PlaybackStarted (22), PlaybackStopped (23), ProjectClosed (7), ProjectOpened (6), ProjectOpening (5), ProjectSaved (9), ProjectSaving (8), RenderFinished (13), RenderProgress (12), RenderStarted (11), RulerFormatChanged (21), StatusLogVideoPlayback (29), TrackCountChanged (14), TrackEventCountChanged (16), TrackEventStateChanged (17), TrackEventTimeChanged (18), TrackStateChanged (15), UploadFinished (28), UploadProgress (26), UploadStarted (25), UploadStatus (27)
  
   """

  AppActivated = None
  AppDeactivate = None
  AppInitialized = None
  AppSkinChanged = None
  AppWindowChanged = None
  First = None
  Last = None
  MarkersChanged = None
  MediaPoolChanged = None
  MissingMedia = None
  PlaybackStarted = None
  PlaybackStopped = None
  ProjectClosed = None
  ProjectOpened = None
  ProjectOpening = None
  ProjectSaved = None
  ProjectSaving = None
  RenderFinished = None
  RenderProgress = None
  RenderStarted = None
  RulerFormatChanged = None
  StatusLogVideoPlayback = None
  TrackCountChanged = None
  TrackEventCountChanged = None
  TrackEventStateChanged = None
  TrackEventTimeChanged = None
  TrackStateChanged = None
  UploadFinished = None
  UploadProgress = None
  UploadStarted = None
  UploadStatus = None

class VideoAlphaType(Enum):
  """ 
  
  enum VideoAlphaType, values: None (0), Premultiplied (2), PremultipliedDirty (3), Straight (1), Undefined (-1)
  
   """

  None_ = None
  Premultiplied = None
  PremultipliedDirty = None
  Straight = None
  Undefined = None


class VideoBusTrack(BusTrack):
  """  Represents a video bus track."""

  BottomFadeColor:  VideoColor

  Bypass:   bool
  
  def CanAddEnvelope(self: VideoBusTrack, type: EnvelopeType) -> bool:
    """ CanAddEnvelope(self: VideoBusTrack, type: EnvelopeType) -> bool
     """
    import System
    return System.Boolean()

  Description:  str
  
  def Equals(self: VideoBusTrack, obj: object) -> bool:
    """ Equals(self: VideoBusTrack, obj: object) -> bool
     """
    import System
    return System.Boolean()

  def GetColor(self: VideoBusTrack, getter: VideoColorGetter) -> VideoColor:
    """ GetColor(self: VideoBusTrack, getter: VideoColorGetter) -> VideoColor
     """
    return None

  def GetHashCode(self: VideoBusTrack) -> int:
    """ GetHashCode(self: VideoBusTrack) -> int
     """
    import System
    return System.int()

  Index:  int
  
  def IsAudio(self: VideoBusTrack) -> bool:
    """ IsAudio(self: VideoBusTrack) -> bool
     """
    import System
    return System.Boolean()

  def IsMaster(self: VideoBusTrack) -> bool:
    """ IsMaster(self: VideoBusTrack) -> bool
     """
    import System
    return System.Boolean()

  def IsVideo(self: VideoBusTrack) -> bool:
    """ IsVideo(self: VideoBusTrack) -> bool
     """
    import System
    return System.Boolean()

  MediaType: MediaType
  
  Name: str
  
  def ReferenceEquals(objA: object, objB: object) -> bool:
    """ ReferenceEquals(objA: object, objB: object) -> bool
     """
    return None

  def SetColor(self: VideoBusTrack, setter: VideoColorSetter, value: VideoColor):
    """ SetColor(self: VideoBusTrack, setter: VideoColorSetter, value: VideoColor) """
    pass
  
  TopFadeColor:  VideoColor
  
 
class VideoColor(r: Single, g: Single, b: Single, a: Single):
  """ Represents a color used in various video properties
  VideoColor()
  VideoColor(r: Single, g: Single, b: Single, a: Single)
  VideoColor(r: Single, g: Single, b: Single)
  VideoColor(argb: int)
  VideoColor(r: Byte, g: Byte, b: Byte, a: Byte)
  VideoColor(r: Byte, g: Byte, b: Byte)
   """

  A: Byte

  Alpha:  Single

  B:  Byte
  
  Blue:  Single
  
  def Equals(self, obj):
    """ Equals(self: VideoColor, obj: object) -> bool
     """
    import System
    return System.Boolean()

  def FromByteValues(r: Byte, g: Byte, b: Byte, a: Byte) -> VideoColor:
    """ FromByteValues(r: Byte, g: Byte, b: Byte, a: Byte) -> VideoColor
    FromByteValues(r: Byte, g: Byte, b: Byte) -> VideoColor
     """
    import ScriptPortal.Vegas
    return ScriptPortal.Vegas.VideoColor()

  G:  Byte

  def GetHashCode(self):
    """ GetHashCode(self: VideoColor) -> int
     """
    import System
    return System.int()

  Green:   Single

  def MembersEqual(self: VideoColor, o: VideoColor) -> bool:
    """ MembersEqual(self: VideoColor, o: VideoColor) -> bool
     """
    return None

  R: Byte
  

  Red:  Single
  

  def ReferenceEquals(objA: object, objB: object) -> bool:
    """ ReferenceEquals(objA: object, objB: object) -> bool
     """
    return None

  def ToArgb(self: VideoColor) -> int:
    """ ToArgb(self: VideoColor) -> int
     """
    import System
    return System.int()

  def ToString(self: VideoColor) -> str:
    """ ToString(self: VideoColor) -> str
     """
    import System
    return System.String()

class VideoDeinterlaceMethod(Enum):
  """ 
  Enumeration of video deinterlace methods.
  enum VideoDeinterlaceMethod, values: BlendFields (1), InterpolateFields (2), None (0)
  
   """

  BlendFields = None
  InterpolateFields = None
  None_ = None


class VideoEvent(TrackEvent_):
  """ Represents an video event.
  VideoEvent(project: Project, start: Timecode, length: Timecode, name: str)
  VideoEvent(start: Timecode, length: Timecode, name: str)
  VideoEvent(start: Timecode, length: Timecode)
  VideoEvent(start: Timecode)
  VideoEvent()
   """

  def CanAddEnvelope(self: VideoEvent, type: EnvelopeType) -> bool:
    """ CanAddEnvelope(self: VideoEvent, type: EnvelopeType) -> bool
     """
    import System
    return System.Boolean()

  Effects:  Effects_

  Envelopes:  Envelopes_
  

  def IsAudio(self: VideoEvent) -> bool:
    """ IsAudio(self: VideoEvent) -> bool
     """
    import System
    return System.Boolean()

  def IsVideo(self: VideoEvent) -> bool:
    """ IsVideo(self: VideoEvent) -> bool
     """
    import System
    return System.Boolean()

  MaintainAspectRatio: bool
   
  MediaType:  MediaType
  
  ReduceInterlace: bool
  
  def ReferenceEquals(objA: object, objB: object) -> bool:
    """ ReferenceEquals(objA: object, objB: object) -> bool
     """
    return None

  ResampleMode: VideoResampleMode
  
  UnderSampleRate: float
  
  VideoMotion: VideoMotion
  

class VideoFieldOrder(Enum):
  """ 
  Enumeration of video field orderings.
  enum VideoFieldOrder, values: LowerFieldFirst (2), ProgressiveScan (0), Unknown (-1), UpperFieldFirst (1)
  
   """


  def IsDefined(self, arg0, arg1):
    """ IsDefined(enumType: Type, value: object) -> bool
     """

  LowerFieldFirst = None
  ProgressiveScan = None
  Unknown = None
  UpperFieldFirst = None
 
class VideoKeyframeType(Enum):
  """ 
  Enumeration of video key frame interpolation types.
  enum VideoKeyframeType, values: Fast (3), Hold (1), Linear (0), Sharp (5), Slow (2), Smooth (4)
  
   """

  Fast = None
  Hold = None
  Linear = None
  Sharp = None
  Slow = None
  Smooth = None

class VideoMotion(object):
  """ Represents the motion of a video event. """

  Keyframes: VideoMotionKeyframes
 
  def ReferenceEquals(objA: object, objB: object) -> bool:
    """ ReferenceEquals(objA: object, objB: object) -> bool
     """
    return None

  ScaleToFill: bool
   

class VideoMotionBounds(object):
  """ Represents a 4 sided bounds polygon used in video motion key frames.
  VideoMotionBounds(topLeft: VideoMotionVertex, topRight: VideoMotionVertex, bottomRight: VideoMotionVertex, bottomLeft: VideoMotionVertex)
  VideoMotionBounds(topLeftX: Single, topLeftY: Single, topRightX: Single, topRightY: Single, bottomRightX: Single, bottomRightY: Single, bottomLeftX: Single, bottomLeftY: Single)
   """

  BottomLeft:  VideoMotionVertex

  BottomRight: VideoMotionVertex
  
  def ReferenceEquals(objA: object, objB: object) -> bool:
    """ ReferenceEquals(objA: object, objB: object) -> bool
     """
    return None

  TopLeft:  VideoMotionVertex

  TopRight: VideoMotionVertex
  

class VideoMotionKeyframe(object):
  """ Represents a key frame for video event motion parameters.
  VideoMotionKeyframe(project: Project, position: Timecode)
  VideoMotionKeyframe(position: Timecode)
   """

  BottomLeft: VideoMotionVertex
  
  BottomRight: VideoMotionVertex
  
  Bounds: VideoMotionBounds
  
  Center: VideoMotionVertex
  
  def IsValid(self: VideoMotionKeyframe) -> bool:
    """ IsValid(self: VideoMotionKeyframe) -> bool
     """
    import System
    return System.Boolean()

  def MoveBy(self: VideoMotionKeyframe, delta: VideoMotionVertex):
    """ MoveBy(self: VideoMotionKeyframe, delta: VideoMotionVertex) """
    import System
    return System.Void()

  Position: Timecode
  

  def ReferenceEquals(objA: object, objB: object) -> bool:
    """ ReferenceEquals(objA: object, objB: object) -> bool
     """
    return None

  def RotateBy(self: VideoMotionKeyframe, delta: float):
    """ RotateBy(self: VideoMotionKeyframe, delta: float) """
    import System
    return System.Void()

  Rotation: float
  
  def ScaleBy(self: VideoMotionKeyframe, delta: VideoMotionVertex) :
    """ ScaleBy(self: VideoMotionKeyframe, delta: VideoMotionVertex) """
    import System
    return System.Void()

  Smoothness:  Single
   
  TopLeft: VideoMotionVertex
  
  TopRight: VideoMotionVertex
  
  Type: VideoKeyframeType
  

class VideoMotionKeyframes(BaseList[VideoMotionKeyframe]):
  """  Collection of video motion key frames for a video event. """

  def BaseAdd(self: VideoMotionKeyframes, item: VideoMotionKeyframe) -> int:
    """ BaseAdd(self: VideoMotionKeyframes, item: VideoMotionKeyframe) -> int
     """
    return 1

  def BaseRemove(self: VideoMotionKeyframes, item: VideoMotionKeyframe) -> bool:
    """ BaseRemove(self: VideoMotionKeyframes, item: VideoMotionKeyframe) -> bool
     """
    return None

  def Clear(self: VideoMotionKeyframes):
    """ Clear(self: VideoMotionKeyframes) """
    import System
    return System.Void()

  def GetCount(self: VideoMotionKeyframes) -> int:
    """ GetCount(self: VideoMotionKeyframes) -> int
     """
    return 1

  def GetItem(self: VideoMotionKeyframes, index: int) -> VideoMotionKeyframe:
    """ GetItem(self: VideoMotionKeyframes, index: int) -> VideoMotionKeyframe
     """
    return None

  def ReferenceEquals(objA: object, objB: object) -> bool:
    """ ReferenceEquals(objA: object, objB: object) -> bool
     """
    return None

class VideoMotionVertex(object):
  """ Represents a vertex used in video motion key frames.
  VideoMotionVertex(x: Single, y: Single)
   """

  def ReferenceEquals(objA: object, objB: object) -> bool:
    """ ReferenceEquals(objA: object, objB: object) -> bool
     """
    return None

  def ToString(self: VideoMotionVertex) -> str:
    """ ToString(self: VideoMotionVertex) -> str
     """
    import System
    return System.String()

  X: Single
  
  Y: Single


class VideoOutputRotation(Enum):
  """ 
  Enumeration of video output rotation settings.
  enum VideoOutputRotation, values: Inverted (2), None (0), QuarterTurnClockwise (1), QuarterTurnCounterclockwise (3)
  
   """
  Inverted = None
  None_ = None
  QuarterTurnClockwise = None
  QuarterTurnCounterclockwise = None


class VideoPreviewSize(Enum):
  """ 
  Enumeration of video preview render size settings.
  enum VideoPreviewSize, values: Auto (1), Full (0), Half (3), PreserveAspect_NOT_USED (2), Quarter (4)
  
   """

  Auto = None
  Full = None
  Half = None
  PreserveAspect_NOT_USED = None
  Quarter = None

class VideoProperties(object):
  """ Base class for objects that represent video properties. """

  FieldOrder:  VideoFieldOrder
  FrameRate:  float
  Height: int
  PixelAspectRatio:  float
  
  def ReferenceEquals(objA: object, objB: object) -> bool:
    """ ReferenceEquals(objA: object, objB: object) -> bool
     """
    return None

  Width: int
   
  
class VideoPropertiesType(Enum):
  """ 
  
  enum VideoPropertiesType, values: Event (4), None (0), Preview (2), Project (1), Stream (3)
  
   """

  Event = None
  None_ = None
  Preview = None
  Project = None
  Stream = None


class VideoRenderQuality(Enum):
  """ 
  Enumeration of video render quality modes.
  enum VideoRenderQuality, values: Best (4), Draft (1), Good (3), Preview (2)
  
   """

  Best = None
  Draft = None
  Good = None
  Preview = None


class VideoResampleMode(Enum):
  """ 
  Enumeration of video resampling modes.
  enum VideoResampleMode, values: Disable (2), Force (1), Smart (0)
  
   """

  Disable = None
  Force = None
  Smart = None

 
class VideoStream(MediaStream_):
  """ Represents a video stream. """

  AlphaChannel:  VideoAlphaType
  
  AverageDataRate:  int
  
  BackgroundColor: VideoColor
  
  ColorDepth:  int
  
  def Equals(self: VideoStream, obj: object) -> bool:
    """ Equals(self: VideoStream, obj: object) -> bool
     """
    import System
    return System.Boolean()

  FieldOrder:  VideoFieldOrder
  
  Format: str
  
  FrameRate: float
  
  def GetHashCode(self: VideoStream) -> int:
    """ GetHashCode(self: VideoStream) -> int
     """
    import System
    return System.int()

  Height:  int
  
  MediaType: MediaType
  
  PixelAspectRatio:  float
  
  def ReferenceEquals(objA: object, objB: object) -> bool:
    """ ReferenceEquals(objA: object, objB: object) -> bool
     """
    return None

  Rotation: VideoOutputRotation
  
  Size:  Size
  
  Stereo3DMode: Stereo3DInputMode
  
  Stereo3DSwap: bool
  
  Width:  int
  
  

class VideoTrack(Track_):
  """ VideoTrack(project: Project, index: int, name: str)
  VideoTrack(index: int, name: str)
  VideoTrack(index: int)
  VideoTrack()
   """

  def AddVideoEvent(self: VideoTrack) -> VideoEvent:
    """ AddVideoEvent(self: VideoTrack) -> VideoEvent
    AddVideoEvent(self: VideoTrack, start: Timecode, length: Timecode) -> VideoEvent
     """
    import ScriptPortal.Vegas
    return ScriptPortal.Vegas.VideoEvent()

  BottomFadeColor: VideoColor
  
  BusTrack: BusTrack_
 
  BypassMotionBlur: bool
  
  def CanAddEnvelope(self: VideoTrack, type: EnvelopeType) -> bool:
    """ CanAddEnvelope(self: VideoTrack, type: EnvelopeType) -> bool
     """
    import System
    return System.Boolean()

  CompositeLevel: Single
  
  CompositeMode:  CompositeMode
  
  CompositeModeEffect:  Effect
  

  class CompositeModeEffectOwner(object):
    """ CompositeModeEffectOwner(track: VideoTrack, isParent: bool, com: IEffectCOM)
     """

    def MembersEqual(self, arg0, arg1):
      """ MembersEqual(self: CompositeModeEffectOwner, that: CompositeModeEffectOwner) -> bool
       """
      return None

    def ReferenceEquals(objA: object, objB: object) -> bool:
      """ ReferenceEquals(objA: object, objB: object) -> bool
       """
      return None

    CompositeNestingLevel:  int
  
  def Equals(self: VideoTrack, obj: object) -> bool:
    """ Equals(self: VideoTrack, obj: object) -> bool
     """
    import System
    return System.Boolean()

  def GetColor(self: VideoTrack, getter: VideoColorGetter) -> VideoColor:
    """ GetColor(self: VideoTrack, getter: VideoColorGetter) -> VideoColor
     """
    return None

  def GetHashCode(self: VideoTrack) -> int:
    """ GetCompositeModeBase(self: VideoTrack, parentMode: bool) -> CompositeMode
     """
    return None

  def GetHashCode(self):
    """ GetHashCode(self: VideoTrack) -> int
     """
    import System
    return System.int()

  def IsAudio(self: VideoTrack) -> bool:
    """ IsAudio(self: VideoTrack) -> bool
     """
    import System
    return System.Boolean()

  IsCompositingChild: bool
   
  IsCompositingParent: bool
  
  def IsVideo(self: VideoTrack) -> bool:
    """ IsVideo(self: VideoTrack) -> bool
     """
    import System
    return System.Boolean()

  MediaType: MediaType
  
  ParentCompositeMode:  CompositeMode
  
  ParentCompositeModeEffect:  Effect
  
  ParentTrackMotion:  TrackMotion
  
  def ReferenceEquals(objA: object, objB: object) -> bool:
    """ ReferenceEquals(objA: object, objB: object) -> bool
     """
    return None

  def SetColor(self: VideoTrack, setter: VideoColorSetter, value: VideoColor):
    """ SetColor(self: VideoTrack, setter: VideoColorSetter, value: VideoColor) """
    pass

  def SetCompositeMode(self: VideoTrack, mode: CompositeMode, showWarningDialog: bool) -> bool:
    """ SetCompositeMode(self: VideoTrack, mode: CompositeMode, showWarningDialog: bool) -> bool
     """
    import System
    return System.Boolean()

  def SetCompositeModeBase(self: VideoTrack, mode: CompositeMode, showWarningDialog: bool, parentMode: bool) -> bool:
    """ SetCompositeModeBase(self: VideoTrack, mode: CompositeMode, showWarningDialog: bool, parentMode: bool) -> bool
     """
    return None

  def SetParentCompositeMode(self: VideoTrack, mode: CompositeMode, showWarningDialog: bool) -> bool:
    """ SetParentCompositeMode(self: VideoTrack, mode: CompositeMode, showWarningDialog: bool) -> bool
     """
    import System
    return System.Boolean()

  TopFadeColor: VideoColor
   
  TrackMotion:  TrackMotion
   
 