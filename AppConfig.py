import os
#Numbers
maxResults=5
maxSuggestions=20
maxGlobalSuggestions=100

#directories
ffmpegLocation="\StreamingEngines\ffmpeg"
ffplayLocation="\StreamingEngines\ffplay"
streamLocation="Stream"
SongsLocation="Songs"
playlistLocation="Playlist"

#Topic ID
topicId="/m/04rlf"

#APIKEY and BASE URL
API_KEY="AIzaSyDR4qtKowtX9gAbDMrg4C5suHKRe2L3fj4"
SEARCH_BASE_URL="https://www.googleapis.com/youtube/v3/search?"
SUGGEST_BASE_URL="https://www.googleapis.com/youtube/v3/search?"
VIDEO_BASE_URL="https://www.googleapis.com/youtube/v3/videos?"

isGlobalSuggestionFeature=False
def isGlobalSuggestion():
    return isGlobalSuggestionFeature

def getmaxResults():
    return maxResults
def getmaxSuggestion():
    return maxSuggestions
def getmaxGlobalSuggestions():
    return maxGlobalSuggestions

def getTopicID():
    return topicId

def getAPIKEY():
    return API_KEY