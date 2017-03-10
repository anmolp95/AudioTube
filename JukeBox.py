"""
https://developers.google.com/youtube/v3/docs/search

"""
import AppConfig
import JukeBoxUtils as JUtils
from urllib2 import urlopen
import time
import sys
import json
import pafy
import re
import Audio
class JukeBox:
    def __init__(self,API_KEY,maxResults,maxSuggestion):
        self.API_KEY=API_KEY
        self.maxResults=maxResults
        self.maxSuggestion=maxSuggestion
        self.topicId=AppConfig.getTopicID()

    def search(self,query):
        typ="video"
        maxResults=str(self.maxResults)
        part="snippet"
        finalQ=JUtils.tokenise(query)
        filter = [("type",typ),("maxResults",maxResults),("q",finalQ),("key",self.API_KEY),("part",part),("topicId",AppConfig.getTopicID())]
        requestURL=JUtils.createAPIURL(AppConfig.SEARCH_BASE_URL, filter)
        (audioTitleList,audioIdList)=JUtils.getAudioList(requestURL)
        print audioIdList
        videoListWithStats= self.videoStatList(audioIdList)
        audioList=[]
        for i,videoStats in enumerate(videoListWithStats):
            audio=Audio.Audio(audioIdList[i],audioTitleList[i],videoStats)
            audioList.append(audio)
        return audioList
    def suggestion(self,audioObject,addToGlobal=AppConfig.isGlobalSuggestion()):
        typ="video"
        maxResults=str(AppConfig.getmaxSuggestion())
        part="snippet"
        filter = [("type",typ),("maxResults",maxResults),("key",self.API_KEY),("part",part),("relatedToVideoId",audioObject.id)]
        requestURL=JUtils.createAPIURL(AppConfig.SUGGEST_BASE_URL, filter)
        print requestURL
        (audioTitleList,audioIdList)=JUtils.getAudioList(requestURL)
        videoListWithStats= self.videoStatList(audioIdList)
        suggestionAudioList=[]
        for i,videoStats in enumerate(videoListWithStats):
            audio=Audio.Audio(audioIdList[i],audioTitleList[i],videoStats)
            suggestionAudioList.append(audio)
        if addToGlobal==True:
            JUtils.addToGlobalSuggestions(suggestionAudioList)
        return suggestionAudioList

    def getGlobalSuggestions(self):
        globalSuggestions=JUtils.getGlobalSuggestionArray()
        return globalSuggestions
    def videoStatList(self, idList):
        typ="video"
        part="statistics,contentDetails"
        id=",".join(idList)
        filter = [("key",AppConfig.API_KEY),("part",part),("id",id)]
        requestURL=JUtils.createAPIURL(AppConfig.VIDEO_BASE_URL,filter)
        print requestURL
        videoStats=JUtils.getVideoStats(requestURL)
        return videoStats

n=JukeBox(AppConfig.getAPIKEY(),AppConfig.maxResults,AppConfig.maxSuggestions)
x=n.search("KK tumhi ho")
sugg=n.suggestion(x[0])
fg=n.getGlobalSuggestions()
for f in fg:
    f.show()